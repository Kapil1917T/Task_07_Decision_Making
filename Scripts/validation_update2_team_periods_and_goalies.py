import pandas as pd
import re

# Run from repo root:
#   python Scripts/validate_update2_team_periods_attendance.py

# ── Load ────────────────────────────────────────────────────────────────────────
goals_df = pd.read_csv("Datasets/Goals_by_Period_2025.csv")
saves_df = pd.read_csv("Datasets/Saves_by_Period_2025.csv")
game_log  = pd.read_csv("Datasets/Game_Log_2025.csv")

# # ── Prompt 8: First vs Second Half scoring ──────────────────────────────────────
first_half  = goals_df[goals_df["period"].isin(["1st","2nd"])].groupby("team")["value"].sum()
second_half = goals_df[goals_df["period"].isin(["3rd","4th"])].groupby("team")["value"].sum()
second_winner = second_half.idxmax()

print("🕒 Prompt 8 — First vs Second Half Scoring")
print(f"First Half:  {first_half.to_dict()}")
print(f"Second Half: {second_half.to_dict()}")
print(f"⚔️ Team that scored more in the 2nd half: {second_winner} — {second_half[second_winner]} goals")

# ── Prompt 9: OT saves ─────────────────────────────────────────────────────────
ot = saves_df[saves_df["period"] == "OT"].groupby("team")["value"].sum()
print("\n🧤 Prompt 9 — OT Saves")
print(f"Syracuse: {ot.get('Syracuse',0)}, Opponents: {ot.get('Opponents',0)}")

# ── Prompt 10: Attendance quick facts ──────────────────────────────────────────
games = len(game_log)
total_att = game_log["attendance"].sum()
avg_att = game_log["attendance"].mean()

# Optional: parse goal differential from 'score' like '21-9'
def goal_diff(score):
    try:
        m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s*$", str(score))
        if m:
            su, opp = int(m.group(1)), int(m.group(2))
            return su - opp
    except Exception:
        pass
    return 0

game_log["gd"] = game_log["score"].apply(goal_diff)
wins   = (game_log["result"].astype(str).str.upper().str.startswith("W")).sum()
losses = (game_log["result"].astype(str).str.upper().str.startswith("L")).sum()

print("\n👥 Prompt 10 — Season Attendance Quick Facts")
print(f"Total Games: {games}")
print(f"Total Attendance: {total_att}")
print(f"Average Attendance: {avg_att:.2f}")
print(f"Record: {wins}-{losses} | Total Goal Differential: {game_log['gd'].sum()}")