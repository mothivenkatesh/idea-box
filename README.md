<div align="center">

# 💡 idea-box

### Stop reading "100 startup ideas" listicles. Start with **1,000 pain points that already have paying users and broken tools.**

<br>

[![Stars](https://img.shields.io/github/stars/mothivenkatesh/idea-box?style=for-the-badge&logo=github&color=FDE047)](https://github.com/mothivenkatesh/idea-box/stargazers)
[![Forks](https://img.shields.io/github/forks/mothivenkatesh/idea-box?style=for-the-badge&logo=github&color=C7D2FE)](https://github.com/mothivenkatesh/idea-box/network/members)
[![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)](./LICENSE)
[![Pain points](https://img.shields.io/badge/pain%20points-1%2C000-0289F7?style=for-the-badge)](./data)
[![Deep-validated](https://img.shields.io/badge/deep--validated-50-8247E5?style=for-the-badge)](./data/validations-s-tier.json)

<br>

**[🔎 Browse the live site](https://mothivenkatesh.github.io/idea-box/web/)** &nbsp;·&nbsp; **[📊 Download the JSON](./data)** &nbsp;·&nbsp; **[🧠 See the schema](./schema.json)** &nbsp;·&nbsp; **[🤝 Add yours](./CONTRIBUTING.md)**

</div>

<br>

---

## The pitch in one paragraph

Most "startup idea" lists are vibes. Bullet points, no audience, no numbers, no sources. **idea-box is the opposite.** Every entry answers six questions a serious builder actually asks:

1. **Who hurts?** (the specific role — not "small businesses")
2. **How badly?** (pain severity, how often it happens, what breaks)
3. **How many of them are there?** (firm counts, industry labor spend)
4. **What are they paying today?** (the pricing at incumbent SaaS tools)
5. **Why don't today's tools fix it?** (the concrete gap)
6. **Why is now a good time to build?** (what infra or rule change made it possible)

Top candidates are then run through a deeper investor-grade check — **market sizing triangulated three ways, unit economics, an 8-factor score, and a "what would have to be true" risk list.**

<br>

## A real entry, unpacked

> **PAIN-0001 — Phone/device repair shop: fragmented quote-to-invoice lifecycle**
>
> - **Who hurts** · 1–5 technician repair-shop owner
> - **What breaks** · Customer texts asking for an iPhone screen price. Owner manually checks stock in a spreadsheet, quotes via SMS, writes the booking in Google Calendar, logs it in the POS. Nothing is connected — parts get oversold, bookings get missed, everything is re-keyed.
> - **How big** · ~150,000 shops in North America alone
> - **What they pay now** · ~$200/month to RepairShopr, RepairDesk, or MyGadgetRepairs
> - **Why incumbents miss it** · Rigid software, no native WhatsApp/SMS agent, no stock-aware intake, weak omnichannel
> - **Why now** · WhatsApp Business API is cheap, LLM voice costs crashed, SMBs expect conversational tools
> - **Sources** · Rossmann Forum thread on shop software · CellSmart POS review roundup
> - **Signal strength** · 9/10 severity · 9/10 tedium · score 92/100

That's what every one of the 1,000 entries gives you. Not a slogan. Not a vibe.

<br>

## Who this is for

| If you are… | You'll use this to… |
|---|---|
| **A founder hunting for an idea** | Skip the vibes lists. Go straight to problems with named customers + known price points. |
| **A VC or angel investor** | Pre-triage decks. If the problem isn't in here — or it is but the listed incumbents already solved it — that's a signal. |
| **A product leader at a scaling company** | Find the 3 adjacent problems your customers have that you could wrap into a new SKU. |
| **A vertical-AI builder** | Map labor budgets to agent workflows. Every entry tags a workflow family (7 of them cover most of B2B). |
| **A researcher or PMM** | The highest-density dataset anywhere on **where unsolved operational pain maps to buyable software.** |

<br>

## What's inside

<table>
<tr>
<td width="50%" valign="top">

### 📦 1,000 entries across 24 batches

Grouped by the kind of builder who'd care:

| # | Batch | Entries |
|---|---|--:|
| 01 | Repair shops, home services | 25 |
| 02 | Marketing, sales, RevOps | 25 |
| 03 | India / Bharat (UPI, Zepto, Porter…) | 25 |
| 04 | Due diligence, compliance, legal | 25 |
| 05 | Healthcare & medical | 20 |
| 06 | Finance, HR, ops, long-tail | 30 |
| 07 | Off-beat niches (funeral, towing, drone…) | 25 |
| 08 | Reconciliation, automation, ServiceTitan | 25 |
| 09 | YC-style agent wedges | 50 |
| 10 | Real Reddit pain threads | 50 |
| 11 | International (EU · APAC · MENA · LATAM) | 50 |
| 12 | Enterprise IT, gaming, climate | 50 |
| 13 | Business-ops deep | 50 |
| 14 | Direct-to-consumer & e-commerce | 50 |
| 15 | Financial services deep | 50 |
| 16 | Supply chain & logistics | 50 |
| 17 | Scientific, pharma, R&D | 50 |
| 18 | Specialty professional services | 50 |
| 19 | Consumer & prosumer | 50 |
| 20 | AI-native emerging categories | 50 |
| 21 | Healthcare adjacent (payer, pharmacy…) | 50 |
| 22 | Public sector / govtech | 50 |
| 23 | Niche B2B long-tail | 50 |
| 24 | Final curated | 50 |

</td>
<td width="50%" valign="top">

### 🔬 The top 50 get a deeper investor-grade check

Each of the 50 highest-scoring entries is run through the **[AI-cofounder](https://github.com/mothivenkatesh/ai-cofounder)** 8-factor rubric. You get:

**Market sizing, triangulated 3 ways**
- **Bottom-up** — firm count × what they'd pay per year
- **Value-based** — hours saved × hourly cost × 15% capture
- **Top-down** — the incumbent category spend
- A **convergence check** that flags the estimate if the three methods disagree by >2×

**Unit economics stub** in SaaS / marketplace / D2C / fintech shapes
- Annual contract value, gross margin, LTV, CAC, LTV:CAC ratio, payback period

**8-layer score** (1–5 each)
- Problem clarity · Market size · Solution differentiation · Unit econ · P&L viability · Timing & moat · Founder fit · Execution risk

**Top 3 riskiest assumptions** — the "what would have to be true" list

**Verdict**
- `Strong signal` · `Conditional pass` · `Fragile` · `Weak`

### 🖥 Browser UI

Zero-build. Single HTML file. Filter by vertical, workflow family, severity, willingness-to-pay direction, and validation verdict. [Try it →](https://mothivenkatesh.github.io/idea-box/web/)

### ⚙ Tooling

- `scripts/add-pain.py` — drop a CSV, get JSON with auto opportunity-scoring
- `scripts/validate-s-tier.py` — re-run the deep-validation rubric anytime

</td>
</tr>
</table>

<br>

## Schema in plain English

Every entry in `data/pains-*.json` has these fields. No acronyms here — what it is and why you care:

| Field | Plain-English meaning | Why a builder cares |
|---|---|---|
| `id` | Permanent ID like `PAIN-0001` | Stable reference across versions |
| `title` | One-line pain in human language | The hook |
| `vertical` | Industry label (e.g. "Device Repair", "Veterinary") | Filters out what you don't want to build in |
| `workflow_family` | 1 of 7 operational patterns | Maps to the kind of agent you'd build |
| `persona` | The specific buyer role — not a category | You have to know who you're calling |
| `pain_description` | What breaks, in their words | The narrative that sells your pitch |
| `pain_severity` | 1–10 — how painful | 10 = losing money or at regulatory risk |
| `tedium_score` | 1–10 — how robotic the task is | 10 = pure data entry, prime AI replacement |
| `frequency` | How often the pain happens | "Daily per shop" signals volume-priced pricing |
| `tam_firms` | Estimated count of target firms | Bottom-up market sizing |
| `tam_labor_spend_usd` | Annual labor spend in the category | Menlo's "labor budget, not IT budget" frame |
| `tam_direction` | Growing, stable, or declining | Decides whether you're surfing or swimming |
| `current_wtp_usd_month` | What they **already pay** to incumbents ($/month) | Anchors your pricing ceiling |
| `incumbent_tools` | Competing SaaS tools today | Your competition |
| `incumbent_gap` | Why today's tools fail them | Your wedge |
| `santifer_pattern` | A one-line solution sketch | Starting point, not a spec |
| `sources` | Reddit threads, forums, reviews | Evidence, not opinion |
| `verbatim_quotes` | Real user complaints pulled from those threads — quoted as written, with author handle + date | The hook that sells the pain: someone's actual words, not your paraphrase |
| `reference_build` | A live implementation of the pattern (if any) | Proof it can be done |
| `why_now` | What changed to make this buildable | The catalyst for today |
| `opportunity_score` | Composite 0–100 signal | Sort on this, then read the details |

*TAM = total addressable market · WTP = willingness to pay · SaaS = subscription software*

<br>

## Quick start

### 🌐 Browse the data (recommended)

**Live:** [mothivenkatesh.github.io/idea-box/web/](https://mothivenkatesh.github.io/idea-box/web/)

Prefer local:
```bash
git clone https://github.com/mothivenkatesh/idea-box.git
cd idea-box
python -m http.server 8000
# open http://localhost:8000/web/
```

### 🔍 Query with jq

```bash
# Top 10 India-specific opportunities
jq '[.[] | select(.vertical | test("Bharat"))] | sort_by(-.opportunity_score) | .[0:10] | map({id, title, persona})' \
   data/pains-03-bharat-india.json

# All deep-validated "Conditional pass" candidates
jq '.[] | select(.ai_cofounder_validation.verdict == "Conditional pass") | .title' \
   data/validations-s-tier.json

# Count entries by workflow family across the whole corpus
jq -s 'add | group_by(.workflow_family) | map({family: .[0].workflow_family, count: length})' \
   data/pains-*.json
```

### 🐍 Query with Python

```python
import json, glob
pains = []
for f in sorted(glob.glob("data/pains-*.json")):
    pains.extend(json.load(open(f, encoding="utf-8")))

# SMB opportunities where target already pays >= $200/month today
opps = sorted(
    [p for p in pains
     if (p.get("current_wtp_usd_month") or 0) >= 200
     and "smb" in p.get("tags", [])],
    key=lambda p: -(p.get("opportunity_score") or 0)
)[:20]
```

<br>

## How the data was built

Synthesized from — and cross-checked against — sources that compound credibility:

- [Santifer's Business OS case study](https://santifer.io/business-os-for-airtable) — 16 years of running a real repair shop, 170 hours/month of operator time saved with the pattern. Applied in 200+ entries.
- [a16z's vertical-AI + vertical-SaaS thesis](https://a16z.com/vertical-saas-now-with-ai-inside/) — the industry-labor-spend framing
- [Menlo Ventures — Software Finally Gets to Work](https://menlovc.com/perspective/software-finally-gets-to-work-the-opportunity-in-vertical-ai/) — $740B healthcare admin vs $63B IT
- [Lyzr AI — 101 enterprise use cases](https://www.lyzr.ai/case-studies/) + [Sierra](https://sierra.ai/about) + [Nurix AI](https://www.nurix.ai/) — what's actually shipping at enterprise today
- [ideabrowser.com](https://www.ideabrowser.com/) (Greg Isenberg) + [painonsocial.com](https://painonsocial.com/) — the "structured idea card" format
- [BigIdeasDB](https://bigideasdb.com/) — 238K real complaints across Reddit, G2, Capterra, Upwork analyzed
- **Direct Reddit reading** — r/smallbusiness, r/Entrepreneur, r/accounting, r/nocode, r/Airtable, r/HVAC, r/realtors, r/medicine, r/sysadmin, r/construction, and ~20 more
- G2 and Capterra 2-star review patterns (gaps hide here)
- NAICS labor-spend data for market-sizing triangulation

<br>

## Who this borrows from (and links back to)

- [Santifer](https://santifer.io/) — the repair-shop pattern that proves the "Airtable + automation + AI agent" bundle works for SMBs
- [Greg Isenberg's ideabrowser](https://www.ideabrowser.com/) — the card-per-idea discipline
- [painonsocial.com](https://painonsocial.com/) — Reddit-mined pain-point scoring
- [BigIdeasDB](https://bigideasdb.com/) — the 238K-complaint validation approach
- [Frappe's Espresso design system](https://github.com/frappe/frappe-ui) — styling for the browser UI

If you found this through any of them, go ⭐ them too.

<br>

## Roadmap

- [x] **v1.0** — 1,000 entries, top 50 deep-validated, live browser
- [x] **v1.1** — `verbatim_quotes` field on the schema, real quotes seeded for the 50 S-tier entries, empty slots on the other 950 for community fill-in
- [ ] **v1.2** — open contributions via PR + issue templates
- [ ] **v1.3** — deep-validation expanded to top 100
- [ ] **v2.0** — automated pipeline: nightly Reddit pull → candidate entries → human review

<br>

## Contributing

PRs welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md). The highest-leverage contributions:

1. **Add a source link** to an existing entry — a Reddit thread, G2 review, or forum post that validates the pain
2. **Fill in missing firm counts or labor-spend estimates** from NAICS or industry reports
3. **Flag duplicates** — open an issue if you find two entries describing the same pain
4. **Submit a new entry** via the [issue template](./.github/ISSUE_TEMPLATE/new-pain.yml)

<br>

---

<div align="center">

### If idea-box helps you find your next build, a ⭐ means a lot.

**[⭐ Star the repo](https://github.com/mothivenkatesh/idea-box)** &nbsp;·&nbsp; **[🐙 Open an issue](https://github.com/mothivenkatesh/idea-box/issues/new)** &nbsp;·&nbsp; **[𝕏 Share](https://twitter.com/intent/tweet?text=idea-box%20%E2%80%94%201%2C000%20validated%20pain%20points%20worth%20building%20for.%20Every%20entry%20has%20a%20persona%2C%20market%20size%2C%20current%20pricing%2C%20and%20the%20gap%20incumbents%20miss.&url=https%3A%2F%2Fgithub.com%2Fmothivenkatesh%2Fidea-box)**

<br>

<sub>MIT-licensed. Built by <a href="https://github.com/mothivenkatesh">@mothivenkatesh</a> with the help of <a href="https://claude.com/claude-code">Claude Code</a>.</sub>

</div>
