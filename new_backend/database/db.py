from sqlalchemy import (Table, Column, Integer, String,
                        MetaData, ForeignKey, create_engine)

class DataAccessLayer:
    """ Allows the database to be accessed from anywhere"""
    conn_string = None
    engine = None
    connection = None
    metadata = MetaData()

    stops = Table('stops', metadata,
        Column('stop_id', Integer(), primary_key=True),
        Column('stop_name', String(50), index=True),
        Column('stop_lat', String(50)),
        Column('stop_lon', String(50))
    )

    lines = Table('lines', metadata,
        Column('line_id', Integer(), primary_key=True),
        Column('line_ref', String(20)),
        Column('line_name', String(50)),
        Column('line_dest', String(50)),
        Column('line_way', String(1))
    )

    links = Table('links', metadata,
        Column('link_id', Integer(), primary_key=True),
        Column('stop_id', ForeignKey("stops.stop_id")),
        Column('line_id', ForeignKey("lines.line_id")),
        Column('stop_ref', String(50))
    )

    def db_init(self, conn_string):
        """ Initialize database """
        self.engine = create_engine(conn_string or self.conn_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

    def db_shutdown(self):
        """ Set connection to None """
        self.connection = None

dal = DataAccessLayer()
