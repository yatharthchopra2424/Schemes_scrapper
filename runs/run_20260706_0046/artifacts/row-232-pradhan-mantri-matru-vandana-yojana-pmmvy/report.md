# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
Pradhan Mantri Matru Vandana Yojana (PMMVY) is a maternity benefit scheme under the Ministry of Women and Child Development (MWCD), Government of India. Launched on January 1, 2017, it provides financial assistance to pregnant and lactating mothers for partial compensation of wage loss and to improve health-seeking behaviour. The scheme is implemented as per provisions under Section 4 of the National Food Security Act (NFSA), 2013. It is a sub-component of the Samarthya sub-scheme under the Mission Shakti umbrella scheme, effective from April 1, 2022. The scheme is pan-India except for Telangana and Odisha, which have their own maternity benefit schemes.

### Objectives
- Provide cash incentive for partial compensation for wage loss so that the woman can take adequate rest before and after delivery.
- Promote health-seeking behaviour among pregnant women and lactating mothers.
- Improve health and nutrition for mother and child.
- Encourage institutional delivery.
- Support women from marginalized and vulnerable sections of society.
- Improve Sex Ratio at Birth (SRB) by providing additional incentive for the second girl child (effective April 1, 2022).
- Prevent female foeticide.

### Eligibility Matrix
Eligibility is granted if the woman meets **any one** of the following criteria:

| Eligibility Criteria | Description |
|----------------------|-------------|
| Socially Disadvantaged Groups | Women belonging to Scheduled Castes (SC) and Scheduled Tribes (ST) |
| Disability | Women who are partially (40%) or fully disabled (Divyang Jan) |
| Economic Status (BPL) | Women holder of BPL ration card |
| Health Insurance | Women beneficiaries under Pradhan Mantri Jan Aarogya Yojana (PMJAY) under Ayushman Bharat |
| Labour Welfare | Women holding E-shram card |
| Agriculture Support | Women farmers who are beneficiaries under Kisan Samman Nidhi |
| Rural Employment | Women holding MGNREGA Job Card |
| Income Criteria | Women whose net family income is less than ₹8 Lakh per annum |
| Anganwadi/ASHA Workers | Pregnant and Lactating Anganwadi Workers (AWWs)/ Anganwadi Helpers (AWHs)/ ASHAs |
| Food Security | Women holding Ration Card under NFSA Act 2013 |
| Other Categories | Any other category as may be prescribed by the Central Government |

**Target Beneficiaries**: Pregnant women; lactating mothers; women belonging to socially and economically disadvantaged sections; SC/ST; disabled women; BPL ration card holders; PMJAY beneficiaries; E-shram card holders; Kisan Samman Nidhi beneficiaries; MGNREGA job card holders.

### Benefits & Financial Support
Financial assistance is provided via Direct Benefit Transfer (DBT) to Aadhaar-linked bank/post office account. Benefits vary based on child order and gender:

| Child | Condition | Instalment Structure | Amount (₹) | Disbursement Conditions |
|-------|-----------|----------------------|------------|--------------------------|
| First Child | Any gender | Two instalments | ₹5,000 | **First Instalment**: ₹3,000 after registration of pregnancy and at least one Ante-Natal Check-up (ANC) within 6 months from LMP date at Anganwadi Centre (AWC)/approved health facility.<br>**Second Instalment**: ₹2,000 after childbirth registration and completion of first cycle of immunization (14 weeks) – BCG, OPV, DPT, Hepatitis-B or equivalent. |
| Second Child | Girl child only | Single instalment | ₹6,000 | After childbirth registration and completion of first cycle of immunization (14 weeks). Registration during pregnancy is mandatory. |
| Additional Benefit | Institutional delivery | — | Eligible for Janani Suraksha Yojana (JSY) | After institutional delivery under Ministry of Health and Family Welfare scheme. |

**Key Financial Notes**:
- Total amount paid to beneficiaries as of June 30, 2026: ₹20,344 Cr.
- 5.04 Cr. beneficiaries enrolled; 4.32 Cr. beneficiaries paid.
- Funds transferred via DBT after online application approval by block level officer.
- Husband’s Aadhaar is **not mandatory** (removed under PMMVY 2.0).
- Aadhaar of beneficiary is mandatory for availing the scheme.
- In case of miscarriage/stillbirth, beneficiary treated as fresh beneficiary for future pregnancy.

### Application Process
The application process involves self-registration or assistance from Anganwadi Worker (AWW)/ASHA worker. The process is digital-first with mandatory document upload.

```mermaid
flowchart TD
    A[Start: Pregnant/Lactating Woman] --> B{Access Point}
    B -->|Nearest Anganwadi/ASHA Worker| C[Worker fills online form via PMMVY portal/app]
    B -->|Self-Registration| D[Beneficiary accesses https://pmmvy.wcd.gov.in or PMMVY Mobile App]
    C --> E[Upload Required Documents]
    D --> E
    E --> F[Aadhaar Card]
    E --> G[Aadhaar-mapped Bank/Post Office Account Details]
    E --> H[Mobile Number]
    E --> I[Eligibility Proof (SC/ST cert, BPL card, PMJAY, E-shram, Kisan Samman Nidhi, MGNREGA, income proof <₹8L, NFSA card, disability cert)]
    E --> J[MCP/RCHI Card (Mother and Child Protection Card)]
    E --> K[LMP Date (Last Menstruation Period)]
    E --> L[ANC Date (Ante-Natal Check-up)]
    E --> M[Child Birth Certificate]
    E --> N[Child Immunization Details (14 weeks)]
    F & G & H & I & J & K & L & M & N --> O[Submit Application Form]
    O --> P[Await Approval from Block Level Officer]
    P -->|Approved| Q[Funds Disbursed via DBT to Aadhaar-linked Account]
    P -->|Rejected| R[Review Deficiencies, Resubmit with Corrected Documents]
    R --> O
    Q --> S[End: Benefit Received]
    S --> T{Track Status}
    T -->|Online| U[https://pmmvy.wcd.gov.in/ManageTrackBeneficiary/TrackBeneficiary]
    T -->|Helpline| V[Call 1515 (9:00 AM - 6:00 PM)]
    T -->|Grievance| W[https://pmmvy.wcd.gov.in/ManageCitizenGrievance/RegisterGrievance]
```

**Process Details**:
1. **Registration Window**: Beneficiary eligible to register till **270 days from childbirth**.
2. **Document Upload**: All documents must be uploaded during online application.
3. **Verification**: Block level officer verifies documents and approves/rejects application.
4. **Disbursement**: Funds credited directly to Aadhaar-linked bank/post office account via DBT.
5. **Grievance Redressal**: Available via portal (grievance registration) or helpline (1515).
6. **Status Tracking**: Beneficiary can track application/payment status using Beneficiary ID or registered mobile number on the portal.
7. **Mobile App**: Available on Google Play Store for field functionaries (AWW/ASHA) and beneficiaries.
8. **Self-Registration**: Introduced nationwide under PMMVY 2.0 (previously limited to Delhi/UP pilot).

### Key Caveats & Recent Changes (PMMVY 2.0, effective April 1, 2022)
> **Important**: Benefits for second child are **only provided if the second child is a girl**. Scheme not implemented in Telangana and Odisha (they have own schemes). Aadhaar of beneficiary is mandatory. In case of miscarriage/stillbirth, beneficiary treated as fresh beneficiary for future pregnancy. Husband’s Aadhaar requirement removed.

**Timeline from LMP to Childbirth**: LMP +140 days to LMP +300 days (pre-mature and post-mature).  
**Age Limit**: Beneficiary age must be **18 years 7 months to 55 years** at time of childbirth.  
**Registration Deadline**: Eligible to register in PMMVY portal till **270 days from childbirth**.  
**Second Girl Child Benefit**: Applicable for beneficiaries of second girl child born **on or after 1.04.2022**.

### Supporting Evidence & Statistics
- **Portal**: https://pmmvy.wcd.gov.in
- **Contact**: Email: pmmvy-mwcd@gov.in | Helpline: 1515 (9:00 AM - 6:00 PM)
- **Updated**: Last updated June 30, 2026 (as per portal footer).
- **Mission Shakti Integration**: PMMVY is a component of Samarthya sub-scheme under Mission Shakti (umbrella scheme for safety, security, and empowerment of women).
- **Field Functionaries**: AWW/ASHA can fill applications online for beneficiaries in their jurisdiction; mobile app available for registration.
- **Additional Features**: 
  - Incentive/honorarium for AWW/ASHA for online application: ₹150 (first child, within 30 days), ₹50 (beyond 30 days); ₹250 (second girl child, within 30 days), ₹100 (beyond 30 days).
  - For self-registration by beneficiaries: ₹150 to AWW/ASHA for field verification within 30 days, ₹50 beyond.
  - Tracking system for citizens on mobile app and web application (to be launched soon).

### Scheme ID & Classification
- **Scheme Name**: Pradhan Mantri Matru Vandana Yojana (PMMVY)
- **Scheme ID**: row-232
- **Ministry/Category**: Social Welfare
- **Scheme Type**: Subsidy
- **Geographic Scope**: Pan-India (except Telangana and Odisha)
- **Implementing Agency**: Ministry of Women and Child Development
- **Status/Deadlines**: Active; registration till 270 days from childbirth
- **Last Updated**: 2026
- **Max Per Entity**: ₹5,000 for first child; ₹6,000 for second child (if girl child)
- **Confidence**: High

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Example*: During a call, a client queries, "Is my husband's Aadhaar required?" You instantly search "husband Aadhaar" and find: "The mandatory provision of the husband’s Aadhaar has been removed (under PMMVY 2.0)." You respond confidently, citing the source.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
*Example*: Before a call with a potential client (a NGO worker), you review the "Problem Framing": "Many pregnant women in disadvantaged sections lose income during pregnancy and lack access to nutrition." You use the Qualification Checklist to ask: "Do you or your clients hold any of these: SC/ST certificate, BPL card, PMJAY, E-shram, MGNREGA job card, or have family income under ₹8 lakh?" When they say, "We only work with urban clients," you use the Objection Handler: "PMMVY explicitly includes urban disadvantaged groups via NFSA ration cards and income criteria—many of your clients likely qualify."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
*Example*: After retainer signing, you check off "Stage 1: Eligibility Confirmation" after verifying client’s BPL card. You move to "Stage 2: Document Collection" and use the template to email: "Hi [Name], as discussed, please upload your Aadhaar, bank details, MCP card, LMP date, ANC date, and child’s birth certificate via the portal. Let me know if you need help locating the Anganwadi worker for assistance."

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
*Example*: During onboarding, you record in Needs Assessment: "Client’s primary concern is delayed payments due to bank KYC issues." As they send documents, you update Compliance Status: "Aadhaar: ✓ | Bank Details: ✗ | Mobile: ✓ | Eligibility Proof (BPL): ✓ | MCP Card: ✗ | LMP Date: ✓ | ANC Date: ✗ | Birth Certificate: ✗ | Immunization: ✗". You prioritize chasing MCP and bank details.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
*Example*: At standup, you see Case #452 is at "Stage 07 - Under review". You check the Escalation Path: "Contact Block Level Officer (CDPO) via PMMVY portal grievance section or call helpline 1515 for status." You call the CDPO office, reference the Beneficiary ID, and get an update that documents are pending verification.

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
*Example*: Client is a district-level NGO with annual turnover of ₹2 Cr. You map to Tier 2 (₹1-5 Cr turnover) in the pricing table: Retainer ₹75,000, Success Fee 12%. You quote: "Retainer: ₹75,000 | Success Fee: 12% of sanctioned amount." You update your pipeline forecast: "Q3: Expected revenue from PMMVY cases = ₹90,000 (based on 2 closures at ₹75k retainer + 12% success on avg. ₹5k benefit × 100 beneficiaries)."

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
*Example*: After a successful discovery call with a women’s SHG, you copy the template, replace:  
- `[CLIENT_NAME]` → "Shakti Mahila Sangh"  
- `[S  
- `[TURNNOVER]` → "₹1.8 Cr"  
- `[ELIGIBILITY_CRITERIA_MET]` → "BPL ration card holders, MGNREGA job card holders"  
- `[PROPOSED_RETAINER]` → "₹70,000"  
- `[SUCCESS_FEE]` → "10%"  
You attach 8A and 8B from COMPLIANCE_AND_LEGAL_PACK.pdf and send: "Please find our proposal for PMMVY application support. Kindly review and sign the attached compliance documents to proceed."

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
*Example*: You attach "8A_Data_Privacy_Consent.pdf" and "8B_Service_Terms.pdf" to the proposal email. You state: "Per our engagement policy, we cannot begin document collection (Step 1 of Application Playbook) until these are signed." If a client’s application is rejected due to incomplete immunization records, you cite the disclaimer: "We assist with application preparation; final approval rests solely with the block level officer per PMMVY guidelines." This shields you from liability for government-side delays.