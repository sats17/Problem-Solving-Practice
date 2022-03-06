
"""
Need to do: Create a tree, which is a binary tree. It will add nodes to the tree.
Simple condition, if value is less than the root, then it will go to the left. 
If value is greater than the root, then it will go to the right.
"""
class BinaryTree:
    def __init__(self, size):
        self.tree = None
        return None

    def getTree(self):
        return self.tree

    def put(self, value, test = False):
        b = self.tree
        self.tree = "hmm"
        print(b)
        print(self.tree)
        # self.tree.append(value)
        return None

if __name__ == "__main__":
    n = [5, 1, 2, 3, 4]
    bt = BinaryTree(1)
    bt.put(5, True)
    print(bt.getTree())