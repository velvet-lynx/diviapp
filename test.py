from scraper import Scraper
from formatter import *
from pprint import pprint


sc = Scraper()

liste = sc.get_stops("tuples")
pprint(liste)
#sc.hydrate_lines()
#liste = sc.get_raw_datas().to_dicts_list()