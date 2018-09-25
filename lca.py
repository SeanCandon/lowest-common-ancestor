class Node:

    def  __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

class BST:

    def ___init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

    def insert(self, key):
        if(self.root is None):
            self.set_root(key)
        else:
            self.insert_node(self.root, key)


    def insert_node(self, curr, key):
        if (key <= curr.key):
            if(curr.left):
                self.insert_node(curr.left, key)
            else:
                curr.left = Node(key)
        elif(key > curr.key):
            if(curr.right):
                self.insert_node(curr.right, key)
            else:
                curr.right = Node(key)

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, curr, key):
        if(curr is None):
            return False
        elif(key is curr.key):
            return True
        elif(val < curr.key):
            return self.find_node(curr.left, key)
        else:
            return self.find_node(curr.right, key)

    def print_tree(self, n, ans):

        if n!=None:
            ans += [n.key]

        if n.left!=None:
            print_tree(n.left, ans)

        if n.right!=None:
            print_tree(n.right, ans)


    def find_path(self, root, path, k):

        if root is None:
            return False

        path.append(root.key)

        if root.key == k:
            return True

        if((root.left!=None and self.find_path(root.left, path, k)) or
           (root.right!=None and self.find_path(root.right, path, k))):
            return True

        path.pop()
        return False

    def find_lca(self, root, n1, n2):

        path1 = []
        path2 = []

        if(not self.find_path(root, path1, n1) or not
           self.find_path(root, path2, n2)):
            return -1

        i=0
        while(i<len(path1) and i<len(path2)):
            if(path1[i] != path2[i]):
                break
            i+=1

        return path1[i-1]



# tree = BST()
# tree.set_root(1)
# tree.insert(5)
# tree.insert(2)
# tree.insert(8)
# tree.insert(7)
# tree.insert(11)
# tree.insert(4)
