# MLB Pitchers Analysis (2026 Season)

A data-driven comparative analysis of three National League aces: **Shohei Ohtani**, **Cristopher Sanchez**, and **Jacob Misiorowski** — the top three pitchers in the NL in 2026 by fan and media recognition.

## Project Overview

This project challenges the popular narrative that Shohei Ohtani has been the best pitcher among the NL's elite in 2026. Using Statcast pitch-by-pitch data, it demonstrates that both Cristopher Sanchez and Jacob Misiorowski have outperformed Ohtani in several critical pitching metrics.

## Repository Structure

```
.
├── data/                          # Raw Statcast CSV files
│   ├── shohei_ohtani.csv
│   ├── cristopher_sanchez.csv
│   └── jacob_misiorowski.csv
├── figures/                       # Generated visualizations (gitignored)
├── script/
│   ├── generate_report.py         # Script to generate .docx report
│   └── generate_presentation.py   # Script to generate .pptx slides
├── report/                        # Generated report files (gitignored)
├── 00_data_exploration.ipynb      # Data overview and summary statistics
├── 01_pitch_arsenal_analysis.ipynb # Pitch type, velocity, movement analysis
├── 02_performance_metrics.ipynb    # K/BB, xwOBA, run expectancy analysis
├── 03_platoon_and_situational.ipynb # Platoon splits and situational analysis
├── ANALYSIS.md                    # Full written report of findings
├── requirements.txt
└── .gitignore
```

## Key Findings

1. **Walk Rate Disparity**: Ohtani walks batters at 7.6% — nearly 60% higher than Sanchez (4.8%)
2. **Run Expectancy**: Sanchez gives up half the run value per pitch (+0.0080) compared to Ohtani (+0.0158)
3. **Whiff Rates**: Ohtani ranks last in overall whiff rate (28.4%) behind Sanchez (29.7%) and Misiorowski (34.3%)
4. **Variance vs Control**: Misiorowski dominates in K% (39.6%) and velocity (100.5 mph); Sanchez dominates in control (4.8% BB%) and ground balls (192)
5. **Workload**: Ohtani's 1,335 pitches in 14 games trail Sanchez's 1,800 in 19 games by 35%

## How to Reproduce

1. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

2. Run the Jupyter notebooks (in order):
  ```bash
  jupyter notebook 00_data_exploration.ipynb
  jupyter notebook 01_pitch_arsenal_analysis.ipynb
  jupyter notebook 02_performance_metrics.ipynb
  jupyter notebook 03_platoon_and_situational.ipynb
  ```

3. Generate the report and slides:
  ```bash
  python script/generate_report.py
  python script/generate_presentation.py
  ```

## Data Source

All data is sourced from MLB Statcast (2026 season, Opening Day through early July).

## License

For research and educational purposes.
