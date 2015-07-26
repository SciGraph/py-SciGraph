__author__ = 'cjm'

import logging
import requests

from scigraph.model.BBOPGraph import BBOPGraph

# TODO: modularize into vocab/graph/etc?

class SciGraph:
    """
    foo
    """

    def __init__(self, url=None):
        if url is not None:
            self.url_prefix = url
        else:
            self.url_prefix = "http://geoffrey.crbs.ucsd.edu:9000/scigraph/"
            #self.url_prefix = "http://datagraph.monarchinitiative.org/"
        return

    def neighbors(self, id=None, params={}):
        response = self.get_response("graph/neighbors", id, "json", params)
        return BBOPGraph(response.json())

    def autocomplete(self, term=None):
        response = self.get_response("vocabulary/autocomplete", term)
        return response.json()['list']

    def annotate(self, content=None):
        ## TODO: post not get
        response = self.get_response("annotations/entities", None, "json", {'content':content})
        return response.json()

    def get_response(self, path="", q=None, format=None, payload={}):
        url = self.url_prefix + path;
        if q is not None:
            url += "/" +q;
        if format is not None:
            url = url  + "." + format;
        print(url)
        r = requests.get(url, params=payload)
        return r
