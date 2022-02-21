from graph_generation import gnp_random_connected_graph
import networkx as nx
from tqdm import tqdm
import time
import matplotlib.pyplot as plt
from prum import prim_algorithm
from crascal import kruskal_algorithm


nx_prim_seconds = 0
our_prim_seconds = 0
nx_kruskal_seconds = 0
our_kruskal_seconds = 0
our_prim = []
nx_prim = []
nx_kruskal = []
our_kruskal = []
NUMBER_OF_ITERATIONS = 100
nodes = [10, 20, 30, 50, 100, 200, 500]
fig, ax = plt.subplots()

for n in nodes:
    for i in tqdm(range(NUMBER_OF_ITERATIONS)):
        G = gnp_random_connected_graph(n, 1)

        start = time.time()
        nx.minimum_spanning_tree(G, algorithm='prim')
        end = time.time()
        nx_prim_seconds += end - start

        start = time.time()
        prim_algorithm(G)
        end = time.time()
        our_prim_seconds += end - start

        start = time.time()
        nx.minimum_spanning_tree(G, algorithm='kruskal')
        end = time.time()
        nx_kruskal_seconds += end - start

        start = time.time()
        kruskal_algorithm(G)
        end = time.time()
        our_kruskal_seconds += end - start
    
    nx_prim.append(nx_prim_seconds/NUMBER_OF_ITERATIONS)
    our_prim.append(our_prim_seconds/NUMBER_OF_ITERATIONS)
    nx_kruskal.append(nx_kruskal_seconds/NUMBER_OF_ITERATIONS)
    our_kruskal.append(nx_kruskal_seconds/NUMBER_OF_ITERATIONS)

ax.plot(nodes, nx_prim, label='NetworkX Prim')
ax.plot(nodes, our_prim, label='Prim Implementation')
ax.plot(nodes, nx_kruskal, label='NetworkX Kruskal')
ax.plot(nodes, our_kruskal, label='Kruskal Implementation')
ax.legend()
plt.title('MST Algorithms')
plt.xlabel('Nodes')
plt.ylabel('Time')
plt.show()