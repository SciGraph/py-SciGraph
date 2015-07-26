__author__ = 'cjm'

import logging
import requests
from subprocess import call

from scigraph.renderers.Renderer import Renderer
from graphviz import Digraph


# TODO: different implementations for different types

def safe(s):
    return s.replace(":","")

def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

class GraphVizRenderer(Renderer):
    """
    gv
    """

    g = Digraph('G', format='png')

    styles = {
        'graph': {
            'label': 'A Fancy Graph',
            'fontsize': '16',
            'fontcolor': 'white',
            'bgcolor': '#333333',
            'rankdir': 'BT',
        },
        'nodes': {
            'fontname': 'Helvetica',
            'shape': 'hexagon',
            'fontcolor': 'white',
            'color': 'white',
            ##'style': 'filled',
            'fillcolor': '#006699',
        },
        'edges': {
            'style': 'dashed',
            'color': 'white',
            'arrowhead': 'open',
            'fontname': 'Courier',
            'fontsize': '12',
            'fontcolor': 'white',
        }        
    }

    cat_attr_map = {
        'disease' : {
            'style' : 'filled'
        }
    }


    def __init__(self):
        Renderer.__init__(self)

    def render(self, obj):
        ## ASSUME BBOP GRAPH
        apply_styles(self.g, self.styles)
        nodes = obj.nodes
        edges = obj.edges
        for node in nodes:
            self.add_node(node)
        for edge in edges:
            self.add_edge(edge)
        filename = self.g.render(filename='img/g')
        call(['open', 'img/g.png'])
        #print(filename)


    def add_node(self, node):
        node_attrs = {
            'label': self.format_label(node.label)
        }
        for c in node.meta.category_list:
            if c in self.cat_attr_map:
                attrs = self.cat_attr_map[c]
                for a in attrs:
                    node_attrs[a] = attrs[a]
        gn = self.g.node(safe(node.id), **node_attrs)

    def add_edge(self, edge):
        edge_attrs = {
            'label': edge.predicate
        }
        self.g.edge(safe(edge.subject), safe(edge.target), **edge_attrs)

    def format_label(self, label):
        if label is None:
            return None
        return "\n".join(label.split(" "))

