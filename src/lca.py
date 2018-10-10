class Node:
    #node class made up of constructor
    #and some getters and setters
    def  __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parents = list()
        self.children = list()
        self.depth = None

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
                n.depth = par.depth+1
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
    def find_path(self, k1, k2):

        print("finding path from %d to %d" % (k1, k2))

        n1 = self.get_node(k1)
        n2 = self.get_node(k2)

        visited = list()
        first = True

        if(n1 is None or n2 is None):
            print("wow")
            return False
        else:
            print("wow2")
            visited.extend([k2])
            return self.__find_path(k2, n1, visited, first)
        #if self.size is 0:
        #    return False
        #else:
        #    return self.__find_path(self.root, path, k)

    #private find path recursive method
    def __find_path(self, k, node, v, first):

        if node.key not in v:
            if node.key == k:
                print("path found")
                return True

        if node.key not in v:
            v.extend([node.key])

        if first is True:
            first = False

        children = node.children

        found = False

        for n in children:
            if n.key == k:
                print("path found")
                return True
            elif n.key not in v:
                print("check %d" % n.key)
                found = self.__find_path(k, n, v, first)
                if found is True:
                    return True

        #if len(v) == len(self.vertices):
        return False
        #else:
        #    return True
        #if root is None:
            #return False

        #path.append(root.key)

        #if root.key == k:
        #    return True

        #if((root.left!=None and self.__find_path(root.left, path, k)) or
         #  (root.right!=None and self.__find_path(root.right, path, k))):
        #    return True

        #path.pop()
        #return False

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

    def __find_ancestors(self, n, orig, anc):

        par = n.parents

        if len(par) == 0:
            return True

        for p in par:
            if p.key not in anc and p.key != orig.key:
                anc.extend([p.key])
                self.__find_ancestors(p, orig, anc)

        return True


g = Graph()
g.set_root(1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(5, 3)
g.add_edge(3, 6)
g.add_edge(6, 7)
print(g.find_lca(4, 7))
#print(b)
#print(g.find_path(1, 1))
#b = g.add_edge(2, 1)
#print(g.find_path(1, 1))
#print(b)
