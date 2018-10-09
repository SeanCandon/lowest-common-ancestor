import unittest
import lca

class TestLCA(unittest.TestCase):

    def test_addEdge(self):
        g = lca.Graph()
        g.set_root(1)
        g.add_edge(1, 2)
        n = g.get_node(1)
        self.assertEqual(len(n.children), 1)
        self.assertEqual(len(n.parents), 0)
        n = g.get_node(2)
        self.assertEqual(len(n.children), 0)
        self.assertEqual(len(n.parents), 1)
        g.add_edge(1, 3)
        n = g.get_node(1)
        self.assertEqual(len(n.children), 2)
        self.assertEqual(len(n.parents), 0)
        self.assertEqual(n.children[0].key, 2)
        self.assertEqual(n.children[1].key, 3)
        g.add_edge(2, 3)
        n = g.get_node(3)
        self.assertEqual(len(n.parents), 2)
        self.assertEqual(n.parents[0].key, 1)
        self.assertEqual(n.parents[1].key, 2)

    def test_addEdgeWithCycles(self):
        g = lca.Graph()
        g.set_root(1)
        b = g.add_edge(1, 2)
        self.assertEqual(b, True)
        b = g.add_edge(1, 3)
        self.assertEqual(b, True)
        b = g.add_edge(2, 3)
        self.assertEqual(b, True)
        b = g.add_edge(3, 1)
        self.assertEqual(b, False)
        b = g.add_edge(2, 4)
        self.assertEqual(b, True)
        self.assertEqual((g.get_node(2)).children[0].key, 3)
        self.assertEqual((g.get_node(2)).children[1].key, 4)
        self.assertEqual(len(g.get_node(2).children), 2)
        b = g.add_edge(4, 1)
        self.assertEqual(b, False)
