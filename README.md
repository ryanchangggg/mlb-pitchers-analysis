# MLB Pitchers Analysis (2026)

A data-driven comparative analysis of three National League aces — **Shohei Ohtani**, **Cristopher Sanchez**, and **Jacob Misiorowski** — challenging the narrative that Ohtani has been the best pitcher among them in the 2026 season.

**Core finding:** The data does not support Ohtani > Sanchez or Misiorowski. Sanchez is the most efficient run preventer; Misiorowski is the most dominant in raw stuff.

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557C?logo=matplotlib)](https://matplotlib.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## Key Results at a Glance

| Metric | Ohtani | Sanchez | Misiorowski | Best |
|---|---|---|---|---|
| Walk Rate (BB%) | **7.6%** | **4.8%** | **6.4%** | Sanchez |
| Strikeout Rate (K%) | 27.9% | 27.6% | **39.6%** | Misiorowski |
| K-BB% | 20.3% | 22.8% | **33.2%** | Misiorowski |
| Whiff% | 28.4% | 29.7% | **34.3%** | Misiorowski |
| AVG Allowed | .162 | .234 | **.135** | Misiorowski |
| OPS Allowed | .474 | .629 | **.410** | Misiorowski |
| Run Exp. per Pitch | **+0.0158** | **+0.0080** | **+0.0222** | Sanchez |
| Hard Hit% | **33.8%** | 44.3% | 34.2% | Ohtani |
| Barrels Allowed | **0** | 8 | 3 | Ohtani |
| Ground Balls | 111 | **192** | 101 | Sanchez |
| Total Pitches | 1,335 | **1,800** | 1,662 | Sanchez |

> **Sanchez** gives up less than **half** the run value per pitch as Ohtani (+0.0080 vs +0.0158).
> **Misiorowski** has a **39.6% K%** — elite in any era.
> Ohtani leads in **contact suppression** (0 barrels, 33.8% HardHit%) but trails in control and run prevention.

---

## Repository Structure

```
├── notebooks/                      # Jupyter notebooks (narrative + analysis)
│   ├── 00_data_exploration.ipynb   # Data overview and understanding
│   ├── 01_pitch_arsenal_analysis.ipynb  # Velocity, movement, whiff rates
│   ├── 02_performance_metrics.ipynb     # K/BB, xwOBA, run expectancy, significance tests
│   ├── 03_platoon_and_situational.ipynb  # Platoon splits, TTO analysis
│   └── 04_summary_dashboard.ipynb       # Radar chart + final verdict
├── data/                           # Raw Statcast CSV files
│   ├── shohei_ohtani.csv
│   ├── cristopher_sanchez.csv
│   ├── jacob_misiorowski.csv
│   └── README.md                   # Column glossary
├── script/                         # Report/slide generation scripts
│   ├── generate_report.py          # .docx generation
│   └── generate_presentation.py    # .pptx generation
├── report/                         # Generated output (.docx, .pptx) — gitignored
├── figures/                        # Generated visualizations — gitignored
├── analysis_utils.py               # Shared module (all metric calculations)
├── ANALYSIS.md                     # Full written report
├── Makefile                        # Pipeline automation
└── requirements.txt
```

---

## Skills Demonstrated

| Skill | Where |
|---|---|
| **Data Wrangling (pandas)** | Cleaning Statcast data, handling ~70% null in batted ball columns, field selection |
| **Statistical Analysis** | Chi-square significance tests for BB%, K%, GB% differences |
| **Visualization (matplotlib/seaborn)** | Radar charts, pie charts, box plots, scatter plots, bar charts |
| **Run Expectancy Modeling** | Leveraging `delta_pitcher_run_exp` Statcast field for run value comparison |
| **Expected Stats (xwOBA/xBA/xSLG)** | Interpreting Statcast's speed-angle models for contact quality |
| **Platoon Analysis** | Splitting by batter handedness, identifying LHB/RHB disparities |
| **Report Generation** | Automated .docx and .pptx generation from Python |
| **Notebook Storytelling** | Narrative-driven notebooks with context before each analysis block |
| **Version Control** | Clean `.gitignore`, structured repo, `Makefile` for reproducibility |

---

## How to Reproduce

### Prerequisites
Python 3.11+ recommended.

### 1. Setup
```bash
pip install -r requirements.txt
```

### 2. Run Full Pipeline
```bash
make all
```

Or step by step:
```bash
# Run notebooks (generates figures)
cd notebooks
jupyter nbconvert --to notebook --execute 00_data_exploration.ipynb --output 00_data_exploration.ipynb
jupyter nbconvert --to notebook --execute 01_pitch_arsenal_analysis.ipynb --output 01_pitch_arsenal_analysis.ipynb
jupyter nbconvert --to notebook --execute 02_performance_metrics.ipynb --output 02_performance_metrics.ipynb
jupyter nbconvert --to notebook --execute 03_platoon_and_situational.ipynb --output 03_platoon_and_situational.ipynb
jupyter nbconvert --to notebook --execute 04_summary_dashboard.ipynb --output 04_summary_dashboard.ipynb

# Generate report and slides
python script/generate_report.py
python script/generate_presentation.py
```

### 3. Explore Interactively
```bash
jupyter notebook notebooks/
```

---

## Data Provenance

All data comes from **MLB Statcast** via Baseball Savant, covering the 2026 regular season from Opening Day through early July. Each CSV contains 119 Statcast tracking columns including velocity, spin rate, movement, launch metrics, and run expectancy deltas. See [data/README.md](data/README.md) for the full column glossary.

---

## Key Analysis Techniques

- **Run Expectancy (RE24):** Uses Statcast's `delta_pitcher_run_exp` field — the gold standard for measuring per-pitch value contribution
- **Expected Stats (xwOBA/xBA/xSLG):** Statcast's speed-angle model estimates contact quality independent of defensive alignment and luck
- **Chi-Square Tests:** Applied to BB%, K%, and GB% differences between pitchers to assess statistical significance
- **Platoon Splits:** Separates LHB/RHB performance to identify handedness vulnerabilities
- **Time Through Order:** Tracks performance degradation as the lineup cycles

---

## License

For research and educational purposes.
