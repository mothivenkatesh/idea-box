# Contributing to idea-box

Thanks for considering a contribution! The value of this database grows with every well-sourced pain point.

## Ways to contribute

### 1. Add a new pain point

**Easiest path:** open an issue using the *New pain* template with the fields below, and a maintainer will add it.

**Direct PR path:**

1. Pick (or create) the right batch file in [`data/`](./data) that matches the vertical. Each batch holds ~25–50 related entries.
2. Append a new entry following [`schema.json`](./schema.json). Use the next free `PAIN-NNNN` ID — check the current max with:
   ```bash
   grep -hE '"id": "PAIN-[0-9]+"' data/*.json | sort | tail -5
   ```
3. Minimum fields required:
   - `id`, `title`, `vertical`, `workflow_family`, `persona`
   - `pain_description`, `pain_severity` (1–10), `tedium_score` (1–10)
   - `tam_direction`, `current_wtp_usd_month`, `santifer_pattern`
4. Strongly encouraged:
   - `incumbent_tools` (list), `incumbent_gap` (what today's tools miss)
   - `sources` (URLs — Reddit/forum threads validating the pain)
   - `tam_firms` and/or `tam_labor_spend_usd` where known
   - `why_now` (what changed that makes this solvable now)

### 2. Enrich existing entries

- Add evidence links to `sources[]`
- Tighten `pain_description` with specific hours/dollars/percentages lost
- Fill in missing `tam_firms` / `tam_labor_spend_usd` with NAICS or industry-report citations
- Add `reference_build` if you know of a live implementation

### 3. Run the validator

To add an S-tier AI-cofounder validation to an existing entry:

```bash
python scripts/validate-s-tier.py
```

The top-50 by `opportunity_score` get scored; see `data/validations-s-tier.json` for the output format.

### 4. Improve the browser

- `web/index.html` is a single-file static app (no build step, no framework)
- Design follows the Frappe Espresso system (Inter for body, Newsreader for hero, tokens in CSS variables at the top)
- Lucide icons via CDN

## What NOT to submit

- Entries without a real persona or at least one source URL
- Solution-heavy specs — this repo stays on **problems**, not answers
- Duplicates — check existing entries in the same vertical first

## Code of conduct

Be kind, be rigorous, cite your sources.
