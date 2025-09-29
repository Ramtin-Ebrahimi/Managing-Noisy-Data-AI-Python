import pandas as pd

# Function to save a DataFrame to a CSV file
def load(data,file_path):
    data.to_csv(file_path, index=False)