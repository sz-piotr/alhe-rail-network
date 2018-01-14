import random
import networkx as nx

def generate_single_tree(n_cities):
    g = nx.Graph()
    for p in range(n_cities):
        for r in range(p + 1, n_cities):
            g.add_edge(p, r, weight=random.uniform(0,10))
    return nx.minimum_spanning_tree(g)

def generate_population(n_cities, population_size):
    return [
        generate_single_tree(n_cities)
        for i in range(population_size)
    ]
