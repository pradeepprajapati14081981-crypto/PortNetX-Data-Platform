from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) # This allows your HTML file to talk to this Python script

def get_db_connection():
    conn = sqlite3.connect('port_database.db')
    conn.row_factory = sqlite3.Row # This lets us access columns by name
    return conn

@app.route('/api/vessels')
def get_vessels():
    conn = get_db_connection()
    # Fetch all vessels from the table we built in the ETL step
    vessels = conn.execute('SELECT * FROM vessel_traffic').fetchall()
    conn.close()
    
    # Convert the SQL rows into a format the website understands (JSON)
    return jsonify([dict(row) for row in vessels])

if __name__ == '__main__':
    app.run(debug=True, port=5000)