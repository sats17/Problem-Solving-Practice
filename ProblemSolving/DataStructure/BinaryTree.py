
"""
Need to do: Create a tree, which is a binary tree. It will add nodes to the tree.
Simple condition, if value is less than the root, then it will go to the left. 
If value is greater than the root, then it will go to the right.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.tree = None
        return None

    def getTree(self):
        return self.tree

    def insert(self, value):
        if self.tree is None:
            self.tree = Node(value)
        else:
            self._insert(value, self.tree)
    
    def _insert(self, value, node):
        print("TEst")


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(2)
    print(tree.getTree())