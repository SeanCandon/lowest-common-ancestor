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
        ans = tree.find_lca(8, 4)
        self.assertEqual(ans, 5)
        ans = tree.find_lca(11, 7)
        self.assertEqual(ans, 8)


    def test_emptyGraph(self):
        tree = lca.BST()
        self.assertEqual((tree.find_lca(2, 1)), -1)


    def test_graphOneNode(self):
        tree = lca.BST()
        tree.set_root(5)
        self.assertEqual((tree.find_lca(5, 5)),
                         tree.root.key)

    def test_findPath(self):
        tree = lca.BST()
        tree.set_root(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(7)
        tree.insert(11)
        tree.insert(4)
        path = []
        tree.find_path(tree.root, path, 4)
        self.assertEqual(path, [1, 5, 2, 4])
        path = []
        tree.find_path(tree.root, path, 11)
        self.assertEqual(path, [1, 5, 8, 11])


    def test_print_tree(self):
        tree = lca.BST()
        tree.set_root(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(7)
        tree.insert(11)
        tree.insert(4)
        ans = []
        tree.print_tree(tree.root, ans)
        self.assertEqual(ans, [1, 5, 2, 4, 8, 7, 11])
