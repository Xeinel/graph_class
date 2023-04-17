import unittest

import Graph


class TestTransposeGraph(unittest.TestCase):
    def test_transpose_directed_graph(self):
        G = Graph.Graph(5, True)
        G.addedge(0, 1)  # 1 -> 0
        G.addedge(0, 3)  # 3 -> 0
        G.addedge(0, 4)  # 4 -> 0
        G.addedge(2, 0)  # 0 -> 2
        G.addedge(3, 2)  # 2 -> 3
        G.addedge(4, 3)  # 3 -> 4
        G.addedge(4, 1)  # 1 -> 4
        newG = G.transpose()
        self.assertTrue(newG.adjlist[0] == [2] and newG.adjlist[1] == [0, 4] and newG.adjlist[2] == [3]
                        and newG.adjlist[3] == [0, 4] and newG.adjlist[4] == [0])

    def test_transpose_undirected_graph(self):
        G = Graph.Graph(3)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        self.assertTrue(G.transpose() is None)
