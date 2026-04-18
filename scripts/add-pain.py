#!/usr/bin/env python3
"""
Append pain-point entries to a JSON data file from a CSV.

Usage:
    python scripts/add-pain.py input.csv data/pains-NN-name.json

CSV columns (minimum):
    title, vertical, workflow_family, persona, pain_description,
    pain_severity, tedium_score, tam_direction, current_wtp_usd_month, santifer_pattern

Optional columns:
    frequency, tam_firms, tam_labor_spend_usd, incumbent_tools, incumbent_gap,
    evidence_count, sources, reference_build, why_now, tags

Multi-value fields (incumbent_tools, sources, tags) are pipe-separated:
    "RepairShopr|RepairDesk|Orderry"

Opportunity score is auto-calculated if not provided.
"""

import csv
import json
import sys
from pathlib import Path

WORKFLOW_FAMILIES = {
    "intake", "triage_routing", "extraction_validation", "outbound_followup",
    "transactional_action", "compliance_audit", "synthesis_reporting", "full_lifecycle"
}

TAM_DIR_WEIGHT = {
    "rapidly-growing": 25, "growing": 15, "stable-growing": 10,
    "stable": 5, "stable-declining": -5, "declining": -10
}


def opportunity_score(row):
    sev = int(row.get("pain_severity", 0) or 0)
    ted = int(row.get("tedium_score", 0) or 0)
    tam = TAM_DIR_WEIGHT.get(row.get("tam_direction", "stable"), 5)
    wtp = float(row.get("current_wtp_usd_month", 0) or 0)
    wtp_w = 15 if wtp > 1000 else 10 if wtp > 300 else 5 if wtp > 100 else 0
    return min(100, round(sev * 4 + ted * 3 + tam + wtp_w))


def next_id(existing):
    if not existing:
        return "PAIN-0001"
    nums = [int(p["id"].split("-")[1]) for p in existing if p.get("id", "").startswith("PAIN-")]
    return f"PAIN-{max(nums) + 1:04d}"


def split_multi(s):
    if not s:
        return []
    return [x.strip() for x in s.split("|") if x.strip()]


def to_entry(row, next_id_fn):
    wf = row.get("workflow_family", "").strip()
    if wf and wf not in WORKFLOW_FAMILIES:
        sys.stderr.write(f"WARN: unknown workflow_family '{wf}' for {row.get('title')}\n")

    entry = {
        "id": row.get("id") or next_id_fn(),
        "title": row["title"],
        "vertical": row["vertical"],
        "workflow_family": wf,
        "persona": row["persona"],
        "pain_description": row["pain_description"],
        "pain_severity": int(row.get("pain_severity", 0)),
        "tedium_score": int(row.get("tedium_score", 0)),
        "tam_direction": row.get("tam_direction", "stable"),
        "current_wtp_usd_month": float(row.get("current_wtp_usd_month", 0) or 0),
        "santifer_pattern": row.get("santifer_pattern", ""),
    }

    # Optional
    for f in ["frequency", "incumbent_gap", "reference_build", "why_now"]:
        v = row.get(f)
        if v:
            entry[f] = v

    for f in ["tam_firms", "evidence_count"]:
        v = row.get(f)
        if v:
            try:
                entry[f] = int(v)
            except ValueError:
                pass

    if row.get("tam_labor_spend_usd"):
        try:
            entry["tam_labor_spend_usd"] = float(row["tam_labor_spend_usd"])
        except ValueError:
            pass

    for f in ["incumbent_tools", "sources", "tags"]:
        vals = split_multi(row.get(f, ""))
        if vals:
            entry[f] = vals

    if "opportunity_score" in row and row["opportunity_score"]:
        entry["opportunity_score"] = int(row["opportunity_score"])
    else:
        entry["opportunity_score"] = opportunity_score(row)

    return entry


def main():
    if len(sys.argv) != 3:
        sys.stderr.write(__doc__)
        sys.exit(1)
    csv_path = Path(sys.argv[1])
    json_path = Path(sys.argv[2])

    existing = []
    if json_path.exists():
        existing = json.loads(json_path.read_text(encoding="utf-8"))

    # Aggregate across all files in the same data dir for global uniqueness
    all_existing = list(existing)
    for other in json_path.parent.glob("pains-*.json"):
        if other == json_path:
            continue
        all_existing.extend(json.loads(other.read_text(encoding="utf-8")))

    new_entries = []

    def nid():
        n = next_id(all_existing + new_entries)
        return n

    with csv_path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("title"):
                continue
            new_entries.append(to_entry(row, nid))

    combined = existing + new_entries
    json_path.write_text(json.dumps(combined, indent=2), encoding="utf-8")
    print(f"Appended {len(new_entries)} entries to {json_path}. Total in file: {len(combined)}.")


if __name__ == "__main__":
    main()
