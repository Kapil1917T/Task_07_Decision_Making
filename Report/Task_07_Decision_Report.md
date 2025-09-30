# 🧠 Post-Season Decision Report: Syracuse Women’s Lacrosse (2025)

**Purpose:**  
This report presents data-driven and ethically audited recommendations for the Syracuse Women’s Lacrosse coaching staff and athletic leadership. The analysis is based on structured season statistics and an LLM-generated narrative interview, with a focus on transparency, risk classification, and reproducibility.

---

## 🔹 Executive Summary

We analyzed the 2025 season performance of the Syracuse Women’s Lacrosse team by combining structured performance metrics with insights from a ChatGPT-generated interview. Each claim from the narrative was cross-validated using real data. Based on this process, we developed tiered recommendations categorized by risk level.

### ✅ Key Recommendations
- Reinforce draw control training — major strength area (Low Risk)
- Prioritize defensive restructuring for transition periods (Low Risk)
- Explore goalie coaching and shot quality review (Medium Risk)
- Disregard fabricated LLM content (High Risk)

### ⚖️ Confidence & Transparency
- Most operational insights were statistically validated from official team data.
- All LLM-generated claims are documented and individually audited.
- Fabricated content was flagged, with risk annotations included in recommendations.

---

## 🎯 Background & Stakeholder Context

This report is designed for:
- **Primary Stakeholders**: Coaching staff and the Athletic Director
- **Decision Context**: Post-season review, tactical planning, and team development
- **Risk Level**: Mixed — operational actions are low-risk, but decisions based on unverifiable LLM content may carry reputational and personnel-related risk.

---

## 📊 Data Provenance & Scope

- **Source**: Official 2025 season data from [cuse.com](https://cuse.com/sports/2013/1/16/WLAX_0116134638)
- **Formats Used**: CSVs manually extracted from PDF stat tables
- **Key Data Tables**:
  - Player stats (goals, assists, draw control, TO, etc.)
  - Team stats (shot %, SOG %, goals per game)
  - Goalie save % and GAA
  - Game log with scores, dates, and outcomes
- **Limitations**: No positional metadata or per-minute play data. No access to video footage or coaching notes.
- **Privacy Note**: No personal or health information included. All players referenced are public athletes.

---

## 🧪 Data & Methods

We used official 2025 Syracuse Women’s Lacrosse season statistics, structured into CSVs (player, team, goalie, and game logs). These datasets were validated and explored using custom Python scripts to verify key performance indicators like goals per game, shot percentage, and draw control rates.

An interview-style narrative was generated using GPT-4, simulating a post-season conversation with the team’s coach. Each claim made by the LLM was traced back to the original data, confirmed, refuted, or flagged where necessary.

### Tools & Workflow:
- **Programming**: Python (Pandas, NumPy)
- **LLM**: GPT-4-turbo (ChatGPT), with saved prompts and outputs
- **Validation Scripts**: `validation_player_stats.py`, `validate_team_periods_and_goalies.py`
- **Claim Verification**: Manual and programmatic matching of LLM output to actual game data

All LLM prompts, transcripts, and audit logs are clearly labeled and available in the repository under `llm_prompts/` and `prompt_log.md`. The full audit trail is documented in the Appendix for reproducibility.

---

## 🔍 Findings

### 📈 Offensive Summary
- **Goals per Game**: 12.37 (LLM claimed "over 13")  
- **Shot Percentage**: 43.7% (LLM rounded to "46%")  
- **SOG Percentage**: 74.7% — top-tier metric  
→ LLM slightly exaggerated offensive output, but underlying performance was strong.

### 🥍 Draw Control Strength
- Meghan Rode led the team with 75 DCs (4.41 per game)
- Supported by Caramelli (39) and Vogelman (31)
→ Validates LLM praise for midfield dominance.

### 🛡️ Defensive Weakness
- UNC and BC games had 16+ GA
- March opened with multiple narrow losses
→ LLM-identified transition defense weakness is supported by GA trends.

### 🧤 Goalie Save Performance
- Daniella Guyette: 43.3% save rate, 11.37 GAA
- No granular breakdown to confirm “late-season dip” at 41% (LLM claim)
→ Overall numbers align directionally with narrative.

### ❌ LLM Fabrications
- "Jordan Thomas", "Maya Patel", and "Sydney Reyes" do not appear in player data
- LLM invented an April win streak and Duke game
→ These were identified and marked as high-risk misinformation.

> 📌 See [claim_validation_log.md](../report/claim_validation_log.md) for full claim-by-claim audit.

---

## 📦 Tiered Recommendations

### ✅ Operational (Low Risk)
- Continue emphasizing **draw control strategies** — performance is team-wide
- Run **transition defense drills** and restructure zone formations
- Reinforce mental performance training during March, a recurring pressure month

### 🟡 Investigatory (Medium Risk)
- Evaluate **goalie coaching interventions or rotation trials**
- Review **shot selection quality** with game film or positional breakdowns
- Pilot short-term **sports psychology workshops** before full team implementation

### 🔴 High-Stakes (High Risk)
- Do not act on fabricated player performances (e.g., Jordan Thomas, Maya Patel)
- Avoid citing hallucinated stats (e.g., April win streak, “over 13 GPG”) in external reports
- Clearly label all LLM-derived insights in internal documentation to prevent future misuse

---

## 🧭 Ethical & Legal Considerations

### ✅ LLM Transparency
- All GPT-4 outputs are labeled and archived
- Interview script was generated from structured prompts and reviewed by the analyst

### ⚠️ Risk Flagging
- All fabricated claims are annotated in the appendix
- Acting on false player narratives may lead to HR issues or coaching missteps

### 📚 Fairness & Bias Checks
- LLM overemphasized offense and invented star players
- Defensive contributions were less visible in narrative
→ Recommending balanced prompt engineering or co-review in future projects

---

## 🚀 Next Steps

- Share this report with athletic stakeholders and coaching staff
- Begin low-risk training interventions (DC, transition defense)
- Monitor outcomes of investigatory trials
- If LLM tools are adopted long-term, consider adding human-in-the-loop review workflows

---

## 📁 Appendix

### A. Claim Validation Log
→ [`claim_validation_log.md`](../report/claim_validation_log.md)

### B. LLM Transcript & Prompts
→ [`interview_script.md`](../llm_prompts/interview_script.md)  
→ [`prompt_log.md`](../llm_prompts/prompt_log.md)

### C. Code & Data
→ [`validation_player_stats.py`](../scripts/validation_player_stats.py)  
→ [`validate_team_periods_and_goalies.py`](../scripts/validate_team_periods_and_goalies.py)  
→ All raw data CSVs are located in the `data/` folder

---

**Author:** Kapil Tare  
**Program:** M.S. Applied Data Science, Syracuse University  
**Model Used:** GPT-5 (ChatGPT)  
**Submitted to:** `jrstrome@syr.edu`  
**Submission Date:** Sept 2025  