class Node:

    def  __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findPath(root, path, k):

    path.append(root.key)

    if root.key == k:
        return True

    if((root.left!=None and findPath(root.left, path, k)) or
       (root.right!=None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False
