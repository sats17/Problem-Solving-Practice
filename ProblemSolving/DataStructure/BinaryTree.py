
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

    def printPreOrderTree(self):
        """
        This is a recursive method, which prints the tree in pre-order.
        Root, left, right.
        """
        print(type(self.tree))
        return self._getPreOrder(self.tree, result = [])

    def _getPreOrder(self, nodes, result):
        """
        First append the current node value, then recursively traverse to left nodes and appends the values. Once left most nodes completes,
        Then we move to right nodes recursively.
        Until all nodes are traversed -
        Step 1 = Visit root node.
        Step 2 - Recursively traverse left subtree.
        Step 3 - Recursively traverse right subtree.
        """
        if nodes == None:
            return None
        result.append(nodes.toString()) # Using object reference to store the value of the node.
        self._getPreOrder(nodes.left, result)
        self._getPreOrder(nodes.right, result)
        return result

    def printInOrderTree(self):
        """
        This is a recursive method, which prints the tree in pre-order.
        Root, left, right.
        """
        print(type(self.tree))
        return self._getInOrder(self.tree, result = [])

    def _getInOrder(self, nodes, result):
        """
        First recursively traverse to left most nodes, once we got final node(Either finalNode.left = None) then we append 
        finalNode.value to array. Then we recursively travese to right nodes. for each left and right nodes we are going recursively
        Hence, after completion of left node we are appending value to array.
        Until all nodes are traversed -
        Step 1 - Recursively traverse left subtree.
        Step 2 - Visit root node.
        Step 3 - Recursively traverse right subtree.
        """
        if nodes == None:
            return None
        self._getInOrder(nodes.left, result)
        result.append(nodes.toString()) # Using object reference to store the value of the node.
        self._getInOrder(nodes.right, result)
        return result
    
    def printPostOrderTree(self):
        """
        This is a recursive method, which prints the tree in post-order.
        left, right, root.
        """
        return self._getPostOrder(self.tree, result = [])

    def _getPostOrder(self, nodes, result):
        """
        First recursively traverse to left most nodes, Then we recursively travese to right nodes. for each left and right nodes we are going recursively
        Hence, after completion of right node we are appending value to array.
        Until all nodes are traversed -
        Step 1 - Recursively traverse left subtree.
        Step 2 - Recursively traverse right subtree.
        Step 3 = Visit root node.
        """
        if nodes == None:
            return None
        self._getPostOrder(nodes.left, result)
        self._getPostOrder(nodes.right, result)
        result.append(nodes.toString()) # Using object reference to store the value of the node.
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
        Until all nodes are traversed -
        Step 1 = Visit root node.
        Step 2 - If value is less than root, Recursively traverse left subtree, if left node is none then put value.
        Step 3 - If value is greater than root, Recursively traverse right subtree, if right node is none then put value.
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
    tree.insert(9)
    tree.insert(7)
    tree.insert(14)
    print("Pre order = ",tree.printPreOrderTree())
    print("In order = ",tree.printInOrderTree())
    print("Post order = ",tree.printPostOrderTree())
    # [5, 2,6, 1, 4, 9, 7, 14]
    # Next action is to reverse the binary tree and level order traversal.s