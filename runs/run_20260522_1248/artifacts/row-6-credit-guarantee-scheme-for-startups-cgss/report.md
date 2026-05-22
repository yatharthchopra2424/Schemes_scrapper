# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The Credit Guarantee Scheme for Startups (CGSS) is a loan-type scheme implemented by the National Credit Guarantee Trust Company (NCGTC) under the Ministry of Commerce and Industry (DPIIT). It provides credit guarantees to loans extended by Member Institutions (MIs) to DPIIT-recognised startups. The scheme does not provide guarantees directly to startups but through NCGTC as a trustee to MIs, who then lend to startups. The application portal is the Jan Samarth Portal: https://www.jansamarth.gov.in/. The scheme has a pan-India geographic scope and targets startups as beneficiaries.

### Objectives
- To provide guarantee up to a specified limit against credit instruments extended by Member Institutions to finance eligible startups
- To provide the much-needed collateral free debt funding to startups
- To enable eligible startups to approach Member Institutions and seek credit assistance under this guarantee scheme
- To facilitate automatic issuance of guarantee cover based on meeting eligibility parameters
- To support eligible Banks, NBFCs and AIFs to lend to DPIIT recognised eligible startups

### Eligibility Matrix

| **Eligibility Criteria** | **Details** | **Source** |
|--------------------------|-------------|------------|
| **Borrower (Startup)** | Must be a DPIIT-recognised startup as per Gazette Notifications issued from time to time | Key Facts, CGSS webpage |
| | Must not be in default to any lending/investing institution | Key Facts, CGSS webpage |
| | Must not be classified as a Non-Performing Asset (NPA) as per RBI guidelines | Key Facts, CGSS webpage |
| | Eligibility must be certified by the Member Institution for the purpose of guarantee cover | Key Facts, CGSS webpage |
| **Lending/Investing Institutions (Member Institutions)** | Scheduled Commercial Banks and Financial Institutions | Key Facts, CGSS webpage |
| | RBI-registered Non-Banking Financial Companies (NBFCs) with a minimum credit rating of BBB and above by external credit rating agencies accredited by RBI | Key Facts, CGSS webpage |
| | NBFCs must have a minimum net worth of ₹100 crore | Key Facts, CGSS webpage |
| | If an NBFC's rating falls below BBB, it becomes ineligible for further guarantee cover until upgraded back to eligible category | Key Facts, CGSS webpage |
| | SEBI-registered Alternative Investment Funds (AIFs) | Key Facts, CGSS webpage |

### Benefits & Financial Support

| **Benefit Type** | **Details** | **Source** |
|------------------|-------------|------------|
| **Maximum Guarantee Cover per Borrower** | ₹20 crore (revised from ₹10 crore) | Key Facts, CGSS webpage |
| **Forms of Assistance** | Venture debt, working capital, subordinated debt/mezzanine debt, debentures, optionally convertible debt, and other fund-based and non-fund-based facilities that have crystallised as debt obligations | Key Facts, CGSS webpage |
| **Guarantee Coverage Models** | **Transaction-based**:<br>- 85% of amount in default for loan amount up to ₹10 crore<br>- 75% of amount in default for loan amount exceeding ₹10 crore<br>**Umbrella-based**:<br>- Actual losses or up to 5% of Pooled Investment on which cover is taken from the fund in Startups, whichever is lower<br>- Subject to a maximum of ₹20 crore per borrower<br>- Runs through the life of the venture debt fund | Key Facts, CGSS webpage |
| **Definition of Losses (Umbrella-based)** | Aggregate of principal investments of written-off assets + three months accrued interest from date of default<br>For partially written-off assets: only the principal portion written off + three months accrued interest thereon from date of default | Key Facts, CGSS webpage |
| **Government Corpus** | Fixed corpus established by the Government of India for providing credit guarantees | Key Facts |

### Application Process (Mermaid Flowchart)
```mermaid
flowchart TD
    A[Startup seeks loan from Member Institution (MI)] --> B{MI evaluates feasibility & viability}
    B -->|Feasible & Viable| C[MI sanctions need-based assistance]
    B -->|Not Feasible| Z[Application rejected]
    C --> D[MI applies for guarantee cover on NCGTC portal]
    D --> E{NCGTC checks eligibility parameters}
    E -->|Eligibility Met| F[Automatic issuance of guarantee cover]
    E -->|Eligibility Not Met| G[Application rejected]
    F --> H[MI disburses loan to startup with guarantee cover]
    H --> I[Startup uses funds for venture debt, working capital, etc.]
    style A fill:#e3f2fd,stroke:#1565c0
    style B fill:#fff3e0,stroke:#ef6c00
    style C fill:#e8f5e8,stroke:#2e7d32
    style D fill:#f3e5f5,stroke:#6a1b9a
    style E fill:#ffebee,stroke:#c62828
    style F fill:#e8f5e8,stroke:#2e7d32
    style G fill:#ffebee,stroke:#c62828
    style H fill:#e3f2fd,stroke:#1565c0
    style I fill:#fff8e1,stroke:#ff6f00
```

> **Key Application Notes**:  
> - **Online Application**: Visit Jan Samarth Portal (https://www.jansamarth.gov.in/) and complete the online application. Refer to the instructional video for guidance.  
> - **Offline Application**: Approach the nearest branch of any Member Lending Institution (MLI) directly. List of eligible MLIs available via designated reference link/document.  
> - **Registration Process for MIs**: Eligible institutions register by submitting a signed undertaking (format on website) and Board Resolution. Upon successful registration, login credentials are created for NCGTC’s portal. To register as an MI, visit NCGTC’s portal.  
> - **DPIIT Recognition Mandatory**: A startup must be recognised by DPIIT to avail benefits under the scheme.  

### Key Caveats
- CGSS does not provide guarantee cover to DPIIT recognised startups directly, but through a Trustee (NCGTC), which in turn provides guarantee cover to MIs who provide loans to startups.  
- In case an NBFC subsequently becomes ineligible due to a downgrade in credit rating below BBB, the NBFC shall not be eligible for further guarantee cover until upgradation again to eligible category.  

### Supporting Evidence References
- Application Portal: https://www.jansamarth.gov.in/  
- Scheme Details: https://startupindia.gov.in/content/sih/en/credit-guarantee-scheme-for-startups.html  
- DPIIT Recognition Criteria: https://startupindia.gov.in/content/sih/en/startup-scheme.html  
- Notification G.S.R. 127(E) dated 19th February 2019 (Defines Startup for government schemes)  

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