import queue
from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}
    stack = [node]
    while stack:
        n_node=stack.pop()
        if visited[n_node] == False:
            visited[n_node] = True
            visit(n_node)
            for neighbor in G.neighbors(n_node):
                if visited[neighbor] == False:
                    stack.append(neighbor)




def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}
    stack = [node]

    def dfs(node):
        visited[node] = True
        for neighbor in G.neighbors(node):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    dfs(node)
    a=[]
    while stack:
        n_node = stack.pop()
        a.append(n_node)
    a.pop(-1)
    print(a)


if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("./graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "./graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")
