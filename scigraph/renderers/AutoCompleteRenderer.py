__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

# TODO: different implementations for different types

class AutoCompleteRenderer(Renderer):
    """
    straight up
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, results):
        for r in results:
            concept = r['concept']
            print(concept['curie'] + " ! " + " ** ".join(concept['labels']) + " #Category:" + ",".join(concept['categories']))
