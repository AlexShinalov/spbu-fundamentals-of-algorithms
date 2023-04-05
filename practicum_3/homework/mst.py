from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST

    dist_dict = {node: float("inf") for node in G.nodes()}
    dist_dict[start_node] = 0

    while rest_set:
        current_node = min(rest_set, key=dist_dict.get)

        rest_set.remove(current_node)
        mst_set.add(current_node)

        if current_node != start_node:
            parent_node = min(G.neighbors(current_node), key=lambda node: G[current_node][node]["weight"])
            mst_edges.add((parent_node, current_node))

        for neighbor in G.neighbors(current_node):
            if neighbor in rest_set:
                dist = G[current_node][neighbor]["weight"]
                if dist < dist_dict[neighbor]:
                    dist_dict[neighbor] = dist

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("./graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
