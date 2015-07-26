__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

class RawRenderer(Renderer):
    """
    straight up
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, obj):
        print(obj)

