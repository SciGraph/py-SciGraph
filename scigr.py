#!/usr/bin/env python3

__author__ = 'nlw'

import argparse
import logging
import unittest

from scigraph.SciGraph import SciGraph
from scigraph.renderers.RawRenderer import RawRenderer

renderer = None

def main():

    parser = argparse.ArgumentParser(description='SciGraph'
                                                 'Client lib for SciGraph',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-u', '--url', type=str, required=False,
                        help='A base URL for SciGraph')
    parser.add_argument('-t', '--to', type=str, default='raw', required=False,
                        help='Renderer')


    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')
    
    # SUBCOMMAND
    parser_n = subparsers.add_parser('n', help='neighbors')
    parser_n.add_argument('-d', '--depth', type=int, help='number of hops')
    parser_n.set_defaults(function=neighbors)
    parser_n.add_argument('ids',nargs='*')

    # SUBCOMMAND
    parser_a = subparsers.add_parser('a', help='autocomplete')
    parser_a.set_defaults(function=autocomplete)
    parser_a.add_argument('terms',nargs='*')

    # SUBCOMMAND
    parser_ann = subparsers.add_parser('ann', help='annotate')
    parser_ann.set_defaults(function=annotate)
    parser_ann.add_argument('content',nargs='*')

    args = parser.parse_args()

    rmap = {
        'raw' : RawRenderer
    }
    renderer_class = rmap[args.to]
    global renderer
    renderer = renderer_class()
    print("R="+str(renderer))


    ## PROCESS GLOBALS

    print(args.url)
    sg = SciGraph(args.url)

    ## PROCESS SUBCOMMAND
    #subcommand = args.subcommand
    func = args.function
    func(sg, args)

    print("--DONE--")

def neighbors(sg, args):
    for id in args.ids:
        g = sg.neighbors(id, {'depth': args.depth})
        renderer.render(g.nodes)

def autocomplete(sg, args):
    t = " ".join(args.terms)
    print("t="+t)
    nodes = sg.autocomplete(t)
    #print(nodes)
    renderer.render(nodes)

def annotate(sg, args):
    t = " ".join(args.content)
    print("t="+t)
    spans = sg.annotate(t)
    print(spans)

def render(obj, args):
    print("R")

if __name__ == "__main__":
    main()
    
