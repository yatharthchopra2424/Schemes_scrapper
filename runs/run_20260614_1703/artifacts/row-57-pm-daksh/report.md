# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive

### Overview
**PM-DAKSH** (Pradhan Mantri Dakshta Aur Kushalta Sampann Hitgrahi) is a centrally sponsored skill development scheme launched by the **Ministry of Social Justice and Empowerment**, Government of India. It operates on a **Pan-India** geographic scope and is designed to uplift marginalized communities through industry-aligned vocational training. The scheme follows a **rolling basis** application model with no fixed deadline, accepting applications throughout the year subject to training slot availability.

### Objectives
The scheme aims to:
- Provide skill development training to target groups from marginalized communities  
- Enhance employability and livelihood opportunities through industry-aligned training  
- Promote inclusive growth by reducing socio-economic disparities  
- Support self-employment and wage employment after training completion  
- Strengthen the skill ecosystem through partnerships with accredited training providers  
- Monitor and ensure quality of training delivery and placement outcomes  

### Eligibility Matrix
| **Criteria**               | **Details**                                                                 | **Source** |
|----------------------------|-----------------------------------------------------------------------------|------------|
| **Target Communities**     | Scheduled Castes (SC), Other Backward Classes (OBC), Safai Karamcharis (including waste pickers), Denotified Tribes (DNT), Sem Nomadic Tribes, Manual Scavengers | Key Facts |
| **Citizenship**            | Must be Indian citizens                                                     | Key Facts |
| **Age Group**              | 18–45 years (relaxable for certain categories)                              | Key Facts |
| **Economic Status**        | Priority given to economically weaker sections within target communities    | Key Facts |
| **Documentation**          | Valid caste certificate, identity proof, address proof, age proof, photographs, contact details | Key Facts |

> **Note**: Relaxation in age limit applies to specific categories as per government norms, though exact relaxations are not specified in the evidence.

### Benefits & Financial Support
| **Benefit Type**           | **Details**                                                                 | **Financial Mechanism** |
|----------------------------|-----------------------------------------------------------------------------|--------------------------|
| **Training Cost Coverage** | 100% financial support for course fees and training material                | Direct payment to empaneled training providers |
| **Stipend**                | Provided during training (where applicable)                                 | Included in 100% support; paid to provider |
| **Training Material**      | Free provision of course material                                           | Included in 100% support |
| **Certification**          | Nationally recognized certificates aligned with NSQF upon successful completion | Issued by training provider |
| **Placement Support**      | Post-training placement assistance or support for self-employment           | Facilitated by training provider; not guaranteed |
| **Course Sectors**         | IT, healthcare, hospitality, construction, textiles (aligned with NSQF)     | Empaneled provider-dependent |

> **Important Caveat**: There is **no direct cash transfer** to beneficiaries. The government bears the entire cost via reimbursement to accredited institutions based on **successful completion and placement outcomes**.

> **Key Limitations**:
> - Training is available **only through empaneled and accredited training partners**
> - Placement or self-employment support is **not guaranteed** and depends on market conditions and individual performance
> - Beneficiaries must maintain **minimum attendance** as prescribed by the training provider
> - False information or document forgery results in **disqualification and blacklisting**

### Required Documents
| **Document**               | **Accepted Examples**                                                       | **Purpose** |
|----------------------------|-----------------------------------------------------------------------------|-------------|
| Caste Certificate          | SC/OBC/DNT certificate as applicable                                        | Verify community eligibility |
| Identity Proof             | Aadhaar Card, Voter ID, PAN Card                                            | Establish identity |
| Address Proof              | Aadhaar, utility bill, ration card                                          | Confirm residence |
| Age Proof                  | Birth Certificate, School Leaving Certificate                               | Validate age (18–45 years) |
| Passport-sized Photographs | Recent color photographs                                                    | Application and ID purposes |
| Contact Details            | Mobile Number and Email ID                                                  | For communication and updates |

### Application Process Flow
```mermaid
flowchart TD
    A[Start: Visit PM-DAKSH Portal<br>https://pmdaksh.dosje.gov.in] --> B[Click 'Beneficiary Registration' or 'Apply Now']
    B --> C[Fill Online Application Form<br>• Personal Details<br>• Educational Background<br>• Category (SC/OBC/etc.)]
    C --> D[Upload Required Documents<br>• Caste Certificate<br>• Identity Proof<br>• Address Proof<br>• Age Proof<br>• Photographs]
    D --> E[Submit Application]
    E --> F[Await Verification by Implementing Agency]
    F --> G{Application Approved?}
    G -->|Yes| H[Select Approved Training Center & Course]
    G -->|No| I[Application Rejected<br>• Rectify Errors<br>• Resubmit]
    H --> J[Attend Training as per Schedule<br>• Maintain Minimum Attendance]
    J --> K[Complete Assessment & Receive NSQF-Aligned Certification]
    K --> L[Avail Placement Support<br>• Wage Employment Assistance<br>• Self-Employment Guidance]
    L --> M[End: Training Completion & Outcome Monitoring]
```

> **Portal Reference**: All applications must be submitted via the official portal: **https://pmdaksh.dosje.gov.in**  
> **Processing Note**: Applications are processed on a rolling basis; approval depends on verification and slot availability at empaneled centers.

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