import os
import argparse
import logging
from pprint import pprint

os.environ["HF_HUB_OFFLINE"] = "1"  # Force HuggingFace to use local cache

from dotenv import load_dotenv
load_dotenv()

from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from ..config import load_settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
logger = logging.getLogger("pinecone_check")

def check_vector_db(query: str = None):
    settings = load_settings()
    index_name = settings.vector_db.index_name

    api_key = os.environ.get("PINECONE_API_KEY")
    if not api_key:
        logger.error("PINECONE_API_KEY not found in environment.")
        return

    pc = Pinecone(api_key=api_key)
    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        logger.error(f"Pinecone index '{index_name}' does not exist.")
        return

    logger.info(f"Connected to Pinecone index: {index_name}")
    index = pc.Index(index_name)
    stats = index.describe_index_stats()
    
    logger.info(f"Index Statistics:")
    logger.info(f"  Dimension: {stats.get('dimension')}")
    logger.info(f"  Total Vector Count: {stats.get('total_vector_count')}")
    
    if query:
        logger.info(f"Performing test query: '{query}'")
        embeddings = HuggingFaceEmbeddings(
            model_name=settings.vector_db.embedding_model,
            model_kwargs={'device': 'cpu'}
        )
        vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
        
        results = vectorstore.similarity_search_with_score(query, k=3)
        logger.info(f"Found {len(results)} matches.")
        for i, (doc, score) in enumerate(results):
            logger.info(f"\n--- Match {i+1} (Score: {score:.4f}) ---")
            logger.info(f"Source: {doc.metadata.get('source_file', 'Unknown')}")
            logger.info(f"Scheme: {doc.metadata.get('scheme_name', 'Unknown')}")
            # print snippet
            snippet = doc.page_content.replace('\n', ' ')[:200]
            logger.info(f"Content snippet: {snippet}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Pinecone Vector DB stats and optionally run a test query.")
    parser.add_argument("--query", "-q", type=str, default="What are the financial benefits for startups?", help="Test query to run against the DB.")
    args = parser.parse_args()
    
    check_vector_db(args.query)
