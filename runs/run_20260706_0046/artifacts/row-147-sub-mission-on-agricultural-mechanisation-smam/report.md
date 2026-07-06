# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The Sub-Mission on Agricultural Mechanisation (SMAM) is a centrally sponsored subsidy scheme implemented by the Department of Agriculture and Farmers Welfare (DA&FW), Ministry of Agriculture and Farmers Welfare, Government of India. It operates on a pan-India geographic scope with rolling basis applications accepted throughout the year as per state-specific timelines and Annual Action Plan (Demand) submission to the M&T Division. The scheme leverages the Direct Benefit Transfer (DBT) portal at https://agrimachinery.nic.in for end-to-end digital processing.

### Objectives
- Increase agricultural productivity through farm mechanization
- Provide financial assistance for procurement of agricultural machinery and equipment
- Promote establishment of Custom Hiring Centres (CHCs), Hi-Tech Hubs, and Farm Machinery Banks
- Ensure quality of farm machinery through performance testing at FMTTIs, SAUs, and ICAR institutions
- Facilitate direct transfer of subsidy to beneficiaries' bank accounts to minimize delays and leakages
- Enable state-specific subsidy top-ups and implementation flexibility
- Support registration and verification of manufacturers, dealers, and importers on the DBT portal

### Eligibility Matrix
| Beneficiary Type | Eligibility Criteria | Required Documents | Special Notes |
|------------------|----------------------|---------------------|---------------|
| Individual Farmers | Must provide Aadhaar number, land records, bank details, and identity proof | 1. Aadhaar card<br>2. Record-of-right of land<br>3. Passport size photograph<br>4. Copy of bank passbook<br>5. Copy of ID proof (except Aadhaar)<br>6. Caste category certificate (for SC/ST/OBC) | Must select correct state, district, block, and village during registration; incorrect furnished details (gender, DOB, mobile, category, bank, land) may lead to application debarment during physical verification |
| Entrepreneurs | Must register with GST certificate and PAN | 1. GST certificate (for Manufacturer/Entrepreneur)<br>2. PAN (for Entrepreneur/Society/Manufacturer)<br>3. Copy of bank passbook<br>4. Copy of ID proof<br>5. Passport size photograph | For CHC projects: additional requirements include agriculture graduate certificate, domicile, and date of birth proof |
| Societies/SHGs/FPOs | Must register using PAN | 1. PAN (for Entrepreneur/Society/Manufacturer)<br>2. Copy of bank passbook<br>3. Copy of ID proof<br>4. Passport size photograph<br>5. GST certificate (if applicable) | For CHC projects: additional requirements include agriculture graduate certificate, domicile, and date of birth proof |
| Manufacturers | Must register with GST certificate and product test reports | 1. GST certificate (for Manufacturer/Entrepreneur)<br>2. PAN (for Entrepreneur/Society/Manufacturer)<br>3. Product test report (for Manufacturer)<br>4. Copy of bank passbook<br>5. Copy of ID proof<br>6. Passport size photograph | Cannot increase MRP after state nodal officer approval; dealer price cannot exceed approved MRP |
| Dealers | Must be registered through manufacturers | 1. GST certificate (for Manufacturer/Entrepreneur)<br>2. Copy of bank passbook<br>3. Copy of ID proof<br>4. Passport size photograph | Must be registered through manufacturers on the portal |

**Target Beneficiaries**: farmers; entrepreneurs; societies/shg/fpo; manufacturers; dealers

### Benefits & Financial Support
Financial support is provided as a shared subsidy between the Centre and State governments. The Centre releases funds to State Governments, which then allocate category-wise and district-wise targets. Subsidy amounts are calculated based on the final negotiated price of machinery, with centre and state/top-up limits applying.

| Support Type | Details | Disbursement Method | Key Conditions |
|--------------|---------|---------------------|----------------|
| Central Subsidy | Released by Centre to State Governments | Direct Benefit Transfer (DBT) via RTGS/NEFT to beneficiary's bank account | Based on final negotiated price of machinery |
| State/Top-up Subsidy | Allocated by State Governments category-wise and district-wise | Direct Benefit Transfer (DBT) via RTGS/NEFT to beneficiary's bank account | Varies by state; applied after central subsidy calculation |
| CHC Projects (Loans > ₹25 lakh) | Requires bank loan documents upload | Payment processed via RTGS/NEFT after physical verification and approval | Bank loan documents and account details must be uploaded |
| Single Implement Purchase | Subsidy on final negotiated price | Direct Benefit Transfer (DBT) via RTGS/NEFT | Disbursed directly to beneficiary's bank account (farmer or dealer, as selected during bill upload) |

**Non-Financial Benefits**:
- Access to performance-tested machinery through FMTTIs, SAUs, and ICAR institutions
- Technical support through Farm Machinery Training and Testing Institutes (FMTTIs)
- Training of candidates by FMTTIs
- Availability of multi-lingual mobile app (FARMS) for CHC operations
- SMS alerts at key stages (registration, dealer selection, bill submission, verification, disbursement)
- Facilitation of machinery hire/sale through the platform
- Transparency via online application tracking, beneficiary reports, and physical verification by government officers

### Application Process Flowchart
```mermaid
flowchart TD
    A[Start: Visit https://agrimachinery.nic.in] --> B[Click 'Registration' from navigation bar]
    B --> C{Select Beneficiary Type}
    C -->|Farmer| D[Enter Aadhaar/mobile/name, state, district, block, village, land area, address, pincode, bank details, identity proof]
    C -->|Entrepreneur/Society| E[Enter GSTN/PAN, contact details, address]
    C -->|Manufacturer| F[Enter GST certificate, product details, test report, bank details]
    D --> G[Accept terms and conditions, submit to receive User ID and password (sent via SMS)]
    E --> G
    F --> G
    G --> H[Login to portal using credentials]
    H --> I{Application Type}
    I -->|Machinery Purchase| J[Select implement, check availability, add application, generate PIN, select dealer, negotiate price, upload bill and joint photographs]
    I -->|CHC Project| K[Apply for CHC establishment, upload project details (agriculture graduate, domicile, DOB certificate), await government officer approval, print permit, upload implement bill and loan documents (if applicable)]
    J --> L[After physical verification by government officer, subsidy approved and payment file generated]
    K --> L
    L --> M[Payment processed via RTGS/NEFT after physical verification and approval]
    M --> N[Subsidy disbursed directly to beneficiary's bank account]
    N --> O[Track application status via Application Tracking system using reference number]
    O --> End
```

**Key Process Notes**:
- OTP is mandatory for registration and transaction notifications
- For CHC projects involving loans over ₹25 lakh, bank loan documents must be uploaded
- Payment is processed via RTGS/NEFT after physical verification and approval by government officers
- Subsidy is disbursed directly to the beneficiary's bank account (farmer or dealer, as selected during bill upload)
- Data sharing via web service requires confidentiality of API key and adherence to LG Directory codes
- Manufacturer cannot increase MRP after state nodal officer approval; dealer price cannot exceed approved MRP
- Farmer's record cannot be updated after receiving subsidy unless requested by State Nodal Officer
- Incorrect furnished details (gender, DOB, mobile, category, bank, land) may lead to application debarment during physical verification

### Critical Deadlines & Timelines
| Activity | Timeline | Responsibility | Details |----------|----------|
| Application Submission** | Rolling basis — applications are accepted throughout the year as per state-specific timelines and Annual Action Plan (Demand) submission to M&T Division. |
|----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Annual Action Plan (Demand) Submission | Annual | Submission of Annual Action Plan (Demand) for Component-3 of SMAM to M&T Division |
| State-specific Timelines | Varies by state | Applications accepted throughout the year as per state-specific timelines |
| Physical Verification | Post-application | Conducted by government officers after document submission |
| Subsidy Disbursement | Post-verification | Payment file generated after successful physical verification and approval |

**Important Caveats**:
> - Subsidy for CHC projects exceeding ₹25 lakh requires upload of bank loan documents  
> - Farmer's record cannot be updated after receiving subsidy unless requested by State Nodal Officer  
> - Incorrect furnished details (gender, DOB, mobile, category, bank, land) may lead to application debarment during physical verification  
> - Manufacturer cannot increase MRP after state nodal officer approval; dealer price cannot exceed approved MRP  
> - Subsidy is only disbursed after successful physical verification of documents and implements by government officer  
> - OTP is mandatory for registration and transaction notifications  
> - Data sharing via web service requires confidentiality of API key and adherence to LG Directory codes  

**Application Portal**: https://agrimachinery.nic.in  
**Key Contacts**:  
- Email: support-agrimech@gov.in  
- Helpline: 011-23604908, 8076258719 (Technical Support)  
- C.R. Lohi (Dy. Commissioner): cr[dot]lohi[at]nic[dot]in 011-23389019  
- Sh.V.N.Kale (Add. Commissioner): vn[dot]kale[at]gov[dot]in 011-233387200  

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