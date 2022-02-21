"""use as a module"""
import networkx as nx


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
    G = list(nx_G.edges(data = True))
    NODES = nx_G.nodes()
    V = len(NODES)
    matrix = [[0 for j in range(V)] for i in range(V)]
    for x, y, z in G:
        matrix[x][y] = z['weight'] + 1
        matrix[y][x] = z['weight'] + 1
    return matrix, V


def prim_tree(G: nx.Graph) -> tuple:
    """
    :param nx.Graph G: graph to use algo on

    """
    G, V = into_matrix(G)
    INF = 9999999
    selected = [0]*V
    no_edge = 0
    selected[0] = True
    edges = []
    weight = 0
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):  
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        edges.append((x,y))
        weight += G[x][y] - 1
        selected[y] = True
        no_edge += 1
    return edges, weight
