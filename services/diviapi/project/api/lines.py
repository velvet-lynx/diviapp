from flask import Blueprint, jsonify

from project.services import get_lines, get_stops

lines = Blueprint('lines', __name__)


@lines.route("/api/lines", methods=['GET'])
def get_lines_route():
    """ API endpoint returning all lines """
    lines = get_lines()
    response = {
        "status": "fail",
        "message": "External API unreachable"
    }
    if lines is not None:
        if not lines:
            response['message'] = "No infos are available"
            return jsonify(response), 400
        else:
            response = {
                "payload": lines,
                "status": "success"
            }
            return jsonify(response), 200
    else:
        return jsonify(response), 400


@lines.route("/api/stops/<code>:<way>", methods=['GET'])
def get_line_route(code, way):
    """ API endpoint returning stops of a given line """
    stops = get_stops(code, way)
    response = {
        "status": "fail",
        "message": "External API unreachable"
    }
    if stops is not None:
        if not stops:
            response['message'] = "No infos are available"
            return jsonify(response), 400
        else:
            response = {
                "payload": stops,
                "status": "success"
            }
            return jsonify(response), 200
    else:
        return jsonify(response), 400