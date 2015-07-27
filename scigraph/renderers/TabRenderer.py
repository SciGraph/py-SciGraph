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

    def render(self, g):
        ## ASSUME BBOP GRAPH
        nodes = g.nodes
        edges = g.edges
        #for node in nodes:
        #    print(str(node) +" C:"+str(node.meta.category_list))
        for e in edges:
            print('{0: <14} {1: <24} -[{2: <12}]-> {3: <14} {4: <24}'.format(e.subject, str(g.get_label(e.subject)), e.predicate, e.target, str(g.get_label(e.target))))
            #print(str(edge))

