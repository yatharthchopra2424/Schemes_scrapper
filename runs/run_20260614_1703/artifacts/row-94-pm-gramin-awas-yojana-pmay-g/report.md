# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
PM Gramin Awas Yojana (PMAY-G) is a centrally sponsored scheme launched by the Ministry of Rural Development, Government of India, aimed at providing pucca houses with basic amenities to all houseless households and those living in kutcha and dilapidated houses in rural areas. The scheme targets achieving 'Housing for All' in rural India by 2024, with a strong focus on inclusion of marginalized sections such as Scheduled Castes (SCs), Scheduled Tribes (STs), minorities, persons with disabilities, and empowerment of women through ownership in their name or joint ownership.

### Objectives
- Provide pucca houses with basic amenities to all houseless and households living in kutcha and dilapidated houses in rural areas  
- Achieve 'Housing for All' in rural areas by 2024  
- Ensure inclusion of marginalized sections including SCs/STs, minorities, and persons with disabilities  
- Promote use of locally available, eco-friendly, and disaster-resistant construction technologies  
- Converge with other schemes for provision of drinking water, sanitation, electricity, and LPG connection  
- Empower women by ensuring house ownership in the name of women or joint ownership  

### Geographic Scope & Implementing Agency
- **Geographic Scope**: Rural areas across India  
- **Implementing Agency**: Ministry of Rural Development, Government of India  
- **Application Portal**: https://pmayg.nic.in/  
- **Status / Deadlines**: Originally targeted for completion by March 2022, later extended to 2024. Beneficiary identification and sanctioning are done periodically based on fund availability and SECC 2011 data.

### Financial Support & Max Per Entity
| Area Type | Financial Assistance (Per Unit) | Notes |
|-----------|-------------------------------|-------|
| Plain Areas | INR 1.20 lakh | Provided in three instalments via DBT |
| Hilly States, Difficult Areas, IAP Districts | INR 1.30 lakh | Higher assistance due to terrain and accessibility challenges |

> **Key Financial Notes**:  
> - Assistance is released in **three instalments** via **Direct Benefit Transfer (DBT)** to the beneficiary's bank/post office account linked with Aadhaar  
> - Release is **strictly tied to construction progress**, verified through **geo-tagged photographs** at different stages  
> - No upgradation of existing kutcha houses is permitted; only **new construction** qualifies  

### Benefits
PMAY-G provides comprehensive support beyond just financial assistance for house construction:
- Financial assistance for construction of a pucca house  
- Provision of basic amenities through convergence with other government schemes:  
  - Toilet (Swachh Bharat Mission-Gramin)  
  - Electricity connection (Saubhagya)  
  - LPG connection (Ujjwala)  
  - Drinking water (Jal Jeevan Mission)  
- Technical support for construction  
- Facilitation of institutional finance through banks  

### Eligibility Criteria
Beneficiaries are identified based on housing deprivation and socio-economic criteria from the **Socio Economic and Caste Census (SECC) 2011**. The scheme prioritizes the most vulnerable.

| Eligibility Parameter | Details |
|------------------------|--------|
| Housing Status | Houseless households; households living in zero, one, or two-room kutcha houses (walls/roof made of grass, thatch, bamboo, wood, mud, unburnt brick, etc.) |
| Pucca House Ownership | Must **not own a pucca house anywhere in India** |
| Social Priority | SCs/STs, freed bonded labourers, non-tribal forest dwellers, manual scavengers, legally released bonded labourers, persons with disabilities |
| Target Groups | Rural poor, houseless, kutcha/dilapidated house dwellers |
| Identification Basis | SECC 2011 data + Gram Sabha verification |

> **Critical Eligibility Caveats**:  
> - Only **new construction** is allowed; renovation/upgradation of existing kutcha houses is **not covered**  
> - Beneficiary must **not own a pucca house anywhere in India** (including urban areas)  
> - Convergence benefits (toilet, electricity, LPG, water) are **dependent on the implementation status** of respective schemes (SBM-G, Saubhagya, etc.) in the area  

### Required Documents
1. Aadhaar number  
2. Bank/Post Office account details linked with Aadhaar  
3. Consent form from the beneficiary  
4. Geo-tagged photographs at different construction stages (for instalment release)  

### Application Process Flow
The following Mermaid flowchart illustrates the end-to-end application and fund disbursement process under PMAY-G:

```mermaid
flowchart TD
    A[Beneficiary Identification via SECC 2011 Data] --> B[Gram Sabha Verification & Intimation]
    B --> C[Obtain Beneficiary Consent]
    C --> D[Selection of House Design from Rural Housing Technology Menu]
    D --> E[Open Bank/Post Office Account Linked with Aadhaar for DBT]
    E --> F[Release of 1st Instalment (40%: INR 48,000 plain / INR 52,000 hilly)]
    F --> G[Commence Construction]
    G --> H[Submit Geo-tagged Photos at Plinth Level]
    H --> I{Verification of 1st Stage}
    I -->|Pass| J[Release of 2nd Instalment (40%: INR 48,000 plain / INR 52,000 hilly)]
    I -->|Fail| G
    J --> K[Continue Construction]
    K --> L[Submit Geo-tagged Photos at Roof Level]
    L --> M{Verification of 2nd Stage}
    M -->|Pass| N[Release of 3rd Instalment (20%: INR 24,000 plain / INR 26,000 hilly)]
    M -->|Fail| K
    N --> O[House Completion]
    O --> P[Final Verification]
    P --> Q[Facilitation of Convergence Benefits: Toilet, Electricity, LPG, Water]
    Q --> R[Scheme Closure & Beneficiary Handover]
```

> **Process Warnings**:  
> - Funds are **released only after successful verification** of geo-tagged images at each stage  
> - Any discrepancy in construction progress **halts further instalments** until compliance  
> - Beneficiary bears responsibility for timely submission of geo-tagged photos  
> - Delays in convergence scheme benefits (e.g., electricity, water) do not affect PMAY-G house completion but may delay full amenity access  

### Timelines & Sanctioning
- Beneficiary identification and sanctioning are **ongoing and periodic**, based on:  
  - Availability of funds  
  - Updates from SECC 2011 database  
  - Gram Sabha recommendations  
- No fixed application window; beneficiaries are **proactively identified** by state/district authorities  
- Construction must commence after 1st instalment release and be completed within a reasonable timeframe (typically 12 months, subject to extension based on verification)  

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Specific Use Case*: During a eligibility check call, if a client asks "Do I qualify if I own a pucca house in another state?", instantly search "pucca house ownership" to confirm the nationwide bar and advise accordingly.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
*Specific Use Case*: When a lead says "I already have a kutcha house, can I just upgrade it?", use the objection handler: "Under PMAY-G, only new construction is permitted—upgradation doesn’t qualify. However, we can help you identify eligible relatives or explore other rural housing schemes for upgradation."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
*Specific Use Case*: After the client submits their consent form and bank details, check off "Stage 1: Documentation Complete" and trigger the email template requesting geo-tagged photos at plinth level once construction begins.

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
*Specific Use Case*: When the client emails their Aadhaar and bank details, update the CRM under "Documents Received" → "Aadhaar: Yes, Bank: Yes" and flag "Consent Form: Pending" to trigger a follow-up call.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
*Specific Use Case*: When a case shows "Stage 06 - 2nd Instalment Pending" for over 15 days, check the escalation path to contact the District Nodal Officer (PMAY-G) with the beneficiary ID and geo-tag submission date to expedite verification.

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
*Specific Use Case*: For a client identified as a SECC-eligible beneficiary with no turnover (typical for PMAY-G), apply the "No Turnover / Rural Poor" tier: Retainer = INR 8,000, Success Fee = 8% of sanctioned amount (INR 9,600–10,400), quoted clearly in the proposal.

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
*Specific Use Case*: After confirming eligibility on a call, open the template, replace `[Client Name]`, `[Village]`, `[District]`, `[Aadhaar Last 4]`, `[House Type]`, and send the PDF within 15 minutes while the conversation is fresh.

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
*Specific Use Case*: Before collecting any documents, send the pack with cover letter: "Please review and sign the Consent to Process Data and Service Agreement. We cannot begin eligibility verification or document collection until these are signed, as per our compliance protocol." If rejected, cite Clause 4.2: "Neither party guarantees scheme approval, as final sanction rests with the Ministry of Rural Development."