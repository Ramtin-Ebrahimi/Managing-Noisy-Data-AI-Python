from extractions import *
from transforms import *
from loads import *

# ---------------------------------------------------------------
# Utility Function To Display DataFrame Sections With Titles
def display(title, data):
    print(f'{title} :\n{data}\n')
    print(100*'-')
    
# ---------------------------------------------------------------
# Define Dataset Columns
columns = ['hospital_name','daily_patients','treated_patients','discharged_patients','deaths']
       
# --------------------------------------------------------------- 
# Extract Data From CSV File
data = extract_data('data/hospital.csv')
df = data.copy()
display('Show All Records', data)
    
# ---------------------------------------------------------------
# Counter For All Noisy Data Types (duplicates, nulls, string noise)
count_of_noisy_data = 0
    
# ---------------------------------------------------------------
# Detect Duplicate Records
duplicate = show_duplicate_records(data, columns)
duplicate_records = duplicate['duplicate_records']
number_duplicated_records = duplicate['number_duplicate_records']
display('Show Duplicate Records', duplicate_records)
display('Show Number Duplicate Records', number_duplicated_records)
count_of_noisy_data += number_duplicated_records
    
# ---------------------------------------------------------------
# Drop Duplicate Records
drop_duplicate = drop_duplicate_records(data)
display('Drop Duplicate Records', drop_duplicate)
    
# ---------------------------------------------------------------
# Detect Null Records
null = show_null_records(data)
null_records = null['null_records']
sum_null_records = null['sum_null_records']
number_null_records = null['number_null_records']
display('Show Null Records', null_records)
display('Show Sum Null Records', sum_null_records)
display('Show Number Null Records', number_null_records)
count_of_noisy_data += number_null_records
    
# ---------------------------------------------------------------
# Fill Null Records With mode/mean Values
data = fill_null_records(data,{
    'hospital_name' : data['hospital_name'].mode()[0],
    'daily_patients' : data['daily_patients'].mode()[0],
    'treated_patients' :  data['daily_patients'].mode()[0],
    'discharged_patients' : pd.to_numeric(data.discharged_patients, errors='coerce').mean(),
    'deaths' : pd.to_numeric(data.deaths, errors='coerce').mean(),
})
display('Fill Null Records', data)
    
# ---------------------------------------------------------------
# Detect And Fix String Noise, Show Noise Count
string_noise = handle_string_noise(data)
data = string_noise["data"]
display('Show Total String Noise Records', string_noise["total_noise_count"])
count_of_noisy_data += string_noise["total_noise_count"]
    
# ---------------------------------------------------------------
# Print Detailed Noise Summary For Each Column
print('Show String Noise Records : ')
for col, info in string_noise["noise_summary"].items():
    print(f"Column: {col}")
    print(f"   Noise Count: {info['noise_count']}")
    print(f"   Unique Noise Values: {', '.join(map(str, info['unique_noise_values']))}")
    print()
print(100*'-')
    
# ---------------------------------------------------------------
# Display Total Noise Data Count
display('Total Number Of Noises Data', count_of_noisy_data)
    
# ---------------------------------------------------------------
# Generate And Save Full Noise Report As CSV
noise_report = generate_full_noise_report(
    original_data=df,
    cleaned_data=data,
    noise_summary=string_noise["noise_summary"],
    duplicate_records=duplicate_records,
    null_records=null_records,
    output_path="data/noise_report.csv"
)
    
# ---------------------------------------------------------------
# Display Noise Report Summary
display('Full Noise Report', noise_report)

# ---------------------------------------------------------------
# Show Cleaned Dataset
display('Show Cleaned Dataset : ', data)

# ---------------------------------------------------------------
# Save Cleaned Dataset To CSV
load(data, 'data/finally_data.csv')