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
        tree.find_path(path, 4)
        self.assertEqual(path, [1, 5, 2, 4])
        path = []
        tree.find_path(path, 11)
        self.assertEqual(path, [1, 5, 8, 11])

    def test_find_pathEmpty(self):
        tree = lca.BST()
        path = []
        self.assertEqual(tree.find_path(path, 3), False)
        self.assertEqual(path, [])

    def test_printTreeEmpty(self):
        tree = lca.BST()
        ans = []
        tree.print_tree(ans)
        self.assertEqual(ans, [])


    def test_printTreeOneNode(self):
        tree = lca.BST()
        tree.set_root(1)
        ans = []
        tree.print_tree(ans)
        self.assertEqual(ans, [1])


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
        tree.print_tree(ans)
        self.assertEqual(ans, [1, 5, 2, 4, 8, 7, 11])

    def test_findTrue(self):
        tree = lca.BST()
        tree.set_root(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(7)
        tree.insert(11)
        tree.insert(4)
        n = tree.find(7)
        assert n == True
        self.assertEqual(tree.find(2), True)

    def test_findFalse(self):
        tree = lca.BST()
        self.assertEqual(tree.find(1), False)
        tree.set_root(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(7)
        tree.insert(11)
        tree.insert(4)
        self.assertEqual(tree.find(6), False)