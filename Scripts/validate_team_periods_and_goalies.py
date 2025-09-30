import pandas as pd

# --- Load data ---
goals_df = pd.read_csv("Datasets/Goals_by_Period_2025.csv")
saves_df = pd.read_csv("Datasets/Saves_by_Period_2025.csv")
goalie_df = pd.read_csv("Datasets/Goalie_Stats_2025.csv")

# --- 1. Which team scored more in 2nd half (3rd + 4th periods)? ---
goals_2nd_half = goals_df[goals_df['period'].isin(['3rd', '4th'])].groupby('team')['value'].sum()
winner = goals_2nd_half.idxmax()
print(f"⚔️ Team that scored more in 2nd half: {winner} — {goals_2nd_half[winner]} goals")

# --- 2. Syracuse's overall save % from all goalies ---
syracuse_goalies = goalie_df[~goalie_df['player'].isin(['Team'])]
syracuse_saves = syracuse_goalies['save'].sum()
syracuse_goals_against = syracuse_goalies['ga'].sum()
syracuse_save_pct = syracuse_saves / (syracuse_saves + syracuse_goals_against)
print(f"🧤 Syracuse Team Save % (All Goalies Combined): {syracuse_save_pct:.3f}")


# opp_save_pct = goalie_df[goalie_df['player'] == 'Opponents']['pct'].astype(float).values[0]

# better_team = 'Syracuse' if syracuse_save_pct > opp_save_pct else 'Opponents'
# print(f"🧤 Better Save %: {better_team} — {max(syracuse_save_pct, opp_save_pct):.3f}")

# --- 3. Total Saves in OT ---
ot_saves = saves_df[saves_df['period'] == 'OT'].groupby('team')['value'].sum()
print(f"🕒 Saves in OT — Syracuse: {ot_saves.get('Syracuse', 0)}, Opponents: {ot_saves.get('Opponents', 0)}")