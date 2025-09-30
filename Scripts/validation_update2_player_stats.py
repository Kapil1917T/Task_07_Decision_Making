import pandas as pd

# Run from repo root:
#   python Scripts/validate_update2_player_metrics.py

# ── Load ────────────────────────────────────────────────────────────────────────
df = pd.read_csv("Datasets/Player_Stats_2025.csv")
df.head()

# Ensure numeric types
num_cols = ["gp","g","a","pts","sh","gw","gb","dc","to","ct","fouls"]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")

# ── Prompt 4: Top 3 goal scorers ────────────────────────────────────────────────
top3_goals = df.sort_values("g", ascending=False)[["player","g"]].head(3).reset_index(drop=True)
print("🏹 Prompt 4 — Top 3 Goal Scorers")
for i, r in top3_goals.iterrows():
    print(f"{i+1}. {r['player']} — {int(r['g'])} goals")

# ── Prompt 6: Best goal-to-shot efficiency (min 10 shots) ──────────────────────
df["g_per_sh"] = df["g"] / df["sh"]
eff = df[df["sh"] >= 10].sort_values("g_per_sh", ascending=False)[["player","g_per_sh"]].head(3).reset_index(drop=True)
print("\n⚡ Prompt 6 — Best Goal-to-Shot Efficiency (min 10 shots)")
for i, r in eff.iterrows():
    print(f"{i+1}. {r['player']} — {r['g_per_sh']:.2f}")

# ── Prompt 7: All‑round Contribution (g + a − to) ──────────────────────────────
df["contrib_score"] = df["g"] + df["a"] - df["to"]
contrib = df.sort_values("contrib_score", ascending=False)[["player","contrib_score"]].head(3).reset_index(drop=True)
print("\n🧠 Prompt 7 — All‑Round Contribution (g + a − to)")
for i, r in contrib.iterrows():
    print(f"{i+1}. {r['player']} — {int(r['contrib_score'])}")