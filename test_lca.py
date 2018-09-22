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
