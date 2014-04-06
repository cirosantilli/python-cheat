#!/usr/bin/env python

"""
Graph library.

Previously LANL.

Homepage: <http://networkx.github.io>

Source: <https://github.com/networkx>

Official tutorial: <http://networkx.github.io/documentation/networkx-1.8/tutorial/index.html>

Install:

    sudo pip install networkx
"""

import networkx as nx

if "##dijkstra":

    edge_weights = [
        (0, 2, 1), (1, 1, 2), (1, 3, 1), (1, 4, 2), (2, 1, 7),
        (2, 3, 3), (3, 4, 1), (4, 0, 1), (4, 1, 1)
    ]
    G = nx.DiGraph()
    G.add_edges_from([(x, y, {'weight':z}) for x,y,z in edge_weights])
    assert nx.dijkstra_path(G, 0, 4) == [0, 2, 3, 4]
