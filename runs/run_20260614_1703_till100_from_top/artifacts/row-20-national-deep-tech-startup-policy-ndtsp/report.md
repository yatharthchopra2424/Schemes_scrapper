# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Scheme Overview
The **National Deep Tech Startup Policy (NDTSP)** is a pan-India initiative implemented by the **Office of the Principal Scientific Adviser (PSA) to the Government of India**. Last updated in 2026, the policy aims to support and nurture the unique requirements of Deep Tech startups in India through strategic incentives, patient capital, and robust intellectual property (IP) protection. The policy is anchored on four pillars: Ensuring the Security of India's Economic Future, Facilitating a Seamless Transition to a Knowledge Driven Economy, Bolstering National Capability and Sovereignty through the Atmanirbhar Bharat Imperative, and Fostering Ethical Innovation.

### Objectives
- Ensuring the Security of India's Economic Future  
- Facilitating a Seamless Transition to a Knowledge Driven Economy  
- Bolstering National Capability and Sovereignty through the Atmanirbhar Bharat Imperative  
- Fostering Ethical Innovation  
- Address systemic challenges through targeted policy interventions  
- Foster an enabling environment for innovation-led growth  
- Establish a foundational framework for India’s emerging deep tech ecosystem  
- Support deep tech startups with strategic incentives, patient capital, and robust intellectual property (IP) protection  

### Eligibility Matrix
Deep tech startups are defined as entities working on producing a solution based on new knowledge/advancements within a scientific or engineering discipline or multiple disciplines, which is yet to be developed or is in the process of being developed; having a high percentage of expenditure on research and development (R&D) activities as a percentage of revenue/funding; owning or being in the process of creating significant novel intellectual property (IP) and taking steps to commercialize the same; and facing extended development timelines, long gestation periods, high capital and infrastructure requirements, and carrying large technical or scientific uncertainty.

| **Criteria** | **Details** |
|--------------|-------------|
| **Definition** | Entities working on solutions based on new scientific/engineering knowledge (single or multi-disciplinary), not yet developed or in development; high R&D expenditure as % of revenue/funding; owning/creating significant novel IP and taking steps to commercialize; facing extended timelines, long gestation, high capital/infrastructure needs, high technical/scientific uncertainty |
| **Turnover Limit (for Deep Tech Startup recognition)** | Up to ₹300 crore for any financial year since incorporation/registration (as per Gazette Notification dated 4th February 2026) |
| **Period of Recognition** | Up to 20 years from date of incorporation/registration (as per Gazette Notification dated 4th February 2026) |
| **Exclusions** | Entities formed by splitting up or reconstruction of an existing business are not considered startups |
| **Target Beneficiaries** | Deep tech startups |
| **Implementing Agency** | Office of the Principal Scientific Adviser (PSA) to the Government of India |
| **Geographic Scope** | Pan-India |
| **Scheme Type** | Other (policy framework with multiple mechanisms) |
| **Last Updated** | 2026 |
| **Fund Size** | ₹10,000 crore (Deep Tech Fund of Funds under Startup India Fund of Funds 2.0) |

### Benefits & Financial Support
The policy provides targeted support including financial incentives and regulatory measures for high-risk, high-impact startups through multiple mechanisms:

| **Benefit Category** | **Details** |
|----------------------|-------------|
| **Deep Tech Fund of Funds (FoF)** | Supported by Startup India Fund of Funds 2.0 with a corpus of ₹10,000 crore to mobilize venture capital; operational guidelines incorporate flexibilities for deep tech including pilot debt-based funding and attraction of patient and global capital |
| **Regulatory Sandboxes** | Sector-specific sandboxes for safe testing, participatory consultations, and standards development; centralized compliance system and Deep Tech Regulatory Advancement Panel; strong data privacy, safety, and evidence-based policymaking |
| **Deep Tech Translation Program** | Identifies high-potential IP for commercialization; strengthens academia-industry partnerships; establishes Technology Transfer Accelerators; provides guidelines for translating publicly funded research into market-ready solutions |
| **IP Regime Alignment** | Single-window platform for IP registration, legal support, and dispute resolution; streamlined policies via faster examinations, reduced fees, patent valuation support; institutional capacity building; centralized IP database; IP insurance; global protection frameworks |
| **Bharat Deep Tech Talent Pool** | National network of scientists, researchers, and prototyping experts; global outreach via foreign missions to attract talent/investment; upskilling support; grant-matching schemes to make deep tech careers viable |
| **Financial Incentives** | Access to venture capital, pilot debt-based funding, patient and global capital, flexibility in government funding caps |
| **IP Support** | IP registration, legal support, dispute resolution, faster examinations, reduced fees, patent valuation support, institutional capacity building, centralized IP database, IP insurance, global protection frameworks |

> **Key Takeaway**: The NDTSP provides a holistic ecosystem support mechanism combining financial instruments (FoF), regulatory facilitation (sandboxes), IP protection, talent development, and translation programs to address the unique challenges of deep tech startups.

### Application Process
The recognition process for startups (including Deep Tech Startups) under the NDTSP framework follows the Startup India recognition procedure administered by DPIIT, with specific attributes for Deep Tech Startup classification.

```mermaid
flowchart TD
    A[Startup Applies for DPIIT Recognition] --> B{Is entity a private limited company, partnership firm, LLP, or cooperative society?}
    B -->|No| C[Reject: Not eligible startup structure]
    B -->|Yes| D[Is entity incorporated/registered in India?]
    D -->|No| C
    D -->|Yes| E[Is entity within 20 years of incorporation/registration? <br/> (Deep Tech specific: up to 20 years vs regular 10 years)]
    E -->|No| C
    E -->|Yes| F[Is turnover for any financial year since incorporation ≤ ₹300 crore? <br/> (Deep Tech specific: ₹300 crore vs regular ₹200 crore)]
    F -->|No| C
    F -->|Yes| G[Is entity working towards innovation/development/improvement of products/services or scalable business model with high employment/wealth potential?]
    G -->|No| C
    G -->|Yes| H[Does entity meet Deep Tech Startup attributes?]
    H -->|No| I[Recognize as regular Startup only]
    H -->|Yes| J[Recognize as Deep Tech Startup]
    J --> K[Access NDTSP benefits: FoF, sandboxes, translation program, IP support, talent pool]
    K --> L[Submit required documents via DPIIT portal for benefit access]
    L --> M[Monitor compliance: annual reporting, IP maintenance, R&D expenditure tracking]
```

**Application Portal**: https://www.startupindia.gov.in (for DPIIT recognition)  
**Key Source**: Gazette Notification No. G.S.R. 108(E) dated 4th February 2026 (Deep Tech Startup definition)  
**Additional Source**: Startup India Fund of Funds 2.0 Notification No. S.O. 1860(E) dated 13th April 2026  

> **Warning**: Deep Tech Startup recognition requires specific documentation proving attributes under the notification (para 1.n), including evidence of new knowledge-based solution, high R&D expenditure % , novel IP creation/commercialization steps, and extended development timelines/high capital requirements. Generic startup applications will not suffice for Deep Tech classification.

> **Note**: The PSA office does not directly process startup applications; recognition is done by DPIIT. However, the PSA office leads policy design, inter-ministerial coordination, and implementation of NDTSP mechanisms like the FoF, sandboxes, and IP framework.

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