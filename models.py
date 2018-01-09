from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class Stop(Base):
	__tablename__ = "stops"

	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	line_stop = relationship("LineStop")

	def __init__(self, datas):
		for key, value in datas.items():
			setattr(self, key, value)

	def __repr__(self):
		return "<Stop :: name=%s>" % self.name


class Line(Base):
	__tablename__ = "lines"

	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	destination = Column(String, nullable=False)
	line_stop = relationship("LineStop")

	def __init__(self, datas):
		for key, value in datas.items():
			setattr(self, key, value)

	def __repr__(self):
		return "<Line :: name=%s, destination=%s" % (self.name, self.destination)


class LineStop(Base):
	__tablename__ = "lines_stops"

	id = Column(Integer, primary_key=True, autoincrement=True)
	line_id = Column(Integer, ForeignKey("lines.id"))
	stop_id = Column(Integer, ForeignKey("stops.id"))
	totem = Column(Integer, nullable=False)
	previous = Column(Integer, ForeignKey("lines_stops.id"))
	line_stop = relationship("LineStop", remote_side=[id])

	def __init__(self, datas):
		for key, value in datas.items():
			setattr(self, key, value)

	def __repr__(self):
		return "<LineStop :: line_id=%d stop_id=%d>" % (self.line_id, self.stop_id)