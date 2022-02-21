import random
import networkx as nx
import matplotlib.pyplot as plt
import prim
from itertools import combinations, groupby
import time
from tqdm import tqdm

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))
    
    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)
                
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,10)
                
    if draw: 
        plt.figure(figsize=(10,6))
        nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    return G

G = gnp_random_connected_graph(6, 1, True)



def execute_algorhythm(num_of_nodes: int, completeness: int):
    time_taken = 0
    NUM_OF_ITERATIONS = 1000
    for i in tqdm(range(NUM_OF_ITERATIONS)):

        # note that we should not measure time of graph creation
        G = gnp_random_connected_graph(num_of_nodes, completeness, False)

        start = time.time()
        prim.prim_tree(G)
        end = time.time()

        time_taken += end - start

    return time_taken / NUM_OF_ITERATIONS

def do_tests():
    test_nodes_list = [10, 20, 50, 100]
    time_taken = []
    for i in test_nodes_list:
        time_taken.append(execute_algorhythm(i, 0.1))
    print(time_taken)

if __name__ == '__main__':

    do_tests()