#!/usr/bin/env python

"""
A simple graph class with some of the essential 
functionalities of graphs.

"""

__author__ = "vivek"



class Graph(object):

    def __init__(self, graph_dict = None)
        """
        Initialize the graph object with graph_dict.
        :param graph_dict: dictionary in form of (node, list_of_nodes)
                       where list_of_nodes have all nodes
                       adjacent to the key node. 
        """

        if graph_dict is None:
            graph_dict = dict()

        self.__graph_dict = graph_dict 
