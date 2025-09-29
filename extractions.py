import pandas as pd

# Function to extract data from a CSV file into a DataFrame
def extract_data(file_path):
    return pd.read_csv(file_path)