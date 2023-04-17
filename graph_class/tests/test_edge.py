import unittest

import Graph


class TestAddEdge(unittest.TestCase):
    def test_addedge_invalidsrc_one(self):
        G = Graph.Graph(3)
        self.assertRaises(Exception, G.addedge, -1, 2, "[ADDEDGE] Invalid edge adding (negative src).")

    def test_addedge_invalidsrc_two(self):
        G = Graph.Graph(3)
        self.assertRaises(Exception, G.addedge, 8, 2, "[ADDEDGE] Invalid edge adding (Too big src).")

    def test_addedge_invaliddst_one(self):
        G = Graph.Graph(3)
        self.assertRaises(Exception, G.addedge, 1, 78, "[ADDEDGE] Invalid edge adding (Too big dst).")

    def test_addedge_invaliddst_two(self):
        G = Graph.Graph(3)
        self.assertRaises(Exception, G.addedge, 1, 78, "[ADDEDGE] Invalid edge adding (negative dst).")

    def test_addedge_valid_directed(self):
        G = Graph.Graph(3, True)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        G.addedge(1, 0)
        self.assertTrue(len(G.adjlist[0]) == 1 and len(G.adjlist[1]) == 2 and len(G.adjlist[2]) == 1
                        , "[ADDEDGE] Invalid adjencylist")

    def test_addedge_invalid_directed(self):
        G = Graph.Graph(3, True)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 0)
        self.assertRaises(Exception, G.addedge, 1, 3, "[ADDEDGE] Invalid edge adding (dst == self.order)")

    def test_addedge_valid_non_directed(self):
        G = Graph.Graph(3)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        self.assertTrue(len(G.adjlist[0]) == 2 and len(G.adjlist[1]) == 2 and len(G.adjlist[2]) == 2
                        , "[ADDEDGE] Invalid adjencylist")

    def test_addedge_valid_non_directed_srcequalsdst(self):
        G = Graph.Graph(3)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        G.addedge(1, 1)
        self.assertTrue(len(G.adjlist[0]) == 2 and len(G.adjlist[1]) == 3 and len(G.adjlist[2]) == 2
                        , "[ADDEDGE] Invalid adjencylist")

    def test_addedge_valid_directed_srcequalsdst(self):
        G = Graph.Graph(3)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        G.addedge(1, 1)
        G.removeedge(1, 1)
        self.assertTrue(len(G.adjlist[0]) == 2 and len(G.adjlist[1]) == 2 and len(G.adjlist[2]) == 2
                        , "[ADDEDGE] Invalid adjencylist")


class TestRemoveEdge(unittest.TestCase):
    def test_removeedge_valid_non_directed(self):
        G = Graph.Graph(3)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        self.assertTrue(G.removeedge(1, 2) and len(G.adjlist[1]) == 1 and len(G.adjlist[2]) == 1
                        and len(G.adjlist[0]) == 2)

    def test_removeedge_valid_directed(self):
        G = Graph.Graph(3, True)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        self.assertTrue(G.removeedge(1, 2) and len(G.adjlist[1]) == 0 and len(G.adjlist[2]) == 1
                        and len(G.adjlist[0]) == 1)

    def test_removeedge_invalid_directed(self):
        G = Graph.Graph(3, True)
        G.addedge(0, 1)
        G.addedge(2, 0)
        G.addedge(1, 2)
        self.assertTrue(not G.removeedge(2, 1) and len(G.adjlist[1]) == 1 and len(G.adjlist[2]) == 1
                        and len(G.adjlist[0]) == 1)
