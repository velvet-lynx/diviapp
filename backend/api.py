from flask import jsonify
from flask_restless import APIManager
from models import Stop, Line
from app_config import db, app
import app_config


"""
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Stop(), methods=['GET', 'DELETE', 'PUT'])
manager.create_api(Line(), methods=['GET', 'DELETE', 'PUT'])
"""

@app.route("/lines/", methods=['GET'])
def get_lines():
    lines = {}
    for line in Line.query.all():
        lines.update(line.to_dict())
    return jsonify(lines)

@app.route("/lines/<int:line_id>/", methods=['GET'])
def get_line(line_id):
    return jsonify(Line.query.get(line_id).to_dict())

@app.route("/stops/", methods=['GET'])
def get_stops():
    stops = {}
    for stop in Stop.query.all():
        stops.update(stop.to_dict())
    return jsonify(stops)

@app.route("/stops/<int:stop_id>", methods=['GET'])
def get_stop(stop_id):
    return jsonify(Stop.query.get(stop_id).to_dict())

if __name__ == "__main__":
    app.run(debug=True)

