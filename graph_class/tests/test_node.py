import unittest

import Graph


class TestAddNode(unittest.TestCase):
    def test_addnode_valid_without_adjlist(self):
        G = Graph.Graph(3)
        G.addnode()
        self.assertTrue(G.order == 4 and len(G.adjlist) == 4, "[ADDNODE] Invalid node adding.")

    def test_addnode_valid_with_adjlist(self):
        G = Graph.Graph(3)
        G.addnode([0,1,2])
        self.assertTrue(G.order == 4 and len(G.adjlist) == 4 and G.adjlist[3] == [0,1,2],
                        "[ADDNODE] Invalid node adding.")
