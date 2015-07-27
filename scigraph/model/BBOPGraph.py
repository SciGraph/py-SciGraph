__author__ = 'cjm'

import logging
import requests

# TODO: consider an external model

class BBOPGraph:

    """
    foo
    """

    nodemap = {}

    def __init__(self, obj={}):
        self.nodes = []
        self.edges = []
        self.add_json_graph(obj)
        return

    def add_json_graph(self, obj={}):
        #print(obj)
        for n in obj['nodes']:
            self.add_node(Node(n))
        for e in obj['edges']:
            self.add_edge(Edge(e))
        #print("EDGES="+str(self.edges))

    def add_node(self, n) :
        self.nodemap[n.id] = n
        self.nodes.append(n)

    def add_edge(self, e) :
        self.edges.append(e)

    def merge(self,g):
        for n in g.nodes:
            self.add_node(n)
        for e in g.edges:
            self.add_edge(e)

    def get_node(self, id) :
        return self.nodemap[id]

    def get_label(self, id) :
        return self.nodemap[id].label

    def get_root_nodes(self, relations=[]):
        roots = []
        for n in self.nodes:
            if (len(self.get_outgoing_edges(n.id, relations)) == 0):
                roots.append(n)
        return roots

    def get_leaf_nodes(self, relations=[]):
        roots = []
        for n in self.nodes:
            if (len(self.get_incoming_edges(n.id, relations)) == 0):
                roots.append(n)
        return roots

    def get_outgoing_edges(self, nid, relations=[]):
        el = []
        for e in self.edges:
            if (e.subject == nid):
                if (len(relations) == 0 or e.predicate in relations):
                    el.append(e)
        return el

    def get_incoming_edges(self, nid, relations=[]):
        el = []
        for e in self.edges:
            if (e.target == nid):
                if (len(relations) == 0 or e.predicate in relations):
                    el.append(e)
        return el

class Node:
    def __init__(self, obj={}):    
        self.id = obj['id']
        self.label = obj['lbl']
        self.meta = Meta(obj['meta'])
    def __str__(self):
        return self.id+' "'+str(self.label)+'"'

class Edge:
    def __init__(self, obj={}):    
        self.subject = obj['sub']
        self.predicate = obj['pred']
        self.target = obj['obj']
    
    def __str__(self):
        return self.subject +"-["+self.predicate+"]->"+self.target


class Meta:
    def __init__(self, obj={}):    
        self.type_list = obj['types']
        self.category_list = []
        if 'category' in obj:
            self.category_list = obj['category']
        self.pmap = obj
    
