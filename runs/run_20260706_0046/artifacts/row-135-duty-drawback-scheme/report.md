# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The **Duty Drawback Scheme** is a tax benefit scheme administered by the **Central Board of Indirect Taxes and Customs (CBIC)**, under the Department of Revenue, Ministry of Finance, Government of India. It provides financial reimbursement of customs and central excise duties paid on inputs used in the manufacture of export goods. The scheme aims to neutralize the tax burden on exports, enhance international competitiveness, and promote export-oriented industrialization in India.

- **Scheme Name**: Duty Drawback Scheme  
- **Scheme ID**: row-135  
- **Ministry / Category**: Commerce & Trade  
- **Scheme Type**: tax_benefit  
- **Geographic Scope**: Pan-India  
- **Implementing Agency**: Central Board of Indirect Taxes and Customs (CBIC), Department of Revenue, Ministry of Finance, Government of India  
- **Application Portal**: [https://www.icegate.gov.in/](https://www.icegate.gov.in/)  
- **Status / Deadlines**: Claims must be filed within **12 months** from the date of let export of the goods, as per Section 75 of the Customs Act, 1962.  
- **Last Updated**: 2026  
- **Confidence**: medium  

> **Warning**: Failure to file within the 12-month window results in time-barred claims. No extensions are permitted under normal circumstances.

### Objectives
The scheme is designed to achieve the following objectives:
- Refund customs and central excise duties paid on inputs used in the manufacture of export goods.
- Neutralize the incidence of taxes and duties on inputs used for export production.
- Enhance the international competitiveness of Indian exports.
- Promote export-oriented industrialization and value addition in domestic manufacturing.
- Reduce the cost burden on exporters and improve realization in global markets.

### Eligibility Matrix
| Eligibility Criteria | Details | Source |
|----------------------|--------|--------|
| **Who Can Apply** | Exporters who have paid customs duty on imported inputs or central excise duty on indigenous inputs used in the manufacture of goods that are subsequently exported. | Key Facts |
| **Target Beneficiaries** | Exporters; Manufacturers; MSMEs | Key Facts |
| **Input Requirements** | Inputs must be used in the production of goods that are exported. Duty drawback is not available if CENVAT credit or input tax credit under GST has been availed on the same inputs. | Key Facts |
| **Export Condition** | Goods must be exported after payment of duties on inputs. No drawback is allowed on goods exported under bond or letter of undertaking (LUT) without payment of IGST. | Key Facts |
| **Time Limit** | Claim must be filed within **12 months** from the date of let export of the goods. | Key Facts, Application Process |
| **Documentation** | Proper records of import, usage in production, and export must be maintained. | Key Facts |

> **Critical Caveat**: If CENVAT credit or GST input tax credit has been claimed on the same inputs, duty drawback is **not available**. This is a common ground for rejection.

### Benefits & Financial Support
| Benefit Category | Details | Source |
|------------------|--------|--------|
| **Financial Reimbursement** | Refund of customs duty paid on imported inputs and central excise duty paid on indigenous inputs used in manufacture of export goods. | Key Facts |
| **Drawback Rate Calculation** | Fixed as a percentage of the FOB value of exports **or** as a fixed amount per unit, based on input-output norms notified by CBIC. Rates are subject to periodic revision. | Key Facts |
| **Refund Disbursement** | Credited directly to the exporter's bank account via electronic transfer after verification of shipping bills and other documentation. | Key Facts |
| **Economic Impact** | Neutralizes tax burden on exports; improves price competitiveness in international markets; encourages value addition and import substitution in export-oriented sectors; complies with WTO principles (tax remission, not a subsidy). | Key Facts |

> **Note**: The exact drawback rate varies by product and is determined by CBIC-notified input-output norms. Exporters must refer to the latest drawback rate schedule on ICEGATE.

### Required Documents
| S.No | Document | Purpose | Source |
|------|---------|--------|--------|
| 1 | Shipping Bill | Proof of export; primary document for claim filing | Key Facts |
| 2 | Bill of Entry for imported inputs | Proof of import and payment of customs duty | Key Facts |
| 3 | Bank Realization Certificate (BRC) or Foreign Inward Remittance Certificate (FIRC) | Proof of receipt of export proceeds | Key Facts |
| 4 | Proof of payment of customs duty | Evidence of duty paid on inputs | Key Facts |
| 5 | Consent letter from the manufacturer | Required if exporter is not the manufacturer | Key Facts |
| 6 | Declaration regarding non-availment of CENVAT credit or other exemptions | Mandatory to confirm no double benefit | Key Facts |
| 7 | Copy of IEC (Importer Exporter Code) | Mandatory identifier for exporters | Key Facts |
| 8 | Bank account details for refund credit | For electronic transfer of drawback amount | Key Facts |

> **Caveat**: Incomplete or discrepant documents may lead to withholding or rejection of the refund.

### Application Process
The application process is entirely electronic via the ICEGATE portal. Below is a Mermaid flowchart illustrating the step-by-step procedure:

```mermaid
flowchart TD
    A[Start: Determine Eligibility] --> B{Check if customs/excise duty paid on inputs used in export goods?}
    B -->|Yes| C[Maintain Records: Bills of Entry, Warehouse Docs, Production Records, Shipping Bills]
    B -->|No| Z[Not Eligible]
    C --> D[File Drawback Claim Electronically via ICEGATE Portal]
    D --> E[Submit Supporting Documents: Shipping Bill, BRC/FIRC, Bill of Entry, Proof of Duty Payment, Consent Letter (if applicable), Declaration, IEC Copy, Bank Details]
    E --> F[Claim Processed by Jurisdictional Customs Office]
    F --> G{Verification: Documents Complete & Within Time Limit?}
    G -->|Yes| H[Approval & Electronic Credit to Bank Account]
    G -->|No| I[Rejection or Withholding Due to Discrepancies/Missing Docs]
    H --> J[End: Refund Received]
    I --> K[End: Claim Rejected - Resubmit After Correction]
    style A fill:#e3f2fd,stroke:#1565c0
    style J fill:#c8e6c9,stroke:#2e7d32
    style Z fill:#ffcdd2,stroke:#c62828
    style I fill:#ffcdd2,stroke:#c62828
```

> **Key Timelines**:  
> - **Filing Deadline**: Within 12 months from date of let export (Section 75, Customs Act, 1962).  
> - **Processing Time**: Varies by customs office; typically 30–60 days post-submission if documents are complete.  
> - **Refund Credit**: Direct to bank account via NEFT/RTGS after approval.

> **Portal Guidance**: All claims must be filed through [https://www.icegate.gov.in/](https://www.icegate.gov.in/). Manual submissions are not accepted.

### Contact Details
- **Email**: cbic@gov.in  
- **Helpline**: 1800-120-0026 (CBIC Helpdesk)  
- **Portal Support**: ICEGATE Helpdesk available via the application portal  

> **Tip**: For status queries, use the ICEGATE portal’s “Track Application” feature with your IEC and shipping bill number.

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.