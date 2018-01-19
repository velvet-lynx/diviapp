from app_config import db
from helper import Pool, ObjectList, XMLHelper
from models import Line, Stop, Link

import traceback

db.drop_all()
db.create_all()

POOL_SIZE = 10

BASE_URL_LINES = "http://timeo3.keolis.com/relais/217.php?xml=1"
BASE_URL_STOPS = "http://timeo3.keolis.com/relais/217.php?xml=3"

lines = ObjectList()
stops = ObjectList()
links = ObjectList()

lines_keys = ["line_ref","line_name","line_way","line_dest"]
stops_keys = ["stop_name", "stop_ref"]

xml_helper = XMLHelper()

# Create a list of tuples.
# Each tuple is made of n successive elements


def create_line(line):
    """ Create a Line object from a dictionnary """
    return Line(
        line_name=line['line_name'],
        line_dest=line["line_dest"],
        line_way=line["line_way"],
        line_ref=line["line_ref"]
    )

def create_stop(stop):
    """ Create a Stop object from a dictionnary """
    return Stop(
        stop_name=stop['stop_name']
    )

def create_link(stop, line, stop_ref):
    """ Create a Link object from a dictionnary """
    link = Link(
        line_id=line.line_id,
        stop_id=stop.stop_id,
        stop_ref=stop_ref
    )
    return link

def get_lines():
    xml_helper.set_url(BASE_URL_LINES)
    xml_helper.set_xpath("//ligne/*[not(self::couleur)]/text()")
    lines_datas = xml_helper.get_datas(lines_keys)
    for row in lines_datas:
        line = create_line(row)
        lines.add(line)

def get_stops(line):
    xml_helper.set_url(BASE_URL_LINES+"&ligne="+line.line_ref+"&sens="+line.line_way)
    xml_helper.set_xpath("//arret/nom/text()|//refs/text()")
    stops_datas = xml_helper.get_datas(stops_keys)
    for row in stops_datas:
        if not stops.has(row["stop_name"]):
            stop = create_stop(row)
            stops.add(stop)
        else:
            stop = stops.get(row["stop_name"])
        link = create_link(stop, line, row["stop_ref"])
        line.link.append(link)
        stop.link.append(link)
        links.add(link)

"""def get_times(stop):
    name = stop[0]
    refs = stop[1]
    ref = iter(refs.split("|"))
    results = []
    while not results:
        try:
            id = next(ref)
        except StopIteration:
            break
        url = BASE_URL_STOPS+"&refs="+id+"&ran=1"
        results = tuple(get_from_xml(url,"//duree/text()"))
    if len(results):
        return results

def process_stops(stops):
    with Pool(POOL_SIZE) as p:
        results = p.map(get_times, stops)
    return results"""

def main():
    
    get_lines()

    for line in lines.all():
        get_stops(line)

    for line in lines.all():
        db.session.add(line)

    for stop in stops.all():
        db.session.add(stop)

    for link in links.all():
        db.session.add(link)

    db.session.commit()

if __name__ == "__main__":
	main()
