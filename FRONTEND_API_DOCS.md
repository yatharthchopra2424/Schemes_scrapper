# Infou Scheme Scraper - Frontend API Integration Guide

This document outlines the available endpoints for the **Infou Scheme RAG API**. It is designed to be easily integrated into frontend applications.

## Base URL
When running locally via `run_api.cmd`, the base URL is:
```
http://127.0.0.1:8000
```
> **Note**: Swagger UI documentation is also automatically available at `/docs` when the server is running.

---

## 1. Full RAG Chat API (Internal / Detailed Use)

This endpoint provides highly detailed, intelligent answers based on the scheme database and includes the exact source files where the data was found.

- **Endpoint**: `/chat`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Payload
```json
{
  "query": "What are the eligibility criteria for PM Kisan?"
}
```

### Response Payload (200 OK)
```json
{
  "answer": "The PM Kisan scheme provides income support to all landholding farmer families. The eligibility criteria require the farmer to possess cultivable land...",
  "referenced_sources": [
    "pm_kisan_guidelines.pdf",
    "agriculture_schemes_2023.docx"
  ]
}
```

---

## 2. Restricted Chat API (External / Public Use)

This endpoint is heavily restricted to prevent sensitive data leaks. It forces the AI to reply with only a **single, simple sentence**. It will strictly **avoid** outputting detailed explanations, financial amounts, or sensitive eligibility data.

- **Endpoint**: `/chat-restricted`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Payload
```json
{
  "query": "What are the benefits of PM Kisan?"
}
```

### Response Payload (200 OK)
```json
{
  "answer": "PM Kisan is a government initiative that provides basic income support to farmers."
}
```
> **Note**: This endpoint intentionally omits the `referenced_sources` array to further prevent any database path/file leakage to public users.

---

## Error Handling

Your frontend should handle the following HTTP error status codes gracefully:

- **`503 Service Unavailable`**: 
  - *Reason*: Returned if the Pinecone or NVIDIA API keys are missing in the backend, meaning the RAG pipeline failed to initialize.
  - *Payload*: `{"detail": "RAG Pipeline is not initialized or failed to start."}`
- **`500 Internal Server Error`**: 
  - *Reason*: Returned if there is an unexpected error while the LLM is generating a response.
  - *Payload*: `{"detail": "<Error message>"}`
- **`422 Unprocessable Entity`**:
  - *Reason*: Returned if the request payload is malformed or missing the `query` field.
