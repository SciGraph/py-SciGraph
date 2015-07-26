__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

# TODO: different implementations for different types

class TabRenderer(Renderer):
    """
    straight up
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, obj):
        ## ASSUME BBOP GRAPH
        nodes = obj.nodes
        edges = obj.edges
        for node in nodes:
            print(str(node) +" C:"+str(node.meta.category_list))
        for edge in edges:
            print(str(edge))

