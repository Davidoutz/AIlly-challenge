# -----------------------------------------------------------
# This class represents a directed graph implemented through
# an adjacency list. Choices and remarks are provided in a
# separated document (README file).
#
# The tests are (in order):
#   1. Constructing the directed graph using a list of vertices
#      and a list of edges as an input
#   2. Computing the number of edge
#   3. Computing the number of vertices
#   4. Compute the in degrees per vertex
#   5. Compute the out degrees per vertex
#   6. Serialize to a file (json)
#   7. Desearialize from a file
#
# 2022 / David Beauverd
# Ailly coding challenge
# -----------------------------------------------------------
import json
import os


class DirectedGraph:
    FILE_NAME = "adjacency_list.json"

    def __init__(self, vertices, edges):
        self.adjacency_list = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []
        for source, destination in edges:
            self.adjacency_list[source].append(destination)

    def print(self):
        print("Printing adjacency list: ", self.adjacency_list)

    def compute_vertices(self):
        count = len(self.adjacency_list)
        print("the graph has", count, "vertices.")

    def compute_edges(self):
        count = 0
        for key, value in self.adjacency_list.items():
            count += len(value)
        print("the graph has", count, "edges.")

    def compute_in_degree(self):
        print("Compute in degrees per vertex:")
        count_track = {}
        for key, value in self.adjacency_list.items():
            if key not in count_track:  # In case a vertex is not in the dict values, we still need to track its count to 0
                count_track[key] = 0
            for vertex in value:
                if vertex in count_track:
                    count_track[vertex] += 1
                else:
                    count_track[vertex] = 1
        for key, value in count_track.items():
            print(key, "->", value)

    def compute_out_degree(self):
        print("Compute out degrees per vertex:")
        for key, value in self.adjacency_list.items():
            print(key, "->", len(value))

    def serialize(self):
        with open(DirectedGraph.FILE_NAME, "w") as file:
            json.dump(self.adjacency_list, file)

    def deserialize(self):
        # Sanity check if file does not exist
        if not (os.path.isfile(DirectedGraph.FILE_NAME) and os.access(DirectedGraph.FILE_NAME, os.R_OK)):
            with open(DirectedGraph.FILE_NAME, "w") as file:
                file.write(json.dumps({}))

        with open("adjacency_list.json", "r") as file:
            self.adjacency_list = json.load(file)
        self.print()

    def add_edge(self, edge):
        v, u = edge
        if u in self.adjacency_list[v]:  # ignore if edge already exists in adjacency list
            return
        self.adjacency_list[v].append(u)


if __name__ == '__main__':
    vertices = ["a", "b", "c", "d"]  # sample vertices input
    edges = [("a", "b"), ("a", "c"), ("c", "d")]  # sample edges input
    graph = DirectedGraph(vertices, edges)
    graph.compute_edges()
    graph.compute_vertices()
    graph.compute_in_degree()
    graph.compute_out_degree()
    graph.serialize()
    graph.deserialize()

    # Extra tests after adding a new edge
    # print("##########################")
    # print("# Adding new edge (b, d) #")
    # print("##########################")
    # graph.add_edge(("b", "d"))
    # graph.compute_edges()
    # graph.compute_vertices()
    # graph.compute_in_degree()
    # graph.compute_out_degree()
    # graph.print()
