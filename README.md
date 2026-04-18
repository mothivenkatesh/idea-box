<div align="center">

# 💡 idea-box

### A structured database of **1,000 real-world pain points** worth building for — with TAM, WTP, incumbents, and AI-cofounder validation scores for the top 50.

<br>

[![Stars](https://img.shields.io/github/stars/mothivenkatesh/idea-box?style=for-the-badge&logo=github&color=FDE047)](https://github.com/mothivenkatesh/idea-box/stargazers)
[![Forks](https://img.shields.io/github/forks/mothivenkatesh/idea-box?style=for-the-badge&logo=github&color=C7D2FE)](https://github.com/mothivenkatesh/idea-box/network/members)
[![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)](./LICENSE)
[![Entries](https://img.shields.io/badge/entries-1%2C000-0289F7?style=for-the-badge)](./data)
[![S-tier validated](https://img.shields.io/badge/S--tier_validated-50-8247E5?style=for-the-badge)](./data/validations-s-tier.json)

<br>

**[🔎 Live demo](https://mothivenkatesh.github.io/idea-box/web/)** &nbsp;·&nbsp; **[📊 Browse all 1000 entries](./data)** &nbsp;·&nbsp; **[🧠 Schema](./schema.json)** &nbsp;·&nbsp; **[🤝 Contribute](./CONTRIBUTING.md)**

</div>

<br>

---

## The problem this repo solves

Every "startup ideas" list on the internet is vibes. A hundred bullet points. No persona, no TAM, no sources, no reason to believe.

**idea-box is different.** Every entry carries:

- **Who hurts** (persona, not "small businesses")
- **What hurts** (pain description with frequency)
- **How much** (severity 1–10, tedium 1–10)
- **How big** (TAM firms / labor spend / direction)
- **What they pay now** (WTP at incumbents)
- **Why incumbents miss** (gap analysis)
- **Why now** (what infra shift made it buildable)
- **Sources** — Reddit threads, forums, G2 reviews, vendor case studies

The top 50 by composite score are run through the [AI-cofounder rubric](https://github.com/mothivenkatesh/ai-cofounder) — TAM triangulation (bottom-up · value-based · top-down), unit economics, 8-layer scoring, riskiest assumptions.

> Modeled after [ideabrowser.com](https://www.ideabrowser.com/) + [painonsocial.com](https://painonsocial.com/), filtered through [a16z's vertical-AI thesis](https://a16z.com/vertical-saas-now-with-ai-inside/) and the [Santifer Business OS pattern](https://santifer.io/business-os-for-airtable).

<br>

## What's inside

<table>
<tr>
<td width="50%" valign="top">

### 📦 1,000 structured entries
Across **24 batch files** in [`/data`](./data), organized by theme:

| # | Theme | Entries |
|---|---|--:|
| 01 | Repair · home services | 25 |
| 02 | Marketing · GTM · RevOps | 25 |
| 03 | Bharat / India (UPI · Zepto · Porter) | 25 |
| 04 | Diligence · compliance · legal | 25 |
| 05 | Healthcare / medical | 20 |
| 06 | Finance · HR · ops · specialty | 30 |
| 07 | Offbeat niches (FleetPanda · Kula) | 25 |
| 08 | Reconciliation · automation | 25 |
| 09 | YC wedges (W25/S25/W26) | 50 |
| 10 | Reddit r/smallbusiness · r/Entrepreneur | 50 |
| 11 | International (EU · APAC · MENA · LATAM) | 50 |
| 12 | Enterprise IT · gaming · climate | 50 |
| 13 | Business ops deep | 50 |
| 14 | D2C + e-commerce deep | 50 |
| 15 | Finance deep | 50 |
| 16 | Supply chain + logistics | 50 |
| 17 | Scientific + pharma R&D | 50 |
| 18 | Specialty professional services | 50 |
| 19 | Consumer + prosumer | 50 |
| 20 | AI-native emerging | 50 |
| 21 | Healthcare adjacent (payer · pharmacy) | 50 |
| 22 | Public sector / govtech | 50 |
| 23 | Niche B2B long-tail | 50 |
| 24 | Final curated | 50 |

</td>
<td width="50%" valign="top">

### 🔬 50 S-tier validations
Top opportunities scored on the **AI-cofounder rubric**:

```
{
  "verdict": "Conditional pass",
  "tam_triangulation": {
    "bottom_up":   { "value_usd": 5000000000 },
    "value_based": { "value_usd": 6750000000 },
    "top_down":    { "value_usd": 10000000000 },
    "convergence": "Strong — within 2×",
    "sam_usd_mid": 7250000000,
    "som_usd_1pct": 72500000
  },
  "unit_economics": {
    "acv_usd": 60000,
    "derived_ltv_usd": 187500,
    "target_cac_usd": 37500,
    "target_ltv_cac": 5.0,
    "implied_payback_mo": 10.0
  },
  "layer_scores": { ... },
  "riskiest_assumptions": [ ... ]
}
```

### 🖥 Static browser UI
[`/web/index.html`](./web) — zero-build, single-file app:
- Sidebar filters with radio + inline dropdowns
- Card grid, 10-per-page pagination
- Keyboard navigation, Lucide icons
- Frappe Espresso design tokens, Newsreader serif hero

### ⚙ Tooling
- `scripts/add-pain.py` — CSV → JSON importer with auto opportunity-scoring
- `scripts/validate-s-tier.py` — batch AI-cofounder rubric runner

</td>
</tr>
</table>

<br>

## Quick start

### 🌐 Browse the data (recommended)

**Live:** [mothivenkatesh.github.io/idea-box/web/](https://mothivenkatesh.github.io/idea-box/web/)

**Or locally:**
```bash
git clone https://github.com/mothivenkatesh/idea-box.git
cd idea-box
python -m http.server 8000
# open http://localhost:8000/web/
```

### 🔍 Query the data (jq)

```bash
# Top 10 opportunities in Bharat
jq '[.[] | select(.vertical | test("Bharat"))] | sort_by(-.opportunity_score) | .[0:10]' \
   data/pains-03-bharat-india.json

# All S-tier Conditional-pass entries
jq '.[] | select(.ai_cofounder_validation.verdict == "Conditional pass") | .title' \
   data/validations-s-tier.json

# Count entries by workflow family across the whole corpus
jq -s 'add | group_by(.workflow_family) | map({family: .[0].workflow_family, n: length})' \
   data/pains-*.json
```

### 🐍 Query with Python

```python
import json, glob
pains = []
for f in sorted(glob.glob("data/pains-*.json")):
    pains.extend(json.load(open(f, encoding="utf-8")))

# Top 20 SMB opportunities with WTP over $200/mo
top = sorted(
    [p for p in pains if p.get("current_wtp_usd_month", 0) >= 200 and "smb" in p.get("tags", [])],
    key=lambda p: -p.get("opportunity_score", 0)
)[:20]
```

<br>

## Entry schema (the 20 fields)

Every entry in `data/pains-*.json` conforms to [`schema.json`](./schema.json):

| Field | Type | Notes |
|---|---|---|
| `id` | string | `PAIN-NNNN` zero-padded |
| `title` | string | Short pain-point title |
| `vertical` | string | Industry label |
| `workflow_family` | enum | 1 of 7: `intake`, `triage_routing`, `extraction_validation`, `outbound_followup`, `transactional_action`, `compliance_audit`, `synthesis_reporting` (+ `full_lifecycle`) |
| `persona` | string | Target buyer — specific role, not a category |
| `pain_description` | string | What hurts, in plain language |
| `pain_severity` | 1–10 | 10 = losing money / regulatory risk |
| `tedium_score` | 1–10 | 10 = pure data entry, prime AI replacement |
| `frequency` | string | Human-readable frequency |
| `tam_firms` | integer | Target firms in category |
| `tam_labor_spend_usd` | number | Annual labor-spend TAM |
| `tam_direction` | enum | `rapidly-growing` · `growing` · `stable-growing` · `stable` · `declining` |
| `current_wtp_usd_month` | number | What incumbents charge today |
| `incumbent_tools` | array | Existing SaaS competing |
| `incumbent_gap` | string | Why today's tools fail |
| `santifer_pattern` | string | One-line solution architecture |
| `sources` | array | Validation URLs |
| `reference_build` | string | Existing build URL (optional) |
| `why_now` | string | What infra/regulation made it solvable |
| `opportunity_score` | 0–100 | Composite signal |

<br>

## Who this is for

- **Founders & operators** — sourcing validated ideas, not LinkedIn listicle bait
- **VCs & angel investors** — a triage layer before you read 200 decks
- **Product leaders** — discovering adjacent opportunities worth a new SKU
- **Vertical-AI builders** — mapping labor budgets to agent workflows
- **Researchers** — who studies "how unsolved ops problems map to buyable software" at scale

<br>

## Methodology

Entries were synthesized from:

- [Santifer — Business OS for Airtable](https://santifer.io/business-os-for-airtable) (the architectural pattern applied in 200+ entries)
- [a16z vertical-AI + vertical-SaaS essays](https://a16z.com/vertical-saas-now-with-ai-inside/)
- [Menlo Ventures — Software Finally Gets to Work](https://menlovc.com/perspective/software-finally-gets-to-work-the-opportunity-in-vertical-ai/)
- [Lyzr case studies](https://www.lyzr.ai/case-studies/) (101 enterprise use cases)
- [Sierra.ai customer roster](https://sierra.ai/about) (CX agent deployments)
- [Nurix AI deployments](https://www.nurix.ai/) (Bharat vernacular agents)
- [ideabrowser.com](https://www.ideabrowser.com/) + [painonsocial.com](https://painonsocial.com/) formats
- [BigIdeasDB](https://bigideasdb.com/) 238K-complaint corpus analysis
- Reddit threads (`r/smallbusiness`, `r/Entrepreneur`, `r/accounting`, `r/nocode`, `r/Airtable`, and ~15 more)
- G2 / Capterra 2-star review patterns
- NAICS labor-spend data for TAM triangulation

<br>

## Roadmap

- [x] **v1.0** — 1,000 entries across 24 batches, top 50 S-tier validated, static browser UI
- [ ] **v1.1** — richer evidence chains (direct quote extraction from Reddit threads)
- [ ] **v1.2** — community PRs open, issue templates, GitHub Discussions
- [ ] **v1.3** — expand S-tier validations to top 100
- [ ] **v2.0** — BigIdeasDB pattern: automated nightly Reddit pull → new entry candidates

<br>

## Contributing

PRs welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md). High-leverage contributions:

1. **Add evidence links** to existing entries (Reddit / forum threads you've seen)
2. **Fill in `tam_firms` / `tam_labor_spend_usd`** for entries where they're null
3. **Run `/strategy` or `/ai-cofounder`** validations and submit the output
4. **Flag dupes** — if you find two entries describing the same pain, open an issue

<br>

## Prior art & thanks

This repo stands on the shoulders of:

- [Santiago Fernández de Valderrama (@santifer)](https://santifer.io/) — the Airtable + n8n + WhatsApp pattern at the heart of 200+ entries
- [ideabrowser.com](https://www.ideabrowser.com/) by Greg Isenberg — the "Idea of the Day" format
- [painonsocial.com](https://painonsocial.com/) — Reddit-mined pain-point scoring
- [BigIdeasDB](https://bigideasdb.com/) — the 238K-complaint validation approach
- Frappe's [Espresso design system](https://github.com/frappe/frappe-ui) — used to style the browser UI

<br>

---

<div align="center">

### If idea-box helps you find your next build, a ⭐ means a lot.

**[⭐ Star the repo](https://github.com/mothivenkatesh/idea-box)** &nbsp;·&nbsp; **[🐙 Open an issue](https://github.com/mothivenkatesh/idea-box/issues/new)** &nbsp;·&nbsp; **[𝕏 Share](https://twitter.com/intent/tweet?text=idea-box%20%E2%80%94%201%2C000%20structured%20pain%20points%20worth%20building%20for.&url=https%3A%2F%2Fgithub.com%2Fmothivenkatesh%2Fidea-box)**

<br>

<sub>MIT-licensed. Built by <a href="https://github.com/mothivenkatesh">@mothivenkatesh</a> with the help of <a href="https://claude.com/claude-code">Claude Code</a>.</sub>

</div>
