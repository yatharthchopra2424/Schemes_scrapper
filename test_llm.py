import logging
import time
from typing import Any, cast
import os
import sys

# Fix Windows console charmap encoding issues
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

from src.scheme_scraper.config import AppSettings
from src.scheme_scraper.llm.nvidia_client import NvidiaLLMClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-8s | %(message)s")
logger = logging.getLogger("test_llm")

def test_deepseek_connection():
    logger.info("Initializing LLM settings...")
    settings = AppSettings()
    
    logger.info("Connecting to NVIDIA API using model: %s", settings.llm.model)
    client = NvidiaLLMClient(settings)
    
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant. Respond in Markdown."},
        {"role": "user", "content": "Explain the concept of Production Linked Incentive (PLI) schemes in India in 3 short bullet points."}
    ]
    
    logger.info("Sending test request to LLM (small prompt)...")
    t0 = time.time()
    try:
        kwargs = {
            "model": client.model,
            "messages": messages,
            "temperature": settings.llm.temperature,
            "top_p": settings.llm.top_p,
            "max_tokens": 1024,
            "stream": False,
        }
        if "nemotron" in client.model.lower():
            logger.info("Nemotron model detected. Injecting extra_body kwargs (enable_thinking: false).")
            kwargs["extra_body"] = {"chat_template_kwargs": {"enable_thinking": False}, "reasoning_budget": 0}
        elif "deepseek" in client.model.lower():
            logger.info("DeepSeek model detected. Injecting extra_body kwargs (thinking: false, reasoning_effort: low).")
            kwargs["extra_body"] = {"chat_template_kwargs": {"thinking": False, "reasoning_effort": "low"}}
            
        completion = client.client.chat.completions.create(**kwargs)
        elapsed = time.time() - t0
        
        content = completion.choices[0].message.content or ""
        
        logger.info("Success! Response received in %.2f seconds.", elapsed)
        print("\n" + "="*50)
        print("LLM RESPONSE:")
        print("="*50)
        print(content)
        print("="*50 + "\n")
        
    except Exception as e:
        logger.error("LLM Request Failed: %s", e)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.environ.get("NVIDIA_API_KEY"):
        logger.error("NVIDIA_API_KEY is not set in your environment. Make sure it is loaded via .env")
    else:
        test_deepseek_connection()
        test_deepseek_connection()
