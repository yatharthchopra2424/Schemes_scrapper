"""
Agentic Browser Fallback Pipeline

Allows the pipeline to dynamically interact with pages when static crawling misses key fields.
"""
from __future__ import annotations

import logging
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from ..models import SchemeInput
from ..llm.nvidia_client import NvidiaLLMClient
from ..extract.html_extract import extract_visible_text

logger = logging.getLogger(__name__)

JS_MARK_ELEMENTS = """
(function() {
    let elements = document.querySelectorAll('a, button, [role="button"], details, summary');
    let interactables = [];
    let idCounter = 1;
    
    for (let el of elements) {
        // Skip hidden elements
        if (el.offsetWidth === 0 || el.offsetHeight === 0) continue;
        
        // Skip elements with no text
        let text = (el.innerText || el.textContent || "").trim();
        if (!text) continue;
        
        let tag = el.tagName.toLowerCase();
        el.setAttribute('data-agent-id', idCounter);
        
        interactables.push({
            id: idCounter,
            tag: tag,
            text: text.substring(0, 50)
        });
        idCounter++;
    }
    return interactables;
})();
"""

JS_CLICK_ELEMENT = """
var el = document.querySelector('[data-agent-id="' + arguments[0] + '"]');
if (el) {
    el.click();
    return true;
}
return false;
"""

def run_agentic_fallback(
    driver: WebDriver,
    scheme: SchemeInput,
    missing_fields: list[str],
    llm_client: NvidiaLLMClient,
    max_steps: int = 5
) -> str:
    """
    Spins up an interactive loop powered by the LLM to find missing information.
    Returns appended evidence text discovered during the interactions.
    """
    logger.info("Initiating agentic fallback for '%s'. Missing: %s", scheme.scheme_name, missing_fields)
    
    try:
        driver.get(scheme.scheme_url)
        time.sleep(3) # Wait for initial render
    except Exception as exc:
        logger.error("Agentic fallback failed to load URL '%s': %s", scheme.scheme_url, exc)
        return ""

    appended_evidence = []
    
    for step in range(max_steps):
        logger.info("Agentic step %d for '%s'", step + 1, scheme.scheme_name)
        
        # 1. Grab visible text
        page_source = driver.page_source
        text = extract_visible_text(page_source)
        appended_evidence.append(f"--- AGENT STEP {step + 1} PAGE TEXT ---\n{text[:5000]}")
        
        # 2. Inject JS to mark and inventory interactable elements
        try:
            interactables = driver.execute_script(JS_MARK_ELEMENTS)
        except Exception as exc:
            logger.warning("Failed to extract DOM for '%s': %s", scheme.scheme_name, exc)
            break
            
        if not interactables:
            logger.info("No interactable elements found.")
            break
            
        # Format simple DOM
        dom_lines = []
        for item in interactables:
            dom_lines.append(f"[ID: {item['id']}] <{item['tag']}>: {item['text']}")
        dom_summary = "\\n".join(dom_lines)[:5000] # Prevents massive token overload
        
        # 3. Ask LLM what to do
        decision = llm_client.decide_browser_action(scheme.scheme_name, dom_summary, missing_fields)
        action = decision.get("action", "done")
        el_id = decision.get("id", 0)
        
        if action == "done":
            logger.info("Agent concluded searching.")
            break
        elif action == "wait":
            logger.info("Agent decided to wait.")
            time.sleep(3)
        elif action == "click":
            logger.info("Agent decided to click ID=%s", el_id)
            try:
                success = driver.execute_script(JS_CLICK_ELEMENT, el_id)
                if not success:
                    logger.warning("Agent attempted to click non-existent ID=%s", el_id)
                time.sleep(3) # Wait for navigation/accordion
            except Exception as exc:
                logger.warning("Agent click failed: %s", exc)
        else:
            logger.warning("Agent returned unknown action: %s", action)
            break
            
    # Compile text gathered
    return "\\n\\n".join(appended_evidence)
