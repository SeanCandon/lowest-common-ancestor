import unittest
import lca

class TestLCA(unittest.TestCase):

    def test_simpleFindLCA(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)
        ans = lca.findLCA(root, 5, 4)
        self.assertEqual(ans, 2)
        ans2 = lca.findLCA(root, 5, 7)
        self.assertEqual(ans2, 1)

    def test_emptyGraph(self):
        root = None
        self.assertEqual((lca.findLCA(root, 2, 1)), -1)

    def test_graphOneNode(self):
        root = lca.Node(1)
        self.assertEqual((lca.findLCA(root, 1, 1)), 1)

    def test_PrintDepthFirst(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)
        ans = []
        lca.printDepthFirst(root, ans)
        self.assertEqual(ans, [1, 2, 4, 5, 3, 6, 7])
