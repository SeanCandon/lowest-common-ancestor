import unittest
import lca

class TestLCA(unittest.TestCase):

    #tests find lca for basic graph
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
        #tests find lca for non-existent node
        self.assertEqual(tree.find_lca(6, 4), -1)

    #tests lca for empty graph
    def test_emptyGraph(self):
        tree = lca.BST()
        self.assertEqual((tree.find_lca(2, 1)), -1)

    #tests lca for graph of size 1
    def test_graphOneNode(self):
        tree = lca.BST()
        tree.set_root(5)
        self.assertEqual((tree.find_lca(5, 5)),
                         tree.root.key)

    #tests find path
    def test_findPath(self):
        tree = lca.BST()
        tree.insert(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(7)
        tree.insert(11)
        tree.insert(4)
        path = []
        #tests find path to key 4
        tree.find_path(path, 4)
        self.assertEqual(path, [1, 5, 2, 4])
        path = []
        #tests find path to key 11
        tree.find_path(path, 11)
        self.assertEqual(path, [1, 5, 8, 11])
        path = []
        #tests find path to non-existent key
        self.assertEqual(tree.find_path(path, 6), False)

    #tests find path for empty graph, expected false
    def test_find_pathEmpty(self):
        tree = lca.BST()
        path = []
        self.assertEqual(tree.find_path(path, 3), False)
        self.assertEqual(path, [])

    #tests print tree for empty tree
    def test_printTreeEmpty(self):
        tree = lca.BST()
        ans = []
        tree.print_tree(ans)
        self.assertEqual(ans, [])

    #tests print tree for graph of size 1
    def test_printTreeOneNode(self):
        tree = lca.BST()
        tree.set_root(1)
        ans = []
        tree.print_tree(ans)
        self.assertEqual(ans, [1])

    #tests print tree for standard tree of size>1
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

    #tests find for key that is present in tree,
    #should be true
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

    #tests find for key that isn't present in tree,
    #should be false
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
