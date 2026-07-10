"""
Shared utilities for MLB Pitchers Analysis.

Provides data loading, metric calculation, and visualization helpers
used across all analysis notebooks.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# ---- Configuration ----

DATA_DIR = Path("data")
FIGURES_DIR = Path("figures")

PITCHERS = {
    "Ohtani": "shohei_ohtani.csv",
    "Sanchez": "cristopher_sanchez.csv",
    "Misiorowski": "jacob_misiorowski.csv"
}

COLORS = {
    "Ohtani": "#1f77b4",
    "Sanchez": "#ff7f0e",
    "Misiorowski": "#2ca02c"
}

MARKERS = {
    "Ohtani": "o",
    "Sanchez": "s",
    "Misiorowski": "D"
}

FIGURES_DIR.mkdir(exist_ok=True)


# ---- Styling ----

def set_style():
    """Apply consistent style across all visualizations."""
    plt.rcParams.update({
        'figure.figsize': (12, 6),
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'axes.titleweight': 'bold',
        'axes.facecolor': '#f8f9fa',
        'axes.edgecolor': '#dee2e6',
        'axes.grid': True,
        'grid.alpha': 0.3,
        'grid.color': '#adb5bd',
    })
    sns.set_style("whitegrid")


# ---- Data Loading ----

def load_pitcher(name):
    """Load a single pitcher's CSV and clean the player_name column."""
    fname = PITCHERS[name]
    df = pd.read_csv(DATA_DIR / fname).copy()
    df['player_name_clean'] = (
        df['player_name']
        .str.replace('\n', ', ', regex=False)
        .str.strip('"')
    )
    return df


def load_all():
    """Load all three pitchers into a dict keyed by short name."""
    return {name: load_pitcher(name) for name in PITCHERS}


# ---- Metric Calculations ----

def plate_discipline(df):
    """Return a dict of plate discipline metrics for a pitcher's DataFrame."""
    total = len(df)
    swings = df[df['description'].str.contains(
        'swinging_strike|hit_into_play|foul', na=False, regex=True)]
    whiffs = df[df['description'].str.contains(
        'swinging_strike', na=False)]
    called_strikes = df[df['description'] == 'called_strike']
    in_play = df[df['description'] == 'hit_into_play']
    ooz = df[df['zone'] > 9]
    ooz_swings = ooz[ooz['description'].str.contains(
        'swinging_strike|hit_into_play|foul', na=False, regex=True)]

    return {
        'total_pitches': total,
        'swing_pct': len(swings) / total * 100,
        'whiff_pct': len(whiffs) / len(swings) * 100 if len(swings) > 0 else 0,
        'contact_pct': (len(swings) - len(whiffs)) / len(swings) * 100 if len(swings) > 0 else 0,
        'called_strike_pct': len(called_strikes) / total * 100,
        'chase_pct': len(ooz_swings) / len(ooz) * 100 if len(ooz) > 0 else 0,
        'zone_pct': (df['zone'].dropna() <= 9).sum() / df['zone'].notna().sum() * 100,
        'strike_pct': len(df[df['type'] == 'S']) / total * 100,
        'ball_pct': len(df[df['type'] == 'B']) / total * 100,
        'in_play_pct': len(df[df['type'] == 'X']) / total * 100,
    }


def k_bb_stats(df):
    """Return K/BB stats from plate appearances (events column)."""
    pa = df[df['events'].notna() & (df['events'] != '')]
    total_pa = len(pa)
    if total_pa == 0:
        return {}

    strikeouts = len(pa[pa['events'] == 'strikeout'])
    walks = len(pa[pa['events'] == 'walk'])
    hbp = len(pa[pa['events'] == 'hit_by_pitch'])
    singles = len(pa[pa['events'] == 'single'])
    doubles = len(pa[pa['events'] == 'double'])
    triples = len(pa[pa['events'] == 'triple'])
    homers = len(pa[pa['events'] == 'home_run'])
    hits = singles + doubles + triples + homers
    tb = singles + 2 * doubles + 3 * triples + 4 * homers

    return {
        'pa': total_pa,
        'k': strikeouts,
        'k_pct': strikeouts / total_pa * 100,
        'bb': walks,
        'bb_pct': walks / total_pa * 100,
        'k_bb_pct': (strikeouts - walks) / total_pa * 100,
        'avg': hits / total_pa,
        'obp': (hits + walks + hbp) / total_pa,
        'slg': tb / total_pa,
        'ops': (hits + walks + hbp) / total_pa + tb / total_pa,
        'hr': homers,
    }


def batted_balls(df):
    """Return batted ball metrics for BIP events."""
    bip = df[df['description'] == 'hit_into_play']
    if len(bip) == 0:
        return {}
    ls = bip['launch_speed'].dropna()
    la = bip['launch_angle'].dropna()
    hh = (ls >= 95).sum() if len(ls) > 0 else 0
    barrels = (
        (ls >= 98) & (la >= 26) & (la <= 30)
    ).sum() if len(ls) > 0 and len(la) > 0 else 0
    bbt = bip['bb_type'].value_counts()

    return {
        'bip': len(bip),
        'avg_ev': ls.mean() if len(ls) > 0 else None,
        'avg_la': la.mean() if len(la) > 0 else None,
        'hard_hit_pct': hh / len(ls) * 100 if len(ls) > 0 else 0,
        'barrels': barrels,
        'gb': bbt.get('ground_ball', 0),
        'fb': bbt.get('fly_ball', 0),
        'ld': bbt.get('line_drive', 0),
        'pu': bbt.get('popup', 0),
    }


def run_expectancy(df):
    """Return run expectancy delta stats."""
    rexp = df['delta_pitcher_run_exp'].dropna()
    return {
        'total_re': rexp.sum(),
        'avg_re': rexp.mean(),
        'n_pitches_re': len(rexp),
        'pos_events': (rexp > 0).sum(),
        'neg_events': (rexp < 0).sum(),
    }


def expected_stats(df):
    """Return expected stat averages from speed/angle models."""
    return {
        'xba': df['estimated_ba_using_speedangle'].dropna().mean(),
        'xwoba': df['estimated_woba_using_speedangle'].dropna().mean(),
        'xslg': df['estimated_slg_using_speedangle'].dropna().mean(),
        'n_contacts': df['estimated_woba_using_speedangle'].dropna().shape[0],
    }


def platoon_splits(df):
    """Return dict of platoon results for LHB and RHB."""
    result = {}
    for stand in ['L', 'R']:
        sub = df[df['stand'] == stand]
        if len(sub) < 10:
            continue
        pa = sub[sub['events'].notna() & (sub['events'] != '')]
        total_pa = len(pa)
        if total_pa == 0:
            continue
        k = len(pa[pa['events'] == 'strikeout'])
        bb = len(pa[pa['events'] == 'walk'])
        s = len(pa[pa['events'] == 'single'])
        d = len(pa[pa['events'] == 'double'])
        t = len(pa[pa['events'] == 'triple'])
        hr = len(pa[pa['events'] == 'home_run'])
        hits = s + d + t + hr
        avg = hits / total_pa
        obp = (hits + bb) / total_pa
        slg = (s + 2*d + 3*t + 4*hr) / total_pa
        result[stand] = {
            'pa': total_pa, 'k_pct': k/total_pa*100, 'bb_pct': bb/total_pa*100,
            'avg': avg, 'obp': obp, 'slg': slg, 'ops': obp+slg, 'hr': hr,
        }
    return result


# ---- Statistical Tests ----

def chi2_independence(observed, expected):
    """Chi-square test for independence using scipy."""
    if observed == 0 or expected == 0:
        return None, 1.0
    table = np.array([[observed, expected],
                      [observed + expected, observed + expected]])
    return stats.chisquare([observed, expected])


# ---- Comparison Summary ----

def build_summary_df(dfs):
    """Build a comprehensive comparison DataFrame across all pitchers."""
    rows = []
    for name, df in dfs.items():
        pd_metrics = plate_discipline(df)
        kb = k_bb_stats(df)
        bb = batted_balls(df)
        re = run_expectancy(df)
        es = expected_stats(df)
        ps = platoon_splits(df)

        row = {
            'Pitcher': name,
            'Pitches': pd_metrics['total_pitches'],
            'Strike%': f"{pd_metrics['strike_pct']:.1f}%",
            'Zone%': f"{pd_metrics['zone_pct']:.1f}%",
            'Swing%': f"{pd_metrics['swing_pct']:.1f}%",
            'Whiff%': f"{pd_metrics['whiff_pct']:.1f}%",
            'Chase%': f"{pd_metrics['chase_pct']:.1f}%",
            'K%': f"{kb.get('k_pct', 0):.1f}%",
            'BB%': f"{kb.get('bb_pct', 0):.1f}%",
            'K-BB%': f"{kb.get('k_bb_pct', 0):.1f}%",
            'AVG': f"{kb.get('avg', 0):.3f}",
            'OBP': f"{kb.get('obp', 0):.3f}",
            'SLG': f"{kb.get('slg', 0):.3f}",
            'OPS': f"{kb.get('ops', 0):.3f}",
            'xBA': f"{es.get('xba', 0):.3f}",
            'xwOBA': f"{es.get('xwoba', 0):.3f}",
            'xSLG': f"{es.get('xslg', 0):.3f}",
            'BIP': bb.get('bip', 0),
            'Avg EV': f"{bb.get('avg_ev', 0):.1f}",
            'HardHit%': f"{bb.get('hard_hit_pct', 0):.1f}%",
            'Barrels': bb.get('barrels', 0),
            'GB': bb.get('gb', 0),
            'HR Allowed': kb.get('hr', 0),
            'Total RE Delta': f"{re.get('total_re', 0):+.3f}",
            'RE per Pitch': f"{re.get('avg_re', 0):+.4f}",
        }
        rows.append(row)
    return pd.DataFrame(rows)
