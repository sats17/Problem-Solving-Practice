class BinaryTree:
    def __init__(self, size):
        self.tree = []
        return None

    def getTree(self):
        return self.tree

    def put(self, value):
        self.tree.append(value)
        return None

if __name__ == "__main__":
    n = [5, 1, 2, 3, 4]
    bt = BinaryTree(1)
    bt.put(5)
    print(bt.getTree())