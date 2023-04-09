import unittest
import graphalgorithm
import Graph


class TestGraph(unittest.TestCase):

    def test_init_graph_directed(self):
        G = Graph.Graph(3)
        res = G.order == 3 and len(G.adjlist) == 3 and not G.is_directed
        self.assertTrue(res, "[INIT] Invalid non directed graph init.")

    def test_init_graph_directed(self):
        G = Graph.Graph(3, True)
        res = G.order == 3 and len(G.adjlist) == 3 and G.is_directed
        self.assertTrue(res, "[INIT] Invalid directed graph init.")

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

    def test_getconnectedcomponents(self):
        G = Graph.Graph(8)
        G.addedge(0, 5)
        G.addedge(0, 6)
        G.addedge(1, 3)
        G.addedge(1, 4)
        G.addedge(2, 3)
        G.addedge(2, 4)
        G.addedge(5, 6)
        self.assertEqual(G.get_connected_components_numbers(), 3)

class TestGraphAlgorithm(unittest.TestCase):

    def test_emptygraph_connected(self):
        G = Graph.Graph(0)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[]])

    def test_oneconnectedcomponents(self):
        G = Graph.Graph(4)
        G.addedge(0, 3)
        G.addedge(1, 3)
        G.addedge(2, 3)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[3,1,2]])

    def test_twoconnectedcomponents(self):
        G = Graph.Graph(7)
        G.addedge(0, 5)
        G.addedge(0, 6)
        G.addedge(1, 3)
        G.addedge(1, 4)
        G.addedge(2, 3)
        G.addedge(2, 4)
        G.addedge(5, 6)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[5,6], [3,2,4]])

    def test_threeconnectedcomponents(self):
        G = Graph.Graph(8)
        G.addedge(0, 5)
        G.addedge(0, 6)
        G.addedge(1, 3)
        G.addedge(1, 4)
        G.addedge(2, 3)
        G.addedge(2, 4)
        G.addedge(5, 6)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[5,6], [3,2,4], []])


if __name__ == '__main__':
    unittest.main()
