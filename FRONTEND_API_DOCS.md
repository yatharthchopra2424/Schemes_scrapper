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

## 3. Structured Scheme Recommendations API

This endpoint accepts a lead-form style JSON payload and returns a structured, ranked list of schemes the user is most likely to benefit from. It is intended for frontend automation, CRM workflows, and follow-up forms.

- **Endpoint**: `/recommend-schemes`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Payload
```json
{
  "timestamp": "2026-06-03T10:50:47.801Z",
  "source": "random_popup",
  "formId": "audit_ugs4vecvi",
  "data": {
    "name": "Aryan Sharma",
    "email": "aryan.main21@gmail.com",
    "phone": "+919650333862",
    "businessName": "Infou",
    "businessType": "Healthcare",
    "businessDescription": "it is a consultancy firm"
  }
}
```

### Response Payload (200 OK)
```json
{
  "timestamp": "2026-06-03T10:50:47.801Z",
  "source": "random_popup",
  "formId": "audit_ugs4vecvi",
  "data": {
    "name": "Aryan Sharma",
    "email": "aryan.main21@gmail.com",
    "phone": "+919650333862",
    "businessName": "Infou",
    "businessType": "Healthcare",
    "businessDescription": "it is a consultancy firm"
  },
  "searchQuery": "Indian government schemes grants subsidies loans startup recognition MSME support | Infou | Healthcare | it is a consultancy firm",
  "totalRecommendations": 1,
  "recommendations": [
    {
      "schemeName": "Startup India Seed Fund Scheme",
      "sourceFile": "row-3-startup-india-seed-fund-scheme-sisfs",
      "ministry": "Department for Promotion of Industry and Internal Trade",
      "schemeDescription": "Startup India Initiative is a flagship Government of India program launched in 2016 by DPIIT to foster innovation, support entrepreneurs, and drive sustainable economic growth. It provides recognition, tax benefits, easier compliance, IPR fast-tracking, and access to funding schemes like Fund of Funds and Seed Fund Scheme.",
      "expectedTimeline": "Not specified in available evidence.",
      "fundingRange": "Up to ₹10 lakh for incubator support and up to ₹20 lakh for seed support, subject to scheme terms.",
      "relevanceScore": 0.8421,
      "confidence": "high",
      "eligibilityMatch": "The retrieved scheme evidence appears relevant to Healthcare.",
      "benefitReason": "This scheme was ranked highly because the indexed evidence overlaps with the submitted business profile and profile keywords: Business type: Healthcare, Keyword match: consultancy, Keyword match: firm.",
      "matchedSignals": [
        "Business type: Healthcare",
        "Keyword match: consultancy",
        "Keyword match: firm"
      ],
      "evidenceExcerpt": "...",
      "recommendedNextStep": "Review the scheme details for Startup India Seed Fund Scheme and confirm eligibility against the evidence in row-3-startup-india-seed-fund-scheme-sisfs."
    }
  ],
  "truncated": true
}
```

### Response Field Notes
- `recommendations` is ordered by the backend ranking logic, with the most relevant scheme first.
- `confidence` is a simple qualitative label: `high`, `medium`, or `low`.
- `schemeDescription` gives a short plain-language description of the scheme.
- `expectedTimeline` gives the estimated time to completion or says `Not specified in available evidence.` when the source text does not contain a reliable estimate.
- `fundingRange` gives the funding amount or range that appears in the source evidence, or `Not specified in available evidence.` when unavailable.
- `matchedSignals` explains why the scheme was selected in plain language.
- `truncated: true` means more matches may exist than the response returned.
- The default behavior is to return up to five recommendation items.

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
