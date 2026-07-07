# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The **Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP)** is a subsidy-type healthcare scheme implemented pan-India by the **Pharmaceuticals & Medical Devices Bureau of India (PMBI)** under the Ministry of Chemicals & Fertilizers, Government of India. Launched in November 2008, the scheme aims to provide quality generic medicines at affordable prices through dedicated outlets known as **Pradhan Mantri Bhartiya Janaushadhi Kendras (PMBJK)**. As of March 2026, more than 19,000 Kendras are functional across the country, with a product basket comprising 2,100 drugs and 300 surgical items. The scheme operates on a rolling basis with no fixed deadline—applications are accepted year-round via the portal: **https://janaushadhi.gov.in**.

### Objectives
The scheme’s core objectives are:
- To make available quality medicines, consumables, and surgical items at affordable prices for all and reduce out-of-pocket expenditure of consumers/patients.
- To popularize generic medicines among the masses and dispel the notion that low-priced generic medicines are inferior or less effective.
- To ensure easy availability of menstrual health services to all women across India.
- To generate employment by engaging individual entrepreneurs in opening Jan Aushadhi Kendras.

### Eligibility Matrix
Eligibility varies by applicant type but centers on professional qualifications, space requirements, financial capacity, and regulatory compliance. The following table summarizes eligibility criteria:

| **Applicant Type** | **Educational Qualification** | **Space Requirement** | **Key Requirements** | **Special Notes** |
|--------------------|-------------------------------|------------------------|------------------------|-------------------|
| **Individual Applicants** | Must hold D.Pharm/B.Pharm degree **or** employ degree holders and provide proof at application/final approval | Minimum 120 sq. ft. owned or hired (with lease agreement ≥3 years) | - Registered pharmacist<br>- Financial capacity (ITR last 2 years, bank statement last 6 months, PAN/Aadhar)<br>- Drug license in Kendra’s name<br>- Adherence to distance policy (min 1 km between Kendras; no restriction within 500m of hospitals with 100+ beds or medical college-associated hospitals) | In government hospital premises, reputed NGOs/charitable organizations are preferred, though individuals are eligible |
| **Entrepreneurs, Pharmacists, Trusts, Societies, Charitable Organizations** | Must employ B.Pharm/D.Pharm degree holders and provide proof | Minimum 120 sq. ft. owned or hired (with lease agreement ≥3 years) | - Registered pharmacist<br>- Financial capacity (ITR last 2 years, bank statement last 6 months, PAN/Aadhar)<br>- Drug license in Kendra’s name<br>- Adherence to distance policy | Must submit category proof (if applicable) for fee exemption/special incentive |
| **Government Hospital Premises (NGOs/Charitable Orgs)** | Not required for org; must employ degreed pharmacist | Minimum 120 sq. ft. (space provided free by State Govt) | - Reputed NGOs/charitable organizations preferred<br>- Drug license in Kendra’s name<br>- Adherence to distance policy | Individuals also eligible; State Govt selects operator but PMBI can replace if performance inadequate |
| **Government/Nominated Agencies** | Not required for agency; must employ degreed pharmacist | Minimum 120 sq. ft. (space provided free by State Govt) | - Drug license in Kendra’s name<br>- Adherence to distance policy<br>- Financial capacity (if Pvt. Entity: ITR last 2 years, bank statement last 6 months) | Must submit supporting documents for space allocation |

> **Key Caveats**:
> - Special incentive is granted only once per eligible owner under **‘One Family – One Grant’** formula; no other family member/relative can claim it thereafter.
> - Application fee of Rs. 5,000 is non-refundable and not exempted unless proof of eligible category (women entrepreneur, Divyang, SC/ST, ex-serviceman, aspirational district, Himalayan, Island, North-Eastern state) is submitted.
> - Incentive disbursement is subject to stocking mandate: 100% payment for 180-200 medicines, 80% for 150-179, 50% for 100-149, no payment for <100 medicines.
> - Distance policy requires minimum 1 km between Kendras; no restriction within 500m of district/government hospitals with 100+ beds or medical college-associated hospitals.
> - Applicant must not transfer or sublet premises; must use PMBI’s software for all billings; must obtain drug license in Kendra’s name.
> - Special incentive reimbursement requires submission of original bills, bank details, Form GFR 19A, undertakings, and documents within 90 days of Kendra opening; false information leads to rejection, recovery, and legal action.

### Benefits & Financial Support
Financial support under PMBJP includes operating margins, normal incentives, and special one-time incentives. Details are outlined below:

#### Financial Support Structure
| **Component** | **Details** | **Amount/Limit** | **Disbursement Mechanism** |
|---------------|-------------|------------------|----------------------------|
| **Operating Margin** | 20% on MRP (excluding taxes) of each drug sold | No ceiling | Built into MRP; retained by Kendra as profit |
| **Normal Incentive** | 20% of monthly purchases from PMBI, subject to monthly ceiling | Max Rs. 20,000/month | Disbursed 50:50:<br>- 50% based on actual purchase (up to Rs. 10,000)<br>- 50% based on stocking mandate (up to Rs. 10,000) |
| **Special One-Time Incentive** | For eligible categories (women entrepreneurs, Divyang, SC/ST, ex-servicemen, aspirational districts, Himalayan, Island, North-Eastern states) | Rs. 2.00 lakhs (one-time)<br>- Rs. 1.50 lakh for furniture/fixtures<br>- Rs. 0.50 lakh for computer/internet/printer/scanner | Reimbursed against original bills within 90 days of opening; restricted to actual expenditure |
| **Application Fee** | Non-refundable fee for processing | Rs. 5,000 | Exempt for eligible categories upon proof of eligibility |

#### Stocking Mandate Details (for Normal Incentive)
| **Product Range (Medicines Stocked)** | **Incentive Payment %** | **Max Incentive Amount** |
|---------------------------------------|--------------------------|---------------------------|
| 180–200 medicines | 100% | Rs. 10,000 (50% of total incentive) |
| 150–179 medicines | 80% | Rs. 8,000 |
| 100–149 medicines | 50% | Rs. 5,000 |
| <100 medicines | 0% | Rs. 0 |

> **Note**: The normal incentive is calculated as:
> - **Purchase Basis**: 10% of monthly purchases (auto-calculated by PoS system), capped at Rs. 10,000.
> - **Stocking Mandate Basis**: 10% based on product range (per table above), capped at Rs. 10,000.
> - Total monthly incentive = Purchase Basis + Stocking Mandate Basis (max Rs. 20,000).

#### Additional Benefits
- Access to PMBI’s supply chain for WHO-GMP certified, NABL-tested generic medicines.
- Authorization to sell allied medical products not supplied by PMBI.
- Use of PMBI’s software for billing and inventory (provided free of cost).
- Training and support via POS system and helpline (18001808080).
- Estimated savings to citizens: >Rs. 45,000 crores (as of March 2026).
- Average sales per Kendra per month: Rs. 1.50 lacs.

### Application Process
The application process is entirely online via the PMBI portal. Below is a Mermaid.js flowchart illustrating the step-by-step procedure:

```mermaid
flowchart TD
    A[Start: Visit https://janaushadhi.gov.in] --> B[Click 'APPLY FOR KENDRA' tab]
    B --> C[Click 'REGISTER NOW' and fill applicant details (mobile, email)]
    C --> D[Receive email with USER ID and PASSWORD]
    D --> E[Login via USER ID/PASSWORD or Get OTP via registered mobile/email]
    E --> F[Fill application form: basic/Kendra details, adhere to distance policy, upload docs (PDF, <5 MB each)]
    F --> G[For location tagging: drag/drop icon within blue circle to exact address/shop/building]
    G --> H{Pay application fee of Rs. 5,000?}
    H -->|Yes| I[Pay via online payment gateway]
    H -->|No (exempt category)| J[Submit proof of eligible category for fee exemption]
    I --> K[Submit application]
    J --> K
    K --> L[Confirmation sent to registered email]
    L --> M[Check status online via portal or call helpline 18001808080]
    M --> N[End: Await approval]
```

#### Detailed Steps:
1. **Registration**: Click ‘REGISTER NOW’ on the portal, enter mobile number and email ID.
2. **Credentials**: Receive unique USER ID and PASSWORD via email after successful registration.
3. **Login**: Use USER ID/PASSWORD or ‘Get OTP’ option with registered mobile/email.
4. **Form Filling**: Enter basic and proposed Kendra details; adhere to distance policy; upload all required documents in PDF format (each <5 MB).
5. **Location Tagging**: Drag and drop location icon within the blue circle on the map to exact address/shop/building.
6. **Fee Payment**: Pay Rs. 5,000 via online payment gateway (exempt for eligible categories with category proof).
7. **Submission**: After submission, confirmation email is sent; check status online or via helpline (18001808080).

#### Required Documents (14 items):
1. Aadhaar Card  
2. PAN Card  
3. Certificate of SC/ST or Divyang (PWD) or General category Registration certificate  
4. Pharmacist Registration Certification  
5. ITR for last two years  
6. Bank statement for last 6 months  
7. Declaration for GST registration once threshold limit is achieved  
8. Undertaking of distance policy as per guideline  
9. Self-Undertaking of PMBJP Kendra for availing one-time special incentive (if applicable under woman entrepreneur/divyaang/SC/ST/ex-serviceman/aspirational district/Himalayan/Island Territories/North-Eastern States)  
10. Three cheques from Indian Nationalized Banks in favor of PMBI  
11. One cancelled cheque from Indian Nationalized Banks to PMBI  
12. Proof of space ownership or lease agreement (minimum 120 sq. ft.)  
13. Proof of securing a pharmacist (name, State Council registration)  
14. Drug License in the name of ‘Pradhan Mantri Janaushadhi Kendra’

### Contact Details
- **Tollfree**: 1800-180-8080  
- **Email for complaints**: complaints[at]janaushadhi[dot]gov[dot]in  
- **Phone**: 011-49431800  
- **Email for technical queries**: it[at]janaushadhi[dot]gov[dot]in  

### Key Supporting Evidence
- Application Portal: **https://janaushadhi.gov.in**  
- Guidelines Document: `guidelines-for-pmbjk-opening.pdf`  
- Agreement Templates: `copy-of-agreement-for-pmbjk-opening.pdf`, `copy-of-tripartite-agreement-for-pmbjk-opening.pdf`  
- Special Incentive Procedure: `procedure-for-reimbursement-of-special-incentive.pdf`  
- PACS Application Procedure: `procedure-for-pacs-application.pdf`  

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Example*: If a client queries the special incentive amount for women entrepreneurs, search "Rs. 2.00 lakhs" or "one-time special incentive" to instantly confirm it comprises Rs. 1.50 lakh for furniture/fixtures and Rs. 0.50 lakh for computer/internet/printer/scanner, reimbursable within 90 days against original bills.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
*Example*: When a lead states they operate in a rural area with low footfall, use the objection handler: "While footfall matters, PMBJP Kendras in government hospitals or near medical colleges are exempt from strict distance rules and often see guaranteed demand from inpatient/outpatient traffic—let’s check if your location qualifies under the 500m hospital exemption."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
*Example*: After retaining a client, use Stage 1 checklist to verify they have: (1) D.Pharm/B.Pharm degree or employed pharmacist, (2) 120 sq. ft. space with lease agreement, (3) drafted undertaking for distance policy. If missing, send the Client Communication Template: "Per PMBI guidelines, we require [missing doc] to proceed—please share by [date] to avoid delays in your application."

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
*Example*: During onboarding, note in Needs Assessment: "Client struggles with understanding stocking mandate for incentive disbursement." As they send documents, update Compliance Status: "Bank statement (6 months) – Received ✓", "Pharmacist registration – Pending ⬜", triggering follow-up.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
*Example*: When a Kendra application shows "Under review" in the tracker, consult the Escalation Path: "Contact PMBI Helpline (18001808080) → Ask for Status Officer → Reference Application ID → If no update in 48hrs, email it[at]janaushadhi[dot]gov[dot]in with subject: 'URGENT: Application ID [XXX] pending review'."

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
*Example*: For a client with turnover <Rs. 50 lakhs, apply Tier 1 pricing: Retainer Rs. 30,000 + Success Fee 10% of sanctioned incentive. If they qualify for Rs. 2.00 lakh special incentive, quote Success Fee = Rs. 20,000. Update pipeline forecast: "Q3: 3 Tier 1 clients → Expected revenue: Rs. 90,000 retainer + Rs. 60,000 success fees."

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
*Example*: After a discovery call where client confirmed they are a woman entrepreneur in an aspirational district with B.Pharm pharmacist and 150 sq. ft. leased space, replace:  
- `[CLIENT_NAME]` → "Ms. Priya Sharma"  
- `[PROPOSED_KENDRA_LOCATION]` → "Kendra near Govt. Hospital, Block B, Ranchi"  
- `[ELIGIBLE_CATEGORY]` → "Woman Entrepreneur + Aspirational District (NITI Aayog-notified)"  
- `[SPECIAL_INCENTIVE_AMOUNT]` → "Rs. 2.00 lakhs"  
Send within 24 hours to capitalize on engagement momentum.

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
*Example*: Before initiating document collection (Step 1 of Playbook), email client: "Per compliance protocol, please sign and return Sections 8A (Undertaking of Distance Policy) and 8B (Self-Undertaking for Special Incentive Eligibility) attached. We cannot proceed with document submission until these are signed, as PMBI rejects applications with incomplete undertakings." If client is later rejected due to false category claim, cite Disclaimer: "Consultant verifies eligibility based on client-declared information; final approval rests solely with PMBI."