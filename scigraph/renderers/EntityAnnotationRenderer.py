__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

# TODO: different implementations for different types

class EntityAnnotationRenderer(Renderer):
    """
    straight up
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, resultset):
        for s in resultset.spans:
            token = s.token
            print('{0: <3} {1: <3} {2: <16} {3: <25} "{4}"'.format(s.start, s.end, token.id, ",".join(token.terms), s.text))
