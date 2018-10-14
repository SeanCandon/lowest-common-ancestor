class Node:
    #node class made up of constructor
    #and some getters and setters
    def  __init__(self, key):
        self.key = key
        self.parents = list()
        self.children = list()
        self.depth = None

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

    def insert(self, key1, key2):

        if key1 not in self.vertices:
            return False
        if key2 not in self.vertices:
            self.vertices.extend([key2])
            n = Node(key2)
            par = self.get_node(key1)
            n.parents.extend([par])
            par.children.extend([n])
            self.nodes.extend([n])
            n.depth = par.depth+1
            return True
        else:
            n1 = self.get_node(key1)
            n2 = self.get_node(key2)
            self.nodes.remove(n1)
            self.nodes.remove(n2)
            n1.children.extend([n2])
            n2.parents.extend([n1])
            self.nodes.extend([n1])
            self.nodes.extend([n2])
            b = self.find_path(key1, key1)
            if b == True:
                n1.children.remove(n2)
                n2.parents.remove(n1)
                return False
            else:
                if n2.depth > (n1.depth+1):
                    self.nodes.remove(n2)
                    n2.depth = n1.depth+1
                    self.nodes.extend([n2])
                return True

    def set_root(self, key):
        self.root = Node(key)
        self.size = 1
        self.vertices.extend([key])
        self.nodes.extend([self.root])
        self.root.depth = 0

    #find path to node with key k2 from node with key k1
    #used to check for cycles
    #calls private recursive method __find_path
    def find_path(self, k1, k2):

        n1 = self.get_node(k1)
        n2 = self.get_node(k2)

        visited = list()

        visited.extend([k2])
        return self.__find_path(k2, n1, visited)

    #private find path recursive method
    def __find_path(self, k, node, v):

        if node.key not in v:
            v.extend([node.key])

        children = node.children

        found = False

        for n in children:
            if n.key == k:
                return True
            elif n.key not in v:
                found = self.__find_path(k, n, v)
                if found is True:
                    return True

        return False

    #method to find lowest common ancestor
    #of two nodes with keys k1 and k2
    def find_lca(self, k1, k2):

        if self.root is None:
            return None

        n1 = self.get_node(k1)
        n2 = self.get_node(k2)

        if n1 is None or n2 is None:
            return None

        n1Anc = list()
        n2Anc = list()

        self.__find_ancestors(n1, n1, n1Anc)
        self.__find_ancestors(n2, n2, n2Anc)

        deepest  = 0
        lca  = self.root.key

        for x in n1Anc:
            for y in n2Anc:
                if x == y and (self.get_node(x)).depth>deepest:
                    deepest = (self.get_node(x)).depth
                    lca = x

        return lca

    #finds ancestors of node orig
    def __find_ancestors(self, n, orig, anc):

        par = n.parents

        if len(par) == 0:
            return True

        for p in par:
            if p.key not in anc and p.key != orig.key:
                anc.extend([p.key])
                self.__find_ancestors(p, orig, anc)

        return True
