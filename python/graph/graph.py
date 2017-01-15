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

    def find_all_paths(self, start_vertex, end_vertex, path = None):
        """
        Find all paths between given start and end vertex. 
        Return None if no path exists.
        :param start_vertex (str): the start vertex.
        :param end_vertex (str): the end vertex.
        :param path (list): the path from source to destination. None by default.

        :return (list): paths as a list of list.
        """ 

        # initialize path list for the first iteration/call.
        if path is None:
            path = list()

        # invalid vertices.
        if start_vertex not in self.__graph_dict or end_vertex not in self.__graph_dict:
            return [] 

        # add the current vertex to path, and see if we reached the destination.
        # if yes, return it in a list.
        
        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return [path]

        # otherwise for each vertex in the neighbour list of current vertex
        # if it is not already on path, consider it for next call.
        # call find_path recursively with current vertex as the start vertex
        # and check if that leads us to the end_vertex.
        # when that happens, the path list will be returned by the call, and recursion terminates.

        all_paths = list()

        for vertex in self.__graph_dict[start_vertex]:
            if vertex not in path:
                updated_paths = self.find_all_paths(vertex, end_vertex, path)
                if updated_paths:
                    for p in updated_paths:
                        all_paths.append(p) 

        return all_paths

    def depth_first_search(self, start_vertex, impl_type = "iter"):
        """
        depth first search calling function based on asked implementation type.
        :param start_vertex (str): the vertex from where to start the search/iteration.
        :param impl_type (str): type of implemention. default value is iterative.  
        """

        if impl_type == "rec":
            return self.depth_first_search_rec(start_vertex)
        else:
            return self.depth_first_search_iter(start_vertex)

    def depth_first_search_iter(self, start_vertex):
        """
        Traverse the graph depth first iteratively starting from given vertex.
        and record all the vertex on the connected component.
        :param start_vertex (str): the vertex from where to start the search/iteration.

        :return (list): list of nodes on the search path. 
        """

        visited = list() 
        # in depth first search, first we mark the current node as visited. 
        # then we add all its neighbours, which we didn't visit before to a list
        # next we pick one of them for next iteration.
        # thus everytime we pick the node from last node's neighbours.
        # so last in first out - for which we use the list as a stack.
        # repeat this until stack has nodes.

        stack = [start_vertex]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.append(vertex)
                not_visited_neighbours = [node for node in self.__graph_dict[vertex] if node not in visited]
                stack.extend(not_visited_neighbours)

        return visited

    def depth_first_search_rec(self, start_vertex, visited = None):
        """
        Traverse the graph depth first recursively starting from given vertex.
        and record all the vertex on the connected component.
        :param start_vertex (str): the vertex from where to start the search/iteration.
        :param visited (list): list of already visited nodes on search path. default value None.

        :return (list): list of nodes on the search path.
        """
        if visited is None:
            visited = list()

        visited.append(start_vertex)

        not_visited_neighbours = [node for node in self.__graph_dict[start_vertex] if node not in visited]

        for next_vertex in not_visited_neighbours:
            self.depth_first_search_rec(next_vertex, visited)
 
        return visited
