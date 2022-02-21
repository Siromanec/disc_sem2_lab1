def prim_algorithm(graph):
    nodes = graph[0]
    edges = graph[1]
    result = []
    connected = {nodes[0]}
    while len(connected) != len(nodes):
        closest = []
        for edge in edges:
            if (edge[0] in connected and edge[1] not in connected) or \
                (edge[1] in connected and edge[0] not in connected):
                closest.append(edge)
        closest_edge = sorted(closest,key = lambda x: x[2])[0]
        result.append(closest_edge)
        connected.add(closest_edge[0])
        connected.add(closest_edge[1])
    return result


from graph_generation import gnp_random_connected_graph
G = gnp_random_connected_graph(10, 1)
edges = list(map(lambda x: (x[0], x[1], x[2]['weight']), G.edges().data()))
nodes = list(G.nodes())
graph = (nodes, edges)
