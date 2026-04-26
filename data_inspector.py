import pandas as pd

# 1. Load the dataset we just generated
filename = 'port_traffic_data.csv'

# Read the CSV file into a Pandas DataFrame (think of this as a Python-powered spreadsheet)
df = pd.read_csv(filename)

# 2. Print the first 5 rows to see what the raw data looks like
print("--- First 5 Rows of Port Data ---")
print(df.head())

# 3. Print a summary of the data (column names, row counts, and data types)
print("\n--- Data Summary ---")
print(df.info())