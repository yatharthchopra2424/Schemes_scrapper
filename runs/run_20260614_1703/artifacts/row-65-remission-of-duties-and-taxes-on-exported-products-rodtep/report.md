# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
The Remission of Duties and Taxes on Exported Products (RoDTEP) is a scheme administered by the Ministry of Commerce & Industry, Government of India. It is designed to refund embedded central, state, and local duties/taxes that are not otherwise exempted or remitted under other export promotion schemes, thereby making Indian exports more competitive in the global market.

### Objectives
- To refund taxes and duties incurred during the manufacturing and distribution of exported goods that are not exempted under existing schemes.
- To enhance the competitiveness of Indian exports by neutralizing the incidence of such taxes and duties.
- To promote exports by ensuring that exported goods are not burdened with domestic taxes that do not get exported.

### Eligibility Matrix
| Eligibility Criteria | Details |
|----------------------|--------|
| **Applicant Type** | Exporters of goods (including merchant exporters and manufacturer exporters) |
| **Coverage** | All exported products as notified under the scheme from time to time |
| **Ineligibility** | - Goods covered under other duty exemption/remission schemes (e.g., Advance Authorization, Duty Drawback)<br>- Products listed in the negative list notified by DGFT<br>- Exports to certain countries as may be notified<br>- Deemed exports |
| **Registration Requirement** | Must have a valid IEC (Importer Exporter Code) issued by DGFT |
| **Compliance** | Must comply with procedural requirements under the scheme, including timely filing of claims and maintenance of records |

> **Note**: The scheme does not cover services, only goods. Exporters must ensure that their products are not included in the negative list issued periodically by DGFT.

### Benefits & Financial Support
| Benefit Component | Details |
|-------------------|--------|
| **Type of Benefit** | Refund as a percentage of the Freight on Board (FOB) value of exports |
| **Rate of Refund** | Product-specific rates notified by DGFT; varies by HS Code and product category<br>Rates are determined based on the incidence of taxes and duties not exempted elsewhere |
| **Form of Refund** | Transferable electronic scrip (issued via ICEGATE) that can be used to pay basic customs duty on imports |
| **Validity of Scrip** | 24 months from the date of generation |
| **Utilization** | Scrip can be transferred or used to offset basic customs duty liabilities |
| **Claim Frequency** | Claims can be filed on a monthly basis |
| **Documentation Required** | - Shipping Bill<br>- e-BRC (Bank Realization Certificate)<br>- Invoice<br>- Packing List<br>- GST Returns (if applicable)<br>- Proof of payment of taxes/duties (where applicable)<br>- Any other document as specified by DGFT |

> **Warning**: The refund is not in cash but in the form of transferable duty credit scrip. Exporters must monitor the ICEGATE portal for scrip generation and validity.

### Application Process
The following Mermaid flowchart illustrates the step-by-step application process for RoDTEP:

```mermaid
flowchart TD
    A[Start: Export Goods] --> B{Check Product Eligibility<br>(Not in Negative List)}
    B -->|Eligible| C[Maintain Records of Taxes/Duties Paid]
    B -->|Not Eligible| Z[End: Not Eligible for RoDTEP]
    C --> D[File Monthly Claim via DGFT Portal<br>(Within prescribed time limit)]
    D --> E{DGFT Processes Claim<br>(Verification of Documents)}
    E -->|Approved| F[Scrip Generated on ICEGATE<br>(Refund as % of FOB Value)]
    E -->|Rejected| G[Receive Deficiency Memo<br>Submit Clarification/Revised Claim]
    G --> E
    F --> H[Scrip Valid for 24 Months]
    H --> I[Use/Transfer Scrip to Pay Basic Customs Duty]
    I --> J[End: Benefit Utilized]
```

**Application Portal**: [https://www.dgft.gov.in/](https://www.dgft.gov.in/) (RoDTEP section under Schemes)  
**Key Sources**: DGFT RoDTEP guidelines, notifications, and procedural circulars (as referenced from the DGFT website)

> **Critical Deadline**: Claims must be filed within the time limit specified in the relevant public notice (typically within 12 months from the date of Let Export Order, but subject to periodic notifications).  
> **Important**: The scheme is subject to periodic review; rates and product coverage are notified from time to time. Exporters must check the latest DGFT notifications.

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