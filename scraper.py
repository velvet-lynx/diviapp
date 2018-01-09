# scraper.py

import requests
from bs4 import BeautifulSoup
from formatter import DictList

class Scraper:

	def __init__(self, url=None, headers=dict(), params=None):
		if not url:
			url = "https://www.divia.fr/"
		if not headers:
			headers = { 'Content-Type': 'application/x-www-form-encoded; charset=UTF-9',
				'X-Requested-With': 'XMLHttpRequest' }
		self.params = params
		self.url = url
		self.headers = headers
		self.datas = DictList()


	def set_url(self, url):
		self.url = url

	def get_url(self):
		return self.url

	def set_headers(self, headers):
		self.headers = headers

	def get_headers(self):
		return self.headers

	def set_params(self, params):
		self.params = params

	def get_params(self):
		return self.params

	def create_soup(self):
		return BeautifulSoup(self.request(), "lxml")

	def request(self):
		"""Execute an HTTP request and return the response body"""
		request = requests.get(self.url, params=self.params, headers=self.headers)
		return request.text

	def find_all(self, tag=None, attrs=None):
		self.soup = self.create_soup()
		return self.soup.find_all(tag, attrs=attrs)

	def create_line(self, line_datas):
		line_id = int(line_datas['value'])
		destination = line_datas.text.strip().strip("> ")
		line_name = line_datas['data-class'].replace(" perturb","")
		return {
			"line_id": line_id,
			"line_name": line_name,
			"destination": destination
		}

	def create_stop(self, stop_datas):
		title = stop_datas.text.strip().split(' - ')
		stop_name = " - ".join(title[:-1])
		stop_totem = int(title[-1])
		return {
			"stop_totem": stop_totem, 
			"stop_name": stop_name
		}

	def create_datas(self):
		self.set_url("https://www.divia.fr/")
		options = self.find_all('option', {'data-class':True})
		self.set_url("https://www.divia.fr/totem/resultat")
		for line_datas in options:
			line = self.create_line(line_datas)
			self.set_params({"ligne": line["line_id"]})
			titles = self.find_all(None, {'class':'title'})
			for stop_datas in titles:
				stop = self.create_stop(stop_datas)
				self.datas.add(dict(stop, **line))

	def get_raw_datas(self):
		return self.datas

	def get_datas(self, keys=None, mode=None):
		if self.datas.is_empty():
			self.create_datas()
		if mode == "tuples":
			return self.datas.to_tuples_set(keys)
		else:
			return self.datas.to_sub_list(keys)

	def get_lines(self, mode=None):
		keys = ["line_id","line_name","destination"]
		return self.get_datas(keys, mode)

	def get_stops(self, mode=None):
		keys = ["stop_totem","stop_name"]
		return self.get_datas(keys, mode)

	