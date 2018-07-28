from flask import jsonify, request
from app_config import app
import app_config
import sys
sys.path.append("../")
from new_backend.database.mongo import db

def remove_id(result):
    copy = dict(result)
    del copy['_id']
    return copy

def to_json(results):
    return jsonify([ remove_id(result) for result in results ])

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials','true')
    return response

@app.route("/lines/", methods=['GET'])
def get_lines():
    """ API endpoint returning all lines """
    results = db.lines.find({},{
        'line_ref' : 1,
        'line_dest' : 1,
        'line_way' : 1,
        'line_color' : 1,
        'line_name' : 1,
    })
    return to_json(results)

@app.route("/lines/<line_ref>/", methods=['GET'])
def get_line(line_ref):
    """ API endpoint returning a single line of id line_id """
    results = db.lines.find({ 'line_ref' : line_ref})
    return to_json(results)

@app.route("/lines/<line_ref>/stops/", methods=['GET'])
def get_stops(line_ref):
    """ API endpoint returning stops of a given line"""
    results = db.lines.find({'line_ref' : line_ref}, { 'line_stops' : 1 })
    return to_json(results)

@app.route("/lines/<line_ref>:<line_way>/", methods=['GET'])
def get_line_with_line_way(line_ref, line_way):
    results = db.lines.find({'line_ref' : line_ref, 'line_way' : line_way })
    return to_json(results)

@app.route("/lines/<line_ref>:<line_way>/stops/", methods=['GET'])
def get_stops_with_line_way(line_ref, line_way):
    results = db.lines.find({'line_ref' : line_ref, 'line_way' : line_way }, {'line_stops' : 1 })
    return to_json(results)

if __name__ == "__main__":
    app.run()
