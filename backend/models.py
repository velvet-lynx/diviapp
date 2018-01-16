from app_config import db

class Link(db.Model):
    __tablename__ = "links"

    stop_id = db.Column(db.Integer, db.ForeignKey("stops.stop_id"), primary_key=True)
    line_id = db.Column(db.Integer, db.ForeignKey("lines.line_id"), primary_key=True)
    stop_ref = db.Column(db.String(100), nullable=False)

    def __init__(self, stop_id=None, line_id=None, stop_ref=None):
        self.stop_id = stop_id
        self.line_id = line_id
        self.stop_ref = stop_ref


class Stop(db.Model):
    __tablename__ = "stops"

    stop_id = db.Column(db.Integer, primary_key=True)
    stop_name = db.Column(db.String(100), nullable=False)
    stop_lat = db.Column(db.String(100))
    stop_lon = db.Column(db.String(100))

    link = db.relationship(Link, backref="stop")

    def __init__(self, stop_name=None, stop_lat=None, stop_lon=None):
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon


class Line(db.Model):
    __tablename__ = "lines"

    line_id = db.Column(db.Integer, primary_key=True)
    line_ref = db.Column(db.String(100), nullable=False)
    line_name = db.Column(db.String(100), nullable=False)
    line_dest = db.Column(db.String(100), nullable=False)
    line_way = db.Column(db.String(1), nullable=False)

    link = db.relationship(Link, backref="line")

    def __init__(self, line_ref=None, line_name=None, line_dest=None, line_way=None):
        self.line_ref = line_ref
        self.line_name = line_name
        self.line_dest = line_dest
        self.line_way = line_way
