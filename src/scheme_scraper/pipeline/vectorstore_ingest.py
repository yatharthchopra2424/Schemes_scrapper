import logging
import os
import time
from pathlib import Path
from typing import List

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
        loader = DirectoryLoader(str(artifacts_dir), glob="**/*.md", loader_cls=TextLoader)
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
            
            for split in splits:
                split.metadata["source_file"] = filename
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

        # Init embeddings (Downloads the local HuggingFace model on first run)
        embeddings = HuggingFaceEmbeddings(model_name=settings.vector_db.embedding_model)

        # Upsert
        PineconeVectorStore.from_documents(
            final_splits, 
            embeddings, 
            index_name=settings.vector_db.index_name
        )

        logger.info("Successfully ingested markdown data into Vector DB.")

    except Exception as exc:
        logger.error("Vector DB Ingestion failed: %s", exc, exc_info=True)
