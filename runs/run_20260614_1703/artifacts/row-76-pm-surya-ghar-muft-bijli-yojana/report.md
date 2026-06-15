# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Scheme Overview
**PM Surya Ghar: Muft Bijli Yojana** is a pan-India subsidy scheme launched by the Ministry of New and Renewable Energy (MNRE) to promote rooftop solar adoption among residential households. The scheme aims to install rooftop solar systems in 1 crore households across India, providing financial subsidies and up to 300 units of free electricity monthly to beneficiaries. The scheme operates through the national portal [https://pmsuryaghar.gov.in/](https://pmsuryaghar.gov.in/) and closes on **31 March 2027**.

### Objectives
- Promote sustainable development and people's well-being through solar energy adoption  
- Provide up to 300 units of free electricity per month to beneficiary households  
- Install rooftop solar systems in 1 crore households across India  
- Reduce dependence on grid electricity and lower household electricity expenses  
- Encourage renewable energy usage at the residential level  

### Eligibility Matrix
| Eligibility Criteria | Details | Source |
|----------------------|---------|--------|
| **Target Beneficiaries** | Residential households across India | Key Facts, Crawled Page |
| **Geographic Scope** | Pan-India | Key Facts |
| **Applicant Type** | Individual consumers or through empanelled vendors | Key Facts, Crawled Page |
| **Mandatory Registration** | Must register on the national portal | Key Facts, Crawled Page |
| **Required Consumer Details** | Mobile number, name, email, address, state, district, PIN code, electricity consumer account number | Key Facts, Crawled Page |
| **Special States** | Eligible for additional 10% subsidy per kW (specific states not listed in evidence) | Key Facts, Crawled Page |
| **GHS/RWA Eligibility** | Group Housing Societies and Resident Welfare Associations eligible for common facilities up to 500 kW | Key Facts, Crawled Page |

### Benefits & Financial Support
#### Subsidy Structure for Residential Households
| System Capacity | Subsidy Rate | Calculation | Max Subsidy | Notes |
|-----------------|--------------|-------------|-------------|-------|
| First 2 kW | Rs. 30,000 per kW | 2 kW × Rs. 30,000/kW | Rs. 60,000 | - |
| Next 1 kW (up to 3 kW) | Rs. 18,000 per kW | 1 kW × Rs. 18,000/kW | Rs. 18,000 | - |
| **Systems > 3 kW** | **Capped** | **Total subsidy capped** | **Rs. 78,000** | **Subsidy does not increase beyond 3 kW** |
| **Special States** | **+10% per kW** | Base rate + 10% | Varies by capacity | Applicable only for notified special states |

#### Subsidy Structure for GHS/RWA
| Entity Type | Subsidy Rate | Capacity Limit | Max Capacity | Notes |
|-------------|--------------|----------------|--------------|-------|
| GHS/RWA (Common Facilities) | Rs. 18,000 per kW | Up to 500 kW | Rs. 90,00,000 (500 kW × Rs. 18,000) | Includes EV charging infrastructure |
| Special States (GHS/RWA) | Rs. 19,800 per kW (18,000 + 10%) | Up to 500 kW | Rs. 99,00,000 | Additional 10% subsidy per kW |

#### Additional Benefits
- **Free Electricity**: Up to 300 units per month after successful installation and verification  
- **Suitable Plant Capacity Guidance** (based on monthly consumption):  
  - 0-150 units: 1-2 kW  
  - 150-300 units: 2-3 kW  
  - >300 units: Above 3 kW  

### Financial Summary
| Metric | Value | Source |
|--------|-------|--------|
| **Total Fund Size** | Rs. 75,000 crores | Key Facts, Crawled Page |
| **Max Subsidy per Household** | Rs. 78,000 (capped for systems >3 kW) | Key Facts, Crawled Page |
| **Subsidy for First 2 kW** | Rs. 30,000 per kW | Key Facts, Crawled Page |
| **Subsidy for Next kW (up to 3 kW)** | Rs. 18,000 per kW | Key Facts, Crawled Page |
| **GHS/RWA Subsidy Rate** | Rs. 18,000 per kW | Key Facts, Crawled Page |
| **Special State Bonus** | +10% per kW | Key Facts, Crawled Page |
| **Free Electricity Benefit** | Up to 300 units/month | Key Facts, Crawled Page |
| **Scheme Close Date** | 31 March 2027 | Key Facts, Crawled Page |
| **Last Updated** | 2026 | Key Facts |
| **Discontinuation Alert** | Repeated module/inverter serial numbers provision ends 26 May 2026 | Key Facts, Crawled Page |

> **> WARNING**: The provision allowing installation submission of applications with repeated module/inverter serial numbers based on vendor undertakings will be **discontinued from 26 May 2026**. After this date, all applications must have unique serial numbers for solar modules and inverters.  
> **> CAVEAT**: Subsidy for systems larger than 3 kW is strictly capped at Rs. 78,000 — no additional subsidy is provided beyond this capacity.  
> **> NOTE**: Additional 10% subsidy per kW applies **only** to special states (as notified by MNRE from time to time).

### Application Process Flow
```mermaid
flowchart TD
    A[Start: Visit https://pmsuryaghar.gov.in/] --> B{Select Path}
    B -->|Option 1| C[Click 'Apply Now' on Consumer Page]
    B -->|Option 2| D[Open Login Dropdown → Select 'Consumer Login']
    C --> E[Enter Registered Mobile Number + Captcha]
    D --> E
    E --> F[Select 'Yes, I have read all guidelines' → Click 'Verify']
    F --> G[Enter Mobile OTP Received via SMS → Click 'Login']
    G --> H[Enter Profile Details: Name, Email, Address, State, District, PIN Code → Click 'Save']
    H --> I[Submit Application]
    I -->|Path A| J[Click 'Apply for Solar Rooftop']
    I -->|Path B| K[Select Vendor → Proceed via Vendor Selection]
    J --> L[Select State, District, Electricity Distribution Company/Utility]
    K --> L
    L --> M[Enter Consumer Account Number → Click 'Fetch Details']
    M --> N[Click 'Next' to Start Filling Application]
    N --> O[Complete Application Form]
    O --> P[Upload Required Documents]
    P --> Q[Submit Final Application]
    Q --> R[Application Received → Acknowledgment Generated]
    R --> S[Vendor/Installation Phase (if applicable)]
    S --> T[Installation & Commissioning]
    T --> U[Verification by Agency]
    U --> V[Subsidy Disbursement (Post-Verification)]
    V --> W[Beneficiary Receives Up to 300 Units Free Electricity/Month]
    W --> X[End: Scheme Benefits Active]
    style A fill:#e3f2fd,stroke:#1565c0
    style X fill:#c8e6c9,stroke:#2e7d32
    style Q fill:#fff3e0,stroke:#ef6c00
    style V fill:#f3e5f5,stroke:#6a1b9a
```

> **> KEY STEP**: After login and profile saving, applicants **must** select their State, District, and Electricity Distribution Company/Utility, then enter their **electricity consumer account number** and click 'Fetch Details' to auto-populate connection details before proceeding.  
> **> PRO TIP**: Applicants can choose to apply directly or through an empanelled vendor. Using a vendor may simplify technical submission but requires coordination for document sharing and installation timelines.

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