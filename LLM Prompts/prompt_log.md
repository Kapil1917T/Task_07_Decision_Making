# 🧠 Prompt Log: Task 05 – Descriptive Stats with LLMs

This log captures natural language prompts used to query 2025 Syracuse Women's Lacrosse stats via ChatGPT, along with the responses and validation results.

---

## 📘 Dataset Summary

- **Source**: [cuse.com](https://cuse.com/sports/2013/1/16/WLAX_0116134638)
- **Season**: 2025
- **Tables Used**: Player stats, team stats, period stats, goalie stats
- **Structured As**: CSVs (not uploaded to GitHub)
- **LLMs Used**: ChatGPT (GPT-4)

---
## Task 05: Update 1

## ✅ Prompt 1: Simple Fact Retrieval

**Prompt**:
> Who scored the most goals on the team?

**LLM Response**:
> Emma Muchnick with 34 goals.

**Validation**:
✔️ Correct — matches `player_stats.csv`.

---

## ✅ Prompt 2: Assists Leader

**Prompt**:
> Which player had the most assists this season?

**LLM Response**:
> Emma Ward with 46 assists.

**Validation**:
✔️ Correct — confirmed using pandas on `player_stats.csv`.

---

## 🔄 Prompt 3: Interpretive Question

**Prompt**:
> Who was the most all-round player based on goals, assists, and fewest turnovers?

**LLM Response**:
> Emma Ward seems well-rounded with 30 goals, 46 assists, and 41 turnovers.

**Comment**:
⚠️ Fair interpretation, but LLM didn’t apply weighting. Follow-up prompt required metric clarification.

---

## Task 05: Update 02

## ➕ Prompt 4: Top 3 Goal Scorers
**Prompt**:
> Using the table below, list the top 3 goal scorers, with player name and goals. Return as “#1 … (# goals)”.

**LLM Response**:
> 1. Emma Muchnick – 34 goals  
> 2. Caroline Trinkaus – 32 goals  
> 3. Emma Ward – 30 goals

**Validation**:
Python sorted `g` column in descending order and returned top 3 players

---

## ➕ Prompt 5: Top 3 in Assists
**Prompt**:
> From the table, who are the top 3 players by assists? Show “Name – assists”.

**LLM Response**:
> 1. Emma Ward – 46 assists  
> 2. Caroline Trinkaus – 11 assists  
> 3. Gracie Britton – 10 assists

**Validation**:
Python sorted `a` column in descending order and returned top 3 players

---

## ➕ Prompt 6: Best Goal-to-Shot Efficiency (min 10 shots)
**Prompt**:
> Using the table, compute goals per shot (G/SH) and list the top 3 players with at least 10 shots. Show “Name – G/SH (rounded to 2 decimals)”.

**LLM Response**:
> 1. Sam DeVito – 0.67  
> 2. Olivia Adamson – 0.56  
> 3. Gracie Britton – 0.49

**Validation**:
Python calculated `g/sh` for players with `sh >= 10` and sorted descending

---

## ➕ Prompt 7: All-round Contribution Score
**Prompt**:
> Define Contribution Score = (goals + assists − turnovers). Using the table, report the top 3 players by this score. Return “Name – score”.

**LLM Response**:
> 1. Emma Ward – 35  
> 2. Caroline Trinkaus – 27  
> 3. Gracie Britton – 14

**Validation**:
Python computed `g + a - to` and sorted descending

---

## ➕ Prompt 8: First vs Second Half Scoring
**Prompt**:
> Using the goals-by-period data, total 1st half = 1st+2nd and 2nd half = 3rd+4th for Syracuse and Opponents.  
> 1) Who scored more in the second half?  
> 2) Was Syracuse stronger in the first or second half?

**LLM Response**:
> First Half – Syracuse: 139, Opponents: 116  
> Second Half – Syracuse: 95, Opponents: 104  
> Syracuse scored more in the first half; Opponents scored more in the second half.

**Validation**:
Python summed period values for each team and compared:  

---

## ➕ Prompt 9: Overtime Shot-Stopping
**Prompt**:
> Using the saves-by-period data, how many OT saves did Syracuse and Opponents make? Who had more?

**LLM Response**:
> Syracuse: 1 OT save  
> Opponents: 2 OT saves  
> Opponents had more OT saves.

**Validation**:
Python filtered for `period == OT` and summed values for each team:  

---

## ➕ Prompt 10: Season Attendance Quick Facts
**Prompt**:
> From the game log, report: total games played, total attendance, and average attendance per game.

**LLM Response**:
> Total Games: 19  
> Total Attendance: 26,666  
> Average Attendance: ~1,403.47 per game

**Validation**:
Python counted rows, summed attendance, and computed average attendance:  

---

## 📌 Notes

- Prompt formatting and data structure heavily impact accuracy.
- Defining metrics inside the prompt improves LLM judgment questions.