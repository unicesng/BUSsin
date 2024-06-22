from flask import Flask
from bus_tracking import bus_timings_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(bus_timings_bp, url_prefix='/bus')

if __name__ == '__main__':
    app.run()