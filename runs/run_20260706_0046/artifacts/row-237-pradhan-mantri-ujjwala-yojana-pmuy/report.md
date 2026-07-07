# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
Pradhan Mantri Ujjwala Yojana (PMUY) is a flagship social welfare scheme launched by the Ministry of Petroleum and Natural Gas (MOPNG) on 1st May 2016 in Ballia, Uttar Pradesh, by Hon'ble Prime Minister Shri Narendra Modi. The scheme aims to provide deposit-free LPG connections to women from poor households, replacing traditional cooking fuels with clean LPG to improve health, reduce environmental degradation, empower women, and achieve universal LPG access in India. As of 02 July 2026, 105,626,870 connections have been released under the scheme, with an additional 2,384,089 connections released under the latest PMUY extension (25 lakh). The scheme operates on a rolling basis with no fixed deadline, accepting applications year-round.

### Objectives
- Provide deposit-free LPG connections to women from poor households
- Replace traditional cooking fuels (firewood, coal, cow-dung) with clean LPG
- Improve health of rural women by reducing indoor air pollution
- Reduce environmental degradation caused by traditional fuels
- Empower women by providing clean cooking fuel access
- Achieve universal access to LPG in India
- Support migrant households through simplified documentation in Ujjwala 2.0

### Eligibility Matrix
| **Criteria** | **Requirement** | **Details** |
|--------------|-----------------|-------------|
| **Applicant Gender** | Female | Must be a woman |
| **Minimum Age** | 18 years | Applicant must have attained 18 years of age; no connection to persons under 18 |
| **Household LPG Status** | No existing LPG connection | No other LPG connection from any Oil Marketing Company (OMC) within the same household |
| **Household Economic Status** | Poor household | Based on submission of a deprivation declaration (as per prescribed format) |
| **Eligible Categories** | Specific beneficiary groups | SC Households, ST Households, Pradhan Mantri Awas Yojana (Gramin), Most Backward Classes, Antyodaya Anna Yojana (AAY), Tea and Ex-Tea Garden tribes, Forest Dwellers, People residing in Islands and River Islands, SECC Households (AHL TIN), Poor Household as per 14-point declaration |
| **Special Provision for Migrants** | Simplified documentation | Self-declaration for Proof of Address (PoA) and family composition suffices; no ration card or address proof required under Ujjwala 2.0 |

### Benefits & Financial Support
| **Benefit Component** | **Amount (14.2 kg Cylinder)** | **Amount (5 kg Cylinder)** | **Coverage Details** |
|------------------------|-------------------------------|----------------------------|----------------------|
| **Total Cash Assistance** | Rs. 1600 | Rs. 1150 | Provided by Government of India |
| **Security Deposit of Cylinder** | Rs. 1250 | Rs. 800 | Covers cylinder deposit |
| **Pressure Regulator** | Rs. 150 | Rs. 150 | Standard regulator cost |
| **LPG Hose (Suraksha Hose)** | Rs. 100 | Rs. 100 | 1.2 m hose pipe |
| **Domestic Gas Consumer Card (DGCC)** | Rs. 25 | Rs. 25 | Booklet for consumer identification |
| **Inspection/Installation/Demonstration Charges** | Rs. 75 | Rs. 75 | Includes pre-installation check and setup |
| **First LPG Refill** | Free | Free | Provided by OMCs along with connection |
| **Stove (Hotplate)** | Free | Free | Two-burner stove provided by OMCs |
| **Total Value to Beneficiary** | ~Rs. 3200+ | ~Rs. 2300+ | Includes free stove and first refill beyond cash assistance |

> **Key Financial Notes**: The cash assistance of Rs. 1600 (14.2 kg) or Rs. 1150 (5 kg) is transferred directly to the beneficiary's bank account via DBTL after successful connection installation and Aadhaar seeding. The OMCs absorb the cost of the stove and first refill. Beneficiaries pay nothing upfront for the connection.

### Application Process
```mermaid
flowchart TD
    A[Start: Eligible Woman Identifies Need] --> B{Application Method}
    B -->|Online| C[Visit https://pmuy.gov.in<br/>Click 'Apply for PMUY Connection']
    B -->|CSC Assistance| D[Visit Nearest CSC Centre<br/>Pay ₹20 service charge]
    B -->|Offline| E[Submit Application at Nearest LPG Distributorship<br/>of OMCs (Indane/Bharat Gas/HP Gas)]
    C --> F[Fill Online KYC Form<br/>Upload Required Documents]
    D --> F
    E --> F
    F --> G[Documents Verified by LPG Distributor]
    G --> H[Biometric Aadhaar Authentication (eKYC)<br/>Mandatory for PMUY]
    H --> I[Pre-Installation Inspection<br/>Conducted at Applicant's Premise]
    I --> J[Connection Released<br/>Deposit-Free LPG Connection]
    J --> K[Receive Free Stove & First Refill<br/>from OMC]
    K --> L[Subsidy Transferred to Bank<br/>via DBTL after Aadhaar Seeding]
    L --> M[End: Active PMUY Beneficiary]
    style M fill:#e6f7e6,stroke:#2e8b57
```

#### Step-by-Step Application Details
1. **Application Channels**:
   - Online: Through the application form at https://pmuy.gov.in (no fee for self-submission)
   - CSC Centres: ₹20 charge applicable for assisted submission
   - Offline: Direct submission at nearest LPG distributorship of OMCs (preferred for offline)

2. **Required Documents** (All mandatory unless specified for migrants):
   - Know Your Customer (KYC) application form (standard format)
   - Proof of Identity: Aadhaar copy of Applicant
   - Proof of Address: Only if Aadhaar address differs from current residence; Self Declaration as per Annexure I for migrant applicants
   - Proof of Family Composition: Ration Card issued by the State or other State Govt. document certifying family composition; Self Declaration as per Annexure I for migrant applicants
   - Aadhaar copy of Applicant and adult family members appearing in family composition document
   - Bank Account details: Passbook copy or Cancelled cheque
   - Deprivation Declaration (Supplementary KYC Document & Undertaking)
   - Self Declaration for Migrants (Annexure I) - for PoA and family composition
   - Pre-Installation Check (Annexure II)
   - Unified PAHAL (DBTL) Joining Form
   - Declaration for new connection
   - Mandate For Giving up LPG Subsidy
   - Grievance Redressal Form for PAHAL (DBTL) Scheme
   - Unified Form for transfer/Regularization of LPG connection
   - Declaration for the loss of Subscription/Termination Voucher

3. **Special Provisions for Migrants (Ujjwala 2.0)**:
   - Self-declaration for Proof of Address and family composition (Annexure I) suffices
   - No requirement to submit ration card or address proof
   - Simplified documentation to support migrant households

4. **Post-Submission Process**:
   - Application verified by LPG distributor
   - Biometric Aadhaar authentication (eKYC) mandatory
   - Pre-Installation inspection mandatory prior to connection release
   - Connection released upon successful verification
   - First LPG refill and stove provided free of cost by OMCs
   - Subsidy transferred to beneficiary's bank account via DBTL after Aadhaar seeding with bank

### Important Caveats & Warnings
> **Critical Restrictions**:
> - Households with Piped Natural Gas (PNG) connection are **not entitled** for subsidized LPG under PMUY
> - Beneficiary must **not position any other LPG gas installations** in the same kitchen
> - PMUY cylinder and stove are **subsidized assets** and **cannot be sold or transferred** to anyone else; must be surrendered back to OMCs
> - Biometric Aadhaar authentication (eKYC) is **mandatory** for all PMUY connections
> - If Aadhaar is not seeded or mapped correctly in NPCI mapper, subsidy **may not be received**
> - Pre-Installation inspection is **mandatory** prior to release of a PMUY connection
> - LPG connection cannot be provided to a person **under 18 years of age**

> **Operational Notes**:
> - Applications accepted year-round on rolling basis; no fixed deadlines
> - Helpline: 1800 266 6696 for status queries and grievances
> - Implementing Agency: Ministry of Petroleum and Natural Gas (MOPNG)
> - Geographic Scope: Pan-India
> - Scheme Type: Subsidy (cash assistance for connection setup)
> - Last Updated: 2026 (as per key facts)

### Scheme Achievements & Scale
- **Total Connections Released (as of 02 Jul 2026)**: 105,626,870
- **Latest Extension (25 lakh)**: 2,384,089 connections released (as of 02 Jul 2026)
- **Cumulative Milestones**:
  - 8 Crore connections achieved by September 2019 (7 months ahead of target)
  - Ujjwala 2.0: Additional 1.6 Crore connections achieved by Dec'22 (total 9.6 Crore)
  - Further 75 lakh allocation under Ujjwala 2.0 (FY 2023-24 to 2025-26) achieved by July 2024 (total 10.35 Crore)
  - Additional 25 lakh connections approved, taking overall target to 10.6 Crore (currently being released)

### Supporting Evidence Sources
- **Primary Portal**: https://pmuy.gov.in (Official application and information hub)
- **Key Pages**: 
  - Eligibility Criteria: https://pmuy.gov.in/about.html
  - Documents Required: https://pmuy.gov.in/faq.html (Q6)
  - Benefits: https://pmuy.gov.in/about.html
  - Application Process: https://pmuy.gov.in/faq.html (Q4)
  - Ujjwala 2.0 Details: https://pmuy.gov.in/ujjwala2.html
  - eKYC Information: https://pmuy.gov.in/e-kyc.html
  - Grievance Helpline: Referenced across FAQ and portal pages
- **Forms Repository**: All KYC, Annexure I, Annexure II, and related forms available for download from https://pmuy.gov.in

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Specific Scenarios*:  
- During eligibility screening, instantly verify if a client belongs to SC/ST/PMAY(Gramin)/Most Backward Classes/AAY/Tea Garden tribes/Forest Dwellers/Island dwellers/SECC or poor household via 14-point declaration  
- When client queries about cylinder size options, reference the exact financial breakdown: Rs. 1600 covers security deposit (Rs. 1250), regulator (Rs. 150), hose (Rs. 100), DGCC (Rs. 25), installation (Rs. 75) for 14.2 kg; Rs. 1150 equivalent for 5 kg  
- For migrant clients, confirm that only Self Declaration as per Annexure I is needed for PoA and family composition—no ration card required  
- If client mentions having a PNG connection, immediately cite the caveat: "Households having Piped Natural Gas connection are not entitled for subsidized LPG"  

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
*Specific Scenarios*:  
- **Problem Framing Script**: "Did you know that over 10.5 crore poor women across India have already switched to clean LPG cooking under PMUY, eliminating harmful smoke from chulhas in their kitchens? Yet millions still rely on firewood, risking respiratory diseases."  
- **Qualification Checklist**:  
  - ☐ Female applicant? (If no → disqualify per scheme rule)  
  - ☐ Age ≥18 years? (Verify via Aadhaar DOB)  
  - ☐ No existing LPG connection in household? (Check ration card/family declaration)  
  - ☐ Belongs to eligible category? (SC/ST/PMAY-Gramin/MBC/AAY/Tea Tribe/Forest Dweller/Island dweller/SECC/Poor HH via 14-point decl)  
  - ☐ Willing to submit deprivation declaration and undergo eKYC?  
- **Objection Handler for "Too Small"**:  
  > *"PMUY is specifically designed for the poorest households—there is no 'too small'. In fact, having no LPG connection currently makes you *more* eligible. The scheme targets those using firewood/cow-dung, often the most marginalized. Let me check if you qualify under the deprivation criteria..."*  
- **Ujjwala 2.0 Hook for Migrants**: "If you've recently moved states for work, you don't need to hunt for old ration cards—just a simple self-declaration about your family and current address is enough to apply."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
*Specific Scenarios*:  
- **Stage 1 (Document Collection)**:  
  - [ ] KYC form completed with applicant photo/signature  
  - [ ] Aadhaar copy of applicant  
  - [ ] Aadhaar copies of all adult family members (as per family composition doc)  
  - [ ] Proof of Address (or Annexure I self-declaration if migrant)  
  - [ ] Family composition proof (ration card or state doc, or Annexure I if migrant)  
  - [ ] Bank passbook/cancelled cheque  
  - [ ] Signed Deprivation Declaration  
  - [ ] Unified PAHAL form  
  - [ ] Declaration for new connection  
  - [ ] Mandate to give up LPG subsidy  
  - [ ] Grievance redressal form  
  - [ ] Pre-Installation Check (Annexure II)  
- **Stage 2 (Submission & Follow-up)**:  
  - [ ] Application submitted via online/CSC/offline channel  
  - [ ] Obtained application reference number  
  - [ ] Scheduled biometric eKYC with distributor  
  - [ ] Coordinated pre-installation inspection date  
- **Client Communication Template for Missing Docs**:  
  > *"Dear [Client Name],*  
  > *To progress your PMUY application, we urgently need:*  
  > *1. [Specify document, e.g., 'Aadhaar copies of all adult family members']*  
  > *2. [Specify document, e.g., 'Signed deprivation declaration']*  
  > *Please provide these by [Date] to avoid delays. Remember, biometric eKYC and pre-installation check cannot proceed without complete docs. For help, call our support line or visit the nearest CSC.*  
  > *Best regards,*  
  > *[Your Name]*"  

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
*Specific Scenarios*:  
- **Needs Assessment Section**:  
  - Current cooking fuel: [ ] Firewood [ ] Coal [ ] Cow-dung [ ] Kerosene [ ] Other: ________  
  - Monthly fuel expenditure: ₹ ________  
  - Primary health concern: [ ] Respiratory issues [ ] Eye irritation [ ] Time spent collecting fuel [ ] Other: ________  
  - Household size: ________ adults, ________ children  
  - Key motivation for switching: [ ] Health [ ] Convenience [ ] Cost savings [ ] Empowerment  
- **Compliance Status Table (Update Daily)**:  
  | **Document** | **Received?** (Y/N) | **Date Received** | **Notes** |  
  |--------------|---------------------|-------------------|-----------|  
  | KYC Form | ☐ | | |  
  | Applicant Aadhaar | ☐ | | |  
  | Family Members' Aadhaar | ☐ | | |  
  | Proof of Address / Annexure I | ☐ | | |  
  | Family Composition Proof | ☐ | | |  
  | Bank Details | ☐ | | |  
  | Deprivation Declaration | ☐ | | |  
  | PAHAL Form | ☐ | | |  
  | New Connection Declaration | ☐ | | |  
  | Subsidy Mandate | ☐ | | |  
  | Grievance Form | ☐ | | |  
  | Pre-Installation Check (Annexure II) | ☐ | | |  
- **Pain Point to Solution Mapping**:  
  - If client cites "smoke-related cough" → Emphasize PMUY's health impact: reduced indoor air pollution improves respiratory health  
  - If client says "collecting firewood takes 3 hrs/day" → Highlight time savings and safety benefits of LPG  
  - If client worries about cost → Clarify zero upfront cost; stove and first refill free; subsidy covers connection setup  

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
*Specific Scenarios*:  
- **Stage Definitions**:  
  - Stage 00: Lead Generated  
  - Stage 01: Discovery Call Completed  
  - Stage 02: Documents Collected (Track via CRM compliance status)  
  - Stage 03: Application Submitted  
  - Stage 04: Biometric eKYC Completed  
  - Stage 05: Pre-Installation Inspection Done  
  - Stage 06: Connection Released  
  - Stage 07: Under Review (Subsidy DBTL Seeding/Aadhaar Mapping)  
  - Stage 08: Active Beneficiary (First Refill Received)  
  - Stage 09: Case Closed / Won  
  - Stage 10: Rejected (With Reason)  
- **Daily Standup Action**:  
  - Sort tracker by "Stage" ascending  
  - For any case in Stage 02: Prioritize document chasing using APPLICATION_PLAYBOOK templates  
  - For any case in Stage 04: Confirm eKYC completion; if pending, contact distributor  
  - For any case in Stage 05: Verify inspection report received  
- **Escalation Path for Stage 07 (Under Review)**:  
  > *"If subsidy not reflecting after connection release:*  
  > *1. Verify Aadhaar is seeded with bank account (client's bank branch*  
  > *2. Check NPCI mapper status: https://www.npci.org.in → Consumer Tab → Bharat Aadhaar Seeding Enabler (BASE) → Aadhaar Mapped Status*  
  > *3. If status ≠ 'Enabled for DBT', guide client to submit Aadhaar Seeding Form at bank*  
  > *4. If issue persists after 7 days, escalate to:*  
  > *   - LPG Distributor's Nodal Officer (DBTL)*  
  > *   - Regional Office of OMC (Indane/Bharat Gas/HP Gas)*  
  > *   - MOPNG PMUY Helpline: 1800 266 6696 (ask for Grievance Redressal Officer)*  
  > *   - District Supply Officer (DSO) of concerned OMC*  
  > *Always reference the client's LPG ID and application number."*  

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
*Specific Scenarios*:  
- **Pricing Tier Mapping (Based on Client Effort/Complexity)**:  
  | **Client Profile** | **Retainer Fee** | **Success Fee** | **Rationale** |  
  |--------------------|------------------|-----------------|---------------|  
  | Standard Rural/Urban Poor HH (Non-migrant) | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | Baseline case; standard document collection |  
  | Migrant Client (Ujjwala 2.0) | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | Slightly lower effort (no ration card needed) but verification complexity |  
  | Client Requiring Multiple Follow-ups (>3 doc chases) | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | Higher operational overhead |  
  | Client in Remote/Hill Area (Access Issues) | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | Increased coordination cost with distant distributor |  
- **Monthly Pipeline Forecast**:  
  | **Month** | **Expected Leads** | **Conversion Rate** | **Expected Wins** | **Revenue Forecast** |  
  |-----------|--------------------|---------------------|-------------------|----------------------|  
  | April 2026 | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] |  
  | May 2026 | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] |  
  | June 2026 | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] |  
  | July 2026 | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] | [TO BE FILLED BY CONSULTANT] |  
- **Usage Example**:  
  > *"Client is a non-migrant rural household. Retainer = [TO BE FILLED BY CONSULTANT], Success Fee = [TO BE FILLED BY CONSULTANT]. Total potential = [TO BE FILLED BY CONSULTANT] x Success Fee. Add to pipeline forecast for next month."*  

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
*Specific Scenarios*:  
- **Immediate Post-Discovery Call Action**:  
  1. Open CLIENT_PROPOSAL_TEMPLATE.md  
  2. Replace all [PLACEHOLDER] tags:  
     - [CLIENT_NAME] → From CRM Needs Assessment  
     - [CURRENT_FUEL] → e.g., "Firewood"  
     - [HOUSEHOLD_SIZE] → e.g., "5 members"  
     - [ELIGIBLE_CATEGORY] → e.g., "SC Household" or "Poor HH per 14-point decl"  
     - [RETAINER_FEE] → From FEE_AND_REVENUE_MODEL.md  
     - [SUCCESS_FEE] → From FEE_AND_REVENUE_MODEL.md  
     - [CYLINDER_SIZE] → Based on client preference (14.2 kg or 5 kg)  
  3. Generate PDF or paste into email body  
  4. Send within 1 hour of call while engagement is high  
- **Key Sections to Customize**:  
  > *"Based on your needs assessment, you currently use [CURRENT_FUEL] for cooking, affecting [HOUSEHOLD_SIZE] household members. As a verified [ELIGIBLE_CATEGORY], you qualify for PMUY's deposit-free LPG connection.*  
  > *Our service includes:*  
  > *- End-to-end application management*  
  > *- Document preparation and verification*  
  > *- Liaison with LPG distributor for eKYC and inspection*  
  > *- Subsidy tracking until DBTL activation*  
  > *Total Cost: [RETAINER_FEE] (retainer) + [SUCCESS_FEE] (success fee upon connection release)"*  
  > *"Act now—PMUY has released over 10.5 crore connections, but slots under the latest 25 lakh extension are filling fast."*  

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
*Specific Scenarios*:  
- **Pre-Proposal Email Attachment**:  
  - Attach **8A: Client Undertaking & Consent** as PDF  
  - Attach **8B: Service Terms & Disclaimers** as PDF  
  - Email body: *"Please find attached the mandatory consent forms. We cannot begin your PMUY application until these are signed and returned. This protects both parties per government scheme guidelines."*  
- **Mandatory Check Before Stage 1 (Document Collection)**:  
  > *"DO NOT PROCEED to collect any client documents or fill KYC forms until:*  
  > *- Client has signed and returned 8A (Client Undertaking)*  
  > *- Client has signed and returned 8B (Service Terms)*  
  > *- You have verified signatures match ID proof*  
  > *Reason: Without these, you risk liability for document mishandling or misrepresenting scheme benefits."*  
- **Disclaimer Usage for Rejection Protection**:  
  > *"If client's application is rejected by distributor/government (e.g., due to existing LPG connection, incomplete docs, or Aadhaar mismatch), point to Section 8B:*  
  > *'Consultant's liability is limited to document submission assistance. Final eligibility and connection release rest solely with the LPG distributor and MOPNG. We guarantee neither approval nor subsidy disbursement.'*  
  > *This prevents clients from blaming you for government-side rejections."*  
- **Critical Clauses to Highlight in 8B**:  
  > *"The Consultant does not guarantee eligibility, approval, or subsidy disbursement under PMUY. All decisions are made by the LPG distributor and Ministry of Petroleum and Natural Gas."*  
  > *"Client is solely responsible for the truthfulness of submitted documents. False declarations may lead to legal action under IPC, and Consultant bears no liability for such outcomes."*  
  > *"Engagement terminates upon connection release or formal withdrawal; no ongoing liability for subsidy tracking post-completion."*  

--- 
**Note**: All placeholders marked `[TO BE FILLED BY CONSULTANT]` require your firm's specific data (win rates, fees, client names, etc.). Scheme-specific details (eligibility, amounts, documents, processes) are fully populated from evidence and must not be altered. Use the portal https://pmuy.gov.in as the ultimate reference for real-time updates.