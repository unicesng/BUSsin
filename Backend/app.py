from flask import Flask,jsonify
from flask_cors import CORS
import os
import json
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from flask_apscheduler import APScheduler
from plyer import notification

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
CORS(app)

favorites = ["176"]

# Specify the relative path to the JSON file in the "bus tracking" folder
file_path = os.path.join('data', 'BusArrival.json')

# Load the JSON data from the file
with open(file_path, 'r') as file:
    bus_arrival_data = json.load(file)

@app.route('/bus-arrival/<service_no>')
def get_bus_arrival(service_no):
    bus_services = bus_arrival_data.get('Services', [])
    
    for service in bus_services:
        if service.get('ServiceNo') == service_no:
            return jsonify({
                'ServiceNo': service_no,
                'BusStopCode': bus_arrival_data.get('BusStopCode'),
                'Operator': service.get('Operator'),
                'NextBus': service.get('NextBus'),
                'NextBus2': service.get('NextBus2'),
                'NextBus3': service.get('NextBus3')
            })
    
    return jsonify({'error': f'Bus service {service_no} not found'})

@app.route('/add-to-favorites/<service_no>', methods=['POST'])
def add_to_favorites(service_no):
    if service_no not in favorites:
        favorites.append(service_no)
        return jsonify({'message': f'Bus service {service_no} added to favorites'})
    return jsonify({'message': f'Bus service {service_no} is already in favorites'})

@app.route('/favorites')
def view_favorites():
    favorite_buses = []
    for service_no in favorites:
        for service in bus_arrival_data.get('Services', []):
            if service.get('ServiceNo') == service_no:
                favorite_buses.append({
                    'ServiceNo': service_no,
                    'BusStopCode': bus_arrival_data.get('BusStopCode'),
                    'Operator': service.get('Operator'),
                    'NextBus': service.get('NextBus'),
                    'NextBus2': service.get('NextBus2'),
                    'NextBus3': service.get('NextBus3')
                })
    return jsonify(favorite_buses)

def send_notification(service_no):
    bus_service = None
    for service in bus_arrival_data.get('Services', []):
        if service.get('ServiceNo') == service_no:
            bus_service = service
            break
    
    if bus_service:
        message = f"Bus {bus_service.get('ServiceNo')} is approaching your bus stop."
        notification.notify(
            title="Bus Arrival Notification",
            message=message,
            app_name="Bus Tracker App"
        )
    else:
        print(f"Bus service {service_no} not found.")

if __name__ == '__main__':
    app.run()