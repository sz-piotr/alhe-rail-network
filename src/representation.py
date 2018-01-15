import datetime
import matplotlib.pyplot as plt
import networkx as nx

def save_chart(path,bests,iterations):
    figure, axes = plt.subplots()
    plt.ylabel('Uzyskany koszt sieci w danej iteracji')
    plt.xlabel('Iteracja')
    plt.plot(range(int(iterations)), bests, linewidth=2.0)
    plt.show()
    plt.savefig(path + "/" + 'chart.png',
                bbox_inches='tight', format='png')


    plt.close(figure)


def get_nodes_with_powerplant(problem, graph):
    nodesWithPowerplant = []
    for i in range(graph.number_of_nodes()):
        if problem.world[i].has_powerplant:
            nodesWithPowerplant.append(i)

    return nodesWithPowerplant


def save_graph(path, problem, graph):

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=600, node_shape='o', node_color='0.75')
    nx.draw_networkx_nodes(graph, pos,nodelist=get_nodes_with_powerplant(problem, graph), node_color='r',node_size=500, alpha=0.8)
    nx.draw_networkx_edges(graph, pos,
                           width=2, edge_color='b')

    plt.axis('off')
    plt.savefig(path +"/" + "last_iteration_best_graph.png", bbox_inches="tight")
    plt.show()
