import json
import logging
import os
from typing import Dict, Any

from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings

from ..config import AppSettings
from ..llm.nvidia_client import NvidiaLLMClient
from ..llm.consultant_prompts import (
    ELIGIBILITY_ANALYST_PROMPT,
    MASTER_CONSULTANT_PROMPT,
    CRITIQUE_PROMPT,
)

logger = logging.getLogger(__name__)

class MultiAgentOrchestrator:
    """
    The Engine: Multi-Agent Orchestration for B2B Government Schemes Consulting.
    """
    def __init__(self, settings: AppSettings):
        self.settings = settings
        self.llm_client = NvidiaLLMClient(settings)
        # Initialize Pinecone and Embeddings
        self.pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
        self.index_name = settings.vector_db.index_name
        self.embeddings = HuggingFaceEmbeddings(model_name=settings.vector_db.embedding_model)
        
    def run_pipeline(self, client_profile: Dict[str, Any], k: int = 5) -> str:
        """
        Executes the full agentic pipeline for a given client profile.
        Returns the final generated Markdown proposal.
        """
        logger.info("Starting Multi-Agent Pipeline for client: %s", client_profile.get("company_name", "Unknown"))
        
        # Agent 1: Context Retriever
        retrieved_context = self._agent_1_retriever(client_profile, k)
        if not retrieved_context.strip():
            return "Error: No relevant scheme chunks found for the given client profile."

        # Agent 2: Eligibility Analyst
        eligibility_analysis = self._agent_2_analyst(client_profile, retrieved_context)
        
        # Agent 3: Consultative Writer
        draft_markdown = self._agent_3_writer(client_profile, retrieved_context, eligibility_analysis)
        
        # Agent 4: Self-Correction / Critique
        final_markdown = self._agent_4_critique(draft_markdown)
        
        logger.info("Multi-Agent Pipeline completed successfully.")
        return final_markdown

    def _agent_1_retriever(self, client_profile: Dict[str, Any], k: int) -> str:
        """
        Agent 1: Takes the client's industry, revenue, and goals, expands the query, 
        and fetches the top k relevant chunks from Pinecone using metadata filtering.
        """
        logger.info("Agent 1: Retrieving context from Pinecone...")
        
        industry = client_profile.get("industry", "")
        goals = client_profile.get("goals", "")
        
        # Simple query expansion
        query_text = f"Government schemes, grants, and incentives for {industry}. Goals: {goals}"
        query_vector = self.embeddings.embed_query(query_text)
        
        # Build metadata filter (assuming vectorstore_ingest.py tagged them)
        # We will use a loose filter for demonstration. In production, exact tags like {"sector": industry} might be too strict
        # if the tagging isn't perfect, so we might just rely on semantic search. 
        # But per the prompt, we should demonstrate metadata filtering.
        filter_dict = {}
        if "state" in client_profile:
             # e.g., filter out schemes meant for other states. 
             # Here we assume the tag 'geographic_scope' matches the state, or is 'National'
             state = client_profile["state"]
             filter_dict["$or"] = [
                 {"state": {"$in": [state, "National", "All India"]}},
                 {"geographic_scope": {"$in": [state, "National", "All India"]}}
             ]
             
        index = self.pc.Index(self.index_name)
        
        try:
            results = index.query(
                vector=query_vector,
                top_k=k,
                include_metadata=True,
                filter=filter_dict if filter_dict else None
            )
        except Exception as e:
            logger.warning("Pinecone query with filter failed (%s). Retrying without filter.", e)
            results = index.query(
                vector=query_vector,
                top_k=k,
                include_metadata=True
            )

        # Structure the Pinecone output
        formatted_context = ""
        for match in results.get("matches", []):
            metadata = match.get("metadata", {})
            scheme_name = metadata.get("scheme_name", metadata.get("source_file", "Unknown Source"))
            chunk_text = metadata.get("text", "") 
            score = match.get("score", 0.0)
            
            formatted_context += f"### Source: {scheme_name}\n"
            formatted_context += f"Extract: {chunk_text}\n"
            formatted_context += f"Relevance Score: {score:.4f}\n\n"
            
        logger.info("Agent 1 retrieved %d chunks.", len(results.get("matches", [])))
        return formatted_context

    def _agent_2_analyst(self, client_profile: Dict[str, Any], retrieved_context: str) -> str:
        """
        Agent 2: Compares the Client JSON against the retrieved Pinecone chunks.
        Calculates a 'Probability of Success' score and identifies bottlenecks.
        """
        logger.info("Agent 2: Analyzing eligibility...")
        client_json_str = json.dumps(client_profile, indent=2)
        prompt = ELIGIBILITY_ANALYST_PROMPT.format(
            client_json_data=client_json_str,
            pinecone_rag_context=retrieved_context
        )
        
        # We can use the simple system generation or directly user prompt
        analysis = self.llm_client.generate_markdown_report_with_system(
            system_prompt="You are an expert Eligibility Analyst.",
            user_prompt=prompt
        )
        return analysis

    def _agent_3_writer(self, client_profile: Dict[str, Any], retrieved_context: str, eligibility_analysis: str) -> str:
        """
        Agent 3: Drafts the final Markdown using the master prompt.
        """
        logger.info("Agent 3: Drafting consultative proposal...")
        client_json_str = json.dumps(client_profile, indent=2)
        industry = client_profile.get("industry", "your sector")
        
        prompt = MASTER_CONSULTANT_PROMPT.format(
            client_json_data=client_json_str,
            pinecone_rag_context=retrieved_context,
            agent_2_analysis=eligibility_analysis,
            client_industry=industry
        )
        
        draft = self.llm_client.generate_markdown_report_with_system(
            system_prompt="You are an elite B2B Government Schemes Consultant.",
            user_prompt=prompt
        )
        return draft

    def _agent_4_critique(self, draft_markdown: str) -> str:
        """
        Agent 4 (Self-Correction): Final LLM pass to ensure no hallucinations and correct formatting.
        """
        logger.info("Agent 4: Critiquing and self-correcting draft...")
        prompt = CRITIQUE_PROMPT.format(draft_markdown=draft_markdown)
        
        final_version = self.llm_client.generate_markdown_report_with_system(
            system_prompt="You are a Quality Assurance AI for a B2B Consulting Firm.",
            user_prompt=prompt
        )
        return final_version
