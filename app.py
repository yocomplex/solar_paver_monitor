from flask import Flask, jsonify, render_template
import random
import datetime

# initializing Flask application
app = Flask(__name__)

# function to simulate real-time data collection
def get_solar_data():
    # Getting the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Simulating energy production between 1.0 and 10.0 kWh
    energy_produced = round(random.uniform(1.0, 10.0), 2) 
    return {
        "time": current_time,
        "energy": energy_produced
    }

# Routing to render the main HTML page
@app.route('/')
def solar_paver_monitor():
    return render_template('solar_paver_monitor.html')

# Routing to provide data in JSON format
@app.route('/data')
def data():
    return jsonify(get_solar_data())

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
