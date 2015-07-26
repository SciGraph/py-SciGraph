__author__ = 'cjm'

import logging
import requests

class BBOPGraph:

    """
    foo
    """

    def __init__(self, obj={}):
        
        self.seed(obj)
        return

    def seed(self, obj={}):
        self.nodes = obj['nodes']
        self.edges = obj['edges']
    
