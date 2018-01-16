import requests
import sqlite3
from bs4 import BeautifulSoup

url = "https://www.divia.fr/totem/reloader"
headers={
	"Content-Type": "application/x-www-form-encoded; charset=UTF-9",
	"X-Requested-With": "XMLHttpRequest"
}

with sqlite3.connect('diviapp.db') as conn:
	c = conn.cursor()
	c.execute(
		"""
			SELECT stop.stop_totem, line.line_id, line_name, destination, stop_name
			FROM stop
			join line_stop on stop.stop_totem = line_stop.stop_totem
			join line on line_stop.line_id = line.line_id
			order by line.line_id
		"""
	)
	results = c.fetchall()

datas = []

for arret in results:
	params = {
		"arret": arret[0],
		"ligne": arret[1]
	}
	response = requests.get(url, params=params, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	tags = soup.find_all(attrs={"data-minut":True})
	values = [tag.text.strip() for tag in tags]
	

	if values:
		print(arret[2]+" > "+arret[3]+" -- "+arret[4]+\
			" : "+values[0]+"mn")
	else:
		print(arret[2]+" > "+arret[3]+" -- "+arret[4]+" : unknown")
	