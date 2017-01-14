#!/usr/bin/env python

"""
A simple graph class with some of the essential 
functionalities of graphs.

Implemented functionalities:
- get the list of vertices.
- get the list of edges.
- add a vertex.
- add an edge. 

"""

__author__ = "vivek"



class Graph(object):

    def __init__(self, graph_dict = None):
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

        return list(self.__graph_dict.keys())

    def edges(self):
        """
        Find the edges of the graph by calling the generate_edges functions.  
        :return (list): list of sets, where each set is a pairs of node of an edge.
        """

        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        Add the given vertex to the graph, if it doesn't already exists.
        :param vertex(str): the vertex to be added
        """

        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        Add the given edge to the graph.
        If any of the vertices don't exist, initialize them and add the edge.
        :param edge(tuple, set or list): the edge to be added.
        """

        edge = set(edge)

        vertex1 = edge.pop()
        if edge:
            # not a self loop. have two nodes.
            vertex2 = edge.pop()
        else:
            # self loop. 
            vertex2 = vertex1

        # add the vertex2 to vertex1's neighbours.
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

        # add the vertex1 to vertex2's neighbours.
        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex2] = [vertex1]

    def __generate_edges(self):
        """
        Generate the edges of the graph by going through the graph_dict.
        Edges are represented as sets with one (a loop back to the vertex) 
        or two with one (a loop back to the vertex) or two vertices. 
        :return (list): list of sets, where each set is an edge - two nodes of an edge. 
        """

        edges = list() 

        for vertex in self.__graph_dict:
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
        for vertex in self.__graph_dict:
            result = result + str(vertex) + " "

        result = result + "\n\nEdges:\n"
        for edge in self.__generate_edges():
            result = result + str(edge) + " "

        return result


