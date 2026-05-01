@echo off
setlocal enabledelayedexpansion

echo.
echo  ==============================================================
echo        INFOU SCHEME RAG API (FASTAPI)
echo  ==============================================================
echo.

set SCRIPT_DIR=%~dp0
set VENV_PYTHON="%SCRIPT_DIR%.venv\Scripts\python.exe"

if not exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    echo  [ERROR] Virtual environment not found at .venv\
    echo          Please run:  python -m venv .venv
    echo          Then:        .venv\Scripts\pip install -e .
    echo          And:         .venv\Scripts\pip install "fastapi[all]" langchain langchain-huggingface langchain-pinecone langchain-nvidia-ai-endpoints pinecone-client sentence-transformers
    pause & exit /b 1
)

echo Starting FastAPI server using Uvicorn...
echo The Chatbot API will be available at http://127.0.0.1:8000/docs
echo.

"%SCRIPT_DIR%.venv\Scripts\uvicorn.exe" src.scheme_scraper.api.main:app --reload
