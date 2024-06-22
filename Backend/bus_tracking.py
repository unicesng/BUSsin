from flask import Blueprint, jsonify

bus_timings_bp = Blueprint('bus_timings', __name__)

@bus_timings_bp.route('/bus-timings/<bus_number>')
def get_bus_timings(bus_number):
    # Logic to retrieve bus timings for the specified bus number
    timings = {'bus_number': bus_number, 'timings': ['8:00 AM', '10:30 AM', '1:00 PM']}
    return jsonify(timings)