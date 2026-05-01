import os
import logging
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from ..config import load_settings

logger = logging.getLogger(__name__)

# Load AppSettings to get Vector DB config and NVIDIA config
settings = load_settings()

if not os.environ.get("PINECONE_API_KEY"):
    logger.warning("PINECONE_API_KEY environment variable is missing. The API will fail to start if Pinecone requires it.")
if not os.environ.get("NVIDIA_API_KEY"):
    logger.warning("NVIDIA_API_KEY environment variable is missing. The API will fail to engage the LLM.")

app = FastAPI(
    title="infou_scrapper RAG API",
    description="Ask questions about scraped government schemes using Pinecone + NVIDIA LLM",
    version="1.0.0",
)

# Initialize RAG components globally
embeddings = None
vectorstore = None
retriever = None
llm = None
rag_chain = None


@app.on_event("startup")
async def startup_event():
    global embeddings, vectorstore, retriever, llm, rag_chain
    try:
        logger.info("Initializing HuggingFace Embeddings Model: %s", settings.vector_db.embedding_model)
        embeddings = HuggingFaceEmbeddings(model_name=settings.vector_db.embedding_model)
        
        logger.info("Connecting to Pinecone Index: %s", settings.vector_db.index_name)
        vectorstore = PineconeVectorStore(index_name=settings.vector_db.index_name, embedding=embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        
        logger.info("Initializing NVIDIA LLM (Model: %s, Base URL: %s)", settings.llm.model, settings.llm.base_url)
        # Using langchain_nvidia_ai_endpoints to match your existing inference stack
        llm = ChatNVIDIA(
            model=settings.llm.model, 
            base_url=settings.llm.base_url,
            temperature=0.1,  # Keep it deterministic for RAG tasks
            max_tokens=1024
        )

        system_prompt = (
            "You are a highly helpful, intelligent assistant. Use the following context to answer the user's question.\n"
            "The context contains metadata showing the source file and header where the information was matched from.\n"
            "You MUST cite your answers by explicitly mentioning the original source file at the end of your response.\n"
            "If you don't know the answer based on the context, just say you don't know and do not invent information.\n\n"
            "Context Information:\n{context}"
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        logger.info("RAG Pipeline successfully initialized and ready for requests.")

    except Exception as exc:
        logger.error("Failed to initialize RAG dependencies: %s", exc)


class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
    referenced_sources: List[str]


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not rag_chain:
        raise HTTPException(status_code=503, detail="RAG Pipeline is not initialized or failed to start.")
        
    try:
        response = rag_chain.invoke({"input": request.query})
        
        # Extract sources from metadata to return alongside the text
        sources = [doc.metadata.get("source_file") for doc in response["context"] if doc.metadata.get("source_file")]
        unique_sources = list(set(sources))

        return ChatResponse(
            answer=response["answer"],
            referenced_sources=unique_sources
        )
    except Exception as e:
        logger.error("Chat endpoint error: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
