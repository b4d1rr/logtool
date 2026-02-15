# starter_period1.py

def main():
    input_file = "logs.txt"
    output_file = "period1_report.txt"

    total_lines = 0
    invalid_lines = 0
    info_count = 0
    warn_count = 0
    error_count = 0
    invalid_level_count = 0

    allowed_levels = {"INFO", "WARN", "ERROR"}

    with open(input_file, "r") as f:
        for line in f:
            total_lines += 1
            parts = [p.strip() for p in line.split("|")]

            # Must have exactly 4 fields
            if len(parts) != 4:
                invalid_lines += 1
                continue

            timestamp, level, service, message = parts
            level = level.upper()

            if level not in allowed_levels:
                invalid_level_count += 1
                continue

            # Count valid levels
            if level == "INFO":
                info_count += 1
            elif level == "WARN":
                warn_count += 1
            elif level == "ERROR":
                error_count += 1

    # Create summary text
    summary = (
        f"Total lines: {total_lines}\n"
        f"Invalid lines: {invalid_lines}\n"
        f"INFO: {info_count}\n"
        f"WARN: {warn_count}\n"
        f"ERROR: {error_count}\n"
        f"INVALID_LEVEL: {invalid_level_count}\n"
    )

    print(summary)

    # Save report
    with open(output_file, "w") as out:
        out.write(summary)


if __name__ == "__main__":
    main()