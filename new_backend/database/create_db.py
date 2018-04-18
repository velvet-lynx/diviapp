import sys
sys.path.append("../")
from multiprocessing import Pool
import new_backend.helpers.xml as xml
import re
from pprint import pprint

POOL_SIZE = 10

BASE_URL_LINES = "http://timeo3.keolis.com/relais/217.php?xml=1"
BASE_URL_STOPS = "http://timeo3.keolis.com/relais/217.php?xml=3"

line_matching_dict = {
    "nom" : "line_name",
    "code" : "line_ref",
    "sens" : "line_way",
    "couleur" : "line_color",
    "vers" : "line_dest"
}
stop_matching_dict = {
    "nom" : "stop_name",
    "refs" : "stop_refs"
}

# Create a list of tuples.
# Each tuple is made of n successive elements

def fetch_lines():
    return xml.get(BASE_URL_LINES)

def fetch_line(line):
    ref = line['line_ref']
    way = line['line_way']
    return xml.get(BASE_URL_LINES+"&ligne="+ref+"&sens="+way)

# def get_lines():
#     xml_helper.set_url(BASE_URL_LINES)
#     xml_helper.set_xpath("//ligne/*[not(self::couleur)]/text()")
#     lines_datas = xml_helper.get_datas(lines_keys)
#     for row in lines_datas:
#         line = create_line(row)
#         lines.add(line)
#     return lines

def get_stops(line):
    return dict(
        line,
        **{ "line_stops" :
            xml.extract(
                xml.query("//arret/nom|//refs", fetch_line(line)),
                stop_matching_dict
            )
        }
    )

def format_stop(stop):
    return {
        "stop_name" : stop['stop_name'],
        "stop_refs" : stop['stop_refs'].split('|')
    }

def format_stops(line):
    return dict(
        line,
        **{
            'line_stops' : [ format_stop(stop) for stop in line['line_stops']]
        }
    )

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

def get_lines():
    return xml.extract(
        xml.query("//ligne/*", fetch_lines()),
        line_matching_dict
    )


def main():
    stops = []
    lines = xml.extract(
        xml.query("//ligne/*", fetch_lines()),
        line_matching_dict
    )
    with Pool(POOL_SIZE) as p:
        new_lines = p.map(get_stops, lines)

    with Pool(POOL_SIZE) as p:
        updated_lines = p.map(format_stops, new_lines)

    pprint(updated_lines[0])

if __name__ == "__main__":
	main()
