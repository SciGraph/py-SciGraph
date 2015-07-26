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
        edges = obj.edges
        for edge in edges:
            print(edge)

