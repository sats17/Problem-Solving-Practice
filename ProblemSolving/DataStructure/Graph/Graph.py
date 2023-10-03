# Ref https://www.bogotobogo.com/python/python_graph_data_structures.php#:~:text=A%20graph%20can%20be%20represented,tuple%20to%20represent%20a%20weight.
class Node:
    def __init__(self, node, name):
        self.id = node
        self.name = name
        self.neighbour = {}
    
    def get_name(self):
        return self.name
    
    def set_neighbour(self, neighbour:"Node"):
        self.neighbour[neighbour.get_node_id()] = neighbour

    def get_neighbour(self):
        return self.neighbour

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
    
    def get_node_by_name(self, name):
        for key, node in self.node_dict.items():
            if name == node.get_name():
                return node

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
    
    def show_friends_suggestion(self, node:Node):
        suggestedFrnds = []
        for c_id, c_val in node.get_neighbour().items():
            for s_key in c_val.get_neighbour().keys():
                if s_key == node.get_node_id() or s_key in node.get_neighbour().keys():
                    continue
                else:
                    suggestedFrnds.append(self.node_dict.get(s_key))
        return suggestedFrnds
        
         

def generate_network():

    network = SocialNetwork()
    alex = Node(1, "alex")
    network.set_node(alex)
    axel = Node(2, "axel")
    network.set_node(axel)
    bob = Node(3, "bob")
    network.set_node(bob)
    alias = Node(4, "alias")
    network.set_node(alias)
        # Adding more nodes
    chris = Node(5, "chris")
    network.set_node(chris)

    dave = Node(6, "dave")
    network.set_node(dave)

    emily = Node(7, "emily")
    network.set_node(emily)

    frank = Node(8, "frank")
    network.set_node(frank)

    grace = Node(9, "grace")
    network.set_node(grace)

    hank = Node(10, "hank")
    network.set_node(hank)

    irene = Node(11, "irene")
    network.set_node(irene)

    jack = Node(12, "jack")
    network.set_node(jack)

    kate = Node(13, "kate")
    network.set_node(kate)

    lucas = Node(14, "lucas")
    network.set_node(lucas)

    megan = Node(15, "megan")
    network.set_node(megan)

    nathan = Node(16, "nathan")
    network.set_node(nathan)

    olivia = Node(17, "olivia")
    network.set_node(olivia)

    peter = Node(18, "peter")
    network.set_node(peter)

    quincy = Node(19, "quincy")
    network.set_node(quincy)

    roger = Node(20, "roger")
    network.set_node(roger)

    network.set_edges(alex, axel)
    network.set_edges(axel, alias)
    network.set_edges(axel, roger)
    network.set_edges(quincy, axel)
    network.set_edges(alex, quincy)
    network.set_edges(bob, peter)
    network.set_edges(bob, alex)
    network.set_edges(alex, megan)
    network.set_edges(olivia, alex)

    return network

if __name__ == '__main__':
    print("Hi there")

    network = generate_network()

    frnds = network.show_friends_suggestion(network.get_node_by_name("bob"))
    for frnd in frnds:
        print(frnd.get_name())