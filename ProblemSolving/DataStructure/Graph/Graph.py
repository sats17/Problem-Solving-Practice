# Ref https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,tuple%20to%20represent%20a%20weight.
class Node:
    def __init__(self, node, name):
        self.id = node
        self.name = name
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
        return f"Node instance with id={self.id} and name={self.name} and neighbour={self.neighbour}"

class SocialNetwork:
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
        if not to.is_neighbour(frm.get_node_id()):
            to.set_neighbour(frm)
    
    def show_suggestions_friends(self, node:Node):
        pass
         

if __name__ == '__main__':
    print("Hi there")
    network = SocialNetwork()
    alex = Node(1, "alex")
    network.set_node(alex)
    axel = Node(2, "axel")
    network.set_node(axel)
    bob = Node(3, "bob")
    network.set_node(bob)
    alias = Node(4, "alias")
    network.set_node(alias)
    network.get_nodes()
    network.set_edges(alex, axel)
    network.set_edges(bob, axel)
    network.get_nodes()