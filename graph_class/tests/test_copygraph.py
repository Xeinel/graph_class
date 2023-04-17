import unittest
import Graph


class TestCopyGraph(unittest.TestCase):
    def test_copygraph(self):
        G = Graph.Graph(5, True)
        G.addedge(0, 1)
        G.addedge(0, 3)
        G.addedge(0, 4)
        G.addedge(2, 0)
        G.addedge(3, 2)
        G.addedge(4, 3)
        G.addedge(4, 1)
        newG = G.copy()
        self.assertTrue(newG.order == 5 and newG.is_directed and newG.adjlist[0] == [1, 3, 4] and newG.adjlist[1] == []
                        and newG.adjlist[2] == [0] and newG.adjlist[3] == [2] and newG.adjlist[4] == [3, 1])
