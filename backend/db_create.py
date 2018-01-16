from sqlalchemy import (Table, Column, Integer, Numeric, String,
	MetaData, ForeignKey)

from _config import DATABASE_URI, db

DATABASE = "diviapp.db"

metadata = MetaData()
stops = Table('stops', metadata,
	Column('stop_id', Integer(), primary_key=True),
	Column('stop_ref', String(100)),
	Column('stop_name', String(100), index=True),
	Column('stop_lat', String(100)),
	Column('stop_lon', String(100))
)

lines = Table('lines', metadata,
	Column('line_id', Integer(), primary_key=True),
	Column('line_ref', String(100)),
	Column('line_name', String(100)),
	Column('line_dest', String(100)),
	Column('line_way', String(1))
)
is_part_of = Table('is_part_of', metadata,
	Column('stop_id', ForeignKey("stops.stop_id"), primary_key=True),
	Column('line_id', ForeignKey("lines.line_id"), primary_key=True),
	Column('stop_ref', String(50))
)

metadata.create_all(db)
