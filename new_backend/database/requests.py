from sqlalchemy.sql import select
from typing import List, Tuple

def query(dal, request) -> List[Tuple]:
    return dal.connection.execute(request).fetchall()

def get_lines(dal) -> List[Tuple]:
    return query(
        dal, 
        select([dal.lines])
    )

def get_line(dal, id: int = -1) -> List[Tuple]:
    if (id > 0):
        return query(
            dal, 
            select([dal.lines]).where(dal.lines.c.line_id == id)
        )
    else:
        return []

def get_stops(dal) -> List[Tuple]:
    return query(
        dal, 
        select([dal.stops])
    )

def get_stop(dal, id: int = -1) -> List[Tuple]:
    if (id > 0):
        return query(
            dal, 
            select([dal.stops]).where(dal.stops.c.stop_id == id)
        )
    else:
        return []

def get_links(dal) -> List[Tuple]:
    return query(
        dal, 
        select([dal.links])
    )

def get_link(dal, id: int = -1) -> List[Tuple]:
    if (id > 0):
        return query(
            dal, 
            select([dal.links]).where(dal.links.c.link_id == id)
        )
    else:
        return []

def get_stops_of_line(dal, id: int = -1) -> List[Tuple]:
    columns = [dal.links.c.link_id, dal.links.c.stop_id,
        dal.links.c.line_id, dal.stops.c.stop_name, dal.links.c.stop_ref]
    if (id > 0):
        return query(
            dal,
            select(columns).select_from(
                dal.stops.join(dal.links).join(dal.lines)
            ).where(dal.links.c.line_id == id)
        )
    else:
        return []