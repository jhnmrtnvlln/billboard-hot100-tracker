# Billboard Hot 100 Chart Tracker

A self-built, Excel-based data pipeline that tracks Billboard Hot 100 chart performance week over week, calculates custom yearly rankings, and produces a publication-ready weekly chart for social media. Maintained continuously since **December 2024**.

---

## Dashboard Preview

**Week 37 — Positions 1–25**
![Week 37 Chart 1-25](WEEK%2037%201-25.png)

**Week 37 — Positions 26–50**
![Week 37 Chart 26-50](WEEK%2037%2026-50.png)

**Week 37 — Positions 51–75**
![Week 37 Chart 51-75](WEEK%2037%2051-75.png)

**Week 37 — Positions 76–100**
![Week 37 Chart 76-100](WEEK%2037%2076-100.png)

---

## Overview

This project started as a personal effort to follow weekly Billboard chart movement in more depth than the official charts show, and grew into a structured, two-layer data system:

1. **`HOT 100 BREAKDOWN.xlsx`** — the raw data layer. Tracks every charting song's weekly points, cumulative total, peak position, and weeks-on-chart, going back through 2025 and into 2026 (37+ weeks tracked in the current year alone).
2. **`HOT 100 PUBMAT.xlsx`** — the publication layer. Pulls ranked data from the breakdown file using **XLOOKUP**, and formats it into a clean, ranked weekly chart used for publishing online.
3. **`BREAKDOWN.xlsx`** — the stacked long-format data feed for Power BI — week-labeled rows enabling slicer-based filtering by chart week.
4. **`HOT 100 PROJECT.pbix`** — the visualization layer. A Power BI dashboard built on top of the breakdown data, visualizing chart trends and individual song trajectories over time.

---

## How It Works

**Data collection (weekly):**
Each week's chart points per song are manually logged into the BREAKDOWN file. Points accumulate into a running yearly total per song.

**Ranking model:**
A custom point-accumulation formula calculates each song's:
- `TOTAL` — cumulative points for the year
- `RANK` — current standing based on total points
- `PEAK` — highest position ever reached
- `WEEKS ON` — number of weeks charting
- `GAIN` — point change from the previous week

**Publication layer:**
The PUBMAT file mirrors the ranked output from BREAKDOWN using XLOOKUP, then formats it into a clean weekly leaderboard showing rank, week-over-week movement (`+/-`), points, gain, peak, and weeks on chart — ready to publish.

**Visualization layer:**
The Power BI dashboard connects to the BREAKDOWN data and visualizes song chart trajectories, yearly rankings, and weekly performance trends over time.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `HOT 100 BREAKDOWN.xlsx` | Raw weekly tracking data — 750+ songs, 30,000+ data points |
| `HOT 100 PUBMAT.xlsx` | Formatted publication output file, linked via XLOOKUP |
| `HOT 100 PROJECT.pbix` | Power BI dashboard — open with Power BI Desktop (free) |
| `WEEK 37 1-25.png` | Screenshot — Week 37 chart positions 1–25 |
| `WEEK 37 26-50.png` | Screenshot — Week 37 chart positions 26–50 |
| `WEEK 37 51-75.png` | Screenshot — Week 37 chart positions 51–75 |
| `WEEK 37 76-100.png` | Screenshot — Week 37 chart positions 76–100 |

---

## Example — Week 37, 2026 (current top 5)

| Rank | +/- | Song | Artist | Points | Gain | Peak | WO |
|------|-----|------|--------|--------|------|------|----|
| 1 | = | Choosin' Texas | Ella Langley | 7,706 | +293 | 1 | 35 |
| 2 | = | Man I Need | Olivia Dean | 7,004 | +164 | 2 | 43 |
| 3 | = | The Fate Of Ophelia | Taylor Swift | 6,487 | +0 | 1 | 32 |
| 4 | = | Golden | HUNTR/X: EJAE, Audrey Nuna & REI AMI | 6,417 | +0 | 1 | 47 |
| 5 | = | Ordinary | Alex Warren | 6,146 | +0 | 1 | 65 |

---

## Output & Publication

Weekly chart results are published consistently to:
- 📺 [YouTube — Top50Singles](https://www.youtube.com/@TheTop50Singles) — 34K+ subscribers, 150K+ average monthly views
- 🐦 [Twitter/X — @TheTop50Singles](https://x.com/TheTop50Singles)

---

## A Note on the Data

This dataset has grown organically since the project began. Earlier weeks have minor structural differences — for example, some early sheets are missing the `Weeks On` column, and the column layout shifted slightly a few times as the tracking system matured. Rather than retroactively cleaning this history, it has been left intact as it reflects how the system actually evolved over a year and a half of continuous, hands-on maintenance. The current format (used from recent weeks onward) is the finalized structure going forward.

---

## Tools Used

- **Microsoft Excel** — data tracking, ranking formulas, XLOOKUP-based cross-file reporting
- **Microsoft Power BI** — dashboard visualization of chart trends and song trajectories
- **CapCut** — used for related video content published alongside the chart data

---

## About

Built and maintained by **John Martin S. Villena**, BS Information Technology graduate (Business Analytics) from Bulacan State University — Sarmiento Campus.

🔗 [LinkedIn](https://www.linkedin.com/in/jhnmrtnvlln/)
📺 [YouTube](https://www.youtube.com/@TheTop50Singles)
🐦 [Twitter/X](https://x.com/TheTop50Singles)
