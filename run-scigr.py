#!/usr/bin/env python3

__author__ = 'nlw'

import argparse
import logging
import unittest

from scigraph.api.SciGraph import SciGraph
from scigraph.renderers.RawRenderer import RawRenderer
from scigraph.renderers.TabRenderer import *
from scigraph.renderers.GraphVizRenderer import *
from scigraph.renderers.AutoCompleteRenderer import *
from scigraph.renderers.SearchResultsRenderer import *
from scigraph.renderers.EntityAnnotationRenderer import *
from scigraph.renderers.GraphTreeRenderer import *

renderer = None

def main():

    parser = argparse.ArgumentParser(description='SciGraph'
                                                 'Client lib for SciGraph',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-u', '--url', type=str, required=False,
                        help='A base URL for SciGraph')
    parser.add_argument('-t', '--to', type=str, required=False,
                        help='Renderer')


    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')
    
    # SUBCOMMAND
    parser_n = subparsers.add_parser('n', help='neighbors')
    parser_n.add_argument('-d', '--depth', type=int, help='number of hops')
    parser_n.set_defaults(function=neighbors)
    parser_n.add_argument('ids',nargs='*')

    # SUBCOMMAND
    parser_n = subparsers.add_parser('g', help='graph')
    parser_n.set_defaults(function=graph)
    parser_n.add_argument('ids',nargs='*')

    # SUBCOMMAND
    parser_a = subparsers.add_parser('a', help='autocomplete')
    parser_a.set_defaults(function=autocomplete)
    parser_a.add_argument('terms',nargs='*')

    # SUBCOMMAND
    parser_s = subparsers.add_parser('s', help='search')
    parser_s.set_defaults(function=search)
    parser_s.add_argument('terms',nargs='*')

    # SUBCOMMAND
    parser_ann = subparsers.add_parser('ann', help='annotate')
    parser_ann.set_defaults(function=annotate)
    parser_ann.add_argument('content',nargs='*')

    args = parser.parse_args()

    renderer_class = RawRenderer
    if (args.subcommand == 'a'):
        renderer_class = AutoCompleteRenderer
    if (args.subcommand == 'ann'):
        renderer_class = EntityAnnotationRenderer
    if (args.subcommand == 's'):
        renderer_class = SearchResultsRenderer
    rmap = {
        'raw' : RawRenderer,
        'png' : GraphVizRenderer,
        'tree' : GraphTreeRenderer,
        'tsv' : TabRenderer
    }
    if args.to is not None:
        renderer_class = rmap[args.to]
    global renderer
    renderer = renderer_class()


    ## PROCESS GLOBALS

    sg = SciGraph(args.url)

    ## PROCESS SUBCOMMAND
    #subcommand = args.subcommand
    func = args.function
    func(sg, args)


def neighbors(sg, args):
    for id in args.ids:
        g = sg.neighbors(id, {'depth': args.depth})
        renderer.render(g)

def graph(sg, args):
    for id in args.ids:
        g = sg.graph(id, {})
        renderer.render(g)

def autocomplete(sg, args):
    t = " ".join(args.terms)
    nodes = sg.autocomplete(t)
    renderer.render(nodes)

def search(sg, args):
    t = " ".join(args.terms)
    concepts = sg.search(t)
    renderer.render(concepts)

def annotate(sg, args):
    t = " ".join(args.content)
    spans = sg.annotate(t)
    renderer.render(spans)


if __name__ == "__main__":
    main()
    
