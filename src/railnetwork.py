import networkx as nx

class RailNetwork:

    def __init__(self):
        self.graph = nx.Graph()

    def score(self, powerplants):
        return 0

    def crossover(self, other):
        full_child = nx.Graph()
        full_child.add_edges_from(self.graph)
        full_child.add_edges_from(other.graph)
        mst = nx.minimum_spanning_edges(full_child, 'weight')

        child = nx.Graph()
        child.add_edges_from(list(mst))

        return child

    def mutate(self)
        mutant = nx.Graph()
        mutant.add_edges_from(self.graph)
        return mutant
