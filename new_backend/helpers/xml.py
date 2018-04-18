from lxml import etree
import urllib.request as urlreq

def get(url):
    if not len(url):
        raise AttributeError('"url" is an empty string')
    else:
        return etree.fromstring(
            urlreq.urlopen(url).read()
        )

def query(request, root):
    return(root.xpath(request))

def to_dict(node):
    if not len(node):
        return { node.tag : node.text }
    else:
        raise RuntimeError("node is not a leaf of the xml tree")

def to_dicts(node_list):
    return [
        to_dict(node)
        for node in node_list
    ]

def match(dict_list, matching_dict):
    return [
        { matching_dict[key] : value }
        for dic in dict_list
        for key, value in dic.items()
    ]

def group(dict_list, size):
    """ Allow you to group up dictionnaries from a list into a list of bigger dictionnaries,
    usually with a reapeating pattern """
    if len(dict_list):
        return [
            {
                key : value
                for dic in dict_list[:size]
                for key, value in dic.items()
            }
        ] + group(dict_list[size:], size)
    else:
        return dict_list

def extract(node_list, matching_dict):
    return group(
        match(
            to_dicts(node_list), matching_dict
        ), len(matching_dict)
    )
