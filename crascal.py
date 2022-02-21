def kruskal_algorithm(graph):
    nodes = graph[0]
    edges = graph[1]
    edges = sorted(edges, key=lambda x: x[2])
    components = [set(node) for node in list(map(lambda x: [x],nodes))]
    result = []
    first_comp = 0
    second_comp = 1
    for edge in edges:
        first_comp = set()
        second_comp = set()
        for component in components:
            if edge[0] in component:
                first_comp = component
            elif edge[1] in component:
                second_comp = component
        if first_comp != second_comp and first_comp!=set() and second_comp!=set():
            first_comp.update(second_comp)
            components.remove(second_comp)
            result.append(edge)
        if len(result) == len(nodes) - 1:
            break
    return result


from graph_generation import gnp_random_connected_graph
import networkx as nx

G = gnp_random_connected_graph(10, 1)
edges = list(map(lambda x: (x[0], x[1], x[2]['weight']), G.edges().data()))
nodes = list(G.nodes())
graph = (nodes, edges)
