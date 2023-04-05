from typing import Any

import networkx as nx

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes

    distances = {node: float('inf') for node in G.nodes()}
    distances[source_node] = 0

    visited = {node: False for node in G.nodes()}

    while not all(visited.values()):
        current_node = min((node for node in G.nodes() if not visited[node]), key=distances.get)


        for neighbor in G.neighbors(current_node):
            distance = distances[current_node] + G.edges[current_node, neighbor]['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited[current_node] = True

    for node in G.nodes():
        if node != source_node:
            path = []
            current_node = node
            while current_node != source_node:
                path.append(current_node)
                for neighbor in G.neighbors(current_node):
                    if distances[neighbor] == distances[current_node] - G.edges[current_node, neighbor]['weight']:
                        current_node = neighbor
                        break
            path.append(source_node)
            shortest_paths[node] = list(reversed(path))


    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("./graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
print(shortest_paths)
