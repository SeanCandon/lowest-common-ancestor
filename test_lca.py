import unittest
import lca

class TestLCA(unittest.TestCase):

    def test_simpleFindLCA(self):
        tree = lca.BST()
        tree.set_root(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(7)
        tree.insert(11)
        tree.insert(4)
        ans = tree.find_lca(tree.root, 8, 4)
        self.assertEqual(ans, 5)
        ans = tree.find_lca(tree.root, 11, 7)
        self.assertEqual(ans, 8)


    # def test_emptyGraph(self):
        # root = None
        # self.assertEqual((lca.findLCA(root, 2, 1)), -1)
#
    # def test_graphOneNode(self):
        # root = lca.Node(1)
        # self.assertEqual((lca.findLCA(root, 1, 1)), 1)
#
    # def test_PrintTree(self):
        # root = lca.Node(1)
        # root.left = lca.Node(2)
        # root.right = lca.Node(3)
        # root.left.left = lca.Node(4)
        # root.left.right = lca.Node(5)
        # root.right.left = lca.Node(6)
        # root.right.right = lca.Node(7)
        # ans = []
        # lca.printTree(root, ans)
