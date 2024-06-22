from flask import Blueprint, jsonify

train_timings_bp = Blueprint('train_timings', __name__)

@train_timings_bp.route('/train-timings/<station_code>')
def get_train_timings(station_code):
    # Logic to fetch train timings for the specified station
    timings = {'station_code': station_code, 'timings': ['9:45 AM', '1:20 PM', '4:30 PM']}
    return jsonify(timings)