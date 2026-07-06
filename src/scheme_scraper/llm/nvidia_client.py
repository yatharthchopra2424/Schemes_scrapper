"""
NVIDIA LLM Client — OpenAI-compatible API wrapper
──────────────────────────────────────────────────
Supports:
  • Structured JSON extraction with retry + JSON repair
  • Gap-fill secondary call when key fields are missing
  • Plain Markdown report generation
  • Exponential backoff via tenacity
  • Robust JSON extraction from fenced and raw responses
  • Multi-key round-robin rotation for free-tier accounts
    (reads NVIDIA_API_KEY, NVIDIA_API_KEY_1, NVIDIA_API_KEY_2 … from .env)
    Rotates on every request AND immediately on 429 rate-limit errors.
"""
from __future__ import annotations

import itertools
import json
import logging
import os
import re
import threading
import time
from typing import Any, cast

from openai import OpenAI, APIConnectionError, APIStatusError, APITimeoutError
from tenacity import (
    Retrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from ..config import AppSettings
from ..models import SchemeInput
from .prompts import (
    MARKDOWN_SYSTEM_PROMPT,
    SYSTEM_PROMPT,
    BROWSER_AGENT_PROMPT,
    build_analysis_prompt,
    build_gap_fill_prompt,
)
from .schema import SchemeInsight

logger = logging.getLogger(__name__)


# ── Key Rotator ────────────────────────────────────────────────────────────────

class _KeyRotator:
    """
    Thread-safe round-robin rotator across multiple NVIDIA API keys.

    Reads keys from environment in this order:
      NVIDIA_API_KEY        — original / primary key
      NVIDIA_API_KEY_1      — first extra key
      NVIDIA_API_KEY_2      — second extra key
      NVIDIA_API_KEY_3 …    — any additional keys

    Usage:
      rotator = _KeyRotator(base_url, timeout)
      client  = rotator.current_client()   # get active OpenAI client
      rotator.rotate(reason="429")          # force switch to next key
    """

    def __init__(self, base_url: str, timeout: float):
        self.base_url = base_url
        self.timeout = timeout
        self._lock = threading.Lock()

        self._keys: list[str] = self._collect_keys()
        if not self._keys:
            raise RuntimeError(
                "No NVIDIA API keys found. Set NVIDIA_API_KEY (and optionally "
                "NVIDIA_API_KEY_1, NVIDIA_API_KEY_2 …) in your .env file."
            )

        # Build one OpenAI client per key (clients are thread-safe)
        self._clients: list[OpenAI] = [
            OpenAI(base_url=base_url, api_key=k, timeout=timeout, max_retries=0)
            for k in self._keys
        ]
        self._cycle = itertools.cycle(range(len(self._keys)))
        self._current_idx: int = next(self._cycle)

        self._request_count = 0  # total requests dispatched (for logging)

        logger.info(
            "KeyRotator: %d NVIDIA API key(s) loaded. Key indices: %s",
            len(self._keys),
            list(range(len(self._keys))),
        )
        for i, k in enumerate(self._keys):
            logger.info("  Key [%d]: %s…%s", i, k[:8], k[-4:])

    @staticmethod
    def _collect_keys() -> list[str]:
        """Collect all non-empty NVIDIA keys from environment."""
        keys: list[str] = []

        # Primary key (no suffix)
        primary = os.environ.get("NVIDIA_API_KEY", "").strip()
        if primary:
            keys.append(primary)

        # Numbered keys: _1, _2, _3 … up to _20
        for i in range(1, 21):
            k = os.environ.get(f"NVIDIA_API_KEY_{i}", "").strip()
            if k and k not in keys:   # deduplicate in case someone repeats primary
                keys.append(k)

        return keys

    def current_client(self) -> tuple[OpenAI, int]:
        """Return the current (client, index) without rotating."""
        with self._lock:
            return self._clients[self._current_idx], self._current_idx

    def rotate(self, reason: str = "next request") -> tuple[OpenAI, int]:
        """Advance to the next key and return (client, new_index)."""
        with self._lock:
            self._current_idx = next(self._cycle)
            logger.info(
                "KeyRotator: rotated to key [%d] (%s)",
                self._current_idx,
                reason,
            )
            return self._clients[self._current_idx], self._current_idx

    def rotate_on_rate_limit(self) -> tuple[OpenAI, int]:
        """Called on 429 — rotate immediately and log clearly."""
        with self._lock:
            old_idx = self._current_idx
            self._current_idx = next(self._cycle)
            logger.warning(
                "KeyRotator: 429 rate-limit hit on key [%d] — switching to key [%d]",
                old_idx,
                self._current_idx,
            )
            return self._clients[self._current_idx], self._current_idx

    @property
    def key_count(self) -> int:
        return len(self._keys)

# Fields that, if all empty, will trigger a gap-fill secondary call
_KEY_FIELDS = [
    "eligibility",
    "financial_support",
    "application_process",
    "benefits",
    "implementing_agency",
]


class NvidiaLLMClient:
    """Thread-safe NVIDIA LLM client with multi-key round-robin rotation."""

    def __init__(self, settings: AppSettings):
        self.settings = settings
        self._rotator = _KeyRotator(
            base_url=self.settings.llm.base_url,
            timeout=self.settings.llm.timeout_seconds,
        )
        self.model = self.settings.llm.model
        logger.info(
            "LLM client initialised. Model: %s | Base: %s | Keys: %d",
            self.model,
            self.settings.llm.base_url,
            self._rotator.key_count,
        )

    # ── Core completion ────────────────────────────────────────────────────────

    def _chat_completion(
        self,
        messages: list[dict[str, Any]],
        max_tokens: int | None = None,
    ) -> str:
        """
        Call the API with tenacity retries and automatic key rotation.

        Key rotation strategy:
          - Each new call gets the current key (already rotated on the previous call's end)
          - On 429 rate-limit: immediately rotate to next key, then retry
          - On 5xx / timeout: retry with same key (transient server issue)
          - After a successful call: rotate key so the next request uses the next key
        """
        effective_max_tokens = max_tokens or self.settings.llm.max_tokens
        max_attempts = self.settings.llm.max_retries + 1

        # Each outer attempt may switch keys on 429; inner tenacity handles 5xx/timeout
        last_exc: Exception | None = None
        # We try each key at least once before giving up
        total_attempts = max(max_attempts, self._rotator.key_count * 2)

        for attempt_num in range(total_attempts):
            client, key_idx = self._rotator.current_client()

            retrying = Retrying(
                retry=retry_if_exception_type((APIConnectionError, APITimeoutError)),
                stop=stop_after_attempt(2),          # 2 tries per key for network issues
                wait=wait_exponential(multiplier=2, min=2, max=15),
                reraise=True,
            )

            try:
                for inner_attempt in retrying:
                    with inner_attempt:
                        t0 = time.perf_counter()
                        kwargs: dict[str, Any] = {
                            "model": self.model,
                            "messages": cast(Any, messages),
                            "temperature": self.settings.llm.temperature,
                            "top_p": self.settings.llm.top_p,
                            "max_tokens": effective_max_tokens,
                            "stream": False,
                        }
                        if "nemotron" in self.model.lower():
                            kwargs["extra_body"] = {
                                "chat_template_kwargs": {"enable_thinking": False},
                                "reasoning_budget": 0,
                            }
                        elif "deepseek" in self.model.lower():
                            kwargs["extra_body"] = {
                                "chat_template_kwargs": {"thinking": False, "reasoning_effort": "low"}
                            }

                        logger.debug(
                            "LLM request attempt %d/%d using key [%d]",
                            attempt_num + 1, total_attempts, key_idx,
                        )
                        completion = client.chat.completions.create(**kwargs)
                        content = completion.choices[0].message.content or ""
                        elapsed = time.perf_counter() - t0
                        usage = completion.usage
                        if usage:
                            logger.debug(
                                "LLM key[%d]: %d prompt + %d completion tokens in %.1fs",
                                key_idx,
                                usage.prompt_tokens,
                                usage.completion_tokens,
                                elapsed,
                            )
                        else:
                            logger.debug(
                                "LLM key[%d]: response received in %.1fs", key_idx, elapsed
                            )

                        # ✓ Success — rotate to next key for the NEXT request
                        self._rotator.rotate(reason="next request after success")
                        return content

            except APIStatusError as exc:
                last_exc = exc
                if exc.status_code == 429:
                    # Rate-limited — immediately switch to next key
                    client, key_idx = self._rotator.rotate_on_rate_limit()
                    # Brief pause before hitting the new key
                    time.sleep(1)
                    continue  # retry outer loop with new key
                elif exc.status_code >= 500:
                    logger.warning(
                        "LLM key[%d]: server error %d — rotating key and retrying",
                        key_idx, exc.status_code,
                    )
                    client, key_idx = self._rotator.rotate(reason=f"5xx error {exc.status_code}")
                    continue
                else:
                    # 4xx (not 429) — not retryable
                    logger.warning(
                        "LLM key[%d]: fatal status error %d: %s",
                        key_idx, exc.status_code, exc.message,
                    )
                    raise ValueError(f"LLM API Error {exc.status_code}: {exc.message}") from exc

            except (APIConnectionError, APITimeoutError) as exc:
                last_exc = exc
                logger.warning(
                    "LLM key[%d]: connection/timeout error: %s — rotating key",
                    key_idx, exc,
                )
                client, key_idx = self._rotator.rotate(reason="connection error")
                continue

        raise RuntimeError(
            f"LLM completion failed after {total_attempts} attempts across "
            f"{self._rotator.key_count} key(s). Last error: {last_exc}"
        )

    # ── JSON extraction utilities ──────────────────────────────────────────────

    @staticmethod
    def _strip_fences(text: str) -> str:
        """Strip ```json ... ``` or ``` ... ``` markdown code fences."""
        stripped = text.strip()
        # Remove opening fence
        fence_match = re.match(r"^```(?:json)?\s*\n?", stripped, re.IGNORECASE)
        if fence_match:
            stripped = stripped[fence_match.end():]
        # Remove closing fence
        if stripped.endswith("```"):
            stripped = stripped[: -3].rstrip()
        return stripped.strip()

    @classmethod
    def _extract_json_block(cls, raw_text: str) -> dict[str, Any]:
        """
        Attempt multiple JSON extraction strategies in order:
          1. Direct parse after stripping fences
          2. Regex extraction of the outermost { ... } block
          3. Greedy bracket-balanced extraction
        """
        cleaned = cls._strip_fences(raw_text)

        # Strategy 1: direct
        if cleaned.startswith("{"):
            try:
                return json.loads(cleaned)
            except json.JSONDecodeError:
                pass

        # Strategy 2: regex outermost object
        match = re.search(r"\{[\s\S]*\}", cleaned)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass

        # Strategy 3: bracket-count walk (handles nested braces)
        start = cleaned.find("{")
        if start != -1:
            depth = 0
            for i, ch in enumerate(cleaned[start:], start):
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        candidate = cleaned[start : i + 1]
                        try:
                            return json.loads(candidate)
                        except json.JSONDecodeError:
                            break

        raise ValueError("No valid JSON object found in model response")

    def _repair_json(self, broken_output: str, scheme_name: str) -> dict[str, Any]:
        """
        Secondary LLM call asking the model to fix a malformed JSON response.
        Returns the repaired parsed dict.
        """
        logger.warning("Attempting JSON repair for scheme: %s", scheme_name)
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a JSON repair specialist. The user will give you a malformed JSON output. "
                    "Return ONLY the corrected, valid JSON object. No explanation. No markdown fences."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Fix the following into valid JSON with all the same keys. "
                    "Do not omit any keys. Do not add new keys.\n\n"
                    f"{broken_output}"
                ),
            },
        ]
        repaired = self._chat_completion(messages, max_tokens=2048)
        return self._extract_json_block(repaired)

    # ── Gap-fill secondary call ────────────────────────────────────────────────

    def _fill_gaps(
        self,
        scheme: SchemeInput,
        evidence_text: str,
        partial: dict[str, Any],
    ) -> dict[str, Any]:
        """
        If key fields are still empty after primary extraction, perform a
        targeted second call asking the model to look specifically for missing data.
        """
        missing = [f for f in _KEY_FIELDS if not partial.get(f)]
        if not missing:
            return partial

        logger.info(
            "Gap-fill triggered for '%s': missing %s", scheme.scheme_name, missing
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": build_gap_fill_prompt(scheme.scheme_name, evidence_text, missing),
            },
        ]
        try:
            raw = self._chat_completion(messages, max_tokens=2048)
            fills = self._extract_json_block(raw)
            for key in missing:
                if key in fills and fills[key]:
                    partial[key] = fills[key]
                    logger.debug("Gap-fill populated '%s.%s'", scheme.scheme_name, key)
        except Exception as exc:
            logger.warning("Gap-fill failed for '%s': %s", scheme.scheme_name, exc)

        return partial

    # ── Agentic Browser Fallback ───────────────────────────────────────────────

    def decide_browser_action(
        self, scheme_name: str, dom_summary: str, missing_fields: list[str]
    ) -> dict[str, Any]:
        """
        Interactive ReAct fallback agent decision step.
        """
        logger.info(
            "Agentic browser decision requested for '%s'. Missing: %s",
            scheme_name, missing_fields
        )
        prompt = BROWSER_AGENT_PROMPT.format(
            missing_fields=", ".join(missing_fields),
            dom_summary=dom_summary
        )
        messages = [{"role": "user", "content": prompt}]
        try:
            raw = self._chat_completion(messages, max_tokens=512)
            return self._extract_json_block(raw)
        except Exception as exc:
            logger.warning("Browser agent decision failed: %s", exc)
            return {"action": "done", "id": 0}

    # ── Public interface ───────────────────────────────────────────────────────

    def analyze_scheme(
        self, scheme: SchemeInput, evidence_text: str
    ) -> tuple[SchemeInsight, str]:
        """
        Primary extraction: crawl evidence → structured SchemeInsight.

        Returns (SchemeInsight, raw_llm_response_text).
        Raises on unrecoverable failure — caller should catch and create SchemeInsight.empty().
        """
        if not evidence_text.strip():
            logger.warning(
                "Empty evidence text for '%s' — LLM will return low-confidence result.",
                scheme.scheme_name,
            )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_analysis_prompt(scheme, evidence_text)},
        ]

        raw = self._chat_completion(messages)

        # JSON extraction with repair fallback
        try:
            payload = self._extract_json_block(raw)
        except ValueError:
            logger.warning(
                "Primary JSON parse failed for '%s'. Attempting repair.",
                scheme.scheme_name,
            )
            try:
                payload = self._repair_json(raw, scheme.scheme_name)
            except Exception as exc:
                logger.error(
                    "JSON repair also failed for '%s': %s", scheme.scheme_name, exc
                )
                return SchemeInsight.empty(f"LLM output could not be parsed: {exc}"), raw

        # Gap-fill if key fields are missing
        payload = self._fill_gaps(scheme, evidence_text, payload)

        # Parse into Pydantic model (tolerant — extra fields are ignored)
        try:
            insight = SchemeInsight.model_validate(payload)
        except Exception as exc:
            logger.error(
                "SchemeInsight validation failed for '%s': %s. Payload: %s",
                scheme.scheme_name,
                exc,
                str(payload)[:500],
            )
            return SchemeInsight.empty(f"LLM output validation failed: {exc}"), raw

        logger.info(
            "LLM analysis complete for '%s': confidence=%s, objectives=%d, docs=%d",
            scheme.scheme_name,
            insight.confidence,
            len(insight.objectives),
            len(insight.required_documents),
        )
        return insight, raw

    def generate_markdown_report(self, prompt: str) -> str:
        """
        Generate a free-form Markdown report (legacy: pitch / how-to / summary).
        Returns raw Markdown string.
        """
        messages = [
            {"role": "system", "content": MARKDOWN_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]
        return self._chat_completion(messages, max_tokens=self.settings.llm.max_tokens)

    def generate_markdown_report_with_system(self, system_prompt: str, user_prompt: str) -> str:
        """
        Generate a Markdown report with a custom system prompt.
        Used by the 8-file business document generator which uses
        BUSINESS_DOCS_SYSTEM_PROMPT instead of the generic MARKDOWN_SYSTEM_PROMPT.
        Returns raw Markdown string.
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        return self._chat_completion(messages, max_tokens=self.settings.llm.max_tokens)
