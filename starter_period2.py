# starter_period2.py

import json
from collections import Counter

def main():
    input_file = "logs.txt"
    clean_file = "clean_logs.txt"
    summary_file = "summary.json"

    allowed_levels = {"INFO", "WARN", "ERROR"}

    total_lines = 0
    valid_lines = 0
    invalid_lines = 0

    level_counts = Counter()
    service_counts = Counter()
    error_messages = Counter()

    clean_lines = []

    with open(input_file, "r") as f:
        for line in f:
            total_lines += 1
            parts = [p.strip() for p in line.split("|")]

            # Must have 4 fields
            if len(parts) != 4:
                invalid_lines += 1
                continue

            timestamp, level, service, message = parts
            level = level.upper()

            if level not in allowed_levels:
                invalid_lines += 1
                continue

            # Valid line
            valid_lines += 1
            level_counts[level] += 1
            service_counts[service] += 1

            if level == "ERROR":
                error_messages[message] += 1

            clean_lines.append(f"{timestamp} | {level} | {service} | {message}")

    # Write clean logs
    with open(clean_file, "w") as out:
        for cl in clean_lines:
            out.write(cl + "\n")

    # Build JSON summary
    summary = {
        "total_lines": total_lines,
        "valid_lines": valid_lines,
        "invalid_lines": invalid_lines,
        "levels": {
            "INFO": level_counts["INFO"],
            "WARN": level_counts["WARN"],
            "ERROR": level_counts["ERROR"]
        },
        "top_services": [
            {"service": svc, "count": cnt}
            for svc, cnt in service_counts.most_common(3)
        ],
        "top_errors": [
            {"message": msg, "count": cnt}
            for msg, cnt in error_messages.most_common(3)
        ]
    }

    with open(summary_file, "w") as out:
        json.dump(summary, out, indent=2)


if __name__ == "__main__":
    main()