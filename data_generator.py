import random
from datetime import datetime, timedelta
import csv

# 1. Set up the column names for our dataset
headers = ['Vessel_ID', 'Vessel_Type', 'Expected_Arrival', 'Actual_Arrival', 'Cargo_Weight_Tons']

# 2. Define the types of ships docking at our port
ship_types = ['Container Ship', 'Bulk Carrier', 'Oil Tanker', 'Ro-Ro (Vehicles)']

# 3. Create an empty list to hold our generated records
mock_data = []
base_time = datetime.now()

# 4. Generate 50 rows of simulated data using a loop
for i in range(1, 51):
    # Create a unique ID for each ship
    vessel_id = f"VESSEL_{i:03d}"
    
    # Pick a random ship type from our list
    vessel_type = random.choice(ship_types)
    
    # Simulate an Expected Arrival Time (anytime in the next 72 hours)
    expected_arrival = base_time + timedelta(hours=random.randint(1, 72))
    
    # Simulate real-world delays: Actual arrival is the expected time plus a random delay (-2 to 12 hours)
    delay_hours = random.randint(-2, 12) 
    actual_arrival = expected_arrival + timedelta(hours=delay_hours)
    
    # Generate a random cargo weight between 5,000 and 150,000 tons
    cargo_weight = random.randint(5000, 150000)
    
    # Add this completed row to our list, formatting the dates cleanly
    mock_data.append([
        vessel_id, 
        vessel_type, 
        expected_arrival.strftime("%Y-%m-%d %H:%M:%S"), 
        actual_arrival.strftime("%Y-%m-%d %H:%M:%S"), 
        cargo_weight
    ])

# 5. Save everything into a CSV file
filename = 'port_traffic_data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)      # Write the column names
    writer.writerows(mock_data)   # Write the 50 rows of data

print(f"Success! Generated {filename} with 50 records.")