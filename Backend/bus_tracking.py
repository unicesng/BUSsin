from flask import Blueprint, jsonify

bus_timings_bp = Blueprint('bus_timings', __name__)

@bus_timings_bp.route('/bus-timings/<bus_stop>')
def get_bus_timings(bus_stop):
    # Logic to retrieve bus timings for all buses at a bus stop
    timings = {
        'bus_stop': {
            '123': {
                'timings': ['8:00 AM', '10:30 AM', '1:00 PM']
            },
            '456': {
                'timings': ['9:00 AM', '11:30 AM', '2:00 PM']
            }
        }
    }
    return jsonify(timings) 

@bus_timings_bp.route('/bus-timings/<bus_stop>/<bus_number>')
def get_bus_timings(bus_number):
    # Logic to retrieve bus timings for the specified bus number at a bus stop
    timings = {'bus_number': bus_number, 'timings': ['8:00 AM', '10:30 AM', '1:00 PM']}
    return jsonify(timings)