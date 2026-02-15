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
