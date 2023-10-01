# Ref https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,tuple%20to%20represent%20a%20weight.
class Node:
    def __init__(self, node):
        self.id = node
        self.neighbour = {}
    
    def set_neighbour(self, neighbour:"Node"):
        self.neighbour[neighbour.get_node_id()] = neighbour

    def is_neighbour(self, id):
        return id in self.neighbour

    def __hash__(self):
        return hash(self.id)
    
    def get_node_id(self):
        return self.id
    
    def __str__(self):
        return f"Node instance with id={self.id} and neighbour={self.neighbour}"

class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

    def set_node(self, node:Node):
        if node.get_node_id() not in self.node_dict:
            self.node_dict[node.get_node_id()] = node
        else:
            print("Node already present, cannot add")
    
    def get_nodes(self):
        for key, value in self.node_dict.items():
            print(f'Node ID: {key}, Value: {value.__str__()}')
    
    def set_edges(self, frm:Node, to:Node):
        if not frm.is_neighbour(to.get_node_id()):
            frm.set_neighbour(to)
         

if __name__ == '__main__':
    print("Hi there")
    graph = Graph()
    node1 = Node(1)
    graph.set_node(node1)
    node2 = Node(2)
    graph.set_node(node2)
    graph.get_nodes()
    graph.set_edges(node1, node2)
    graph.get_nodes()
