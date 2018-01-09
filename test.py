import urllib.request
from lxml import etree
from pprint import pprint

BASE_URL = "http://timeo3.keolis.com/relais/217.php?xml=1"

# Create a list of tuples.
# Each tuple is made of n successive elements
def grouped(iterable, n):
	return list(zip(*[iter(iterable)]*n))

def get_xml_from_url(url):
	result = urllib.request.urlopen(url)
	try:
		return etree.fromstring(result.read())
	except etree.XMLSyntaxError:
		print("Not only XML in response from :\n    "+url)

def get_from_xml(url, xpath):
	root = get_xml_from_url(url)
	return root.xpath(xpath)



lines = get_from_xml(
		BASE_URL,
		"//ligne/*[self::code or self::sens]/text()"
	)
lines = grouped(lines, 2)

# For every line_code ...
for line, way in lines:
	print(line+" "+way+":")
	url = BASE_URL+"&ligne="+line+"&sens="+way

	stops = get_from_xml(
			url,
			"//arret/nom/text() | //refs/text()"
		)
	stops = grouped(stops, 2)

	new_url = "http://timeo3.keolis.com/relais/217.php?xml=3"
	for name, refs in stops:
		ref = iter(refs.split("|"))
		results = None
		while not results:
			try:
				id = next(ref)
			except StopIteration:
				break
			url = new_url+"&refs="+id+"&ran=1"
			results = get_from_xml(url,"//duree/text()")
		if len(results) == 2:
			print("    "+name+":"+" ->"+results[0]+" ->"+results[1])
		else:
			print(results)