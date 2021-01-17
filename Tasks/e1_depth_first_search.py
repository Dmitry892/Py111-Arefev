from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    q = [start_node]
    a = []
    while q:
        c = q.pop()
        a.append(c)
        for node in g.neighbors(c):
            if node not in a and node not in q:
                q.append(node)
    return a
