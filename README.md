### logtool 

# Cloud Log Filtering CLI Tool

This project is a Python command-line tool that reads cloud-style logs,
validates them, and filters them by level and/or service.

## Features
- Reads logs.txt
- Filters logs by:
  - `--level` (INFO, WARN, ERROR)
  - `--service` (auth, api, db, etc.)
- Ignores invalid log lines
- Writes results to an output file
- Prints summary to the terminal

## Example Commands

Filter by level:

##

PL202 — Day 1 Independent Tasks (Grade 11)

Files included:
- logs.txt
- starter_period1.py
- starter_period2.py
- expected_output_example.json

How to run:
1) Put all files in ONE folder.
2) Open Terminal in that folder.
3) Period 1:
   python starter_period1.py
   -> creates period1_report.txt
4) Period 2:
   python starter_period2.py
   -> creates clean_logs.txt and summary.json

Notes:
- Do not rename logs.txt
- Outputs should be created in the same folder.
