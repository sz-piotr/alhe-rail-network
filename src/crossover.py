import random
import networkx as nx

def crossover(graph1, graph2):
    g = nx.Graph()
    g.add_edges_from(graph1.edges)
    g.add_edges_from(graph2.edges)

    for (u, v) in g.edges:
        g.edges[u, v]['weight'] = random.uniform(0,10)

    return nx.minimum_spanning_tree(g)

