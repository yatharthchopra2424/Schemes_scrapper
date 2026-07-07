# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The ECGC Export Credit Guarantee Schemes are administered by the Export Credit Guarantee Corporation of India Limited (ECGC), a wholly-owned Government of India enterprise under the Ministry of Commerce and Industry. The scheme provides credit guarantee covers to protect Indian exporters against payment defaults by overseas buyers due to commercial and political risks, including insolvency, protracted default, or events like war and civil disturbance. It facilitates easier access to export finance from banks by mitigating risk, thereby enhancing the creditworthiness of exporters and supporting both pre-shipment and post-shipment finance. The scheme operates on a rolling basis with applications accepted throughout the year based on export transactions. The official application portal is https://www.ecgc.in, and support is available via email at info@ecgc.in or helpline 1800-22-7788.

### Objectives
- Provide credit guarantee covers to protect exporters against payment defaults by overseas buyers  
- Facilitate easier access to export finance from banks and financial institutions  
- Promote Indian exports by mitigating commercial and political risks  
- Support MSME exporters through tailored guarantee products  
- Enhance competitiveness of Indian goods and services in international markets  

### Eligibility Matrix
| Eligibility Criteria | Details | Source |
|----------------------|---------|--------|
| **Applicant Type** | Indian exporters (including MSMEs) engaged in export of goods or services who have obtained an export order and require credit protection against buyer default. Banks lending to such exporters can also avail guarantees to secure their export credit exposure. | KEY FACTS |
| **Geographic Scope** | Pan-India | KEY FACTS |
| **Required Documents** | 1. Export order or contract<br>2. Commercial invoice<br>3. Bill of lading or airway bill<br>4. Buyer details and creditworthiness information<br>5. Bank sanction letter (if seeking finance)<br>6. Export credit guarantee application form<br>7. RCMC or IEC certificate<br>8. GST registration certificate | KEY FACTS |
| **Target Beneficiaries** | Exporters; Banks; MSME | KEY FACTS |
| **Ineligibility** | Fraudulent claims or misrepresentation lead to rejection and legal action. Policy must be obtained before shipment or extension of credit. Certain high-risk countries or buyers may be excluded or require higher premium. | KEY FACTS |

### Benefits & Financial Support
| Benefit Type | Details | Source |
|--------------|---------|--------|
| **Coverage Limit** | ECGC provides credit guarantee covers typically up to 90% of the export value | KEY FACTS |
| **Risk Coverage** | Protection against commercial and political risks, including buyer default due to insolvency, protracted default, or political events | KEY FACTS |
| **Financial Support** | Enables banks to extend pre-shipment and post-shipment finance to exporters on better terms | KEY FACTS |
| **Additional Benefits** | Improved access to bank finance, enhanced creditworthiness, coverage for both pre-shipment and post-shipment risks, support for export bill discounting and collection | KEY FACTS |
| **Claim Settlement** | Claims are settled upon buyer default due to insolvency, protracted default, or political events. Payments are made after exhaustion of legal remedies and proof of default. | KEY FACTS |
| **Premium** | Premium is paid based on risk assessment and coverage amount | KEY FACTS |

### Application Process Flowchart
```mermaid
flowchart TD
    A[Exporter or Bank Identifies Export Opportunity] --> B[Obtain Export Order/Contract]
    B --> C[Gather Required Documents:<br/>Export Order, Invoice, BL/AWB, Buyer Details, Bank Sanction (if needed), RCMC/IEC, GST Cert, Application Form]
    C --> D[Submit Application to ECGC via Portal or Branch]
    D --> E[ECGC Evaluates Risk & Buyer Creditworthiness]
    E --> F{Risk Acceptable?}
    F -->|Yes| G[ECGC Issues Credit Guarantee Policy]
    F -->|No| H[Application Rejected with Reasons]
    G --> I[Exporter Pays Premium Based on Risk Assessment]
    I --> J[Policy Issued; Can Be Used to Secure Bank Finance]
    J --> K[Shipment Made & Credit Extended]
    K --> L{Buyer Default?}
    L -->|No| M[Policy Expires; No Claim]
    L -->|Yes| N[File Claim with ECGC:<br/>Proof of Default, Exhaustion of Legal Remedies, Supporting Docs]
    N --> O[ECGC Processes Claim]
    O --> P{Claim Valid?}
    P -->|Yes| Q[ECGC Settles Claim (Up to 90% of Export Value)]
    P -->|No| R[Claim Rejected; Legal Recourse Available]
    Q --> S[Exporter/Bank Receives Compensation]
    style A fill:#e3f2fd,stroke:#1565c0
    style Q fill:#c8e6c9,stroke:#2e7d32
    style H fill:#ffebee,stroke:#c62828
    style R fill:#ffebee,stroke:#c62828
```

> **Key Takeaway**: The application process is document-intensive and risk-based. ECGC does not lend directly but provides guarantees that enable banks to finance exporters. Claims require proof of default and exhaustion of legal remedies, making timely documentation critical.

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage:** Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage:** Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage:** Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage:** Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage:** Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage:** Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage:** Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage:** Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.