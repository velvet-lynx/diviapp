from flask import Blueprint, jsonify

from project.services import get_times

times = Blueprint('times', __name__)


@times.route('/api/times/<code>', methods=['GET'])
def get_times_route(code):
    """API endpoint returning next arrivals given a stop code."""
    times = get_times(code)
    response = {
        "status": "fail",
        "message": "External API unreachable"
    }
    if times is not None:
        if not times:
            response['message'] = "No infos are available"
            return jsonify(response), 500
        else:
            response = {
                "payload": times,
                "status": "success"
            }
            return jsonify(response), 200
    else:
        return jsonify(response), 50
