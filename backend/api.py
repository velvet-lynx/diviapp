from flask import jsonify
from flask_restless import APIManager
from models import Stop, Line, Link
from app_config import db, app
import app_config

def create_dict(tup, keys, id_col):
    """ Create a JSONlike dictionnary from keys and values in tuple
        with id_col being the object identifier"""
    return {    
        tup[id_col]: { 
            key: tup[i] for i, key in enumerate(keys) if i != id_col
        }
    }

def get_datas(query, id_col=None):
    """ Create a dictionnary of JSONlike objects from an SQLAlchemy query """
    records = None
    datas = {}
    if isinstance(query, db.Model):
        datas = query.to_dict()
    else:
        keys = [col["name"] for col in query.column_descriptions]
        records = query.all()
        if records is list and isinstance(records[0], db.Model):
            for record in records:
                datas.update(record.to_dict())
        else:
            for record in records:
                datas.update(create_dict(record, keys, id_col))
    return datas


@app.route("/lines/", methods=['GET'])
def get_lines():
    """ API endpoint returning all lines """
    query = db.session.query(Line)
    return jsonify(get_datas(query))

@app.route("/lines/<int:line_id>/", methods=['GET'])
def get_line(line_id):
    """ API endpoint returning a single line of id line_id """
    query = db.session.query(Line).get(line_id)
    return jsonify(get_datas(query))

@app.route("/stops/", methods=['GET'])
def get_stops():
    """ API endpoint returning all stops """
    query = db.session.query(Stop)
    return jsonify(get_datas(query))

@app.route("/stops/<int:stop_id>", methods=['GET'])
def get_stop(stop_id):
    """ API endpoint returning a single stop of id stop_id """
    query = db.session.query(Stop).get(stop_id)
    return jsonify(get_datas(query))

@app.route("/lines/<int:line_id>/stops/", methods=['GET'])
def get_links(line_id):
    """ API endpoint returning links between a given line (line_id) and it's stops """
    query = db.session.query(
        Line.line_name,
        Line.line_dest,
        Stop.stop_id,
        Stop.stop_name,
        Link.link_id,
        Link.stop_ref
    )
    query = query.join(Link).join(Stop).filter(Link.line_id == line_id)
    return jsonify(get_datas(query, 4))

@app.route("/lines/<int:line_id>/stops/<int:stop_id>", methods=['GET'])
def get_link(line_id, stop_id):
    """ API endpoint returning link between a given line (line_id) and a given stop (stop_id) """
    query = db.session.query(
        Line.line_name,
        Line.line_dest,
        Stop.stop_id,
        Stop.stop_name,
        Link.link_id,
        Link.stop_ref
    )
    query = query.join(Link).join(Stop).filter(
        db.and_(Link.line_id == line_id, Link.stop_id == stop_id)
    )
    return jsonify(get_datas(query, 4))

if __name__ == "__main__":
    app.run(debug=True)
