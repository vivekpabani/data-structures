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

    def find_path(self, start_vertex, end_vertex, path = None):
        """
        Find a path between given start and end vertex. 
        Return None if no path exists.
        :param start_vertex (str): the start vertex.
        :param end_vertex (str): the end vertex.
        :param path (list): the path from source to destination. None by default.

        :return (list): path as a list.
        """ 

        # initialize path list for the first iteration/call.
        if path is None:
            path = list()

        # invalid vertices.
        if start_vertex not in self.__graph_dict or end_vertex not in self.__graph_dict:
            return None

        # add the current vertex to path, and see if we reached the destination.
        path.append(start_vertex)

        if start_vertex == end_vertex:
            return path

        # otherwise for each vertex in the neighbour list of current vertex
        # if it is not already on path, consider it for next call.
        # call find_path recursively with current vertex as the start vertex
        # and check if that leads us to the end_vertex.
        # when that happens, the path list will be returned by the call, and recursion terminates.

        for vertex in self.__graph_dict[start_vertex]:
            if vertex not in path:
                updated_path = self.find_path(vertex, end_vertex, path)

                if updated_path:
                    return updated_path

        return None
