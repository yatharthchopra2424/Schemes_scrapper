# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Scheme Overview
The **Small Hydro Power Programme (SHP)** is a subsidy-based initiative under the **Ministry of New and Renewable Energy (MNRE)**, Government of India, aimed at promoting decentralized renewable energy generation through small hydro power projects (up to 25 MW capacity). The scheme operates on a **rolling basis** with **no fixed deadline**—applications are accepted throughout the year. It was last updated in **2026**.

**Implementing Agency**: Ministry of New and Renewable Energy (MNRE)  
**Geographic Scope**: Pan-India  
**Scheme ID**: row-192  
**Application Portal**: [https://mnre.gov.in](https://mnre.gov.in)  
**Contact Details**:  
- Email: spankaj@nic.in  
- Helpline: 011-20849116  

> **Key Takeaway**: The SHP scheme is designed to enhance energy access in remote, hilly, and inaccessible regions while contributing to national renewable energy targets and reducing greenhouse gas emissions.

---

### Scheme Objectives
The programme seeks to achieve the following strategic goals:
- Promote development of small hydro power projects (up to 25 MW) for renewable energy generation  
- Enhance energy access in remote, hilly, and inaccessible regions through decentralized power  
- Support survey and investigation of potential small hydro sites  
- Encourage private and public sector participation in small hydro development  
- Reduce dependence on fossil fuels and contribute to India's clean energy targets  
- Strengthen grid connectivity and stability in rural and mountainous areas  

---

### Eligibility Matrix
| **Eligible Entities** | **Project Requirements** | **Preference Criteria** |
|------------------------|---------------------------|--------------------------|
| State Governments      | Capacity up to 25 MW      | Projects in hilly and remote areas |
| State Power Utilities  | Technically feasible as per CEA guidelines | — |
| Public Sector Undertakings (PSUs) | Must submit Detailed Project Report (DPR) | — |
| Private Developers     | Obtain necessary clearances (forest, environment, irrigation) | — |
| Cooperative Societies  | Implementing agency must submit DPR and clearances | — |

> **Critical Caveats**:
> - Projects exceeding **25 MW capacity** are **not eligible** under SHP  
> - CFA is subject to availability of funds and approval by the Project Appraisal Committee (PAC)  
> - Beneficiaries must submit utilization certificates and progress reports for subsequent instalments  
> - Projects must be commissioned within the stipulated timeline; extensions require approval with penalties  

---

### Financial Support & Benefits
#### Central Financial Assistance (CFA) Structure
| **Activity** | **General States** | **Special Category States**<br>(North Eastern & Himalayan) | **Notes** |
|--------------|--------------------|------------------------------------------------------------|-----------|
| Survey & Investigation | 90% of project cost<br>(up to ₹10 lakh per project) | 100% of project cost<br>(up to ₹10 lakh per project) | CFA capped at ₹10 lakh for S&I |
| Project Implementation | Up to ₹5 crore per MW<br>(ceiling: ₹20 crore per project) | Up to ₹7 crore per MW<br>(ceiling: ₹20 crore per project) | CFA released in instalments based on milestones |
| **Total CFA Ceiling** | **₹20 crore per project** | **₹20 crore per project** | Applies to both categories |

#### Additional Benefits
- Technical guidance from MNRE and its institutes (NISE, NIWE, etc.)  
- Facilitation of clearances and approvals from relevant departments  
- Promotion of renewable energy in underserved regions  
- Contribution to national renewable energy targets and GHG emission reduction  

> **Warning**: CFA disbursement is **strictly tied to project milestones** and requires submission of **utilization certificates** for each tranche. Failure to comply may result in withholding of funds or penalties.

---

### Required Documents
Applicants must submit the following documents as part of their application:
1. Detailed Project Report (DPR) as per CEA guidelines  
2. Land ownership or lease documents  
3. Clearances from forest, environment, and irrigation departments  
4. Geological and hydrological survey reports  
5. Single line diagram and layout plan  
6. Power Purchase Agreement (PPA) or consent from State Utility  
7. Incorporation/registration documents of the applicant  
8. Financial viability report  
9. Undertaking for completion of project within stipulated time  

> **Note**: All documents must be self-attested where required. Incomplete submissions will lead to rejection.

---

### Application Process Flowchart
```mermaid
flowchart TD
    A[Identify Potential Small Hydro Site] --> B[Prepare DPR as per CEA Guidelines]
    B --> C[Obtain Necessary Clearances<br>(Forest, Environment, Irrigation)]
    C --> D[Submit DPR + Application to State Nodal Agency (SNA)]
    D --> E[SNA Forwards Proposal to MNRE]
    E --> F[MNRE Appraises via Project Appraisal Committee (PAC)]
    F --> G{Approval?}
    G -->|Yes| H[Administrative Sanction Issued by MNRE]
    G -->|No| I[Revise & Resubmit Based on PAC Feedback]
    H --> J[Funds Released in Instalments<br>Based on Project Milestones]
    J --> K[Submit Utilization Certificates & Progress Reports]
    K --> L[Next Instalment Released]
    L --> M[Project Commissioning]
    M --> N[Final Utilization Certificate Submission]
    style A fill:#e3f2fd,stroke:#1565c0
    style H fill:#c8e6c9,stroke:#2e7d32
    style I fill:#ffebee,stroke:#c62828
    style J fill:#fff3e0,stroke:#ef6c00
```

> **Process Notes**:
> - The SNA acts as the first-level filter and forwarding agency  
> - PAC appraisal includes technical, financial, and viability assessment  
> - Fund release is **milestone-based**—no upfront disbursement  
> - Continuous monitoring via progress reports and utilization certificates is mandatory  

---

### Timelines & Deadlines
| **Activity** | **Timeline** | **Responsible Agency** |
|--------------|--------------|------------------------|
| Application Submission | Rolling basis (no fixed deadline) | Applicant → SNA |
| SNA Forwarding to MNRE | Within 15 days of receipt | State Nodal Agency |
| PAC Appraisal | 45–60 days after receipt | MNRE |
| Administrative Sanction | Within 7 days of PAC approval | MNRE |
| 1st Instalment Release | On award of project (EA acceptance) | MNRE |
| Subsequent Instalments | Tied to 25%, 75%, 100% project completion | MNRE (after PAC verification) |
| Project Commissioning | As per DPR timeline (max 2–3 years typical) | Beneficiary |
| Final Closure | Upon submission of final utilization certificate | MNRE |

> **Penalty Clause**: Extensions beyond stipulated timeline require PAC approval and attract a penalty of **@1% of financial support released** per month of delay.

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Example Use Case Scenario: During a discovery call, a private developer asks, "Is there a minimum project size for SHP?" You instantly search "minimum capacity" and confirm: "Projects must be up to 25 MW—no minimum specified, but viability is assessed via DPR."*

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
* Example Use: When a cooperative society says, "We don’t have the clearances yet," you deploy the handler: "That’s exactly why we start with the DPR and clearance mapping—our playbook includes a checklist for forest/env/irrigation NOCs to fast-track this."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
* Example Use: After signing a PSU client, you check "Stage 1: DPR Preparation" → confirm geological survey done → move to "Stage 2: Clearances" → use the template to email: "Per our playbook, we now need forest and irrigation NOCs—please share status by EOD."

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
* Example Use: During onboarding, a state utility mentions delays in land lease docs → you log this in Needs Assessment → as they send the lease agreement, you update Compliance Status from "Pending" to "Received" → triggers next step in tracker.

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
* Example Use: At 9 AM standup, you see a case moved to "Stage 07 - Under review" → you check the Escalation Path: "Call PAC Secretary at MNRE via spankaj@nic.in with LoA reference" → you place the call before 11 AM.

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
* Example Use: A private developer with ₹500 crore turnover falls into Tier 2 → you quote Retainer: ₹2.5 lakh, Success Fee: 8% of CFA secured → you log this in your pipeline forecast as "Expected closure: Q3."

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
* Example Use: After a positive discovery call with a cooperative society, you replace [CLIENT_NAME], [PROJECT_CAPACITY], [LOCATION] in the template → generate PDF → send within 1 hour with subject: "Proposal: SHP Support for 5 MW Project in Himachal."

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
* Example Use: Before initiating DPR preparation (Stage 1), you email the Legal Pack → client signs and returns Annexures VIII & XII → you mark CRM as "Legal Cleared" → only then do you assign consultant to begin DPR review. If rejected later, you cite Clause 13(v) to show client-managed risk.