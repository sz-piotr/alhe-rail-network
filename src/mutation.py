import random
import networkx as nx

def mutation(graph, del_orig=True):

    edges = list(graph.edges)
    nonedges = list(nx.non_edges(graph))

    chosen_edge = random.choice(edges)
    chosen_nonedge = random.choice([x for x in nonedges if chosen_edge[0] == x[0]])


    if del_orig:
        # delete chosen edge
        graph.remove_edge(*chosen_edge)
        # add new edge
    graph.add_edge(*chosen_nonedge)
    return graph

def mutation_simple(graph):
    nonedge = random.choice(list(nx.non_edges(graph)))
    graph.add_edge(*nonedge)
    return nx.minimum_spanning_tree(graph)
