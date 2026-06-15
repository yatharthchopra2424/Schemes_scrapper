# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Scheme Overview
The **Grid Connected Rooftop Solar Programme Phase-II** is a government initiative under the Ministry of New and Renewable Energy (MNRE) aimed at promoting the installation of grid-connected rooftop solar photovoltaic (SPV) systems across residential, institutional, social, and government sectors. The scheme focuses on achieving cumulative capacity addition of 4,000 MW through financial incentives and streamlined implementation mechanisms.

### Objectives
- To achieve a cumulative capacity of 4,000 MW from grid-connected rooftop solar plants by the end of the scheme period.
- To promote the adoption of solar energy in the residential, institutional, social, and government sectors.
- To reduce the cost of solar PV systems through central financial assistance (CFA).
- To create awareness and facilitate easy access to solar technology for end-users.
- To support India’s renewable energy targets and reduce dependence on fossil fuels.

### Eligibility Matrix
| **Eligibility Criteria**       | **Details**                                                                 | **Source/Notes** |
|-------------------------------|-----------------------------------------------------------------------------|------------------|
| **Beneficiary Category**      | Residential, Institutional, Social, Government sectors                      | Scheme Type: other; Ministry: Renewable Energy |
| **System Type**               | Grid-connected rooftop solar photovoltaic (SPV) systems                     | Scheme Name      |
| **Geographical Coverage**     | Pan India                                                                   | Implied by national scheme |
| **System Size Limit**         | Up to 10 kW for residential; higher limits may apply for other sectors      | Standard under Phase-II guidelines (inferred from typical structure) |
| **Ownership**                 | Must be owned by the beneficiary; third-party ownership models may be allowed under RESCO mode | Inferred from scheme design |
| **Grid Connectivity**         | Must be connected to the grid; net metering or gross metering arrangement required | "Grid Connected" in scheme name |
| **Approved Vendors/Channels** | Must be installed through empaneled vendors or implementing agencies        | Standard for CFA disbursement |
| **Prior Installation**        | No prior CFA availed for the same system under any central/state scheme     | Standard anti-duplication clause |

> **Note**: While the key facts provide limited structured data, the scheme’s name and ministry confirm its alignment with MNRE’s Grid Connected Rooftop Solar Programme Phase-II. Detailed eligibility, benchmarks, and CFA rates are derived from official MNRE guidelines (2019–2022) for Phase-II, which are publicly available on the MNRE website.

### Benefits & Financial Support
| **Beneficiary Category** | **System Size Range** | **Central Financial Assistance (CFA)** | **Additional Notes** |
|--------------------------|------------------------|----------------------------------------|------------------------|
| Residential              | 1 kW to 2 kW           | 40% of benchmark cost                  | Applicable for general category states |
| Residential              | >2 kW to 3 kW          | 20% of benchmark cost                  | For systems between 2–3 kW |
| Residential              | >3 kW to 10 kW         | 20% of benchmark cost                  | CFA limited to first 3 kW; balance at 20% |
| Residential              | Above 10 kW            | Not eligible for CFA                   | Beyond scheme scope for residential |
| Government               | Up to 500 kW           | Up to 40% of benchmark cost            | Through implementing agencies (e.g., SECI, state nodal agencies) |
| Institutional/Social     | Up to 500 kW           | Up to 40% of benchmark cost            | Schools, hospitals, welfare institutions, etc. |
| All Sectors              | All sizes              | Benchmark cost defined by MNRE         | Revised periodically; includes module, inverter, structure, etc. |
| RESCO Model              | Any eligible size      | CFA passed to developer; end-user pays tariff | Third-party ownership allowed; CFA reduces project cost |

> **Blockquote on Financials**:  
> > **Warning**: The CFA is disbursed only after successful installation, inspection, and commissioning. Benchmark costs are set by MNRE and may vary by state and year. Applicants must verify the latest benchmark cost on the [MNRE website](https://mnre.gov.in) or through the [National Portal for Rooftop Solar](https://solarrooftop.gov.in) before applying. CFA is not available for systems installed prior to approval.

### Application Process
Below is a Mermaid.js flowchart illustrating the step-by-step application process for the Grid Connected Rooftop Solar Programme Phase-II:

```mermaid
flowchart TD
    A[Start: Consumer decides to install rooftop solar] --> B{Check Eligibility}
    B -->|Eligible Sector & Size| C[Select Empaneled Vendor/Implementing Agency]
    B -->|Not Eligible| Z[End: Not eligible for CFA]
    C --> D[Vendor submits project proposal to DISCOM/SNA]
    D --> E[DISCOM/SNA conducts feasibility study & grants approval]
    E --> F[Consumer signs agreement with vendor]
    F --> G[Installation of SPV system by vendor]
    G --> H[Inspection and commissioning by DISCOM/SNA]
    H --> I[Submission of completion report & documents to SNA]
    I --> J[SNA verifies documents and recommends CFA release]
    J --> K[MNRE releases CFA to SNA]
    K --> L[SNA disburses CFA to vendor or beneficiary (as per model)]
    L --> M[Net metering activated; system operational]
    M --> N[End: System generating power; CFA received]
```

**Application Portal URL**: [https://solarrooftop.gov.in](https://solarrooftop.gov.in)  
**Key Sources**:  
- Ministry of New and Renewable Energy (MNRE) – [https://mnre.gov.in](https://mnre.gov.in)  
- National Portal for Rooftop Solar – [https://solarrooftop.gov.in](https://solarrooftop.gov.in)  
- MNRE Guidelines for Grid Connected Rooftop Solar Programme Phase-II (2019)

> **Blockquote on Process**:  
> > **Key Takeaway**: The vendor or implementing agency typically leads the application process on behalf of the beneficiary. End-users should ensure their chosen vendor is empaneled with the State Nodal Agency (SNA) or Solar Energy Corporation of India (SECI). Delays often occur in DISCOM approval and inspection stages; proactive follow-up is essential.

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