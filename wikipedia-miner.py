#!/usr/bin/env python3

__author__ = 'nlw'

import argparse
import logging
import unittest
import re

from scigraph.api.SciGraph import SciGraph
from scigraph.renderers.TabRenderer import *
from scigraph.renderers.RawRenderer import *
from scigraph.renderers.EntityAnnotationTabRenderer import *
import wikipedia

renderer = EntityAnnotationTabRenderer()

def main():

    parser = argparse.ArgumentParser(description='SciGraph-wikiparser'
                                                 'Wikipedia section parser',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-u', '--url', type=str, default="http://scigraph-ontology-dev.monarchinitiative.org/scigraph/",
                        help='A base URL for SciGraph')
    parser.add_argument('-t', '--to', type=str, required=False,
                        help='Renderer')
    parser.add_argument('-p', '--page', type=str, required=True,
                        help='Page')

    args = parser.parse_args()

    sg = SciGraph(args.url)
    
    parse_wikipage(sg, args.page)


def parse_wikipage(sg, n):
    page = wikipedia.page(n)
    print("#TITLE: " + page.title)
    sentences = page.content.split("\n")
    h2 = 'Main'
    h3 = ''
    for sentence in sentences:
        if (sentence == ""):
            continue
        m = re.match("=== (.*) ===", sentence)
        if m:
            h3 = m.group(1)
            sentence = h3
        else:
            m = re.match("== (.*) ==", sentence)
            if m:
                h2 = m.group(1)
                sentence = h2

        print("#HEADING: " + h2 + " . " +h3)

        rs = sg.annotate(sentence)
        print("#TEXT: \"" + sentence + "\"")
        print("#SPANS:")
        for span in rs.spans:
            vals = [str(x) for x in [page.title,h2,h3,span.start, span.end, span.token.id, ",".join(span.token.terms), span.text]]
            print("\t".join(vals))

            

if __name__ == "__main__":
    main()
    
