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
