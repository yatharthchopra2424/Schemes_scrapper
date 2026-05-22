import json
import logging
from pathlib import Path

from ..config import AppSettings
from .multi_agent import MultiAgentOrchestrator
from ..output.pdf_converter import generate_pdf_from_markdown

logging.basicConfig(level=logging.INFO)

def main():
    print("Loading settings...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    settings = AppSettings()
    
    # Assumes run from project root
    client_profile_path = Path("client_profile.json")
    if not client_profile_path.exists():
        print("client_profile.json not found!")
        return
        
    with open(client_profile_path, "r", encoding="utf-8") as f:
        client_profile = json.load(f)

    print(f"Running Multi-Agent Orchestrator for {client_profile.get('company_name')}...")
    # NOTE: To run this successfully, PINECONE_API_KEY, NVIDIA_API_KEY, etc. must be set in .env
    try:
        import time
        orchestrator = MultiAgentOrchestrator(settings)
        t0 = time.time()
        final_markdown = orchestrator.run_pipeline(client_profile, k=3)
        elapsed = time.time() - t0
        print(f"Multi-Agent Orchestrator finished in {elapsed:.2f} seconds.")
        
        output_md_path = Path("runs/test_proposal.md")
        output_md_path.parent.mkdir(parents=True, exist_ok=True)
        
        output_md_path.write_text(final_markdown, encoding="utf-8")
        print(f"Markdown generated successfully: {output_md_path}")
        
        output_pdf_path = Path("runs/pdfs/test_proposal.pdf")
        output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
        generate_pdf_from_markdown(output_md_path, output_pdf_path)
        print(f"PDF generated successfully: {output_pdf_path}")
        
    except Exception as e:
        print(f"Pipeline test failed: {e}")

if __name__ == "__main__":
    main()
