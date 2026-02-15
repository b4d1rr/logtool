# logtool — Cloud Log Reader (Period 1)

logtool is a simple Python command-line tool that reads raw cloud logs, validates them, counts log levels, and generates a clean text report.

This tool was created as part of a cloud engineering assignment focusing on:
- log parsing  
- validation  
- data quality checks  
- text reporting

---

## 📌 Features
- Reads **logs.txt**
- Splits each log into 4 fields:
  - `timestamp | level | service | message`
- Validates:
  - Correct number of fields
  - Level must be: `INFO`, `WARN`, or `ERROR`
- Counts:
  - Total lines
  - Invalid lines
  - INFO / WARN / ERROR logs
  - Invalid levels
- Generates a summary report:
  - Printed in terminal
  - Saved as **period1_report.txt**

---

## 🚀 How to Run

1. Place the following in the same folder:
   - `starter_period1.py`
   - `logs.txt`

2. Run the tool:

```bash
python starter_period1.py
```

Output file created:

period1_report.txt
📄 Output Example
Total lines: 120
Invalid lines: 8
INFO: 60
WARN: 35
ERROR: 17
Invalid levels: 3
📁 Files Included

starter_period1.py

logs.txt (input)

period1_report.txt (generated)

✔️ Author

Created for Cloud Engineering — Period 1


---

# ⭐ **README for logtool-v2 (Task 2 / Period 2)**  
### `README.md`

# logtool-v2 — Cloud Log Cleaner & JSON Summary (Period 2)

logtool-v2 is the upgraded version of **logtool**, focused on producing real cloud-dashboard-ready outputs:
- cleaned logs
- level counts
- top services
- top error messages
- structured JSON summary

This tool simulates real DevOps / cloud engineering log-pipeline workflow.

---

## 📌 Features

### 🔍 **Validates Logs**
A log is considered valid if:
- It has **exactly 4 fields**
- The level is **INFO / WARN / ERROR**

Invalid logs are ignored for output but counted for statistics.

---

### 🧼 **Produces Clean Logs**  
Writes valid logs to:


clean_logs.txt


Format:

timestamp | LEVEL | service | message

*(LEVEL is always uppercase)*

---

### 🧾 **Generates JSON Summary**

Creates:


summary.json


With the required structure:
```json
{
  "total_lines": 0,
  "valid_lines": 0,
  "invalid_lines": 0,
  "levels": {"INFO": 0, "WARN": 0, "ERROR": 0},
  "top_services": [{"service": "auth", "count": 0}],
  "top_errors": [{"message": "DB timeout", "count": 0}]
}
```

Includes:

top 3 services by count

top 3 ERROR messages by frequency

🚀 How to Run

Place the following in the same folder:

starter_period2.py

logs.txt

Run:

python starter_period2.py

Outputs created:

clean_logs.txt
summary.json
📁 Files Included

starter_period2.py

logs.txt (input)

clean_logs.txt

summary.json
