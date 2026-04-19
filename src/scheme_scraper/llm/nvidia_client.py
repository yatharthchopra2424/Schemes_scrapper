"""
NVIDIA LLM Client — OpenAI-compatible API wrapper
──────────────────────────────────────────────────
Supports:
  • Structured JSON extraction with retry + JSON repair
  • Gap-fill secondary call when key fields are missing
  • Plain Markdown report generation
  • Exponential backoff via tenacity
  • Robust JSON extraction from fenced and raw responses
"""
from __future__ import annotations

import json
import logging
import os
import re
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

# Fields that, if all empty, will trigger a gap-fill secondary call
_KEY_FIELDS = [
    "eligibility",
    "financial_support",
    "application_process",
    "benefits",
    "implementing_agency",
]


class NvidiaLLMClient:
    """Thread-safe NVIDIA LLM client for scheme intelligence extraction."""

    def __init__(self, settings: AppSettings):
        self.settings = settings
        api_key = os.environ.get("NVIDIA_API_KEY", "")
        if not api_key:
            raise RuntimeError(
                "NVIDIA_API_KEY is missing. Set it in your .env file or environment."
            )

        self.client = OpenAI(
            base_url=self.settings.llm.base_url,
            api_key=api_key,
            timeout=self.settings.llm.timeout_seconds,
            max_retries=0,                      # We handle retries via tenacity
        )
        self.model = self.settings.llm.model
        logger.info("LLM client initialised. Model: %s | Base: %s", self.model, self.settings.llm.base_url)

    # ── Core completion ────────────────────────────────────────────────────────

    def _chat_completion(
        self,
        messages: list[dict[str, Any]],
        max_tokens: int | None = None,
    ) -> str:
        """
        Call the API with tenacity retries for transient errors.
        Returns the raw string content of the first choice.
        """
        retrying = Retrying(
            retry=retry_if_exception_type((APIConnectionError, APITimeoutError)),
            stop=stop_after_attempt(self.settings.llm.max_retries + 1),
            wait=wait_exponential(multiplier=2, min=2, max=30),
            reraise=True,
        )

        effective_max_tokens = max_tokens or self.settings.llm.max_tokens

        for attempt in retrying:
            with attempt:
                t0 = time.perf_counter()
                try:
                    completion = self.client.chat.completions.create(
                        model=self.model,
                        messages=cast(Any, messages),
                        temperature=self.settings.llm.temperature,
                        top_p=self.settings.llm.top_p,
                        max_tokens=effective_max_tokens,
                        stream=False,
                    )
                    content = completion.choices[0].message.content or ""
                    elapsed = time.perf_counter() - t0
                    usage = completion.usage
                    if usage:
                        logger.debug(
                            "LLM response: %d prompt + %d completion tokens in %.1fs",
                            usage.prompt_tokens,
                            usage.completion_tokens,
                            elapsed,
                        )
                    else:
                        logger.debug("LLM response received in %.1fs", elapsed)
                    return content
                except APIStatusError as exc:
                    # 4xx errors are not retryable — log and re-raise immediately
                    logger.warning(
                        "LLM API status error %d: %s", exc.status_code, exc.message
                    )
                    raise

        raise RuntimeError("LLM completion failed after all retries")

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
