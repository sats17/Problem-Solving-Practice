
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
    
    def toString(self):
        return self.value


class BinarySearchTree:
    def __init__(self):
        self.tree = None
        return None

    def printBasicTree(self):
        return self._getBasicTree(self.tree, result = [])

    def _getBasicTree(self, nodes, result):
        if nodes == None:
            return None
        result.append(nodes.toString()) # Using object reference to store the value of the node.
        self._getBasicTree(nodes.left, result)
        self._getBasicTree(nodes.right, result)
        return result

    def insert(self, value):
        if self.tree == None:
            self.tree = Node(value)
        else:
            self._insert(value, self.tree)

    
    def _insert(self, value, node):
        """
        This is a recursive method, which inserts a value in the tree. 
        If value is less than the root, then it will go to the left.
        If value is greater than the root, then it will go to the right.
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        else:
            print("Value already exists")


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    print(tree.printBasicTree())