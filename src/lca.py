class Node:
    #node class made up of constructor
    #and some getters and setters
    def  __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parents = list()
        self.children = list()

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

#graph class
class Graph:

    root = None
    size = 0

    def __init__(self):
        self.vertices = list()
        self.nodes = list()

    def get_node(self, key1):
        if key1 not in self.vertices:
            return None
        for n in self.nodes:
            if n.key == key1:
                return n

    def add_edge(self, key1, key2):
        if key1 not in self.vertices:
            return False
        if key2 not in self.vertices:
            self.vertices.extend([key2])
            n = Node(key2)
            par = self.get_node(key1)
            if par != None:
                n.parents.extend([par])
                par.children.extend([n])
                self.nodes.extend([n])
                return True
            else:
                return False
        else:
            n1 = self.get_node(key1)
            n2 = self.get_node(key2)
            self.nodes.remove(n1)
            self.nodes.remove(n2)
            n1.children.extend([n2])
            n2.parents.extend([n1])
            self.nodes.extend([n1])
            self.nodes.extend([n2])
            return True

    def set_root(self, key):
        self.root = Node(key)
        self.size = 1
        self.vertices.extend([key])
        self.nodes.extend([self.root])

    #insert key into tree, calls private insert method
    def insert(self, key):
        if(self.root is None):
            self.set_root(key)
        else:
            self.__insert(self.root, key)
            self.size+=1

    #private insert recursive method
    def __insert(self, curr, key):
        if (key <= curr.key):
            if(curr.get_left()):
                self.__insert(curr.get_left(), key)
            else:
                curr.left = Node(key)
        elif(key > curr.get_key()):
            if(curr.get_right()):
                self.__insert(curr.get_right(), key)
            else:
                curr.right = Node(key)

    #find key in tree, calls private recursive method
    def find(self, key):
        return self.__find(self.root, key)

    #private recursive find method
    def __find(self, curr, key):
        if(curr is None):
            return False
        elif(key is curr.key):
            return True
        elif(key < curr.key):
            return self.__find(curr.left, key)
        else:
            return self.__find(curr.right, key)

    #print tree depth first, calls privte method
    def print_tree(self, ans):
        if self.size is 0:
            ans = []
        else:
            self.__print_tree(self.root, ans)

    #private print method
    def __print_tree(self, n, ans):

        if n!=None:
            ans += [n.key]

        if n.left!=None:
            self.__print_tree(n.left, ans)

        if n.right!=None:
            self.__print_tree(n.right, ans)

    #find path to node from root, called by findLCA
    def find_path(self, path, k):

        if self.size is 0:
            return False
        else:
            return self.__find_path(self.root, path, k)

    #private find path recursive method
    def __find_path(self, root, path, k):

        #if root is None:
            #return False

        path.append(root.key)

        if root.key == k:
            return True

        if((root.left!=None and self.__find_path(root.left, path, k)) or
           (root.right!=None and self.__find_path(root.right, path, k))):
            return True

        path.pop()
        return False

    #method to find lowest common ancestor
    #of two nodes n1 and n2
    def find_lca(self, n1, n2):

        if self.root is None:
            return -1

        path1 = []
        path2 = []

        if(not self.find_path(path1, n1) or not
           self.find_path(path2, n2)):
            return -1

        i=0
        while(i<len(path1) and i<len(path2)):
            if(path1[i] != path2[i]):
                break
            i+=1

        return path1[i-1]


g = Graph()
g.set_root(1)
g.add_edge(1, 2)
v = g.vertices
print(*v)
