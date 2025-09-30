# 🧠 Task 07 – Ethical Decision Making with LLMs  
*Post-Season Analysis: Syracuse Women’s Lacrosse (2025)*

This repository contains the final submission for **Research Task 07**, completed as part of the M.S. in Applied Data Science program at Syracuse University.

The objective of this task was to simulate a real-world stakeholder decision report using:
- LLM-generated content (via GPT-4)
- Real player and team performance data
- Ethical evaluation of AI outputs
- Clear, reproducible, and risk-tiered recommendations

---

## 🎯 Project Goal

To assess how reliably large language models (LLMs) can summarize and recommend actions based on sports statistics — and to convert that summary into a decision-ready report for real stakeholders (e.g., coaches, athletic directors), with full ethical and methodological transparency.

---

## 🗂️ Repository Structure

Task_07_Decision_Making/
├── Datasets/
│   ├── Game_Log_2025.csv
│   ├── Player_Stats_2025.csv
│   ├── Team_Stats_2025.csv
│   ├── Goalie_Stats_2025.csv
│   └── [Other period-level breakdowns]
├── Scripts/
│   ├── validation_player_stats.py
│   ├── validate_team_periods_and_goalies.py
│   └── [Optional updated versions]
├── llm_prompts/
│   ├── interview_script.md
│   ├── prompt_log.md
├── report/
│   ├── Task_07_Decision_Report.md
│   ├── claim_validation_log.md
└── README.md

---

## 🧪 Tools Used

- **Python 3.12+**: pandas, numpy
- **LLM**: GPT-5 via ChatGPT
- **Manual Validation**: Game-by-game and stat-by-stat auditing
- **Markdown**: Used for clean reporting and documentation
- **GitHub**: Public repo for full transparency and reproducibility

---

## 📋 Project Highlights

- ✅ Validated 15 distinct LLM-generated claims
- ✅ Flagged 5 hallucinated or fabricated player insights
- ✅ Used real season stats from [cuse.com](https://cuse.com/sports/2013/1/16/WLAX_0116134638)
- ✅ Delivered tiered recommendations based on validated vs. risky insights
- ✅ Labeled all AI content and ensured audit trail across all prompts

---

## 📄 Key Deliverables

| File | Purpose |
|------|---------|
| `Task_07_Decision_Report.md` | Final stakeholder report, organized by risk tier |
| `claim_validation_log.md` | Line-by-line verification of all LLM statements |
| `interview_script.md` | Original LLM-generated interview content |
| `validation_player_stats.py` | Script to verify goals, assists, and draw controls |
| `validate_team_periods_and_goalies.py` | Script for SOG %, save %, and team-level checks |

---

## 📬 Submission Details

- **Submitted To:** `jrstrome@syr.edu`
- **Author:** Kapil Tare  
- **Program:** M.S. Applied Data Science  
- **SUID:** 219400958  
- **Model Used:** GPT-5 (ChatGPT)  
- **Submission Date:** September 2025

---

## ✅ Learning Outcomes

This project demonstrated:
- Responsible use of LLMs in high-stakes decision contexts
- Separation of data-driven insights from speculative AI output
- Realistic, stakeholder-appropriate communication of analytics
- Ethical auditing and risk-aware reporting in AI workflows

---

## 🔗 License

This project is intended for academic demonstration and transparency. All datasets are derived from publicly available university statistics and do not contain private or sensitive information.
