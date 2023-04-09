import graphalgorithm

class Graph:
    def __init__(self, order, is_directed = False):
        self.adjlist = [[] for _ in range(order)]
        self.order = order
        self.is_directed = is_directed

    def addnode(self, node):
        if node < self.order:
            raise Exception("[ADDEDGE] This node is already in the graph")
        self.order += 1
        self.adjlist.append([])

    def addedge(self, src, dst):
        if src == dst:
            return
        if src >= self.order or dst >= self.order or src < 0 or dst < 0:
            raise Exception("[ADDEDGE] Invalid src or dst.")
        if dst in self.adjlist[src]:
            raise Exception(f'[ADDEDGE] dst is already in src adjency list ({dst} in {src})')
        if not self.is_directed and src in self.adjlist[dst]:
            raise Exception(f'[ADDEDGE] src is already in dst adjency list ({src} in {dst})')
        self.adjlist[src].append(dst)
        if not self.is_directed:
            self.adjlist[dst].append(src)

    def removeedge(self, src, dst):
        if src == dst:
            return
        if src >= self.order or dst >= dst >= self.order or src < 0 or dst < 0:
            raise Exception("[REMOVEEDGE] Invalid src or dst.")
        valid = False
        if dst in self.adjlist[src]:
            self.adjlist[src].remove(dst)
            valid = True
        if not self.is_directed and src in self.adjlist[dst]:
            self.adjlist[dst].remove(src)
        return valid

    def get_connected_components_numbers(self):
        return len(graphalgorithm.get_connected_components(self))

    def get_connected_components(self):
        return graphalgorithm.get_connected_components(self)

    def is_connected(self):
        return len(graphalgorithm.get_connected_components(self)) == 1