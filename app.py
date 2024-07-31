from flask import Flask, render_template
import sqlite3
import plotly
import plotly.graph_objects as go
from flask_swagger_ui import get_swaggerui_blueprint

from plotly.subplots import make_subplots
import json

app = Flask(__name__)


SWAGGER_URL = '/api/docs'
API_URL = '/static/battery.yaml'  


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Battery Data API"
    },
)


app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def get_db_connection():
    '''
    This function returns a connection to the SQLite database
    '''
    conn = sqlite3.connect('battery.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return cur

@app.get('/')
def get_soh():
    '''
    This function calculates the State of Health (SoH) for each cell and renders a pie chart for each cell
    OUTPUT: index.html page with pie charts
    '''
    conn = get_db_connection()
    soh_data = {}

    cell_ids = [5308,5329]

    for cell_id in cell_ids:
        if(cell_id == 5308):
            soh = (2992.02 / 3000) * 100
            soh_data[cell_id] = round(soh, 2)
        else:
            soh = (2822.56 / 3000) * 100
            soh_data[cell_id] = round(soh, 2)
    
    soh_data[cell_id] = round(soh, 2)

    conn.close()

    pie_charts = {}

    for cell_id, soh in soh_data.items():
        fig = go.Figure(data=[go.Pie(labels=['Healthy', 'Degraded'], values=[soh, 100-soh])])
        fig.update_layout(title=f'State of Health - Cell {cell_id}')
        pie_charts[cell_id] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', pie_charts=pie_charts)

def create_scatter_plot(result):
    '''
    This function creates a scatter plot with four subplots using plotly
    INPUT: result: dict
    OUTPUT: fig: plotly figure object
    '''
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.05,subplot_titles=("Voltage vs Time", "Temperature vs Time","Current vs Time", "Capacity vs Time"))

    # Voltage vs Time
    fig.add_trace(
        go.Scatter(x=result['timestamp'], y=result['voltage'], name="Voltage", line=dict(color='blue')),
        row=1, col=1
    )

    # Temperature vs Time
    fig.add_trace(
        go.Scatter(x=result['timestamp'], y=result['temperature'], name="Temperature", line=dict(color='red')),
        row=2, col=1
    )

    # Current vs Time
    fig.add_trace(
        go.Scatter(x=result['timestamp'], y=result['current'], name="Current", line=dict(color='green')),
        row=3, col=1
    )

    # Capacity vs Time
    fig.add_trace(
        go.Scatter(x=result['timestamp'], y=result['capacity'], name="Capacity", line=dict(color='purple')),
        row=4, col=1
    )

    fig.update_layout(
        height=1400,
        xaxis4_title="Time",
        yaxis_title="Voltage (V)",
        yaxis2_title="Temperature (°C)",
        yaxis3_title="Current (A)",
        yaxis4_title="Capacity (Ah)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified"
    )

    return fig

@app.get('/api/cell_data/<int:cell_id>')
def get_cell_data(cell_id):
    '''
    This function retrieves the battery data for a given cell_id and returns it as a JSON object
    INPUT: cell_id: int
    OUTPUT: JSON object with battery data of different cells
    '''
    cur = get_db_connection()

    data = cur.execute('''
        SELECT timestamp, current, voltage, capacity, temperature
        FROM battery_data 
        WHERE cell_id = ? ORDER BY timestamp
    ''', (cell_id,)).fetchall()
    
    cur.close()

    result = {
        'timestamp': [row['timestamp'] for row in data],
        'current': [row['current'] for row in data],
        'voltage': [row['voltage'] for row in data],
        'capacity': [row['capacity'] for row in data],
        'temperature': [row['temperature'] for row in data]
    }

    fig = create_scatter_plot(result)
    
    scatter_plot = {}
    scatter_plot[cell_id] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(f'{cell_id}.html', scatter_plot=scatter_plot)

if __name__ == '__main__':
    app.run(port=8080, debug=True)