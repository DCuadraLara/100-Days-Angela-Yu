# 🐍 100 Days of Code — Python Journey

> “My journey through code: daily exercises, challenges, and projects.”

![Build Status](https://img.shields.io/github/actions/workflow/status/DCuadraLara/100-Days-Angela-Yu/weekly-review.yml?label=Review%20Status&logo=github)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Progress](https://img.shields.io/badge/Days-100-lightgrey)

---

A curated collection of **mini-projects and daily exercises** from my Python learning path — mainly following the **100 Days of Code (Angela Yu, Udemy)** challenge.  
Each script helped me **practice core programming concepts**, experiment with tools, and **build real coding habits** one day at a time.

---

## 🚀 Highlights

- 🧩 **Structured exercises** organized by day under `exercises/day_xx/`
- ⚙️ **Automated Code Reviewer** — a custom Python bot that:
  - Runs `ruff`, `black`, `isort`, `mypy`, `bandit`, `radon`, and `pydocstyle`
  - Generates Markdown reports and weekly PDF summaries
  - Provides style feedback, docstring checks, and improvement tips
- 📊 **Weekly report generator** powered by GitHub Actions
- 🧠 **Progress tracking** and self-review of code quality and complexity

---

## 📂 Repository Structure

📦 100-Days-Angela-Yu/
├── exercises/ # Daily Python exercises
│ ├── day_01/
│ ├── day_02/
│ └── ...
├── reports/ # Markdown reviews per exercise
├── pdf_report_weekly/ # Weekly compiled PDF summaries
├── tools/ # Reviewer scripts and rules
├── requirements.txt # Dependencies (linting, analysis, PDF)
├── pyproject.toml # Formatting and linting config
└── .github/workflows/ # GitHub Actions automation

---

## 🧾 Example Output

Each exercise automatically produces a review file like:

reports/day_04_report.md

That includes:
- Style issues and formatting suggestions  
- Code complexity metrics (Radon)  
- Docstring and typing feedback  
- Recommended refactors and next steps  

A weekly PDF summary is generated at:

pdf_report_weekly/week-YYYY-MM-DD.pdf


---

## 🧰 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python 3.11** | Main language |
| **Black** | Code formatting |
| **Ruff** | Style & lint checks |
| **Isort** | Import sorting |
| **MyPy** | Static typing |
| **Bandit** | Security analysis |
| **Radon** | Code complexity metrics |
| **pydocstyle** | Docstring validation |
| **ReportLab** | PDF generation |
| **GitHub Actions** | Automation pipeline |

---

## 💬 Author

**David Cuadra Lara**  
Currently documenting my Python journey while building tools that make learning more efficient and fun.  
Always open to collaboration, feedback, or nerdy discussions 👨‍💻✨  

📫 **Find me on GitHub:** [@DCuadraLara](https://github.com/DCuadraLara)

---

> _“Consistency beats motivation — one commit at a time.”_

