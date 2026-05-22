import logging
import os
import time
import argparse
from pathlib import Path
from typing import List

import os
os.environ["HF_HUB_OFFLINE"] = "1"  # Force HuggingFace to use local cache and prevent network requests

from dotenv import load_dotenv
load_dotenv()

from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document

from ..config import AppSettings

logger = logging.getLogger(__name__)

def ingest_markdown_data(artifacts_dir: Path, settings: AppSettings) -> None:
    """
    Scans the given artifacts directory for markdown `.md` files
    and ingests them into a Pinecone vector database using HuggingFace sentence transformers.
    """
    logger.info("Starting Vector DB Ingestion from %s", artifacts_dir)

    # Ensure PINECONE_API_KEY gets set internally if provided elsewhere, or assume it's in the environment.
    if not os.environ.get("PINECONE_API_KEY"):
        logger.warning("PINECONE_API_KEY not found in environment. Ingestion might fail unless using a local mock.")

    try:
        # Load all .md files from the artifacts directory (recursive)
        loader = DirectoryLoader(str(artifacts_dir), glob="**/*.md", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
        docs = loader.load()
        if not docs:
            logger.info("No Markdown documents found to ingest.")
            return

        logger.info("Loaded %d markdown documents. Starting chunking...", len(docs))

        # Markdown splitting strategy
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
            ("####", "Header 4"),
        ]
        md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

        all_splits: List[Document] = []
        for doc in docs:
            # Splitting text
            splits = md_splitter.split_text(doc.page_content)
            
            # Attach the original source filename to the chunk metadata 
            # to keep precise tracking for references
            source_path = doc.metadata.get("source", "unknown.md")
            filename = os.path.basename(source_path)
            
            # Try to load ai_summary.json from the same directory to attach metadata
            scheme_dir = os.path.dirname(source_path)
            summary_path = os.path.join(scheme_dir, "ai_summary.json")
            metadata_tags = {}
            if os.path.exists(summary_path):
                try:
                    import json
                    with open(summary_path, "r", encoding="utf-8") as f:
                        summary = json.load(f)
                        metadata_tags["scheme_name"] = summary.get("scheme_name", "")
                        metadata_tags["ministry"] = summary.get("ministry_or_category", "")
                        metadata_tags["geographic_scope"] = summary.get("geographic_scope", "")
                        
                        # Extract implied sector and revenue constraints for Agent 1 filtering
                        # For simplicity we extract keywords. A more advanced extraction could use LLM here.
                        metadata_tags["sector"] = summary.get("target_beneficiaries", "") 
                        metadata_tags["state"] = summary.get("geographic_scope", "")
                except Exception as e:
                    logger.warning("Could not read ai_summary.json for %s: %s", filename, e)

            for split in splits:
                split.metadata["source_file"] = filename
                # Inject parsed metadata for Pinecone RAG
                for k, v in metadata_tags.items():
                    if v:
                        split.metadata[k] = str(v)
            all_splits.extend(splits)

        # Secondary split for massive chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.vector_db.chunk_size, 
            chunk_overlap=settings.vector_db.chunk_overlap
        )
        final_splits = text_splitter.split_documents(all_splits)

        index_name = settings.vector_db.index_name
        pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
        existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

        if index_name not in existing_indexes:
            logger.info("Pinecone index '%s' does not exist. Creating a Serverless index...", index_name)
            pc.create_index(
                name=index_name,
                dimension=384, # all-MiniLM-L6-v2 implies 384 dimensions
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )
            # Wait for the index to be ready
            while not pc.describe_index(index_name).status["ready"]:
                time.sleep(1)
            logger.info("Index '%s' is successfully created and ready.", index_name)
        else:
            logger.info("Connecting to existing Pinecone index '%s'.", index_name)

        logger.info("Chunking complete. Upserting %d chunks to Pinecone index: %s", len(final_splits), settings.vector_db.index_name)

        # Init embeddings (Uses strictly offline cached model on CPU)
        embeddings = HuggingFaceEmbeddings(
            model_name=settings.vector_db.embedding_model,
            model_kwargs={'device': 'cpu'}
        )

        # Upsert
        t0 = time.time()
        PineconeVectorStore.from_documents(
            final_splits, 
            embeddings, 
            index_name=settings.vector_db.index_name
        )
        elapsed_time = time.time() - t0

        logger.info("Successfully ingested markdown data into Vector DB in %.2f seconds.", elapsed_time)

    except Exception as exc:
        logger.error("Vector DB Ingestion failed: %s", exc, exc_info=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest markdown artifacts into Pinecone Vector DB.")
    parser.add_argument("--run-dir", required=False, help="Path to the run directory containing artifacts. Defaults to latest run if not specified.")
    args = parser.parse_args()

    # Setup basic logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")

    from ..config import load_settings
    settings = load_settings()

    if args.run_dir:
        run_dir = Path(args.run_dir)
    else:
        # Auto-detect latest run
        runs_path = Path("runs")
        if not runs_path.exists():
            logger.error("No 'runs' directory found and no --run-dir specified.")
            exit(1)
        subdirs = [d for d in runs_path.iterdir() if d.is_dir() and d.name.startswith("run_")]
        if not subdirs:
            logger.error("No run directories found in 'runs/'.")
            exit(1)
        run_dir = sorted(subdirs)[-1]
        logger.info(f"Targeting latest run directory: {run_dir}")

    artifacts_dir = run_dir / "artifacts"
    
    if artifacts_dir.exists():
        ingest_markdown_data(artifacts_dir, settings)
    else:
        logger.error("Artifacts directory not found: %s", artifacts_dir)
