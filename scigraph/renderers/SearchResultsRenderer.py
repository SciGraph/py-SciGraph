__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

# TODO: different implementations for different types

class SearchResultsRenderer(Renderer):
    """
    straight up
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, concepts):
        for c in concepts:
            print('{0: <16} {1: <60} #{2: <24}'.format(c.id, ",".join(c.labels), ",".join(c.categories)))
