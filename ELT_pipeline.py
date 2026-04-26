import pandas as pd
import sqlite3

print("Starting ETL Pipeline...")

# --- 1. EXTRACT ---
# Pull the raw data from our generated CSV file
filename = 'port_traffic_data.csv'
df = pd.read_csv(filename)
print(f"Extracted {len(df)} rows of raw data.")

# --- 2. TRANSFORM ---
# Convert the text-based dates into actual 'datetime' objects so Python can do math with them
df['Expected_Arrival'] = pd.to_datetime(df['Expected_Arrival'])
df['Actual_Arrival'] = pd.to_datetime(df['Actual_Arrival'])

# Calculate the exact delay in hours (Actual minus Expected) and round it to 2 decimal places
df['Delay_Hours'] = (df['Actual_Arrival'] - df['Expected_Arrival']).dt.total_seconds() / 3600
df['Delay_Hours'] = df['Delay_Hours'].round(2)

# Create a new column to flag if a ship is severely delayed (more than 5 hours late)
df['Severe_Delay_Flag'] = df['Delay_Hours'] > 5
print("Data transformed: Added 'Delay_Hours' and 'Severe_Delay_Flag' columns.")

# --- 3. LOAD ---
# Connect to a local SQLite database (this automatically creates the file 'port_database.db' if it doesn't exist)
conn = sqlite3.connect('port_database.db')

# Load our cleaned and transformed Pandas DataFrame directly into a new SQL table called 'vessel_traffic'
df.to_sql('vessel_traffic', conn, if_exists='replace', index=False)

# Always close your database connection when finished!
conn.close()
print("Pipeline Complete! Data loaded successfully into SQLite database.")