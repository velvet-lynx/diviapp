import sys
sys.path.append("../")
from multiprocessing import Pool
import new_backend.helpers.xml as xml
import new_backend.helpers.format as format
from new_backend.database.mongo import db
from pprint import pprint

POOL_SIZE = 10

BASE_URL_LINES = "http://timeo3.keolis.com/relais/217.php?xml=1"

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

def fetch_lines():
    return xml.get(BASE_URL_LINES)

def fetch_line(line):
    ref = line['line_ref']
    way = line['line_way']
    return xml.get(BASE_URL_LINES+"&ligne="+ref+"&sens="+way)

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

def format_line(line):
    return dict(
        line,
        **{
            'line_color' : format.decimal_to_color_hex(line['line_color']),
            'line_stops' : [ format_stop(stop) for stop in line['line_stops']]
        }
    )

def get_lines():
    return xml.extract(
        xml.query("//ligne/*", fetch_lines()),
        line_matching_dict
    )


def main():
    print("Erasing previous database ...")
    db.lines.drop()

    print("Fetching lines ...")
    lines = get_lines()

    print("Fetching stops ...")
    with Pool(POOL_SIZE) as p:
        new_lines = p.map(get_stops, lines)

    print("Formating ...")
    with Pool(POOL_SIZE) as p:
        updated_lines = p.map(format_line, new_lines)

    print("Filling up database ...")
    db.lines.insert_many(updated_lines)

    print("Done.")

if __name__ == "__main__":
	main()
