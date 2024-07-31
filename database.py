import sqlite3
import pandas as pd
import os

conn = sqlite3.connect('battery.db')
cursor = conn.cursor()


'''Creating the battery_data table'''

cursor.execute('''
CREATE TABLE IF NOT EXISTS battery_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cell_id INTEGER,
    record_index INTEGER,
    current REAL,
    voltage REAL,
    capacity REAL,
    temperature REAL,
    timestamp DATETIME
)
''')


def import_csv(file_path, cell_id):
    '''
    This function reads a CSV file and imports the data into the database
    INPUT: file_path: str, cell_id: int
    OUTPUT: None
    '''

    df = pd.read_csv(file_path)
    df['cell_id'] = cell_id
    df['timestamp'] = pd.to_datetime(df['Time'])
    df = df.rename(columns={
        'Record Index': 'record_index',
        'Current': 'current',
        'Voltage': 'voltage',
        'Capacity': 'capacity',
        'Temperature': 'temperature'
    })
    
    df[['cell_id', 'record_index', 'current', 'voltage', 'capacity', 'temperature', 'timestamp']].to_sql('battery_data', conn, if_exists='append', index=False)


csv_files = ['cell_5308.csv', 'cell_5329.csv']

for file in csv_files:
    cell_id = int(file.split('_')[1].split('.')[0])
    if os.path.exists(file):
        import_csv(file, cell_id)


conn.commit()
conn.close()

print("Database setup complete")