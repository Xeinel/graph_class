# Nombre de composantes connexes d'un graphe

def __dfs(G, visited, node, actual_comp):
    visited[node] = True
    for n in G.adjlist[node]:
        if not visited[n]:
            actual_comp.append(n)
            __dfs(G, visited, n, actual_comp)


def get_connected_components(G):
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
