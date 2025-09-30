import pandas as pd

# Load the CSV (adjust path if needed)
df = pd.read_csv("Datasets/Player_Stats_2025.csv")

# 1. Top Scorer
top_scorer = df.loc[df['g'].idxmax()]
print(f"Top Scorer: {top_scorer['player']} — {top_scorer['g']} goals")

# 2. Most Assists
top_assist = df.loc[df['a'].idxmax()]
print(f"Most Assists: {top_assist['player']} — {top_assist['a']} assists")

# 3. Best Goal Efficiency (Goals per Shot)
df['goal_efficiency'] = df['g'] / df['sh']
most_efficient = df[df['sh'] > 0].sort_values(by='goal_efficiency', ascending=False).iloc[0]
print(f"Highest Goal Efficiency: {most_efficient['player']} — {most_efficient['goal_efficiency']:.2f} G/Shot")

# 4. Most Well-Rounded (Goals + Assists - Turnovers)
df['contribution_score'] = df['g'] + df['a'] - df['to']
top_allround = df.sort_values(by='contribution_score', ascending=False).iloc[0]
print(f"Most All-Round Player: {top_allround['player']} — Score: {top_allround['contribution_score']}")