import warnings
import graphalgorithm


class Graph:
    def __init__(self, order, is_directed=False):
        """ Ctor for graph class with the following attributes :
        :param order: Number of node in the graph
        :param is_directed: Boolean to indicate if the graph is directed or not
        """
        self.adjlist = [[] for _ in range(order)]
        self.order = order
        self.is_directed = is_directed

    def addnode(self, adjlist=[]):
        """ Add a node to the graph.
        :param adjlist: (List) The adjency list
        """
        self.order += 1
        self.adjlist.append(adjlist)

    def addedge(self, src, dst):
        """ Add an edge between two nodes.
        :param src: (int) Source of the edge
        :param dst: (int) Destination of the edge
        """
        if src >= self.order or dst >= self.order or src < 0 or dst < 0:
            raise Exception("[ADDEDGE] Invalid src or dst.")
        if dst in self.adjlist[src]:
            raise Exception(f'[ADDEDGE] dst is already in src adjency list ({dst} in {src})')
        if not self.is_directed and src in self.adjlist[dst]:
            raise Exception(f'[ADDEDGE] src is already in dst adjency list ({src} in {dst})')
        self.adjlist[src].append(dst)
        if not self.is_directed and src != dst:
            self.adjlist[dst].append(src)

    def removeedge(self, src, dst):
        """ Remove an edge between two nodes.
        :param src: (int) Source of the edge
        :param dst: (int) Destination of the edge
        :return: (Boolean) True if the edge had been successfully removed, False otherwise
        """
        if src >= self.order or dst >= dst >= self.order or src < 0 or dst < 0:
            raise Exception("[REMOVEEDGE] Invalid src or dst.")
        valid = False
        if dst in self.adjlist[src]:
            self.adjlist[src].remove(dst)
            valid = True
        if not self.is_directed and src in self.adjlist[dst]:
            self.adjlist[dst].remove(src)
        return valid

    def get_connected_components(self):
        """ Get all the connected components
        :return: List[List(int)] All connected components
        """
        if self.is_directed:
            raise Exception("[GET_CONNECTED_COMPONENTS] The actual graph is directed.")
        return graphalgorithm.get_connected_components(self)

    def is_connected(self):
        """ Verify if the graph is connected or not
        :return: (Boolean) True if the graph is connected, else False
        """
        if self.is_directed:
            raise Exception("[IS_CONNECTED] The actual graph is directed.")
        return len(graphalgorithm.get_connected_components(self)) == 1

    def copy(self):
        """ Create a copy of a graph
        :return: Newly created graph
        """
        newG = Graph(self.order, self.is_directed)
        for i in range(self.order):
            for node in self.adjlist[i]:
                newG.addedge(i, node)
        return newG

    def transpose(self):
        """ Transpose the graph
        :return: The transposed graph
        """
        if not self.is_directed:
            warnings.warn("Transpose: This graph is not directed. The graph has not been transposed.")
            return
        G = Graph(self.order, self.is_directed)
        for i in range(self.order):
            for node in self.adjlist[i]:
                G.addedge(node, i)
        return G
