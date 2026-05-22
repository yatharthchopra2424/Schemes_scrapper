"""
LLM Prompts for Scheme Intelligence Pipeline
─────────────────────────────────────────────
All prompts follow a consistent structure:
  1. Role & Persona (high-specificity, domain-anchored)
  2. Task Definition (explicit, measurable output)
  3. Constraints (use evidence only, no hallucination)
  4. Output Schema (embedded JSON schema with types)
  5. Few-shot exemplar (for format calibration)
  6. Evidence block (injected at call time)

SECTION A — Analysis prompts (used during crawl+enrich phase)
SECTION B — 8 Business Document prompts (used in report generation phase)
           Each produces one specific Markdown file using the exact template
           structure provided by the firm.

This file is the single source of truth for all LLM instructions.
Changes here affect analysis quality directly — edit with care.
"""
from __future__ import annotations

from ..models import SchemeInput


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION A — ANALYSIS PROMPTS  (structured JSON extraction during crawl)
# ══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = """You are a senior policy intelligence analyst specializing in Indian government schemes, \
government funding programs, DPIIT regulations, startup ecosystems, MSME support, and public financial \
instruments. You work for a policy intelligence firm that produces machine-readable, structured datasets \
from scraped government web sources.

YOUR STRICT OUTPUT RULES:
1. Return ONLY a valid JSON object — no prose, no markdown fences, no preamble, no explanation.
2. Every JSON field must be populated. If data is genuinely unavailable in the evidence, write an \
   empty string "" or empty list [] — never omit the key, never write "N/A" or "Unknown".
3. Use ONLY information from the provided evidence text. Do NOT invent, hallucinate, or supplement \
   with general knowledge.
4. Extract verbatim URLs from the evidence when citing sources.
5. For confidence: "high" = evidence clearly covers all major fields; "medium" = evidence is \
   partial or ambiguous; "low" = evidence is sparse or the page was mostly empty.
6. The JSON must be parseable by Python's json.loads() without modification.
"""


# Few-shot exemplar embedded in the analysis prompt for format calibration
_ANALYSIS_FEW_SHOT = """\
EXAMPLE (abbreviated — your output must be this structure):
{
  "overview": "Startup India Initiative is a flagship Government of India program launched in 2016 by DPIIT to foster innovation, support entrepreneurs, and drive sustainable economic growth.",
  "scheme_type": "recognition",
  "target_beneficiaries": ["startups", "entrepreneurs", "MSME"],
  "geographic_scope": "Pan-India",
  "objectives": [
    "Create a robust startup ecosystem with regulatory ease",
    "Provide tax incentives to eligible startups for 3 years"
  ],
  "eligibility": "Private Limited Company, LLP, or Registered Partnership with turnover < INR 100 Cr, incorporated < 10 years ago, working on innovative products/services/processes.",
  "benefits": "DPIIT recognition, 3-year income tax exemption under 80-IAC, self-certification under 9 labour laws, faster patent examination at 80% rebated fees.",
  "financial_support": "Fund of Funds for Startups (FFS) of INR 10,000 Cr managed by SIDBI invests in SEBI-registered Alternative Investment Funds (AIFs) that fund startups.",
  "fund_size_crores": "10000",
  "grant_amount_per_entity": "Up to INR 20 Lakhs from SISFS for early-stage validation",
  "application_process": "1. Register on startupindia.gov.in 2. Fill DPIIT recognition form with business description 3. Upload Certificate of Incorporation, PAN, pitch deck 4. Submit and await approval (typically 2-7 business days).",
  "application_portal_url": "https://www.startupindia.gov.in/",
  "required_documents": [
    "Certificate of Incorporation / Registration",
    "PAN of the entity",
    "Pitch deck or business description",
    "Authorization letter from authorized signatory",
    "Details of funding received (if any)"
  ],
  "deadlines": "Rolling basis — no fixed deadline. Applications are accepted year-round.",
  "implementing_agency": "Department for Promotion of Industry and Internal Trade (DPIIT), Ministry of Commerce and Industry",
  "contact_details": "Email: startupindia@dipp.gov.in | Helpline: 1800-11-5565",
  "caveats": [
    "Tax benefits under 80-IAC require separate Inter-Ministerial Board (IMB) approval",
    "Startup status expires when turnover exceeds INR 100 Cr or after 10 years"
  ],
  "source_cited_notes": [
    "https://www.startupindia.gov.in/ — Main portal, all program details",
    "https://startupindia.gov.in/recognize-startup — Recognition form details"
  ],
  "last_updated_date": "2024",
  "confidence": "high"
}
END EXAMPLE."""


def build_analysis_prompt(scheme: SchemeInput, evidence_text: str) -> str:
    schema = """\
Required JSON keys and their types:
  "overview"               : string  — 2-4 sentence factual summary of the scheme
  "scheme_type"            : enum    — one of: grant | loan | subsidy | recognition | incubation | tax_benefit | other
  "target_beneficiaries"   : array   — e.g. ["startups", "women entrepreneurs", "SC/ST", "MSME", "agri-startups"]
  "geographic_scope"       : string  — e.g. "Pan-India", "Maharashtra only", "Rural districts"
  "objectives"             : array   — 3-8 key programme objectives as bullet points
  "eligibility"            : string  — full eligibility criteria paragraph
  "benefits"               : string  — comprehensive list of non-financial + financial benefits
  "financial_support"      : string  — paragraph on quantum, type, and mechanism of financial support
  "fund_size_crores"       : string  — total corpus in INR Crores (number only, e.g. "10000"), or ""
  "grant_amount_per_entity": string  — maximum per-entity entitlement, or ""
  "application_process"    : string  — numbered step-by-step application procedure
  "application_portal_url" : string  — direct URL of the application/registration portal, or ""
  "required_documents"     : array   — exhaustive list of documents required at application
  "deadlines"              : string  — application window, submission dates, or "Rolling basis"
  "implementing_agency"    : string  — full legal name of the implementing ministry/department
  "contact_details"        : string  — email, phone, helpline from the evidence, or ""
  "caveats"                : array   — important restrictions, exclusions, expiry conditions
  "source_cited_notes"     : array   — list of URLs from the evidence that support the analysis
  "last_updated_date"      : string  — year or date string from evidence (e.g. "2024"), or ""
  "confidence"             : enum    — low | medium | high"""

    return f"""TASK: Extract structured policy intelligence from the scraped government scheme evidence below.

SCHEME CONTEXT:
  Category   : {scheme.ministry_or_category}
  Scheme Name: {scheme.scheme_name}
  Seed URL   : {scheme.scheme_url}

OUTPUT SCHEMA:
{schema}

{_ANALYSIS_FEW_SHOT}

CHAIN OF THOUGHT (do this internally before writing JSON):
  1. Read all evidence pages carefully, noting which URL each fact comes from.
  2. Identify the primary and sub-schemes (sometimes a URL covers multiple schemes).
  3. Extract financial numbers precisely (fund corpus, per-entity limits, loan amounts).
  4. Extract the application process as numbered steps.
  5. Determine confidence: if major fields are empty, it's "low"; if most fields are filled from evidence, "high".
  6. Write the final JSON only after completing steps 1–5.

EVIDENCE:
{evidence_text}

Return JSON now:"""


# ──────────────────────────────────────────────────────────────────────────────
#   GAP-FILL PROMPT   (secondary LLM call when fields are missing)
# ──────────────────────────────────────────────────────────────────────────────

def build_gap_fill_prompt(scheme_name: str, evidence_text: str, missing_fields: list[str]) -> str:
    fields_str = "\n".join(f"  - {f}" for f in missing_fields)
    return f"""You previously analyzed the scheme "{scheme_name}" but the following fields were left empty:
{fields_str}

Re-read the evidence carefully and focus ONLY on finding information for these specific missing fields.
Return a JSON object containing ONLY these keys with their values.
If the information truly does not exist in the evidence, return an empty string "" for that key.

Evidence:
{evidence_text}

Return JSON with only the missing keys:"""


# ══════════════════════════════════════════════════════════════════════════════
#  SECTION B — BUSINESS DOCUMENT PROMPTS  (8 separate LLM calls per scheme)
# ══════════════════════════════════════════════════════════════════════════════
#
#  These use the exact template structures provided by the firm.
#  The LLM must:
#    1. Populate all fields it can from the evidence + key_facts
#    2. Use [TO BE FILLED BY CONSULTANT] for firm-specific operational data
#    3. Use the EXACT section headers provided below
#
# ══════════════════════════════════════════════════════════════════════════════

BUSINESS_DOCS_SYSTEM_PROMPT = """You are a senior government scheme consulting expert and professional \
business writer. You produce complete, polished Markdown business documents for a scheme advisory firm. \
Your documents are used by consultants to win clients, execute applications, and manage cases.

YOUR RULES:
1. Return ONLY clean, well-structured Markdown. No JSON. No code fences around the output.
2. Use the EXACT section headers specified in the task. Do not rename or reorder them.
3. Populate every field you can with real data from the KEY FACTS block and supporting evidence.
4. For operational fields the firm must fill in themselves (e.g. "Our Win Rate", "Last Successful Client", \
   retainer amounts, consultant names), write [TO BE FILLED BY CONSULTANT] as the placeholder.
5. Do NOT write placeholder text for scheme data (eligibility, amounts, documents, etc.) \
   — these must be populated from the evidence.
6. Write in professional, clear English. No jargon. Tables and bullet lists preferred over long paragraphs.
7. Always cite the application portal URL and key sources at the relevant section.
"""


def _evidence_block(key_facts: str, full_text: str) -> str:
    """Build the standard evidence injection block used in all 8 prompts."""
    parts = []
    if key_facts:
        parts.append(key_facts)
    if full_text:
        parts.append("=== SUPPORTING EVIDENCE (crawled web pages + downloaded PDFs) ===\n" + full_text)
    return "\n\n".join(parts)


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 1 — SCHEME_MASTER_DATABASE.md
# ──────────────────────────────────────────────────────────────────────────────

def build_scheme_master_db_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete SCHEME_MASTER_DATABASE.md entry for the scheme described in the evidence below.

This is the firm's master database — the AI brain used for client qualification.
Populate every field from the evidence. Use [TO BE FILLED BY CONSULTANT] only for firm-internal operational data.

Use EXACTLY these headings and structure:

---

# Scheme Master Database

## Meta
- Last updated: [TODAY'S DATE]
- Total schemes listed: 1
- Categories: (pick from: Government grants | Tax incentives | Subsidies | Equity schemes | Loan schemes | Export schemes | R&D schemes | Employment schemes | Recognition schemes)

---

### [SCHEME NAME]
- **Scheme ID:** SCH-001
- **Category:** [Grant / Tax / Subsidy / Loan / Equity / Recognition / Incubation]
- **Geography:** [Country / State / City / Pan-India / EU / UK / US]
- **Administering Body:** [Ministry / Agency / Bank / Authority — from evidence]
- **Portal / Application URL:** [link — from evidence]
- **Current Status:** Open | Closed | Rolling | Seasonal
- **Window:** [Dates or "Always Open" — from evidence]

#### Eligibility Criteria
- Business type: [from evidence]
- Age of business: [from evidence]
- Sector: [from evidence]
- Revenue cap: [from evidence — e.g. turnover < ₹25 Cr]
- Employee count: [from evidence or leave blank if not mentioned]
- Other: [any other eligibility conditions from evidence]

#### What It Offers
- Amount / Benefit: [from evidence — specific numbers]
- Disbursement mode: [Reimbursement / Direct credit / Tax offset — from evidence]
- Duration of benefit: [One-time / Annual / 3 years — from evidence]

#### Documents Required
(numbered list from evidence — be exhaustive)

#### Application Process (numbered steps)
(extract from evidence — every step on its own line)

#### Timeline
- Processing time: [from evidence or [TO BE FILLED BY CONSULTANT]]
- Success rate: [TO BE FILLED BY CONSULTANT]

#### Our Fee
- Retainer: [TO BE FILLED BY CONSULTANT]
- Success fee: [TO BE FILLED BY CONSULTANT]

#### Internal Notes
- Key officer contact: [from evidence contact details, or [TO BE FILLED BY CONSULTANT]]
- Common rejection reasons: [infer from caveats/eligibility or [TO BE FILLED BY CONSULTANT]]
- Our win rate on this scheme: [TO BE FILLED BY CONSULTANT]
- Last successful client: [TO BE FILLED BY CONSULTANT]

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 2 — PITCH_AND_SALES_SCRIPTS.md
# ──────────────────────────────────────────────────────────────────────────────

def build_pitch_scripts_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete PITCH_AND_SALES_SCRIPTS.md document for the scheme described in the evidence.

This is the consultant's call playbook. Personalise the discovery questions, pitch narrative,
and objection handlers using the REAL scheme name, eligibility criteria, financial amounts,
and sector focus from the evidence. Do NOT use generic placeholders for scheme data.

Use EXACTLY these headings and structure:

---

# Pitch & Sales Scripts

## Philosophy
We are advisors, not salespeople. We diagnose first. We only pitch a scheme if it fits the client. We never oversell success rates.

---

## 1. Discovery Call Script (First Contact — 20 min)

### Opening (2 min)
(Write a warm, consultative opening referencing the scheme's sector/beneficiary focus)

### Discovery Questions
(6-8 questions tailored to this scheme's eligibility criteria — e.g. if it's for startups < 10 years old, ask about incorporation date)

### Qualification Checklist (internal — don't read aloud)
(Checkboxes derived from the scheme's actual eligibility criteria from evidence)

### Transition to Pitch
(2-3 lines that bridge from discovery to pitching THIS specific scheme — use the real scheme name and benefit amount)

---

## 2. Scheme Pitch (5 min)

### Structure: Problem → Scheme → Value → Proof → Next Step

**Problem framing:**
(What problem does this scheme solve for its target beneficiary? Use evidence.)

**Scheme intro:**
(Introduce the scheme with its full name, administering body, type of benefit, and amount — all from evidence)

**Why they qualify (personalised):**
(Reference specific eligibility boxes from evidence — 3-4 criteria as bullet points)

**Proof:**
"We've helped [N] similar businesses get approved for this. [TO BE FILLED BY CONSULTANT]"

**Next step:**
(Standard next step — free eligibility check, no commitment, success fee only model)

---

## 3. Objection Handlers

| Objection | Response |
|---|---|
| "I've heard these schemes never get approved" | (Tailor response using evidence of successful applicants or approval data if available) |
| "How much do you charge?" | [TO BE FILLED BY CONSULTANT] |
| "I'll try it myself first" | (Mention 2 common mistakes from the scheme's caveats/eligibility) |
| "We're too small / too big" | (Reference exact revenue/employee eligibility thresholds from evidence) |
| "I don't have the documents ready" | (List the 3 most commonly missing documents for this scheme from evidence) |
| "We already work with a CA" | "Great — we work alongside CAs. They handle your accounts; we handle the scheme strategy and applications." |

---

## 4. Closing Script

(Standard 3-sentence closing — summarise the top 2 benefits, propose a 30-min document review, reference the scheme's portal URL as a credibility anchor)

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 3 — APPLICATION_PLAYBOOK.md
# ──────────────────────────────────────────────────────────────────────────────

def build_application_playbook_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete APPLICATION_PLAYBOOK.md for the scheme described in the evidence.

This is the team's step-by-step execution manual. Every section must be populated using the
real eligibility criteria, documents, application steps, and portal details from the evidence.

Use EXACTLY these headings and structure:

---

# Application Playbook

## How to Use This File
For each new client case, assign it a Case ID, pick the target scheme, and follow the steps below.

---

## Stage 1: Eligibility Verification (Day 1–3)

### Checklist
(Generate a detailed checklist with ✅ boxes based on the scheme's ACTUAL eligibility criteria from evidence.
Include: registration type, turnover threshold, employee count, sector, age of business, other conditions.)

---

## Stage 2: Document Collection (Day 3–10)

### Universal Documents (always required)
(Standard government documents list — inc, PAN, ITR, GST, bank statements, Udyam)

### Scheme-Specific Documents
(Extract from evidence — documents uniquely required for this scheme beyond the universal set)

### Document Quality Check
(Standard checklist — file size, name matching, certification requirements, language)

### Client Communication Template
(Write a specific message for THIS scheme including scheme name, portal, and deadline info from evidence)

---

## Stage 3: Application Drafting (Day 10–18)

### Project Report / DPR (if required)
(Note whether DPR is required for this scheme. If yes, list standard sections. If not mentioned, flag "verify with nodal officer.")

### Application Form Filling Protocol
(7-8 critical rules for filling the form — include portal-specific notes from evidence if available)

### Internal Review Gate
(Standard review checklist — all fields complete, docs attached, declarations signed)

---

## Stage 4: Submission & Follow-Up (Day 18–30)

### Submission Protocol
(Standard — screenshot of submission, store reference number, set follow-up reminders)

### Follow-Up Script (to nodal officer or portal helpdesk)
(Template email using the actual scheme name and contact details from evidence)

### Escalation Path
- Level 1: [Portal helpdesk from evidence, or helpline if available]
- Level 2: [Nodal officer details from evidence, or [TO BE FILLED BY CONSULTANT]]
- Level 3: RTI filing if no response within statutory SLA

---

## Stage 5: Post-Approval (Day 30–90+)

### Approval Actions
(Standard checklist — approval letter, verify sanctioned amount, utilization certificate, invoice success fee)

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 4 — CLIENT_ONBOARDING_AND_CRM.md
# ──────────────────────────────────────────────────────────────────────────────

def build_client_onboarding_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete CLIENT_ONBOARDING_AND_CRM.md document for the scheme described in the evidence.

This is the client intake and CRM system. The Needs Assessment section must reference the scheme's
real sector focus and financial benefits. The Compliance Status table must match the documents
actually required by this scheme.

Use EXACTLY these headings and structure:

---

# Client Onboarding & CRM

## New Client Intake Form

**Date:** [DATE]
**Assigned consultant:** [TO BE FILLED BY CONSULTANT]
**Lead source:** [Referral / Website / Cold call / Partner]

### Business Details
(Standard fields: Legal name, Trading name, Registration type, CIN/LLPIN, Date of incorporation,
Registered address, Operational address, Website)

### Promoter / Director Details
| Name | Role | % Shareholding | PAN | Mobile | Email |
|---|---|---|---|---|---|
| | | | | | |

### Business Profile
(Standard fields: Industry/sector, NIC code, Primary products/services, Current annual turnover, No. of employees, Existing registrations)

Note which registrations are specifically required for this scheme based on evidence.

### Needs Assessment
- What outcome are you seeking? (tick all that apply — list options relevant to THIS scheme's benefit type)
- Investment planned in next 12 months:
- Any pending government applications? Details:
- Any past rejected applications? What scheme and why:

### Compliance Status
(Table of documents — include ALL documents required by this scheme from evidence.
Mark which are critical vs. optional.)

| Document | Available? | Year/Period | Notes |
|---|---|---|---|
(populate rows based on scheme's required documents from evidence)

### Engagement Terms
- Retainer fee: [TO BE FILLED BY CONSULTANT]
- Success fee: [TO BE FILLED BY CONSULTANT]
- Target schemes: [Scheme name from evidence]
- Engagement start date:
- Expected application date: (note deadlines from evidence)

### Communication Preferences
(Standard — primary contact, preferred channel, update frequency)

---

## CRM Stage Pipeline

(Standard 10-stage pipeline — Lead through Disbursed/Rejected.
Add a scheme-specific note at the "In preparation" stage about this scheme's DPR/portal requirements.)

| Stage | Description | Action |
|---|---|---|
| 01 - Lead | Initial contact made | Schedule discovery call |
| 02 - Qualified | Eligibility confirmed for [scheme name] | Send proposal |
| 03 - Engaged | Retainer signed | Start onboarding |
| 04 - Docs collection | Gathering documents | Chase missing items |
| 05 - In preparation | Drafting application on [portal URL from evidence] | Internal review |
| 06 - Submitted | Application filed on [portal] | Begin follow-up |
| 07 - Under review | With [implementing agency from evidence] | Monitor + respond to queries |
| 08 - Approved | Sanction letter received | Invoice success fee |
| 09 - Disbursed | Money received by client | Close case, request testimonial |
| 10 - Rejected | Application declined | Analyze, re-apply or alternate scheme |

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 5 — LIVE_CASE_TRACKER.md
# ──────────────────────────────────────────────────────────────────────────────

def build_case_tracker_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete LIVE_CASE_TRACKER.md for the scheme described in the evidence.

This is a real-time operations dashboard. Create one pre-filled example case (CST-001) for this
specific scheme, populating every field with real scheme data from the evidence.
All client-specific data (company name, consultant name, etc.) should use [PLACEHOLDER].

Use EXACTLY these headings and structure:

---

# Live Case Tracker

## Active Cases

(Table with one example row for this scheme. Populate scheme name, implementing agency,
estimated value from evidence. Leave client/consultant columns as [PLACEHOLDER].)

| Case ID | Client | Scheme | Consultant | Stage | Submitted | Next Action | Deadline | Est. Value (₹) | Status |
|---|---|---|---|---|---|---|---|---|---|
| CST-001 | [PLACEHOLDER] | [scheme name from evidence] | [PLACEHOLDER] | Submitted | DD/MM | Follow-up call | [deadline from evidence or DD/MM] | [amount from evidence or TO BE FILLED] | 🟡 In progress |

---

## Case Detail Sheet

### Case ID: CST-001
**Client:** [PLACEHOLDER]
**Scheme:** [Full scheme name from evidence + scheme ID]
**Target benefit:** ₹[amount from evidence, or TO BE FILLED BY CONSULTANT]
**Consultant lead:** [PLACEHOLDER]
**Support analyst:** [PLACEHOLDER]

#### Timeline Log
(Pre-populate with the standard milestones for this scheme: discovery → proposal → retainer → docs → submission.
Include scheme-specific steps like portal registration, DPR submission if applicable based on evidence.)

| Date | Action | By | Notes |
|---|---|---|---|
| DD/MM | Discovery call | [Name] | Client confirmed eligible for [scheme name] |
| DD/MM | Proposal sent | [Name] | Awaiting sign-off |
| DD/MM | Retainer received | [Name] | ₹[TO BE FILLED] |
| DD/MM | Docs collection started | [Name] | [N]/[total docs from evidence] docs received |
| DD/MM | Registered on [portal from evidence] | [Name] | Portal login created |
| DD/MM | Application submitted | [Name] | Ref# XXXXX |

#### Document Tracker
(Use the actual list of required documents for this scheme from evidence.
Pre-fill with Received = ❌, Quality Check = — for a fresh case.)

| Document | Received | Quality Check | Notes |
|---|---|---|---|
(populate rows based on scheme-specific documents from evidence)

#### Correspondence Log
| Date | Channel | From | To | Summary |
|---|---|---|---|---|
| DD/MM | Email | Us | [Implementing agency from evidence] | Requested status update |

#### Risks & Blockers
(List 2-3 common risks specific to this scheme based on its caveats/eligibility from evidence)

#### Fee Tracking
| Item | Amount | Invoice # | Status |
|---|---|---|---|
| Retainer | [TO BE FILLED BY CONSULTANT] | INV-001 | Paid |
| Success fee | [TO BE FILLED BY CONSULTANT] | — | Pending approval |

---

## Monthly Metrics Dashboard

| Metric | This Month | Last Month | Target |
|---|---|---|---|
| New cases opened | | | |
| Applications submitted | | | |
| Approvals received | | | |
| Total value approved (₹) | | | |
| Avg. processing time (days) | [from evidence if available] | | |
| Success rate % | | | |
| Revenue — retainers | | | |
| Revenue — success fees | | | |

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 6 — FEE_AND_REVENUE_MODEL.md
# ──────────────────────────────────────────────────────────────────────────────

def build_fee_model_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete FEE_AND_REVENUE_MODEL.md for consulting on the scheme described in the evidence.

Use the scheme's actual financial benefit amounts to calibrate the revenue projections table.
Retainer and success fee amounts are set by the firm and should use [TO BE FILLED BY CONSULTANT].

Use EXACTLY these headings and structure:

---

# Fee & Revenue Model

## Pricing Tiers

(Standard 4-tier table. Add a "Scheme Applicability" column showing which client tier typically
applies for this specific scheme based on its eligibility criteria — e.g. if it's for startups
with turnover < ₹100 Cr, note which tier that maps to.)

| Tier | Client Type | Retainer | Success Fee | Typical Scheme Value | Scheme Applicability |
|---|---|---|---|---|---|
| Starter | Micro / Proprietorship | [TO BE FILLED BY CONSULTANT] | 8–10% | < ₹10L | [applies / does not apply — based on evidence] |
| Growth | MSME / Startup | [TO BE FILLED BY CONSULTANT] | 6–8% | ₹10L–₹1Cr | [applies / does not apply] |
| Scale | Mid-market | [TO BE FILLED BY CONSULTANT] | 4–6% | ₹1Cr–₹10Cr | [applies / does not apply] |
| Enterprise | Large / Group | Custom | 2–4% | > ₹10Cr | [applies / does not apply] |

## Pricing Principles
(Standard 4 principles — include a scheme-specific note about the risk profile of THIS scheme
based on its processing time and evidence of success from the crawled data)

## Invoice Templates

### Retainer Invoice
(Standard template — populate with scheme name from evidence in the description field)

### Success Fee Invoice
(Standard template — populate with scheme name from evidence and implementing agency)

## Revenue Projections (Monthly Model)

(Standard 3-month projection table. In the "Avg scheme value" row, use the actual
grant/benefit amount from the evidence. Add a footnote if processing time from evidence
affects the revenue lag assumption.)

| Item | Assumption | Month 1 | Month 3 | Month 6 |
|---|---|---|---|---|
| New clients | | 5 | 10 | 20 |
| Avg retainer/client | | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] |
| Retainer revenue | | | | |
| Approvals (lag 3 months) | Typical for [scheme name] | 0 | 3 | 8 |
| Avg scheme value | [amount from evidence] | — | [amount from evidence] | [amount from evidence] |
| Success fee @ [X]% | | — | | |
| Success fee revenue | | — | | |
| **Total revenue** | | | | |

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 7 — CLIENT_PROPOSAL_TEMPLATE.md
# ──────────────────────────────────────────────────────────────────────────────

def build_client_proposal_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete CLIENT_PROPOSAL_TEMPLATE.md for the scheme described in the evidence.

This is a ready-to-send client proposal. All scheme-specific data (name, benefit amount, timeline,
eligibility summary, portal URL) must be populated from the evidence. Client-specific fields
(company name, retainer amount) use [PLACEHOLDER].

Use EXACTLY these headings and structure:

---

# Client Proposal

**Prepared for:** [Client Legal Name]
**Prepared by:** [Firm Name]
**Date:** [DATE]
**Valid until:** [DATE + 15 days]
**Proposal Ref:** PROP-[YEAR]-[SEQ]

---

## 1. Executive Summary
(2-3 sentences. Reference the scheme name, administering body, and potential benefit amount from evidence.
Example structure: "Based on our initial review of [Client]'s business profile, we have identified
[scheme name] — a [type] scheme administered by [agency] — for which your business appears eligible.
The potential benefit is approximately ₹[X].")

## 2. Recommended Schemes

| Scheme | Potential Benefit | Est. Timeline | Confidence Level |
|---|---|---|---|
| [Scheme name from evidence] | ₹[amount from evidence] | [processing time from evidence or "3–6 months"] | High / Medium |

## 3. Our Scope of Work
(Standard 7-point scope list. Add a scheme-specific item about portal registration on [portal URL from evidence]
and whether a DPR/project report is required based on evidence.)

## 4. What We Need From You
(Standard 3-point list — documents per attached checklist, point of contact, 2-day response SLA.
Reference the scheme's document list from evidence in item 1.)

## 5. Our Fees

| Item | Amount |
|---|---|
| Engagement retainer (one-time) | [TO BE FILLED BY CONSULTANT] + GST |
| Success fee (on actual sanction) | [TO BE FILLED BY CONSULTANT]% of sanctioned amount + GST |

*No success fee is payable if the scheme is not sanctioned.*

## 6. Our Track Record
(Standard track record section. Leave [TO BE FILLED BY CONSULTANT] for client count and approval rate.
Add a scheme-specific line: "This scheme — [scheme name] — is administered by [agency from evidence]
and has a [rolling / seasonal from evidence] application window.")

## 7. Terms & Conditions (Summary)
(Standard 6-point T&C summary. Include scheme-specific item:
"Engagement is for [scheme name] as listed in Section 2 only.")

## 8. Acceptance
(Standard signature block)

---

EVIDENCE:
{evidence}
"""


# ──────────────────────────────────────────────────────────────────────────────
#  FILE 8 — COMPLIANCE_AND_LEGAL_PACK.md
# ──────────────────────────────────────────────────────────────────────────────

def build_compliance_pack_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce a complete COMPLIANCE_AND_LEGAL_PACK.md for consulting on the scheme described in the evidence.

Sections 8A–8D must be standard legal templates. Personalise where indicated using the scheme name,
implementing agency, and jurisdiction from the evidence.

Use EXACTLY these headings and structure:

---

# Compliance & Legal Pack

## 8A. Engagement Letter / Service Agreement (Summary Template)

(Standard service agreement template. Insert the scheme name and implementing agency from evidence
in the "Services" clause. Keep the "No guarantee clause" verbatim — government approval is always
at the authority's discretion.)

This Agreement is between [FIRM NAME] ("Consultant") and [CLIENT NAME] ("Client") dated [DATE].

**Services:** Consultant agrees to provide scheme identification, eligibility assessment, application
preparation, and submission support for [scheme name from evidence] administered by
[implementing agency from evidence].

**Fees:** As per the attached proposal. Retainer is payable upfront. Success fee is payable on sanction.

**No guarantee clause:** Consultant makes no representation that any scheme will be approved.
Approval is at the sole discretion of [implementing agency from evidence].

**Client obligations:** Client to provide accurate information and documents. Misrepresentation by
the client absolves Consultant of liability.

**Confidentiality:** Both parties agree not to disclose confidential information to third parties.

**Data protection:** Client data is stored securely and not shared except as required for scheme
applications submitted to [implementing agency from evidence].

**Termination:** Either party may terminate with 15 days notice. Retainer already paid is non-refundable.

**Jurisdiction:** [City] courts. Governing law: Indian law.

---

## 8B. NDA Template

(Standard NDA template — applicable for sharing client financial data with the implementing agency.
Add a scheme-specific note: "This NDA covers all materials submitted as part of the
[scheme name from evidence] application process.")

---

## 8C. Standard Disclaimers

1. "This assessment is based on information provided by the client and publicly available guidelines
   for [scheme name from evidence]. Eligibility is subject to final verification by
   [implementing agency from evidence]."
2. "Scheme guidelines, eligibility criteria, and benefit amounts for [scheme name from evidence]
   are subject to change by [implementing agency from evidence] without notice. We recommend
   verifying current guidelines at [portal URL from evidence] before submission."
3. "[Firm Name] is a consulting firm. We are not a government body and have no authority to approve
   or reject any application under [scheme name from evidence]."
4. "Success fees are earned for facilitation services only and do not imply any guarantee of outcome."

---

## 8D. Internal Data Handling Policy

(Standard data handling policy — encrypted cloud storage, 2FA, limited access, no personal devices,
2-year retention post case closure, 24-hour breach notification.)

Add a scheme-specific note:
"All documents submitted to [implementing agency from evidence] under [scheme name from evidence]
must be retained for a minimum of [3 years / as per scheme guidelines from evidence] for audit purposes."

---

EVIDENCE:
{evidence}
"""
# ──────────────────────────────────────────────────────────────────────────────
#  FILE 9 — REPORT.md (Comprehensive Learning Path & File Guide)
# ──────────────────────────────────────────────────────────────────────────────

def build_comprehensive_report_prompt(key_facts: str, full_text: str) -> str:
    evidence = _evidence_block(key_facts, full_text)
    return f"""TASK: Produce an extremely comprehensive and highly visual REPORT.md for the scheme described in the evidence.

CRITICAL INSTRUCTIONS FOR GENERATION:
1. **Length & Depth:** Do NOT summarize briefly. Extract every single detail, number, deadline, and eligibility criteria from the evidence. The report should be long, exhaustive, and act as a complete masterclass on the scheme.
2. **Visual Formatting:** You MUST use rich Markdown elements:
   - Use **Mermaid.js flowcharts** (`mermaid`) to illustrate the application process or fund flow.
   - Use **Tables** extensively for financials, eligibility criteria, and timelines.
   - Use **Blockquotes** (`>`) for important warnings, caveats, or key takeaways.
   - Use **Bold** text for critical numbers, dates, and entity names.

This report serves two main purposes:
1. An exhaustive learning-path-style deep dive into the scheme.
2. An actionable, real-time "Guide to Generated Files" section that tells the consultant EXACTLY how to use the other 8 business documents in their day-to-day workflow.

Use EXACTLY these headings and structure:

---

# Comprehensive Scheme Masterclass & File Guide

## Scheme Deep Dive
(Provide an exhaustive breakdown of the scheme. Start from the basic overview, move to objectives, eligibility matrix [use a table], benefits & financial support [use tables], and application process [use a Mermaid flowchart]. Leave absolutely NO important points out from the evidence.)

## Consultant's Field Guide to Generated Files
(Provide highly actionable, real-time instructions for how you, the consultant, will actually use these 8 files during a client engagement. Use specific "When to use" and "How to use" scenarios, rather than just describing the file.)

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

---

EVIDENCE:
{evidence}
"""


# ══════════════════════════════════════════════════════════════════════════════
#  LEGACY MARKDOWN PROMPTS  (kept for backward compatibility — report.md only)
# ══════════════════════════════════════════════════════════════════════════════

MARKDOWN_SYSTEM_PROMPT = """You are an expert policy communications specialist with deep knowledge of Indian \
government programs. You produce high-quality Markdown documents for policy briefs, grant applications, and \
official communications.

YOUR RULES:
1. Return ONLY clean, well-structured Markdown. No JSON. No code fences around the output.
2. Use evidence-only facts. Do not hallucinate figures, URLs, or details not in the evidence.
3. Be comprehensive but concise. Aim for 400–700 words per document.
4. Use proper Markdown: ## headers, bullet lists, **bold** for key terms, tables where appropriate.
5. Always cite source URLs at the bottom under a ## Sources section.
"""


def build_pitch_prompt(scheme_name: str, evidence_text: str) -> str:
    return f"""TASK: Write a compelling policy pitch document for the scheme: **"{scheme_name}"**

STRUCTURE (use these exact headings):
## Why This Scheme Matters
(2-3 sentences: the big-picture problem it solves)

## What You Get
(bullet list of top 5 most impactful benefits — financial and non-financial)

## Who Qualifies
(concise eligibility summary — 1 short paragraph or bullet list)

## Financial Support
(specific numbers: fund corpus, per-entity limit, type of support: grant/loan/equity)

## How to Get Started
(3-5 step quick-start guide)

## Key Contact
(portal URL, email, helpline if available in evidence)

## Sources
(list of URLs from the evidence)

Use ONLY information from this evidence:
{evidence_text}"""


def build_howto_prompt(scheme_name: str, evidence_text: str) -> str:
    return f"""TASK: Write a detailed, step-by-step "How to Apply" guide for: **"{scheme_name}"**

STRUCTURE (use these exact headings):
## Prerequisites
(who is eligible — bullet checklist with ✅ for each criterion)

## Documents Required
(numbered list of every document needed — be exhaustive)

## Step-by-Step Application Process
(numbered steps — each step on its own line, sub-steps indented as a, b, c)

## Timeline & Deadlines
(application window, processing times, when to expect outcomes)

## Common Mistakes to Avoid
(3-5 pitfalls based on the evidence / eligibility criteria)

## After Submission
(what happens next: timeline, notifications, approval process)

## Help & Support
(portal URL, helpline, email contacts from evidence)

## Sources
(list of source URLs)

Use ONLY information from this evidence:
{evidence_text}"""


def build_summary_prompt(scheme_name: str, evidence_text: str) -> str:
    return f"""TASK: Write an authoritative executive summary for policy officials on: **"{scheme_name}"**

STRUCTURE (use these exact headings):
## Scheme at a Glance
(brief 1-paragraph overview with scheme type, ministry, and year of launch if known)

## Programme Objectives
(bullet list of 4-6 primary objectives)

## Target Beneficiaries
(who the scheme is designed for — startups, MSME, agriculture, women, SC/ST etc.)

## Financial Architecture
(fund size, per-entity limit, type of support — present as a Markdown table if data is available:
| Parameter | Value |
|---|---|
| Fund Corpus | ₹ X Cr |
| Max Per Entity | ₹ Y L |)

## Implementation Mechanism
(how funds flow or services are delivered — through which agencies, what intermediaries)

## Current Status & Impact
(any available statistics: beneficiaries, amount disbursed, states covered)

## Key Caveats
(important restrictions, eligibility expiry, compliance requirements)

## Sources
(list of URLs from the evidence)

Use ONLY information from this evidence:
{evidence_text}"""


# ──────────────────────────────────────────────────────────────────────────────
#  FALLBACK BROWSER AGENT PROMPT
# ──────────────────────────────────────────────────────────────────────────────

BROWSER_AGENT_PROMPT = """You are an autonomous web navigator trying to locate missing information about a government scheme.
The fields that are currently MISSING and urgently needed are:
{missing_fields}

Below is a simplified DOM representation of the current web page. It lists interactable elements (buttons, links, accordions) along with their text. Each element has an [ID].

Your job is to decide the single best next action to uncover the missing information. 
You can click an element that you think might reveal the data (like "Eligibility", "How to apply", "Guidelines").

You must return ONLY a JSON object with your chosen action.
Valid actions:
1. {{"action": "click", "id": <integer_id>}} - click an element to open it (use the ID from the DOM).
2. {{"action": "wait", "id": 0}} - just wait if you think content is still loading.
3. {{"action": "done", "id": 0}} - if you believe the missing information is likely now visible on the screen or hopelessly unavailable.

Example JSON:
{{"action": "click", "id": 45}}

CURRENT DOM SUMMARY:
{dom_summary}

Return ONLY raw JSON action. No markdown fences, no explanation.
Action:"""
