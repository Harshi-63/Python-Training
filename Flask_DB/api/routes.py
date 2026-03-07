from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


# Route 1 → /api/status
@api.route('/status')
def status():
    return jsonify({'status': 'API is running'})


# Route 2 → /api/data
@api.route('/data')
def data():
    sample_data = {
        "name": "Flask API",
        "version": "1.0",
        "description": "A simple API endpoint"
    }
    return jsonify(sample_data)
