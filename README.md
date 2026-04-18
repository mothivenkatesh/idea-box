# Pain DB

A structured database of product / AI-agent pain points, modeled after [ideabrowser.com](https://www.ideabrowser.com/) and [painonsocial.com](https://painonsocial.com/), filtered through a16z's vertical-AI thesis and the Santifer repair-lifecycle architectural pattern.

Current seed: **1000 entries** across 24 files. **Roadmap complete.**

## Quick start

Open `web/index.html` in a browser — it loads all 8 JSON files and renders a searchable, filterable grid. No build step.

```
# serve locally (any static server works)
cd pain-db
python -m http.server 8000
# → open http://localhost:8000/web/
```

## Schema

Every entry conforms to `schema.json`. Key fields:

| Field | Type | Notes |
|---|---|---|
| `id` | string | `PAIN-NNNN` zero-padded |
| `title` | string | Short pain title |
| `vertical` | string | Industry label |
| `workflow_family` | enum | `intake`, `triage_routing`, `extraction_validation`, `outbound_followup`, `transactional_action`, `compliance_audit`, `synthesis_reporting`, `full_lifecycle` |
| `persona` | string | Target buyer/user |
| `pain_description` | string | What hurts, in plain language |
| `pain_severity` | 1-10 | 10 = losing money / compliance risk |
| `tedium_score` | 1-10 | 10 = pure data entry, prime AI replacement |
| `tam_firms` | int | Target firms in category |
| `tam_labor_spend_usd` | number | Annual labor spend in category |
| `tam_direction` | enum | `rapidly-growing`, `growing`, `stable-growing`, `stable`, `stable-declining`, `declining` |
| `current_wtp_usd_month` | number | What incumbents charge for nearest tool |
| `incumbent_tools` | array | Existing SaaS competing in this pain |
| `incumbent_gap` | string | Why incumbents fail |
| `santifer_pattern` | string | One-line solution architecture |
| `sources` | array | URLs validating the pain |
| `reference_build` | string | URL of existing build if any |
| `why_now` | string | What changed to make it buildable |
| `opportunity_score` | 0-100 | Composite |
| `tags` | array | Free-form tags |

Workflow family taxonomy is derived from looking across Sierra, Nurix, Lyzr, ERP-AI, a16z, and Santifer — every deployed vertical-AI use case maps to one of these seven.

## Directory layout

```
pain-db/
├── README.md                                        ← this file
├── schema.json                                      ← JSON Schema for entries
├── data/
│   ├── pains-01-repair-home-services.json          ← 25 entries
│   ├── pains-02-marketing-gtm-revops.json          ← 25 entries
│   ├── pains-03-bharat-india.json                  ← 25 entries
│   ├── pains-04-diligence-compliance-legal.json    ← 25 entries
│   ├── pains-05-healthcare-medical.json            ← 20 entries
│   ├── pains-06-finance-hr-ops-specialty.json      ← 30 entries
│   ├── pains-07-offbeat-niches.json                ← 25 entries
│   ├── pains-08-reconciliation-automation-pm.json  ← 25 entries
│   ├── pains-09-yc-wedges.json                     ← 50 entries
│   ├── pains-10-reddit-threads.json                ← 50 entries
│   ├── pains-11-international.json                 ← 50 entries
│   ├── pains-12-enterprise-it-gaming-climate.json  ← 50 entries
│   ├── pains-13-business-ops-deep.json             ← 50 entries
│   ├── pains-14-d2c-ecommerce-deep.json            ← 50 entries
│   ├── pains-15-finance-deep.json                  ← 50 entries
│   ├── pains-16-supply-chain-logistics.json        ← 50 entries
│   ├── pains-17-scientific-pharma-rnd.json         ← 50 entries
│   ├── pains-18-specialty-professional-services.json ← 50 entries
│   ├── pains-19-consumer-prosumer.json             ← 50 entries
│   ├── pains-20-ai-native-emerging.json            ← 50 entries
│   ├── pains-21-healthcare-adjacent.json           ← 50 entries
│   ├── pains-22-public-sector-govtech.json         ← 50 entries
│   ├── pains-23-niche-b2b-longtail.json            ← 50 entries
│   └── pains-24-final-curated.json                 ← 50 entries
├── web/
│   └── index.html                                   ← static browser UI
└── scripts/
    └── add-pain.py                                  ← append CSV rows as entries
```

## Sources informing the 200 seed entries

- [Santifer — Business OS for Airtable / repair lifecycle](https://santifer.io/business-os-for-airtable)
- [a16z — "AI Inside" opens new markets for VSaaS](https://a16z.com/vsaas-vertical-saas-ai-opens-new-markets/)
- [a16z — Vertical SaaS with AI Inside](https://a16z.com/vertical-saas-now-with-ai-inside/)
- [a16z — Rise of Vertical AI in Accounting](https://a16z.com/newsletter/the-rise-of-vertical-ai-in-accounting/)
- [a16z — Big Ideas 2026 Parts 1-3](https://a16z.com/newsletter/big-ideas-2026-part-1/)
- [Menlo Ventures — Software Finally Gets to Work](https://menlovc.com/perspective/software-finally-gets-to-work-the-opportunity-in-vertical-ai/)
- [Activant — Vertical Software Is Having A Moment](https://activantcapital.com/research/vertical-software-is-having-a-moment)
- [Lyzr case studies](https://www.lyzr.ai/case-studies/) + [101 use cases](https://www.lyzr.ai/template/101-ai-use-cases/)
- [Sierra — about + customer list](https://sierra.ai/about)
- [Nurix — use cases](https://www.nurix.ai/resources/ai-agents-use-cases-in-the-real-world)
- [PainOnSocial — 50+ Vertical SaaS Ideas](https://painonsocial.com/blog/vertical-saas-ideas)
- [BigIdeasDB — 50 validated micro SaaS ideas](https://bigideasdb.com/micro-saas-ideas-2026)
- [FleetPanda](https://www.fleetpanda.com/customer-showcase/), [Kula.ai](https://www.kula.ai/product/kula-flows), [Recko/Stripe](https://stripe.com/en-at/newsroom/news/recko)
- [ChatFin — ERP AI agents](https://chatfin.ai/blog/autonomous-finance-ai-agents-erp-integration-for-oracle-sap-netsuite-2026/)
- [ServiceTitan — HVAC / plumbing workflows](https://www.servicetitan.com/)
- [Sarvam AI](https://www.sarvam.ai/), [Rapido](https://en.wikipedia.org/wiki/Rapido_(company)), [Porter](https://inc42.com/startups/porter-intracity-last-mile-delivery-pan-india-logistics-quick-commerce/), [Zepto](https://yourstory.com/2026/04/inside-dark-stores-blinkit-zepto-how-10-minute-delivery-works), [NoBroker](https://www.nobroker.in/tenant-verification)

## Roadmap to 1000 entries

Current **400** → target **1000**. Plan:

### Phase 2 (partial, done): +200 entries (to 400 total)
- ✅ YC W25/S25/W26 agent-company wedges (50)
- ✅ Reddit r/Entrepreneur, r/smallbusiness, r/accounting, r/photography, r/realtors etc. (50)
- ✅ International: EU, UK, LATAM, APAC, MENA, Africa, Nordic, Israel (50)
- ✅ Enterprise IT + SOC/FinOps + Gaming + Climate + GovTech (50)

### Phase 2 remainder: +300 entries (to 700 total)
- **BigIdeasDB pull** — 238K complaints across Reddit/G2/Capterra/Upwork; sample 200 with 8+ validation. Ref: [bigideasdb.com](https://bigideasdb.com/micro-saas-ideas-2026)
- **PainOnSocial subreddit queries** — systematic pull from r/Entrepreneur, r/smallbusiness, r/accounting, r/construction, r/healthIT with severity scoring. Ref: [painonsocial.com](https://painonsocial.com/)
- **YC W25/S25/W26 company list** — each yc company = at minimum 1 pain statement (their wedge). ~100 agent companies

### Phase 3: +300 entries (to 800)
- **G2 / Capterra 2-star reviews** — pull top-10 competitors per vertical, scrape negative reviews, extract pain points
- **LinkedIn — "I wish" posts from operators** — broad pattern of founders/operators articulating gaps
- **Reddit threads from `r/automation`, `r/Airtable`, `r/nocode`** where people ask "how do I automate X?" — each is a pain

### Phase 4: +200 entries (to 1000)
- **Regulatory-driven**: CSRD, SEC 10-K AI disclosures, HIPAA, GDPR enforcement rulings — compliance is a pain-driver
- **International**: Bharat/SEA/LATAM/Africa specific gaps (UPI, PIX, mobile money, regional languages)
- **Emerging**: agentic-commerce, on-chain finance, autonomous industry, manufacturing-AI — from a16z Big Ideas 2026 Parts 1-3

## Scoring rubric (opportunity_score)

Composite calculation to rank entries:

```
opportunity_score = min(100, round(
  (severity * 4) +
  (tedium * 3) +
  (tam_direction_weight) +   # rapid=25, growing=15, stable-growing=10, stable=5, declining=-10
  (wtp_weight)               # >$1000=15, >$300=10, >$100=5, <$100=0
))
```

Not auto-calculated in seed entries (scored subjectively); to automate, see `scripts/add-pain.py`.

## Adding entries

### Manual
Add objects to any JSON file in `data/`, or create a new file `pains-NN-topic.json` and add its path to `FILES` in `web/index.html`.

### From CSV
```
python scripts/add-pain.py input.csv data/pains-09-new-batch.json
```
See `scripts/add-pain.py` for the CSV column spec.

## Gaps in current seed

- **Enterprise IT / DevOps / security** — covered lightly; add 20-30 more
- **Gaming / entertainment / media** — 1 entry; underserved
- **Non-US regulated verticals** — EU / APAC compliance rare
- **Public sector / govtech (non-India)** — 1 entry
- **Scientific / academic workflows** — 1 entry
- **Climate / sustainability / carbon** — 0 entries, growing TAM

## License

Data is curated from public sources. No warranty. Attribute sources if you republish entries.
