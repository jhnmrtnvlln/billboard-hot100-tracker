# Billboard Hot 100 Chart Tracker

A self-built, Excel-based data pipeline that tracks Billboard Hot 100 chart performance week over week, calculates custom yearly rankings, and produces a publication-ready weekly chart for social media. Maintained continuously since **December 2024**.

## Overview

This project started as a personal effort to follow weekly Billboard chart movement in more depth than the official charts show, and grew into a structured, two-layer data system:

1. **`HOT_100_BREAKDOWN.xlsx`** — the raw data layer. Tracks every charting song's weekly points, cumulative total, peak position, and weeks-on-chart, going back through 2025 and into 2026 (36+ weeks tracked in the current year alone).
2. **`HOT_100_PUBMAT.xlsx`** — the publication layer. Pulls ranked data from the breakdown file using **XLOOKUP**, and formats it into a clean, ranked weekly chart used for publishing online.

As of **Week 36**, the system is tracking **750+ songs** and **30,000+ individual weekly data points** across both files.

## How it works

**Data collection (weekly):**
Each week's chart points per song are manually logged into the BREAKDOWN file. Points accumulate into a running yearly total per song.

**Ranking model:**
A custom point-accumulation formula calculates each song's:
- `TOTAL` — cumulative points for the year
- `RANK` — current standing based on total points
- `PEAK` — highest position ever reached
- `WEEKS ON` — number of consecutive weeks charting
- `GAIN` — point change from the previous week

**Publication layer:**
The PUBMAT file mirrors the ranked output from BREAKDOWN using XLOOKUP, then formats it into a clean weekly leaderboard showing rank, week-over-week movement (`+/-`), points, gain, peak, and weeks on chart — ready to publish.

**Example — Week 36, 2026 (current top 5):**

| Rank | +/- | Song | Artist | Points | Gain | Peak | WO |
|------|-----|------|--------|--------|------|------|----|
| 1 | = | Choosin' Texas | Ella Langley | 7,706 | +293 | 1 | 35 |
| 2 | = | Man I Need | Olivia Dean | 7,004 | +164 | 2 | 43 |
| 3 | = | The Fate Of Ophelia | Taylor Swift | 6,487 | +0 | 1 | 32 |
| 4 | = | Golden | HUNTR/X: EJAE, Audrey Nuna & REI AMI | 6,417 | +0 | 1 | 47 |
| 5 | = | Ordinary | Alex Warren | 6,146 | +0 | 1 | 65 |

**Visualization:**
A Power BI dashboard built on top of the BREAKDOWN data visualizes chart trends and individual song trajectories over time.

**Output:**
Weekly chart results are published consistently to [YouTube (Top50Singles)](https://www.youtube.com/@TheTop50Singles) — 34K+ subscribers, 150K+ average monthly views — and [X/Twitter (Top50Singles)](https://x.com/TheTop50Singles).

## A note on the data

This dataset has grown organically since the project began. Earlier weeks have minor structural differences — for example, some early sheets are missing the `Weeks On` column, and the column layout shifted slightly a few times as the tracking system matured. Rather than retroactively "cleaning" this history, it's been left intact, since it reflects how the system actually evolved over a year and a half of continuous, hands-on maintenance. The current format (used from recent weeks onward) is the finalized structure going forward.

## Tools used

- **Microsoft Excel** — data tracking, ranking formulas, XLOOKUP-based cross-file reporting
- **Microsoft Power BI** — dashboard visualization of chart trends and song trajectories
- **CapCut** — used for related video content published alongside the chart data

## About

Built and maintained by **John Martin S. Villena**, BS Information Technology graduate (Business Analytics) from Bulacan State University.

📊 [LinkedIn](https://www.linkedin.com/in/jhnmrtnvlln/)
