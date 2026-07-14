# Billboard Hot 100 Chart Tracker

A self-built, Excel-based data pipeline that tracks Billboard Hot 100 chart performance week over week, calculates custom yearly rankings, and produces a publication-ready weekly chart for social media. Maintained continuously since **December 2024**.

---

## From Raw Data to Published Output

### Power BI Dashboard
![Power BI Dashboard](POWERBI%20DASHBOARD.png)

### Weekly Chart — Excel Publication Format
![Excel PUBMAT Weekly Chart](EXCEL%20PUBMAT%20WEEKLY%20CHART.png)

### Published Output — Twitter/X
![Published Chart Output](PUBLISHED%20OUTPUT.jpg)

---

## Overview

This project started as a personal effort to follow weekly Billboard chart movement in more depth than the official charts show, and grew into a structured, three-layer data system:

1. **`HOT 100 BREAKDOWN.xlsx`** — the raw data layer. Tracks every charting song's weekly points, cumulative total, peak position, and weeks-on-chart, going back through 2025 and into 2026 (39+ weeks tracked in the current year alone).
2. **`BREAKDOWN.xlsx`** — the Power BI data feed. A stacked long-format version of the tracking data with week-labeled rows, structured specifically to enable slicer-based filtering by chart week in Power BI.
3. **`HOT 100 PUBMAT.xlsx`** — the publication layer. Pulls ranked data from the breakdown file using **XLOOKUP**, and formats it into a clean, ranked weekly chart used for publishing online.
4. **`HOT 100 PROJECT.pbix`** — the visualization layer. A Power BI dashboard built on top of the stacked data feed, visualizing chart trends and individual song trajectories over time.

As of **Week 39**, the system is tracking **750+ songs** and **30,000+ individual weekly data points** across both files.

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
The Power BI dashboard connects to the stacked BREAKDOWN data and visualizes song chart trajectories, yearly rankings, and weekly performance trends over time using interactive slicers for week-by-week filtering.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `HOT 100 BREAKDOWN.xlsx` | Raw weekly tracking data — 750+ songs, 30,000+ data points |
| `BREAKDOWN.xlsx` | Stacked long-format data feed for Power BI slicer-based filtering |
| `HOT 100 PUBMAT.xlsx` | Formatted publication output file, linked via XLOOKUP |
| `HOT 100 PROJECT.pbix` | Power BI dashboard — open with Power BI Desktop (free) |
| `POWERBI DASHBOARD.png` | Sample screenshot — Power BI visualization layer |
| `EXCEL PUBMAT WEEKLY CHART.png` | Sample screenshot — Excel publication output |
| `PUBLISHED OUTPUT.jpg` | Sample — final graphic published to social media |

---

## Example — Week 39, 2026 (current top 5)

| Rank | +/- | Song | Artist | Points | Gain | Peak | WO |
|------|-----|------|--------|--------|------|------|----|
| 1 | = | Choosin' Texas | Ella Langley | 8,302 | +294 | 1 | 38 |
| 2 | = | Man I Need | Olivia Dean | 7,485 | +168 | 2 | 46 |
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
