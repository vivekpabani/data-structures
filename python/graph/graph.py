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
        :param graph_dict (str, list): dictionary in form of (node, list_of_nodes)
               where list_of_nodes have all nodes adjacent to the key node.
        """

        if graph_dict is None:
            graph_dict = dict()

        self.__graph_dict = graph_dict 

    def vertices(self):
        """
        Find the vertices of the graph.
        :return (list): the vertices of the graph
        """

        return self.__graph_dict.keys()

    def edges(self):
        """
        Find the edges of the graph by calling the generate_edges functions.  
        :return (list): list of sets, where each set is a pairs of node of an edge.
        """

        return self.__generate_edges()

    def __generate_edges(self):
        """
        Generate the edges of the graph by going through the graph_dict.
        Edges are represented as sets with one (a loop back to the vertex) 
        or two with one (a loop back to the vertex) or two vertices. 
        :return (list): list of sets, where each set is an edge - two nodes of an edge. 

        edges = list() 

        for vertex in self.__graph_dict.keys():
            for neighbour in self.__graph_dict[vertex]:
                # if the reverse edge does not exist already
                # then add the current one. 
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})

        return edges

    def __str__(self):
        """
        String representation of the graph.
        to be used by print method.
        :return (string): graph data as string.
        """

        result = "vertices:\n"
        for vertex in self.__graph_dict.keys():
            result = result + str(vertex) + " "

        result = result + "\n\nEdges:\n"
        for edge in self.__generate_edges():
            result = result + str(edge) + " "

        return result
