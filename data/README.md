# Data: Statcast Pitch-by-Pitch (2026 Season)

## Source
Pitch-by-pitch data collected from MLB Statcast for three National League pitchers during the 2026 regular season (Opening Day through early July).

## Files

| File | Pitcher | Pitches | Games | Date Range |
|---|---|---|---|---|
| `shohei_ohtani.csv` | Shohei Ohtani (LAD) | 1,335 | 14 | Mar 31 - Jul 3 |
| `cristopher_sanchez.csv` | Cristopher Sanchez (PHI) | 1,800 | 19 | Mar 26 - Jul 6 |
| `jacob_misiorowski.csv` | Jacob Misiorowski (MIL) | 1,662 | 18 | Mar 26 - Jul 7 |

## Key Columns (119 total)

| Column | Description |
|---|---|
| `pitch_type` | Pitch code (FF=4-seam, SI=sinker, SL=slider, CH=changeup, CU=curveball, FC=cutter, FS=splitter, ST=sweeper) |
| `game_date` | Date of game |
| `release_speed` | Pitch velocity at release (mph) |
| `release_spin_rate` | Spin rate (rpm) |
| `pfx_x` | Horizontal movement from pitcher's perspective (inches) |
| `pfx_z` | Vertical movement relative to gravity (inches) |
| `release_extension` | Extension toward home plate at release (feet) |
| `zone` | Strike zone position (1-9 = in zone, 11-14 = out of zone) |
| `events` | Plate appearance outcome (strikeout, walk, single, etc.) |
| `description` | Pitch-level result (swinging_strike, called_strike, hit_into_play, foul, ball) |
| `stand` | Batter side (L/R) |
| `bb_type` | Batted ball type (ground_ball, fly_ball, line_drive, popup) |
| `launch_speed` | Exit velocity (mph) |
| `launch_angle` | Launch angle (degrees) |
| `hit_distance_sc` | Projected hit distance (feet) |
| `estimated_woba_using_speedangle` | Expected wOBA based on launch speed/angle |
| `estimated_ba_using_speedangle` | Expected batting average based on launch speed/angle |
| `estimated_slg_using_speedangle` | Expected slugging based on launch speed/angle |
| `delta_pitcher_run_exp` | Change in run expectancy attributed to pitcher (positive = bad) |
| `delta_home_win_exp` | Change in home win expectancy |
| `n_thruorder_pitcher` | Times through the batting order |

## Data Quality Notes
- `estimated_woba_using_speedangle` is only populated for balls in play (~25-30% of pitches)
- `launch_speed` and `launch_angle` only exist on batted ball events
- Misiorowski's data has 2 null rows for most movement/spin columns (likely recording errors)
- No substantial missing data in core pitch metrics (velocity, spin, zone, description)
