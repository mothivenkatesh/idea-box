#!/usr/bin/env python3
"""
Apply the ai-cofounder ideavalidator skill to the top-50 S-tier pain entries.

Rubric + templates sourced from:
https://github.com/mothivenkatesh/ai-cofounder/blob/main/skill/SKILL.md

This is a *mechanical* pass — it assigns 1-5 scores per layer using heuristics
over the existing pain-db fields, then computes TAM triangulation + unit econ
stubs per model-type benchmark. For high-stakes decisions run the full
adaptive ai-cofounder flow on each idea separately.

Usage:
    python scripts/validate-s-tier.py
Writes: data/validations-s-tier.json
"""

import json
import glob
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

# Unit economics benchmarks from skill/SKILL.md
MODEL_BENCHMARKS = {
    "B2B SaaS":    {"gross_margin": 0.75, "target_ltv_cac": 5,  "payback_target_mo": 10, "monthly_churn": 0.02},
    "B2B Vertical":{"gross_margin": 0.70, "target_ltv_cac": 4,  "payback_target_mo": 12, "monthly_churn": 0.015},
    "Marketplace": {"gross_margin": 0.65, "target_ltv_cac": 3,  "payback_target_mo": 14, "monthly_churn": 0.03},
    "D2C":         {"gross_margin": 0.50, "target_ltv_cac": 3,  "payback_target_mo": 5,  "monthly_churn": 0.05},
    "Fintech":     {"gross_margin": 0.60, "target_ltv_cac": 4,  "payback_target_mo": 12, "monthly_churn": 0.01},
    "Services":    {"gross_margin": 0.40, "target_ltv_cac": 3,  "payback_target_mo": 9,  "monthly_churn": 0.03},
    "SMB SaaS":    {"gross_margin": 0.70, "target_ltv_cac": 3,  "payback_target_mo": 8,  "monthly_churn": 0.04},
}


def classify_model(pain):
    """Infer business-model archetype from fields."""
    tags = set(pain.get("tags", []))
    v = pain.get("vertical", "").lower()
    wtp = pain.get("current_wtp_usd_month", 0)
    if "fintech" in v or "bfsi" in v or "banking" in v or "payments" in v or "insurance" in v or "lending" in v:
        return "Fintech"
    if "d2c" in tags or "ecommerce" in tags or "e-commerce" in v or "retail" in v:
        return "D2C"
    if "marketplace" in v or "marketplace" in tags:
        return "Marketplace"
    if wtp >= 1000:
        return "B2B SaaS"
    if wtp < 100 and ("smb" in tags or "reddit" in tags or "consumer" in tags):
        return "SMB SaaS"
    if "enterprise" in tags or wtp >= 500:
        return "B2B SaaS"
    return "B2B Vertical"


def tam_triangulation(pain):
    """Three-method TAM triangulation."""
    firms = pain.get("tam_firms")
    labor = pain.get("tam_labor_spend_usd")
    wtp_mo = pain.get("current_wtp_usd_month", 0) or 0
    arpu_annual = wtp_mo * 12 if wtp_mo else 0

    # Bottom-up: firms × ARPU
    bottom_up = None
    if firms and arpu_annual:
        bottom_up = {
            "calc": f"{firms:,} firms × ${arpu_annual:,}/yr ARPU",
            "value_usd": int(firms * arpu_annual)
        }

    # Value-based: labor spend × 15% capture (if known), else ARPU × inferred buyer count
    value_based = None
    if labor:
        value_based = {
            "calc": f"${labor/1e9:.1f}B annual labor × 15% AI capture",
            "value_usd": int(labor * 0.15)
        }
    elif firms and arpu_annual:
        value_based = {
            "calc": f"{firms:,} firms × ${arpu_annual*3:,} (3× WTP = value signal)",
            "value_usd": int(firms * arpu_annual * 3)
        }

    # Top-down (industry category proxy — stubbed)
    top_down = None
    if firms and arpu_annual:
        top_down = {
            "calc": f"{firms:,} firms × ${arpu_annual*2:,} (incumbent category spend)",
            "value_usd": int(firms * arpu_annual * 2)
        }

    # Convergence test
    values = [x["value_usd"] for x in [bottom_up, value_based, top_down] if x]
    convergence = None
    sam_usd = None
    if len(values) >= 2:
        ratio = max(values) / max(1, min(values))
        if ratio <= 2:
            convergence = f"Strong — methods within {ratio:.1f}×"
            sam_usd = int(sum(values) / len(values))
        else:
            convergence = f"Divergent — methods differ {ratio:.1f}×; conservative SAM"
            sam_usd = min(values)

    # SOM = 1% SAM assumption
    som_usd = int(sam_usd * 0.01) if sam_usd else None

    return {
        "bottom_up": bottom_up,
        "value_based": value_based,
        "top_down": top_down,
        "convergence": convergence,
        "sam_usd_mid": sam_usd,
        "som_usd_1pct": som_usd
    }


def unit_economics(pain, model_type):
    """Stub unit economics using WTP as price + model benchmarks."""
    wtp_mo = pain.get("current_wtp_usd_month", 0) or 0
    acv = wtp_mo * 12
    b = MODEL_BENCHMARKS.get(model_type, MODEL_BENCHMARKS["B2B SaaS"])
    gm = b["gross_margin"]
    churn = b["monthly_churn"]
    life_mo = 1 / churn if churn else 60
    ltv = acv / 12 * gm * life_mo
    # Target CAC = LTV / target_ltv_cac
    cac = ltv / b["target_ltv_cac"] if ltv else 0
    monthly_gp = (acv / 12) * gm
    payback_mo = cac / monthly_gp if monthly_gp else 999

    return {
        "model_type": model_type,
        "acv_usd": int(acv),
        "assumed_gross_margin_pct": int(gm * 100),
        "assumed_monthly_churn_pct": round(churn * 100, 1),
        "derived_ltv_usd": int(ltv),
        "target_cac_usd": int(cac),
        "target_ltv_cac": round(ltv / cac, 1) if cac else None,
        "implied_payback_mo": round(payback_mo, 1),
        "green_flag": payback_mo < 12 and (ltv / cac if cac else 0) >= 3
    }


def score_layers(pain, tam, ue):
    """Score 8 layers 1-5 using heuristics over pain fields."""
    sev = pain.get("pain_severity", 0)
    ted = pain.get("tedium_score", 0)
    evc = pain.get("evidence_count", 0)
    sources = len(pain.get("sources", []))
    tam_dir = pain.get("tam_direction", "stable")
    wtp = pain.get("current_wtp_usd_month", 0) or 0
    incumb_gap_len = len(pain.get("incumbent_gap", ""))
    why_now_len = len(pain.get("why_now", ""))

    # Problem clarity
    if sev >= 9 and ted >= 9 and (evc >= 10 or sources >= 2):
        problem = 5
    elif sev >= 8 and ted >= 8:
        problem = 4
    elif sev >= 7:
        problem = 3
    elif sev >= 5:
        problem = 2
    else:
        problem = 1

    # Market size
    firms = pain.get("tam_firms", 0) or 0
    labor = pain.get("tam_labor_spend_usd", 0) or 0
    if tam_dir == "rapidly-growing" and (firms > 100000 or labor > 10e9) and wtp >= 500:
        market = 5
    elif tam_dir in ("rapidly-growing", "growing") and (firms > 50000 or labor > 5e9):
        market = 4
    elif tam_dir in ("growing", "stable-growing"):
        market = 3
    elif tam_dir == "stable":
        market = 2
    else:
        market = 1

    # Solution differentiation
    if incumb_gap_len > 50 and why_now_len > 30:
        solution = 4
    elif incumb_gap_len > 30:
        solution = 3
    elif incumb_gap_len > 0:
        solution = 3
    else:
        solution = 2

    # Unit economics
    if ue["green_flag"] and ue["target_ltv_cac"] and ue["target_ltv_cac"] >= 5:
        unit_econ = 5
    elif ue["green_flag"]:
        unit_econ = 4
    elif ue["implied_payback_mo"] < 18:
        unit_econ = 3
    elif ue["implied_payback_mo"] < 24:
        unit_econ = 2
    else:
        unit_econ = 1

    # P&L viability (leveraged from unit econ + model type)
    if ue["assumed_gross_margin_pct"] >= 70:
        pnl = 4 if unit_econ >= 4 else 3
    elif ue["assumed_gross_margin_pct"] >= 50:
        pnl = 3
    else:
        pnl = 2

    # Market timing + moat
    if tam_dir == "rapidly-growing" and why_now_len > 20:
        timing = 5
    elif tam_dir in ("rapidly-growing", "growing"):
        timing = 4
    elif tam_dir == "stable-growing":
        timing = 3
    elif tam_dir == "stable":
        timing = 2
    else:
        timing = 1

    # Execution + kill risk clarity (heuristic: shorter gap = clearer wedge)
    if incumb_gap_len > 40 and why_now_len > 20:
        exec_risk = 4
    elif incumb_gap_len > 20:
        exec_risk = 3
    else:
        exec_risk = 2

    return {
        "problem_clarity": problem,
        "market_size": market,
        "solution_differentiation": solution,
        "unit_economics": unit_econ,
        "pnl_viability": pnl,
        "market_timing_moat": timing,
        "founder_fit": "N/A (no founder profile)",
        "execution_kill_risk": exec_risk,
        "traction_pmf": "N/A (pre-product)"
    }


def verdict_for(score_total, max_total):
    """Normalize to 40-pt scale and apply thresholds."""
    if max_total == 0:
        return ("No score", "Missing data")
    normalized = round(score_total * 40 / max_total)
    if normalized >= 34:
        return ("Strong signal", f"Ready to build. Normalized {normalized}/40.")
    if normalized >= 28:
        return ("Conditional pass", f"2-3 gaps block commitment. Normalized {normalized}/40.")
    if normalized >= 22:
        return ("Fragile", f"Core assumptions unvalidated. Normalized {normalized}/40.")
    if normalized >= 16:
        return ("Weak", f"Multiple foundational gaps. Normalized {normalized}/40.")
    return ("No signal", f"Do not build yet. Normalized {normalized}/40.")


def riskiest_assumptions(pain, ue):
    """Generate the top 3 riskiest assumptions using pain fields + unit econ."""
    risks = []
    incumbents = pain.get("incumbent_tools", [])
    if incumbents:
        risks.append(f"Incumbent response: {incumbents[0] if incumbents else 'existing vendors'} and {len(incumbents)-1} others can copy if the wedge is clear")
    if pain.get("tam_direction") not in ("rapidly-growing", "growing"):
        risks.append(f"Market growth: TAM marked '{pain.get('tam_direction')}' — expansion may require category-creation")
    if ue["implied_payback_mo"] > 12:
        risks.append(f"CAC payback {ue['implied_payback_mo']} mo exceeds SaaS benchmark; pricing or channel economics need validation")
    if pain.get("evidence_count", 0) < 5 and len(pain.get("sources", [])) < 2:
        risks.append("Evidence depth: <5 validation sources — run customer interviews before committing")
    if "regulated" in pain.get("tags", []) or "compliance" in pain.get("vertical", "").lower():
        risks.append("Regulatory risk: compliance-heavy vertical, liability if AI hallucinates; human-in-loop required")
    if not risks:
        risks.append("Differentiation depth: santifer_pattern may be replicable by incumbents within 2 quarters")
    return risks[:3]


def validate_pain(pain):
    model = classify_model(pain)
    tam = tam_triangulation(pain)
    ue = unit_economics(pain, model)
    layers = score_layers(pain, tam, ue)
    scored_values = [v for v in layers.values() if isinstance(v, int)]
    total = sum(scored_values)
    max_total = len(scored_values) * 5
    has_ones = any(v == 1 for v in scored_values)
    if has_ones:
        cap_note = "Conviction override: a layer scored 1 caps verdict at Weak"
    else:
        cap_note = None
    verdict, rationale = verdict_for(total, max_total)
    if has_ones and verdict in ("Strong signal", "Conditional pass"):
        verdict, rationale = ("Weak", f"{cap_note}. Raw normalized {round(total * 40 / max_total)}/40.")

    return {
        "run_date": str(date.today()),
        "idea_type": model,
        "stage": "idea" if not pain.get("reference_build") else "pattern_validated",
        "tam_triangulation": tam,
        "unit_economics": ue,
        "layer_scores": layers,
        "raw_total": total,
        "max_possible": max_total,
        "verdict": verdict,
        "verdict_rationale": rationale,
        "conviction_override": cap_note,
        "riskiest_assumptions": riskiest_assumptions(pain, ue)
    }


def main():
    all_pains = []
    for f in sorted(DATA.glob("pains-*.json")):
        all_pains.extend(json.loads(f.read_text(encoding="utf-8")))
    all_pains.sort(key=lambda p: p.get("opportunity_score", 0), reverse=True)
    s_tier = all_pains[:50]
    validated = []
    for p in s_tier:
        v = validate_pain(p)
        validated.append({
            "id": p["id"],
            "title": p["title"],
            "vertical": p["vertical"],
            "opportunity_score": p["opportunity_score"],
            "ai_cofounder_validation": v
        })
    out = DATA / "validations-s-tier.json"
    out.write_text(json.dumps(validated, indent=2), encoding="utf-8")
    print(f"Wrote {len(validated)} S-tier validations to {out}")
    # Summary
    verdicts = {}
    for v in validated:
        verdicts[v["ai_cofounder_validation"]["verdict"]] = verdicts.get(v["ai_cofounder_validation"]["verdict"], 0) + 1
    print("\nVerdict distribution:")
    for k, v in sorted(verdicts.items(), key=lambda kv: -kv[1]):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
