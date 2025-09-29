import pandas as pd


# ---------------------------------------------------------------
# Show Duplicate Records
def show_duplicate_records(data, subset):
    resault = {}

    duplicate_records = data.duplicated(subset=subset, keep=False)
    resault["duplicate_records"] = data[duplicate_records].sort_values(by=[subset[0]])

    number_duplicate_records = duplicate_records.sum()
    resault["number_duplicate_records"] = number_duplicate_records

    return resault


# ---------------------------------------------------------------
# Drop Duplicate Records
def drop_duplicate_records(data):
    data.drop_duplicates(keep="first", inplace=True)
    return f"Duplicate Records Deleted\nDrop Duplicate Records : {data.duplicated(keep=False).sum()}"

# ---------------------------------------------------------------
# String Data Noise
def handle_string_noise(data):
    report = {}
    total_noise_count = 0
    noise_summary = {}

    for col in data.columns[1:]:
        coerced = pd.to_numeric(data[col], errors="coerce")
        mask = coerced.isna() & data[col].notna()

        if mask.any():
            noise_count = mask.sum()
            total_noise_count += noise_count
            noise_summary[col] = {
                "unique_noise_values": data.loc[mask, col].unique().tolist(),
                "noise_count": noise_count,
            }

            mean_val = pd.to_numeric(data[col], errors="coerce").mean()

            data.loc[mask, col] = mean_val

        data[col] = pd.to_numeric(data[col], errors="coerce")

    report["total_noise_count"] = total_noise_count
    report["noise_summary"] = noise_summary
    report["data"] = data
    return report


# ---------------------------------------------------------------
# Show Null Records
def show_null_records(data):
    resault = {}

    null_records = data[data.isnull().any(axis=1)]

    sum_null_records = data.isnull().sum()

    number_null_records = data.isnull().sum().sum()
    
    resault["null_records"] = null_records
    resault["sum_null_records"] = sum_null_records
    resault["number_null_records"] = number_null_records

    return resault


# ---------------------------------------------------------------
# Fill Null Records
def fill_null_records(data, fill_data):
    data = data.fillna(value=fill_data)
    return data

# ---------------------------------------------------------------
# Generate Full Noise Report
def generate_full_noise_report(
    original_data,
    cleaned_data,
    noise_summary,
    duplicate_records,
    null_records,
    output_path="data/noise_report.csv",
):
    report_rows = []

    for col, info in noise_summary.items():
        coerced = pd.to_numeric(original_data[col], errors="coerce")
        mask = coerced.isna() & original_data[col].notna()
        mean_val = pd.to_numeric(original_data[col], errors="coerce").mean()

        for idx in original_data[mask].index:
            report_rows.append(
                {
                    "row_index": idx,
                    "column": col,
                    "original_value": original_data.loc[idx, col],
                    "status": "Replaced with Mean",
                    "new_value": mean_val,
                }
            )

    for idx in duplicate_records.index:
        if idx in original_data.index:
            report_rows.append(
                {
                    "row_index": idx,
                    "column": "ALL",
                    "original_value": original_data.loc[idx].to_dict(),
                    "status": "Dropped (Duplicate)",
                    "new_value": None,
                }
            )
            
    for idx in null_records.index:
        row = original_data.loc[idx].to_dict()
        for col, val in row.items():
            if pd.isna(val):
                report_rows.append(
                    {
                        "row_index": idx,
                        "column": col,
                        "original_value": None,
                        "status": "Filled (Null)",
                        "new_value": cleaned_data.loc[idx, col],
                    }
                )

    report_df = pd.DataFrame(report_rows)
    report_df.to_csv(output_path, index=False)
    return report_df
