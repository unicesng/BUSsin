from flask import Flask
from bus_timings import bus_timings_bp
from train_timings import train_timings_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(bus_timings_bp, url_prefix='/bus')
app.register_blueprint(train_timings_bp, url_prefix='/train')

if __name__ == '__main__':
    app.run()