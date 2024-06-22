from flask import Flask, jsonify  # Import jsonify function
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bus-timings/<bus_number>')
def get_bus_timings(bus_number):
    # Add logic here to retrieve the bus timings for the specified bus number
    timings = {'bus_number': bus_number, 'timings': ['8:00 AM', '10:30 AM', '1:00 PM']}
    return jsonify(timings)

if __name__ == '__main__':
    app.run()