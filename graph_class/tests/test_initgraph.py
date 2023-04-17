import unittest

from graph_class import Graph


class TestInitGraph(unittest.TestCase):

    def test_init_graph_non_directed(self):
        G = Graph.Graph(3)
        res = G.order == 3 and len(G.adjlist) == 3 and not G.is_directed
        self.assertTrue(res, "[INIT] Invalid non directed graph init.")

    def test_init_graph_directed(self):
        G = Graph.Graph(3, True)
        res = G.order == 3 and len(G.adjlist) == 3 and G.is_directed
        self.assertTrue(res, "[INIT] Invalid directed graph init.")