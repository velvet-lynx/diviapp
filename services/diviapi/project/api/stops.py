from flask import Blueprint, jsonify

from project.services import get_stops

stops = Blueprint('stops', __name__)


@stops.route("/api/stops/<code>:<way>", methods=['GET'])
def get_stops_route(code, way):
    """ API endpoint returning stops of a given line """
    stops = get_stops(code, way)
    response = {
        "status": "fail",
        "message": "External API unreachable"
    }
    if stops is not None:
        if not stops:
            response['message'] = "No infos are available"
            return jsonify(response), 500
        else:
            response = {
                "payload": stops,
                "status": "success"
            }
            return jsonify(response), 200
    else:
        return jsonify(response), 500
