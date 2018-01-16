import urllib.request
from lxml import etree
from helper import Pool
from pprint import pprint
from sqlalchemy import insert
from models import Line, Stop, Link, db

import traceback

POOL_SIZE = 10

BASE_URL_LINES = "http://timeo3.keolis.com/relais/217.php?xml=1"
BASE_URL_STOPS = "http://timeo3.keolis.com/relais/217.php?xml=3"

lines = []
stops = []
links = []
lines_columns = ["line_ref","line_name","line_way","line_dest"]
stops_columns = ["stop_name", "stop_ref"]

# Create a list of tuples.
# Each tuple is made of n successive elements
def grouped(iterable, n):
	return list(zip(*[iter(iterable)]*n))

def create_line(line):
    return Line(
        line_name=line['line_name'],
        line_dest=line["line_dest"],
        line_way=line["line_way"],
        line_ref=line["line_ref"]
    )

def create_stop(stop):
    return Stop(
        stop_name=stop['stop_name']
    )

def create_link(stop, line, stop_ref):
    link = Link(
        line_id=line.line_id,
        stop_id=stop.stop_id,
        stop_ref=stop_ref
    )
    return link


def create_dic_list(tup_list, keys):
	list = []
	for tup in tup_list:
		dic = {}
		for key in keys:
			dic[key] = tup[keys.index(key)]
		list.append(dic)
	return list

def get_xml_from_url(url):
	result = urllib.request.urlopen(url)
	try:
		return etree.fromstring(result.read())
	except etree.XMLSyntaxError:
		print("Not only XML in response from :\n    "+url)

def get_from_xml(url, xpath):
	root = get_xml_from_url(url)
	return root.xpath(xpath)

def get_lines():
    url = BASE_URL_LINES
    xpath = "//ligne/*[not(self::couleur)]/text()"
    lines_datas = get_from_xml(url,xpath)
    lines_dics = create_dic_list(grouped(lines_datas, 4), lines_columns)
    for row in lines_dics:
        line = create_line(row)
        lines.append(line)

def add_to_db(*args):
    for obj in args:
        db.session.add(obj)

def get_stops(line):
    url = BASE_URL_LINES+"&ligne="+line.line_ref+"&sens="+line.line_way
    xpath = "//arret/nom/text() | //refs/text()"
    stops_datas = get_from_xml(url, xpath)
    stops_dics = create_dic_list(grouped(stops_datas, 2), stops_columns)
    for row in stops_dics:
        try:
            stop = create_stop(row)
            stops.append(stop)
            link = create_link(stop, line, row["stop_ref"])
            line.link.append(link)
            stop.link.append(link)
            add_to_db(stop, line, link)
        except AttributeError as e:
            traceback.print_tb(e.__traceback__)
    db.session.commit()
        

def get_times(stop):
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
	return results

def main():

    get_lines()

    with Pool(POOL_SIZE) as stop_pool:
        stop_pool.map(get_stops, lines)
    
    

"""
	stops_datas = create_dic_list

	with Pool(POOL_SIZE) as p:
		results = p.map(process_stops, stops_list)
"""


if __name__ == "__main__":
	main()
