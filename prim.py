"""use as a module"""
import networkx as nx
import sys

# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph
 
import sys # Library for INT_MAX
 
class Graph3():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print ("Edge \tWeight")
        min_weight = 0
        edges = []
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][parent[i]])
            min_weight += self.graph[i][parent[i]]
            edges.append((parent[i], i))
        print("MST weight:", min_weight)
        print("MST edges:", edges)
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1 # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.printMST(parent)
def into_matrix(nx_G: nx.Graph)->int:
    """
    transforms input from graph generator into
    readable matrix
    input:
    e. g. EdgeDataView([(0, 1, {'weight': 4}),
                        (0, 2, {'weight': 1}),
                        (0, 3, {'weight': 6}),
                        (0, 4, {'weight': 6}),
                        (0, 5, {'weight': 0}),
                        (1, 3, {'weight': 8}),
                        (1, 2, {'weight': 7}),
                        (1, 4, {'weight': 1}),
                        (1, 5, {'weight': 7}),
                        (2, 5, {'weight': 0}),
                        (2, 3, {'weight': 9}),
                        (2, 4, {'weight': 2}),
                        (3, 5, {'weight': 1}),
                        (3, 4, {'weight': 2}),
                        (4, 5, {'weight': 10})])

    """
    #G = list(nx_G.edges(data = True))

    #NODES = nx_G.nodes()
    #V = len(NODES)
    V= 6
    matrix = [[0 for j in range(V)] for i in range(V)]
    
    for x, y, z in nx_G:
        matrix[x][y] = z['weight']
        matrix[y][x] = z['weight']
    return matrix, V
    #for i in range(NODES):

        #for j in range(NODES):


def prim_algo(nx_G: nx.Graph):
    """
    ties everything together
    """
    matrix, V = into_matrix(nx_G)
    g = Graph3(V)
    g.graph = matrix
    g.primMST()
