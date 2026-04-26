import streamlit as st
import pandas as pd
import sqlite3

# 1. Page Configuration
st.set_page_config(page_title="PortNetX Dashboard", layout="wide")
st.title("🚢 PortNetX: Smart Port Operations Dashboard")
st.markdown("Real-time vessel traffic, congestion analytics, and delay tracking.")

# 2. Extract Data from Database
# We connect to SQLite, grab everything from our table, and close the connection
conn = sqlite3.connect('port_database.db')
df = pd.read_sql('SELECT * FROM vessel_traffic', conn)
conn.close()

# 3. Calculate Key Metrics
total_ships = len(df)
avg_delay = df['Delay_Hours'].mean()
severe_delays = len(df[df['Severe_Delay_Flag'] == 1])

# 4. Display the Metrics at the top of the dashboard
st.subheader("Current Port Status")
col1, col2, col3 = st.columns(3)
col1.metric("Total Vessels Logged", total_ships)
col2.metric("Average Delay (Hours)", f"{avg_delay:.2f}")
col3.metric("Severe Delays (>5 Hrs)", severe_delays)

# 5. Visualizations
st.markdown("---")
st.subheader("Average Delay by Vessel Type")
# Group the data to see which types of ships are causing the most backups
delay_by_type = df.groupby('Vessel_Type')['Delay_Hours'].mean()
st.bar_chart(delay_by_type)

# 6. Show the Raw Data Table
st.markdown("---")
st.subheader("Live Vessel Traffic Log")
st.dataframe(df)