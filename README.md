# Battery Cell Data Visualization Dashboard

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)
7. [Data Structure](#data-structure)
8. [Visualization Details](#visualization-details)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

The Battery Cell Data Visualization Dashboard is a Flask-based web application designed to visualize and analyze performance metrics of battery cells over time. This tool provides an interactive interface to monitor voltage, temperature, current, and capacity data for individual battery cells.

## Features

- Interactive time-series visualization of four key battery metrics:
  - Voltage
  - Temperature
  - Current
  - Capacity
- Data retrieval from a SQLite database
- Dynamic plot generation using Plotly
- Responsive web interface
- Individual cell data views

## Requirements

- Python 3.7+
- Flask
- Plotly
- SQLite3

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/battery-cell-dashboard.git
   cd battery-cell-dashboard
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter a cell ID to view its data visualization

## API Endpoints

- `/api/cell_data/<cell_id>`: Retrieves and visualizes data for a specific cell ID

## Data Structure

The application expects the following table structure in the SQLite database:

```sql
CREATE TABLE battery_data (
    cell_id TEXT,
    timestamp DATETIME,
    current REAL,
    voltage REAL,
    capacity REAL,
    temperature REAL
);
```

## Visualization Details

The dashboard creates a figure with four subplots:

1. Voltage vs Time (blue)
2. Temperature vs Time (red)
3. Current vs Time (green)
4. Capacity vs Time (purple)

All subplots share the same x-axis (time) for easy comparison.

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
