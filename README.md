# Battery Cell Data Visualization

This Flask-based application provides a visual interface for monitoring battery cell data, including State of Health (SoH) and various performance metrics over time. The application uses data stored in a SQLite database, which is populated from CSV files containing battery cell data.

## Features

- Display State of Health (SoH) for multiple battery cells using pie charts
- Visualize detailed cell data including voltage, temperature, current, and capacity over time
- Interactive plots using Plotly
- Data stored and retrieved from SQLite database
- Data import from CSV files

## Project Structure

- `app.py`: Main Flask application file containing route definitions and data processing logic
- `database.py`: Script for setting up the SQLite database and importing data from CSV files
- `battery.db`: SQLite database storing battery cell data
- `templates/`: Directory containing HTML templates
  - `index.html`: Home page displaying SoH pie charts
  - `5308.html` and `5329.html`: Individual cell data pages
- `cell_5308.csv`, `cell_5329.csv`: CSV files containing raw battery cell data

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/JoshiSneh/Battery-Cell-Data-Visualization.git
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Database Setup

1. Ensure you have the CSV files (`cell_5308.csv` and `cell_5329.csv`) in the project root directory.

2. Run the database setup script:
   ```
   python database.py
   ```

   This script will create the `battery.db` SQLite database and import data from the CSV files.

## Usage

1. After setting up the database, run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:8080` to view the application.

## API Endpoints

- `/`: Displays the home page with SoH pie charts for all cells
- `/api/cell_data/<cell_id>`: Retrieves and displays detailed data for a specific cell

## Data Structure

The `battery_data` table in the SQLite database has the following structure:

- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `cell_id`: INTEGER
- `record_index`: INTEGER
- `current`: REAL
- `voltage`: REAL
- `capacity`: REAL
- `temperature`: REAL
- `timestamp`: DATETIME

## Dependencies

This project relies on the following main libraries:
- Flask
- SQLite3
- Plotly
- Pandas
