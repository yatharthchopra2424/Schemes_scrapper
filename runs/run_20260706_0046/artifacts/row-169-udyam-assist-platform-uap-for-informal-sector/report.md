# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The Udyam Assist Platform (UAP) is a government initiative by the Ministry of MSME, Government of India, implemented by the Small Industries Development Bank of India (SIDBI). It facilitates the registration of Informal Micro Enterprises (IMEs) that are not registered on the Udyam Registration Portal (URP) and operate outside the GST ecosystem. The platform does not provide direct financial support but enables access to financial services by issuing a Udyam Registration Number (URN) and Udyam Assist Certificate (UAC), which are essential for classifying bank loans under Priority Sector Lending (PSL) as per RBI guidelines.

**Application Portal:** [https://udyamassist.gov.in](https://udyamassist.gov.in)  
**Status / Deadlines:** Rolling basis — no fixed deadline. Applications are accepted year-round.  
**Last Updated:** 2026  
**Implementing Agency:** Small Industries Development Bank of India (SIDBI)  
**Contact Email:** udyamassist@sidbi.in  

### Objectives
- Provide Udyam Registration to Informal Micro Enterprises (IMEs) not registered with GST authorities  
- Enable access to Priority Sector Lending (PSL) for loans to Udyam-registered IMEs  
- Facilitate integration of IMEs into digital payment ecosystems via merchant QR codes  
- Create a central digital identity (URN) for future access to governance, financial services, and digital marketplaces  
- Generate quality data for better policy interventions for the informal sector  
- Provide access to knowledge and skills development for IMEs  

### Eligibility Matrix
| Criteria | Details |
|--------|---------|
| **Target Beneficiaries** | Informal Micro Enterprises (IMEs); micro enterprises outside GST ecosystem |
| **Eligibility Condition** | IMEs not registered on Udyam Registration Portal (URP) and outside GST ecosystem |
| **Registration Mechanism** | IMEs cannot register directly; must approach a Designated Agency (DA) for assistance |
| **Designated Agencies (DAs)** | Scheduled Commercial Banks (SCBs), Micro Finance Institutions (MFIs), Non Banking Financial Companies (NBFCs), etc., or any other agency approved by MoMSME |
| **Data Sharing Requirement** | DAs must share customer data with the consent of IME customers |
| **Direct Registration Bar** | Informal Micro Enterprises cannot register directly on UAP; must use a DA |

### Benefits & Financial Support
| Benefit Type | Details |
|--------------|---------|
| **Direct Financial Support** | None. UAP does not provide grants, loans, or subsidies. |
| **Indirect Financial Access** | URN enables classification of bank loans under Priority Sector Lending (PSL) per RBI guidelines, encouraging higher credit flow from banks. |
| **Digital Payments** | Facilitates issuance of merchant QR codes for digital payments. |
| **Digital Identity** | URN acts as a passport for access to digital systems in governance, financial services, and marketplaces. |
| **Certification** | Registered IMEs receive Udyam Assist Certificate (UAC). |
| **Policy & Data** | Data generated supports policy interventions for the informal sector. |
| **Knowledge & Skills** | Access to knowledge and skills development is provided. |

> **Key Caveats**  
> - Mere sharing of data by DAs does not entitle IMEs to URN/UAC; issuance is subject to validation as per program methodology.  
> - The Udyam Assist Platform does not provide direct financial benefits; it enables access to financial services through registration.  
> - Data shared by DAs must be with the consent of the IME customers.  
> - The platform is governed by the guidelines of the MSME Formalisation Project and Udyam Assist Platform terms and conditions.  
> - UAP does not grant permission to reproduce copyrighted material; authorization must be obtained from MoMSME.  
> - Users are solely responsible for compliance with UAP and MSME Formalisation terms.  
> - MoMSME/SIDBI shall not be liable for any damages arising from use of UAP.  

### Application Process Flowchart
```mermaid
flowchart TD
    A[Designated Agency (DA) Preparation] --> B[DA Registers on UAP]
    B --> C{DA Type?}
    C -->|NBFC/NBFC-MFI| D[Submit RBI Registration Certificate]
    C -->|MFI (non-NBFC)| E[Submit SRO Confirmation Letter]
    C -->|Other DA (SCB, etc.)| F[Proceed]
    D --> G[Submit DA Letter of Authorisation + RBI Cert]
    E --> H[Submit DA Letter of Authorisation + SRO Letter]
    F --> I[Submit DA Letter of Authorisation]
    G --> J[Accept Terms and Conditions]
    H --> J
    I --> J
    J --> K[SIDBI Reviews Application]
    K --> L{Approved?}
    L -->|No| M[Rejection / Resubmit]
    L -->|Yes| N[Receive Login Credentials]
    N --> O[Nodal Officer Adds Up to 5 Sub-users]
    O --> P[DA Uploads IME Customer Data via SFTP/Smart EXCEL]
    P --> Q[UAP Processes Data & Validates]
    Q --> R[Generate URN & UAC]
    R --> S[URN/UAC Made Available to DA]
    S --> T[DA Informs IME via SMS/Email]
    T --> U[IME Downloads UAC from Portal]
    style A fill:#e3f2fd,stroke:#1565c0
    style N fill:#fff3e0,stroke:#ef6c00
    style U fill:#e8f5e9,stroke:#2e7d32
```

### Application Process Steps (Detailed)
1. **DA Registration Initiation**: Designated Agencies (DAs) such as banks, NBFCs, MFIs must register on the Udyam Assist Platform (www.udyamassist.gov.in) by submitting a Letter of Authorisation designating a Nodal Officer.  
2. **Category-Specific Documents**:  
   - NBFCs and NBFC-MFIs must additionally submit their RBI registration certificate.  
   - MFIs not classified as NBFCs must submit a letter of confirmation from their Self-Regulatory Organisation (SRO).  
3. **Terms Acceptance**: DAs must accept the Terms and Conditions of the platform.  
4. **Agency Approval**: Upon approval by the Implementing Agency (SIDBI), DAs receive login credentials.  
5. **User Setup**: The DA’s Nodal Officer can add up to 5 sub-users for platform access.  
6. **Data Upload**: Registered DAs upload data of their Informal Micro Enterprise (IME) customers via SFTP, smart EXCELs, or other approved protocols.  
7. **Data Processing**: The Udyam Assist Platform processes the data, conducts validations, and generates Udyam Registration Number (URN) and Udyam Assist Certificate (UAC).  
8. **Credential Delivery**: The URN and UAC are made available to the DA, which then informs the IME via SMS/Email.  
9. **Certificate Access**: IMEs can download the UAC from the portal (www.udyamassist.gov.in) after validation.  
10. **Ongoing Monitoring**: DAs are provided with a Dashboard for MIS/reports to monitor registration status of IMEs onboarded by them.  

### Key Statistics (as of 05 Jul 2026)
| Metric | Value |
|-------|-------|
| Total Registration & Classified | 3,82,74,366 |
| Micro Enterprises Registered | 3,82,74,366 |
| Total Employment Generated | 5,40,53,905 |
| Launch Date | January 11, 2023 |

### Supporting Evidence Sources
- Application Portal: [https://udyamassist.gov.in](https://udyamassist.gov.in)  
- Factsheet: [https://udyamassist.gov.in](https://udyamassist.gov.in) (Dated: 05 Jul 2026 10:30:00 AM)  
- MSME Formalisation Details: [https://udyamassist.gov.in/msme-formalisation](https://udyamassist.gov.in/msme-formalisation)  
- FAQ: [https://udyamassist.gov.in/faq](https://udyamassist.gov.in/faq)  
- Designated Agency FAQ: [https://udyamassist.gov.in/designated-faq](https://udyamassist.gov.in/designated-faq)  
- Terms & Conditions: [https://udyamassist.gov.in/terms-condition](https://udyamassist.gov.in/terms-condition)  
- Privacy Policy: [https://udyamassist.gov.in/privacy-policy](https://udyamassist.gov.in/privacy-policy)  
- Disclaimer: [https://udyamassist.gov.in/disclaimer](https://udyamassist.gov.in/disclaimer)  
- Contact: udyamassist@sidbi.in  

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage:** Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
**Pro Tip:** Use it to quickly verify DA eligibility criteria during partner outreach — e.g., confirming whether an NBFC needs an RBI certificate or an MFI needs an SRO letter.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage:** Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
**Pro Tip:** Customize the "Problem Framing" script using the client’s actual turnover or sector (e.g., textile, retail) pulled from your CRM to increase relevance.

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage:** Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
**Pro Tip:** Attach the relevant DA document checklist (from this playbook) to your email when requesting the DA’s Letter of Authorisation or RBI certificate — reduces back-and-forth by 70%.

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage:** Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
**Pro Tip:** Color-code the Compliance Status table (e.g., Red = Missing, Yellow = Pending Review, Green = Approved) for instant visual tracking during team huddles.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage:** Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
**Pro Tip:** Set a daily 9 AM calendar reminder to update this file — delays in Stage 07 often stem from missing DA validations, which this tracker helps you anticipate.

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage:** Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
**Pro Tip:** Since UAP has no direct financials, base your fees on the value of enabled PSL access — e.g., "Our fee is 2% of the expected PSL loan amount facilitated."

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage:** Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
**Pro Tip:** Always attach Sections 8A and 8B of the COMPLIANCE_AND_LEGAL_PACK.md as PDFs — clients trust proposals more when legal safeguards are visible upfront.

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage:** Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
**Pro Tip:** Highlight the consent clause in Section 8B during signing — it shifts data-sharing liability to the client/DAs and is often overlooked.