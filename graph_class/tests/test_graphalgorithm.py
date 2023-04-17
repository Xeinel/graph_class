import unittest

from graph_class import Graph
from graph_class import graphalgorithm

class TestGraphAlgorithm(unittest.TestCase):
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

    def test_emptygraph_connected(self):
        G = Graph.Graph(0)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[]])

    def test_oneconnectedcomponents(self):
        G = Graph.Graph(4)
        G.addedge(0, 3)
        G.addedge(1, 3)
        G.addedge(2, 3)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[3, 1, 2]])

    def test_twoconnectedcomponents(self):
        G = Graph.Graph(7)
        G.addedge(0, 5)
        G.addedge(0, 6)
        G.addedge(1, 3)
        G.addedge(1, 4)
        G.addedge(2, 3)
        G.addedge(2, 4)
        G.addedge(5, 6)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[5, 6], [3, 2, 4]])

    def test_threeconnectedcomponents(self):
        G = Graph.Graph(8)
        G.addedge(0, 5)
        G.addedge(0, 6)
        G.addedge(1, 3)
        G.addedge(1, 4)
        G.addedge(2, 3)
        G.addedge(2, 4)
        G.addedge(5, 6)
        self.assertEqual(graphalgorithm.get_connected_components(G), [[5, 6], [3, 2, 4], []])