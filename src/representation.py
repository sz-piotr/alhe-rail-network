import datetime
import matplotlib.pyplot as plt
import networkx as nx

def save_chart(name, bests, iterations):
    figure, axes = plt.subplots()
    plt.ylabel('Uzyskany koszt sieci w danej iteracji')
    plt.xlabel('Iteracja')
    plt.plot(range(int(iterations)), bests, linewidth=2.0)
    plt.savefig(name, bbox_inches='tight')
    plt.show()


def get_nodes_with_powerplant(problem, graph):
    nodesWithPowerplant = []
    for i in range(graph.number_of_nodes()):
        if problem.world[i].has_powerplant:
            nodesWithPowerplant.append(i)

    return nodesWithPowerplant


def save_graph(name, problem, graph):
    pos = [[city.x, city.y] for city in problem.world]
    powerplants = get_nodes_with_powerplant(problem, graph)

    nx.draw_networkx_nodes(graph, pos, node_size=40, node_color='0')
    nx.draw_networkx_nodes(graph, pos, nodelist=powerplants, node_size=100, node_color='0')
    nx.draw_networkx_nodes(graph, pos, nodelist=powerplants, node_color='1',node_size=40, alpha=1)

    nx.draw_networkx_edges(graph, pos, width=2, edge_color='b')

    plt.axis('off')
    plt.savefig(name, bbox_inches="tight")
    plt.clf()

    # plt.show()
