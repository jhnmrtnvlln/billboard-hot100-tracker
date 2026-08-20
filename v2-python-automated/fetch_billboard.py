"""
fetch_billboard.py

Pulls the Billboard Hot 100 chart (all 100 entries) using the billboard.py
package, and can walk backwards through past weeks to build a history file.

WHAT THIS SCRIPT DOES:
1. Fetches a Billboard Hot 100 chart for a given date (or the current week
   if no date is given).
2. Walks backwards through previous weeks, one at a time, for as many weeks
   as you tell it to.
3. SAFELY merges the results into your existing CSV file:
   - If a week is already in the file, it's left completely untouched
     (so any column you added by hand, like "points", is never overwritten).
   - Only genuinely new weeks get added.
   - The whole file gets sorted by date afterward, so it always reads in
     order no matter what order weeks were fetched in.

You do NOT need to understand every line to run this. Just follow the
"HOW TO RUN THIS" instructions from before - nothing about running it
has changed.
"""

import billboard
import csv
import os
import time
from datetime import datetime, timedelta


# ---------------------------------------------------------
# SETTINGS - change these values to control what gets pulled
# ---------------------------------------------------------

# How many weeks of chart history do you want to pull?
# Example: 5 means "this week + the 4 weeks before it"
NUMBER_OF_WEEKS_TO_PULL = 5

# Leave this as None to start from the MOST RECENT chart.
# Or set a specific starting date, like "2024-01-06" (format: YYYY-MM-DD)
STARTING_DATE = None

# Name of the CSV file that gets read from and saved back to
OUTPUT_FILENAME = "h100_raw.csv"

# Seconds to wait between each request (be polite to Billboard's servers)
SECONDS_BETWEEN_REQUESTS = 1

# These are the columns this script knows how to fill in. Any OTHER
# columns found in your existing file (like a "points" column you added
# by hand) are preserved automatically - you don't need to list them here.
SCRIPT_MANAGED_COLUMNS = ["chart_date", "rank", "title", "artist",
                           "last_week", "peak_pos", "weeks_on_chart"]


# ---------------------------------------------------------
# MAIN SCRIPT - you shouldn't need to edit anything below this line
# ---------------------------------------------------------

def ask_for_settings():
    """
    Asks a couple of quick questions when the script starts, so you can
    change how many weeks to pull WITHOUT opening and editing this file.
    Just press Enter on any question to use the default shown in [brackets].
    """
    print("=" * 50)
    print("Billboard Hot 100 Fetcher")
    print("=" * 50)

    weeks_input = input(
        f"How many weeks to pull? [default: {NUMBER_OF_WEEKS_TO_PULL}]: "
    ).strip()
    weeks = int(weeks_input) if weeks_input else NUMBER_OF_WEEKS_TO_PULL

    date_input = input(
        "Starting date (YYYY-MM-DD), or press Enter for the most recent chart: "
    ).strip()
    starting_date = date_input if date_input else STARTING_DATE

    print()  # blank line before the fetching starts
    return weeks, starting_date


def normalize_date(date_value):
    """
    Takes a date in pretty much any common format (e.g. "2026-08-08",
    "8/8/2026", "08/08/2026") and converts it to a consistent
    "YYYY-MM-DD" string. This matters because Excel silently reformats
    date-looking text when you open and save a CSV - so without this,
    the same date could be stored as two different-looking text values
    and the duplicate-check below would fail to catch them.
    If the value can't be parsed as a date at all, it's returned as-is.
    """
    date_value = str(date_value).strip()
    possible_formats = ["%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y", "%d/%m/%Y"]
    for fmt in possible_formats:
        try:
            return datetime.strptime(date_value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date_value  # couldn't parse it - fall back to whatever it was


def make_row_key(row):
    """
    Builds a unique identifier for a row, so we can tell whether a
    song/week combination is already in the file. We use chart_date +
    title + artist together, since rank alone isn't a reliable ID
    (rank changes song to song), and title alone isn't unique across
    different weeks.

    The date is normalized and the title/artist are trimmed and
    lowercased for comparison purposes only, so small formatting
    differences (extra spaces, a reformatted date, different
    capitalization) don't cause the same song/week to be treated as
    two different rows.
    """
    normalized_date = normalize_date(row.get("chart_date", ""))
    normalized_title = str(row.get("title", "")).strip().lower()
    normalized_artist = str(row.get("artist", "")).strip().lower()
    return (normalized_date, normalized_title, normalized_artist)


def load_existing_rows(filename):
    """
    Reads whatever is already in the CSV file, if it exists.
    Returns (list_of_row_dicts, list_of_column_names_in_original_order).
    Every column already in the file is preserved exactly as-is,
    including ones this script doesn't manage (like "points").
    """
    if not os.path.exists(filename):
        return [], []

    with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        existing_fieldnames = reader.fieldnames or []
        existing_rows = list(reader)

    return existing_rows, existing_fieldnames


def fetch_chart_history(weeks_to_pull=None, starting_date=None):
    # Fall back to the SETTINGS values at the top of the file if nothing
    # was passed in (keeps this script usable even without the prompts).
    if weeks_to_pull is None:
        weeks_to_pull = NUMBER_OF_WEEKS_TO_PULL
    if starting_date is None:
        starting_date = STARTING_DATE

    new_rows = []  # this will hold every song/week combo we fetch this run

    print("Fetching starting chart...")
    if starting_date:
        chart = billboard.ChartData('hot-100', date=starting_date)
    else:
        chart = billboard.ChartData('hot-100')

    weeks_collected = 0

    while weeks_collected < weeks_to_pull:
        print(f"Processing chart dated {chart.date} "
              f"({len(chart.entries)} entries)...")

        for entry in chart.entries:
            new_rows.append({
                "chart_date": chart.date,
                "rank": entry.rank,
                "title": entry.title,
                "artist": entry.artist,
                "last_week": entry.lastPos if entry.lastPos else "-",
                "peak_pos": entry.peakPos,
                "weeks_on_chart": entry.weeks,
            })

        weeks_collected += 1

        if weeks_collected >= weeks_to_pull:
            break

        # Figure out the previous week's date ourselves (Billboard charts
        # are always dated to a Saturday, so we just go back 7 days).
        current_chart_date = datetime.strptime(chart.date, "%Y-%m-%d")
        previous_chart_date = current_chart_date - timedelta(days=7)
        previous_date_str = previous_chart_date.strftime("%Y-%m-%d")

        time.sleep(SECONDS_BETWEEN_REQUESTS)

        chart = billboard.ChartData('hot-100', date=previous_date_str)

    return new_rows


def merge_and_save(new_rows, filename):
    existing_rows, existing_fieldnames = load_existing_rows(filename)

    # Build a set of keys that are already in the file, so we know what
    # to skip.
    existing_keys = {make_row_key(row) for row in existing_rows}

    added_count = 0
    skipped_count = 0

    for row in new_rows:
        key = make_row_key(row)
        if key in existing_keys:
            # Already have this song/week - leave the existing row (and
            # any manual data on it, like points) completely untouched.
            skipped_count += 1
            continue
        existing_rows.append(row)
        existing_keys.add(key)
        added_count += 1

    if added_count == 0 and skipped_count == 0:
        print("No data to save.")
        return

    # Figure out the final column order: whatever columns the file
    # already had, in the same order, plus any script-managed columns
    # that weren't already present (this handles the very first run,
    # when the file doesn't exist yet).
    final_fieldnames = list(existing_fieldnames)
    for col in SCRIPT_MANAGED_COLUMNS:
        if col not in final_fieldnames:
            final_fieldnames.append(col)

    # Sort everything by date, then by rank, so the file always reads
    # in chronological order no matter what order weeks were fetched in.
    def sort_key(row):
        date_str = row.get("chart_date", "")
        try:
            rank_val = int(row.get("rank", 0))
        except (ValueError, TypeError):
            rank_val = 0
        return (date_str, rank_val)

    existing_rows.sort(key=sort_key)

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=final_fieldnames)
        writer.writeheader()
        writer.writerows(existing_rows)

    print(f"\nDone! Added {added_count} new row(s), "
          f"skipped {skipped_count} row(s) already in the file.")
    print(f"'{filename}' now has {len(existing_rows)} total row(s).")


if __name__ == "__main__":
    chosen_weeks, chosen_date = ask_for_settings()
    start_time = datetime.now()
    fetched_rows = fetch_chart_history(chosen_weeks, chosen_date)
    merge_and_save(fetched_rows, OUTPUT_FILENAME)
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"Finished in {elapsed:.1f} seconds.")