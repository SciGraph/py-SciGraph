__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

class GraphTreeRenderer(Renderer):
    """
    denormalized tree
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, g):
        self.graph = g
        nodes = g.nodes
        edges = g.edges
        roots = g.get_root_nodes()
        for n in roots:
            self.write_tree(n.id)

    def write_tree(self, nid, relations=[], relation='*root*', depth=0):
        indent = "   " * depth
        print(indent, end="")
        print(relation + " ", end="")
        n = self.graph.get_node(nid)
        self.write_node(n)
        for e in self.graph.get_incoming_edges(nid):
            self.write_tree(e.subject, relations, '^-[' + e.predicate+']', depth+1)

    def write_node(self, n):
        print(n.id + " ! " + str(n.label))
