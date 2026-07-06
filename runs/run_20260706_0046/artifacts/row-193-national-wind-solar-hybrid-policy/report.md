# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Scheme Overview
The **National Wind-Solar Hybrid Policy** (Scheme ID: row-193) is a pan-India initiative implemented by the **Ministry of New and Renewable Energy (MNRE)** to promote large grid-connected wind-solar PV hybrid systems. The policy does not provide direct financial subsidies but enables access to financial benefits under existing wind and solar schemes through a dedicated fund mechanism. Applications are accepted on a rolling basis throughout the year via the MNRE portal: [https://mnre.gov.in](https://mnre.gov.in).

### Objectives
- Promote large grid-connected wind-solar PV hybrid systems  
- Optimize and efficiently utilize transmission infrastructure and land  
- Reduce variability in renewable power generation  
- Achieve better grid stability  
- Encourage new hybrid projects and hybridization of existing wind or solar projects  
- Provide a framework for promoting hybrid projects through fiscal and financial incentives  
- Outline the methodology for determining the tariff for hybrid projects  

### Eligibility Matrix
| Criteria | Requirement | Source |
|---------|-------------|--------|
| Project Type | All wind and solar power projects, including existing projects seeking hybridization and new hybrid projects | Key Facts |
| Grid Connection | Must be grid-connected and comply with technical standards and grid connectivity norms as specified by the Central Electricity Authority (CEA) | Key Facts |
| Hybridization Requirement | Must ensure optimal utilization of infrastructure and must not exceed the sanctioned capacity at the point of interconnection | Key Facts |
| Target Beneficiaries | Power producers; renewable energy developers; independent power producers (IPPs); state utilities | Key Facts |
| Geographic Scope | Pan-India | Key Facts |

### Benefits & Financial Support
| Benefit Type | Details | Source |
|--------------|---------|--------|
| Infrastructure Utilization | Optimal utilization of transmission infrastructure and land | Key Facts |
| Grid Stability | Reduced variability in power output leading to better grid stability; extended hours of power generation | Key Facts |
| Fiscal Incentives | Eligibility for various fiscal and financial incentives available for wind and solar power projects under existing schemes (e.g., accelerated depreciation, concessional customs duty exemption, priority sector lending) | Key Facts |
| Financial Support Mechanism | Access to dedicated fund; enables availing of financial benefits under existing wind and solar schemes such as generation-based incentives (GBI), accelerated depreciation, and concessional finance through institutions like IREDA | Key Facts |
| Quantum of Support | Depends on the specific scheme under which the project is availing benefits | Key Facts |
| Tariff Framework | Policy outlines methodology for determining the tariff for hybrid projects | Key Facts |

> **Warning**: The policy does not create a new financial incentive but relies on existing wind and solar schemes for benefits. Benefits such as accelerated depreciation and customs duty exemption are subject to the provisions of the respective wind and solar policies.

### Application Process (Mermaid Flowchart)
```mermaid
flowchart TD
    A[Project Developer] -->|1. Submit DPR| B[SECI or State Nodal Agency]
    B -->|2. Evaluate DPR for technical feasibility and grid impact| C{Approved?}
    C -->|No| D[Revise and Resubmit]
    C -->|Yes| E[Project Registration]
    E -->|3. Proceed to Implementation| F[Commissioning]
    F -->|4. Apply for Incentives| G[Respective Implementing Agencies (Wind/Solar Schemes)]
    G -->|5. Avail Benefits| H[GBI, Accelerated Depreciation, Concessional Finance, etc.]
    style A fill:#f9f,stroke:#333
    style H fill:#9f9,stroke:#333
```

#### Detailed Application Steps:
1. **Submission**: Project developers must submit a detailed project report (DPR) to the Solar Energy Corporation of India Limited (SECI) or the respective state nodal agency.  
2. **DPR Contents**: Must include details of wind and solar components, hybridization methodology, single point of grid connection, and compliance with CEA technical standards.  
3. **Evaluation**: SECI or the state nodal agency evaluates the proposal for technical feasibility and grid impact.  
4. **Approval & Registration**: Upon approval, the project is registered and proceeds to implementation.  
5. **Post-Commissioning**: After commissioning, the project can apply for applicable incentives under wind and solar policies through the respective implementing agencies.  

### Required Documents
1. Detailed Project Report (DPR)  
2. Certificate of Incorporation/Registration  
3. Memorandum and Articles of Association  
4. Board resolution authorizing the project  
5. Power Purchase Agreement (PPA) or intent to enter into PPA  
6. Land documents (ownership or lease agreement)  
7. Single line diagram and layout plan  
8. Technical specifications of wind turbines and solar PV modules  
9. Grid connectivity approval from the concerned transmission utility  
10. Environmental and forest clearances (if applicable)  
11. No Objection Certificate (NOC) from the Aviation Authority (if applicable)  
12. Clearance from the Ministry of Defence (if applicable)  

### Key Caveats
- Hybrid projects must not exceed the sanctioned capacity at the point of interconnection  
- The wind and solar components must be connected at a single point to the grid  
- Projects must comply with the Central Electricity Authority (CEA) technical standards for grid connectivity  
- The policy does not create a new financial incentive but relies on existing wind and solar schemes for benefits  
- Benefits such as accelerated depreciation and customs duty exemption are subject to the provisions of the respective wind and solar policies  

### Contact Details
- **Email**: info@mnre.gov.in  
- **Helpline**: Not explicitly mentioned in evidence  
- **Application Portal**: [https://mnre.gov.in](https://mnre.gov.in)  

---

## Consultant's Field Guide to Generated Files

### 1. SCHEME_MASTER_DATABASE.md
**Real-time Usage**: Keep this open in a background tab during all client calls. When a client asks "What is the turnover limit?" or "Who administers this?", CTRL+F in this document to give an immediate, authoritative answer without checking the portal.  
*Example Use Case*: During a discovery call, a client asks, "Is there a minimum project size for hybridization?" You instantly search "sanctioned capacity" in SCHEME_MASTER_DATABASE.md and respond: "The policy requires that hybridization must not exceed the sanctioned capacity at the point of interconnection, but does not specify a minimum size—only grid connectivity and CEA compliance."

### 2. PITCH_AND_SALES_SCRIPTS.md
**Real-time Usage**: Open this file 5 minutes before your first Discovery Call with a lead. Read the "Problem Framing" out loud to hook them, then use the Qualification Checklist to interrogate their eligibility live on the phone. Keep the Objection Handlers table visible so you can immediately counter when they say "We're too small for this."  
*Example Use Case*: A lead says, "Our 50 MW solar farm is too small to benefit." You open the Objection Handlers table and respond: "Actually, the policy encourages hybridization of existing projects—even small ones. A 50 MW solar plant can add 20 MW wind to optimize land use and reduce variability, qualifying for GBI and accelerated depreciation under existing schemes."

### 3. APPLICATION_PLAYBOOK.md
**Real-time Usage**: Print this out or pin it to your desktop once the client signs the retainer. Check off each box in "Stage 1" before moving to "Stage 2". Use the "Client Communication Template" to copy-paste directly into your email when chasing them for pending documents.  
*Example Use Case*: After signing the retainer, you check "Stage 1: DPR Preparation" in APPLICATION_PLAYBOOK.md. You use the Client Communication Template to email: "Per our playbook, we need your single line diagram and CEA grid approval by Friday to proceed to SECI submission."

### 4. CLIENT_ONBOARDING_AND_CRM.md
**Real-time Usage**: Fill this out during or immediately after the onboarding call. Use the Needs Assessment to record their exact pain points. Update the "Compliance Status" table as they email you documents to maintain a single source of truth for what's missing.  
*Example Use Case*: During onboarding, you log in the Needs Assessment: "Client’s main pain point is curtailment due to solar intermittency." As they send the PPA, you update Compliance Status: "PPA received ✅ — awaiting land documents."

### 5. LIVE_CASE_TRACKER.md
**Real-time Usage**: Review this document every morning during your standup. Update the "Stage" column daily. If a case hits "Stage 07 - Under review", use the Escalation Path notes here to know exactly who to call at the government department today.  
*Example Use Case*: At standup, you see a case at "Stage 07 - Under review (SECI)". You check the Escalation Path and call the SECI Hybrid Desk lead (contact from tracker) to inquire: "Just checking on the DPR for Project SuryaHybrid—any feedback needed?"

### 6. FEE_AND_REVENUE_MODEL.md
**Real-time Usage**: Use this file when drafting the proposal. Look at the client's turnover, map them to the pricing tier in the table, and quote that exact Retainer and Success Fee. Use the monthly projection table to update your personal sales pipeline forecast for the quarter.  
*Example Use Case*: A client has ₹250 Cr turnover. You map to Tier 2 in FEE_AND_REVENUE_MODEL.md and quote: "Retainer: ₹3.5 Lakh/month, Success Fee: 8% of incentive value secured." You then update your pipeline forecast with this value.

### 7. CLIENT_PROPOSAL_TEMPLATE.md
**Real-time Usage**: Copy this entire file, paste it into an email or PDF generator, replace the [PLACEHOLDER] tags with the client's actual details gathered from the CRM, and send it immediately after a successful discovery call.  
*Example Use Case*: After a discovery call confirming eligibility, you open CLIENT_PROPOSAL_TEMPLATE.md, replace [CLIENT_NAME], [PROJECT_CAPACITY], [LOCATION], and [PAIN_POINT], then send: "Dear [CLIENT_NAME], based on your 100 MW wind farm in Gujarat facing curtailment, we propose hybridization with 50 MW solar to leverage GBI and accelerated depreciation..."

### 8. COMPLIANCE_AND_LEGAL_PACK.md
**Real-time Usage**: Attach sections 8A and 8B as PDFs to the proposal email. Refuse to start Step 1 of the Application Playbook until the client signs these. Use the Disclaimers to protect yourself legally if the client is rejected by the government agency.  
*Example Use Case*: Before initiating DPR preparation (Step 1 of APPLICATION_PLAYBOOK.md), you email the client: "Please sign and return the attached COMPLIANCE_AND_LEGAL_PACK.md (Sections 8A–8B) as a precondition to engagement. This ensures mutual understanding of scheme limitations and protects both parties per MNRE guidelines." If SECI rejects the project later, you cite Section 8B: "As disclosed, benefits depend on underlying wind/solar schemes—we cannot guarantee GBI approval."