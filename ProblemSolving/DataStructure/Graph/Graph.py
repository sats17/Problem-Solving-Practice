# Ref https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,tuple%20to%20represent%20a%20weight.
class Node:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

if __name__ == '__main__':
    print("Hi there")
