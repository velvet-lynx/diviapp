import multiprocessing
import multiprocessing.pool
from lxml import etree
import urllib.request

class NoDaemonProcess(multiprocessing.Process):
    """ Modified version of multiprocessing process
        with daemon parameter set to false"""
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

class Pool(multiprocessing.pool.Pool):
    """ Modified version of multiprocessing Pool allowing
        the creation of children pools of workers """
    Process = NoDaemonProcess

class ObjectList:
    def __init__(self):
        self.object_list = []

    def all(self):
        return self.object_list

    def get(self, name):
        object_list = iter(self.object_list)
        found = False
        obj = None
        while not found:
            try:
                temp = next(object_list)
                if name.lower() == str(temp).lower():
                    obj = temp
                    found = True
            except StopIteration:
                found = True
        return obj

    def has(self, obj):
        return self.get(str(obj)) is not None

    def add(self, obj):
        if not self.has(obj):
            self.object_list.append(obj)
    
    def delete(self, name):
        self.object_list.remove(self.get(name))
    
    def get_names(self):
        return [str(obj) for obj in self.object_list]

class XMLHelper:
    
    def __init__(self, url=None, xpath=None):
        self.url = url
        self.xpath = xpath
    
    def get_xml(self):
        root = None
        if self.url:
            result = urllib.request.urlopen(self.url)
            try:
                root = etree.fromstring(result.read())
            except etree.XMLSyntaxError:
                print("Not only XML in response from :\n    "+self.url)
        return root
    
    def create_dictionnary(self, keys, datas):
        return { key: datas[i] for i, key in enumerate(keys)}

    def format_datas(self, keys, datas):
        size = len(datas)
        if size:
            if size > 1:
                return [
                    self.create_dictionnary(keys, row)
                    for row in datas
                ]
            else:
                return self.create_dictionnary(keys, datas)

    def get_datas(self, keys=None):
        root = self.get_xml()
        if len(root) and len(self.xpath):
            datas = root.xpath(self.xpath)
            if datas:
                if keys:
                    rows = self.grouped(datas, len(keys))
                    return self.format_datas(keys, rows)
                else:
                    return datas
            else:
                return None
        else:
            return None

    def grouped(self, datas, amount):
	    return list(zip(*[iter(datas)]*amount))
    
    def set_url(self, url):
        self.url = url
    
    def set_xpath(self, xpath):
        self.xpath = xpath

