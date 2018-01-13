import random
import networkx as nx

def generate_single_tree(points):

    g = nx.Graph()
    for p in points:
        for r in points:
            if  p != r:
                g.add_edge(p,r,weight=random.uniform(0,10))

    return nx.minimum_spanning_tree(g)

def generate_population(points, number):
    population = []
    for i in range(0,number):
        population.append(generate_single_tree(points))

    return population
