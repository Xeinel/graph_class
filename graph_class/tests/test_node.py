import unittest

from graph_class import Graph

class TestAddNode(unittest.TestCase):
    def test_addnode_valid(self):
        G = Graph.Graph(3)
        G.addnode(4)
        res = G.order == 4 and len(G.adjlist) == 4
        self.assertTrue(res, "[ADDNODE] Invalid node adding.")

    def test_addnode_invalid_negative(self):
        G = Graph.Graph(3)
        self.assertRaises(Exception, G.addnode, -1, "[ADDNODE] Invalid node adding (negative).")

    def test_addnode_invalid(self):
        G = Graph.Graph(3)
        self.assertRaises(Exception, G.addnode, 1, "[ADDNODE] Invalid node adding (error).")