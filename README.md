# Managing-Noisy-Data-AI-Python

## 🏥 Hospital Data Quality ETL Pipeline

## 📌 Description

### This project implements a clean and modular ETL pipeline to identify and report problematic records in hospital datasets stored as CSV files. It focuses on data quality assurance by detecting:

### - 🧨 Noisy records — rows with missing or non-numeric values in key numerical columns.
### - 🔁 Duplicate records — repeated entries that may distort analysis.
### - 📊 Combined issues — a unified view of all problematic rows for inspection or downstream cleaning.
---

# ⚙️ ETL Workflow

`mermaid
graph TD
    A[Extract CSV File] --> B[Identify Noisy Records]
    B --> C[Detect Duplicates]
    C --> D[Combine & Report Issues]
    D --> E[Print or Export Results]
`

---

# 🧪 Features

- ✅ Modular ETL structure (Extract → Transform → Load)
- ✅ Detects missing or invalid numeric values in:
  - daily_patients
  - treated_patients
  - discharged_patients
  - deaths
- ✅ Flags duplicate rows using pandas.duplicated()
- ✅ Combines noisy and duplicate records into a single report
- ✅ Easy to extend for cleaning, exporting, or integration

---

# 📦 Sample Output

`bash
Total problematic records (noisy + duplicate): 57

# 🔍 Noisy or duplicate records:
| hospitalname | dailypatients | treatedpatients | dischargedpatients | deaths |
|---------------|----------------|------------------|----------------------|--------|
| Lind          | NaN            | 45               | 38                   | 2      |
| Crona         | r              | 50               | 40                   | 1      |
| ...           | ...            | ...              | ...                  | ...    |
`

---

# 🚀 Getting Started

## 🔧 Requirements

### - Python 3.8+
### - pandas

▶️ Run the ETL

`bash
python etl_hospital.py
`

## Make sure hospital.csv is in your working directory. You can customize column names or add export logic as needed.

---

# 📁 File Structure

`
├── etl_hospital.py       # Main ETL script
├── hospital.csv          # Input dataset
└── README.md             # Project documentation
`

---

# 📜 License

## This project is licensed under the MIT License. Feel free to use, modify, and share.

---

# 🤝 Contributing

## Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
