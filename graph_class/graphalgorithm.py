# Nombre de composantes connexes d'un graphe

def __dfs(G, visited, node, actual_comp):
    """ Create the list of node in the current connected components
    :param G: (Graph) The provided graph
    :param visited: List(Boolean) List of visited node
    :param node: (int) The actual node to visit
    :param actual_comp: List(int) List of node in the current connected components
    """
    visited[node] = True
    for n in G.adjlist[node]:
        if not visited[n]:
            actual_comp.append(n)
            __dfs(G, visited, n, actual_comp)


def get_connected_components(G):
    """ Get connected components in a graph
    :param G: (Graph) The provided graph
    :return: List[List(int)] List of connected components
    """
    if G.order == 0:
        return [[]]
    visited = [False] * G.order
    components = []
    for i in range (G.order):
        actual_comp = []
        if not visited[i]:
            __dfs(G, visited, i, actual_comp)
            components.append(actual_comp)
    return components
