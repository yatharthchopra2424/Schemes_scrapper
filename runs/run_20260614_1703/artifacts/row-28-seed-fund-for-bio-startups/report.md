# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The **Seed Fund for Bio Startups** (Scheme ID: row-28) is a **grant-type** scheme implemented by the **Biotechnology Industry Research Assistance Council (BIRAC)**, a Public Sector Enterprise set up by the Department of Biotechnology (DBT), Government of India. It operates on a **Pan-India** geographic scope with a **rolling basis** application process—no fixed deadline, applications accepted year-round through selected incubators. The scheme was last updated in **2026**.

### Objectives
The Seed Fund aims to:
- Provide capital assistance to post-Proof of Concept (PoC) startups with new and meritorious ideas, innovations, and technologies.
- Act as a bridge between promoter’s investment and angel/venture investment.
- Enable startups to reach a stage where they can raise angel/VC funding or seek bank loans.
- Support startups in covering early-stage costs such as equipment, supplies, and hiring.
- Strengthen the incubator ecosystem by granting funds to BioNEST incubators for deployment.
- Ensure structured monitoring and reporting through half-yearly progress and utilization reports.
- Facilitate exit mechanisms where incubators retain 50% of returns and return the other 50% to BIRAC.

### Eligibility Matrix
| Entity Type | Eligibility Criteria |
|-------------|----------------------|
| **Incubator** | Must have been supported through BIRAC’s BioNEST programme.<br>Must be operational for the last three years.<br>Must have in-house capacity in incubating & mentoring early-stage Biotech/Life Sciences startups.<br>Must have established IP&TT facilitation services for startups.<br>Must have prior experience in management of early-stage funding schemes or other grants. |
| **Startup** | Must be registered under the Companies Act, 2013.<br>Must have at least 51% shareholders as Indian citizens (excluding OCI/PIO).<br>Must be post-PoC startups.<br>Must be early-stage life sciences startups. |

> **Key Caveats** (from evidence):
> - No startup will receive BIRAC Seed Funding support more than once.
> - SEED and LEAP fund support to any startup should be non-concurrent.
> - Incubator must have prior experience in management of early-stage funding schemes or other grants.
> - Grant must be utilized within 36 months from the date of signing the SEED Fund Implementation Agreement (SIFA).
> - Equity and equity-linked instruments shall be held in the name of the incubator.
> - Incubator shall have a BIRAC nominee as integral part of the SEED Fund Governance Committee.

### Benefits & Financial Support
| Aspect | Details |
|--------|---------|
| **Fund Size** | INR 300 Crore (total scheme corpus) |
| **Max Per Entity (Startup)** | Up to INR 30 lakhs per startup |
| **Grant to Incubator** | BIRAC provides grant-in-aid of INR 100–200 lakhs per cycle to selected BioNEST incubators for deployment in biotech startups. |
| **Fund Utilization** | Grant is parked in the incubator’s savings account under a separate account head and must be utilized within 36 months from the date of signing the SEED Fund Implementation Agreement (SIFA). |
| **Investment Instrument** | Equity or equity-linked instruments up to INR 30 lakhs per startup. |
| **Management Fees** | No management fees for incubators. |
| **Return Sharing** | Structured investment and exit framework: 50% return retention by incubator, 50% restitution to BIRAC. |
| **Non-Financial Support** | Access to incubator infrastructure, mentoring, IP&TT support, monitoring, and hand-holding support from incubators. |
| **Reporting** | Half-yearly reporting to BIRAC for transparency and accountability (Utilization Certificates, Statement of Accounts, project progress). |

> **Impact Metrics** (from crawled evidence):
> - 112 SEED Fund Partner BioNEST Incubators
> - 112 startups supported with equity investment of INR 30 Cr
> - INR 398 Cr follow-on funding raised by 71 startups
> - Combined valuation of 89 startups: INR 118 Cr
> - 118 number of products commercialized by startups (last updated Feb 2023)

### Application Process
The application process is incubator-mediated. Startups apply through selected BioNEST incubators, not directly to BIRAC. The process involves:

```mermaid
flowchart TD
    A[BIRAC identifies and selects eligible BioNEST incubators via BISF Committee] --> B[Selected incubators sign SEED Fund Implementation Agreement (SIFA) with BIRAC]
    B --> C[BIRAC disburses grant-in-aid (INR 100–200 lakhs) to incubator’s savings account under separate head]
    C --> D[Incubator designs selection mechanism to screen startups based on vesting requirements]
    D --> E[Incubator identifies Indian startups (registered under Companies Act, 2013, with ≥51% Indian citizen shareholders)]
    E --> F[Incubator provides funding as equity/equity-linked instruments up to INR 30 lakhs per startup]
    F --> G[Legally binding agreement signed between incubator and startup with terms for funding and investment]
    G --> H[Incubator monitors milestones and provides hand-holding support]
    H --> I[Incubator submits half-yearly implementation reports to BIRAC including UC, SOA, and project progress]
    I --> J[On exit, incubator retains 50% of gross return and restitutes 50% to BIRAC within 60 days]
```

**Application Portal**: https://birac.nic.in/seedFundNew.php  
**Key Contacts**: Email: dkumar[at]birac[dot]nic[dot]in, tech03[at]birac[dot]nic[dot]in | Helpline: Not explicitly mentioned

### Required Documents
1. Certificate of Incorporation / Registration  
2. PAN of the entity  
3. Shareholding pattern certified by CA/CS (minimum 51% Indian citizen holding)  
4. Business description or pitch deck  
5. Details of funding received (if any)  
6. Authorization letter from authorized signatory  
7. Project progress reports and utilization certificates (for half-yearly reporting)  
8. Exit report with disinvestment summary (at exit)

> **Note**: The shareholding pattern certificate must be issued by a Chartered Accountant (CA) or Company Secretary (CS) on their letterhead, as per the template in `1650344722-ca-or-cs-certificate-for-shareholding-12-04-2022.docx`.

### Scheme Type & Implementation
- **Type**: Grant (via incubator-mediated equity/equity-linked investment)
- **Implementing Agency**: BIRAC (through BioNEST incubators)
- **Status**: Active, rolling basis
- **Last Updated**: 2026
- **Confidence**: High (per key facts)

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Example*: If a client asks, "What is the maximum funding per startup under Seed Fund?", search for "Max Per Entity" to find "Up to INR 30 lakhs per startup" instantly.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
*Example*: Use the objection handler: "Many startups we work with began with just a prototype and 2 founders—this fund is designed for exactly that stage. Let’s check if you meet the 51% Indian shareholding and post-PoC criteria."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
*Example*: After signing the retainer, check off "Verify incubator is BioNEST-supported and operational ≥3 years" in Stage 1. When chasing for shareholding certificate, use the template: "Hi [Name], per BIRAC guidelines, we need your CA/CS-certified shareholding pattern showing ≥51% Indian citizen holding. Can you share this by EOD tomorrow?"

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
*Example*: During onboarding, note in Needs Assessment: "Client struggles with equipment costs for prototyping." As documents arrive, update Compliance Status: "Shareholding pattern cert. – RECEIVED (2026-06-15); Pitch deck – PENDING."

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
*Example*: When a case reaches "Stage 07 - Under review (BIRAC)", call the BIRAC SEED Fund Committee contact (dkumar@birac.nic.in) to inquire about timelines, using the escalation path: "Contact Technical Officer → Deputy Manager → Joint Director."

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
*Example*: If client turnover is INR 50 lakhs, map to Tier 2 pricing: Retainer = INR 1.5 lakhs, Success Fee = 8% of grant amount. Update pipeline: "Q3 Forecast: +2 Seed Fund clients @ INR 1.5L retainer each."

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
*Example*: After a discovery call confirming eligibility, replace `[CLIENT_NAME]`, `[TURNOVER]`, `[INCUBATOR_NAME]`, and send the proposal with attached `COMPLIANCE_AND_LEGAL_PACK.md` sections.

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
*Example*: Attach `8A_Data_Privacy_Consent.pdf` and `8B_Terms_of_Engagement.pdf` to the proposal. If client refuses to sign, do not proceed—cite disclaimer: "Consultant not liable for scheme eligibility outcomes; client bears responsibility for document accuracy."