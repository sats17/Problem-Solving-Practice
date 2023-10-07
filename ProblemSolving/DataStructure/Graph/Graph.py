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
    
    def show_friends_suggestion_dfs(self, node:Node):
        suggestedFrndsIds = []
        visitedIds = []
        for id, val in node.get_neighbour().items():
            print("============\nSuggesting frnd's frnd from ID ", id)
            print("\n============================\n")
            self.travel_recursively(val, node.get_node_id(), node.get_neighbour(), node.get_node_id(), suggestedFrndsIds, visitedIds, 1)

        print("Suggested frnds IDs are \n")
        print(suggestedFrndsIds)

    def travel_recursively(self, node:Node, og_id, og_frnds, current_id, suggestedFrndsIds, visitedIds, depth):
        if depth == 2:
            print("\n===============\nDepth limit reached with ID = ", node.get_node_id())
            print("Validating what all frnds this Id have ",node.get_node_id())
            for id, val in node.get_neighbour().items():
                print("Validation: Iterating frnd Id ", id)
                if(id == og_id):
                    print("Validation: Skipping frnd Id, because it is original guy whom we are suggesting frnds ", id)
                    continue
                # if(id == current_id):
                #     print("Skipping current Id, because it is previously comes ", id)
                #     continue
                
                if id not in og_frnds:
                    print("Validation: This ID can be suggested, will move to next iteration ", id)
                    if id not in suggestedFrndsIds:
                        suggestedFrndsIds.append(id)
            print("Returning to previous recursion")
            print("===============\n")
            return
        else:
            print("We have reached to the ID = ", node.get_node_id(), ", We will search his frnds and depth to travel further")
            if node.get_node_id() in visitedIds:
                print("Skipping this id =", node.get_node_id()," as it is already visited")
                return
            for id, val in node.get_neighbour().items():
                print("Recursive frnd Id ", id, ", Which is frnd of ",node.get_node_id())
                if(id == og_id):
                    print("Skipping frnd Id, because it is original guy id whom we are searching frnd", id)
                    continue
                if(id == current_id):
                    print("Skipping this Id, because we travelled from this Id only ", id)
                    continue
                
                if id not in og_frnds:
                    print("This ID can be suggested, will move to next depth ", id)
                    if id not in suggestedFrndsIds:
                        suggestedFrndsIds.append(id)
                print("As no validation satiesfied, we will move to the next depth, depth number = ",depth + 1)
                self.travel_recursively(val, og_id, og_frnds, node.get_node_id(), suggestedFrndsIds, visitedIds, depth + 1)
            print("Done from recursive function")
            visitedIds.append(node.get_node_id())

        
         

def generate_network():

    network = SocialNetwork()
    bob = Node(1, "bob")
    network.set_node(bob)
    alias = Node(2, "alias")
    network.set_node(alias)
    axel = Node(3, "axel")
    network.set_node(axel)
    alex = Node(4, "alex")
    network.set_node(alex)
    mark = Node(5, "mark")
    network.set_node(mark)
    kia = Node(6, "kia")
    network.set_node(kia)
    mia = Node(7, "mia")
    network.set_node(mia)
    tork = Node(8, "tork")
    network.set_node(tork)
    molnar = Node(9, "molnar")
    network.set_node(molnar)


    network.set_edges(bob, alias)
    network.set_edges(bob, alex)
    network.set_edges(alias, axel)
    network.set_edges(alias, mark)
    network.set_edges(axel, kia)
    network.set_edges(kia, mia)
    network.set_edges(mark, molnar)
    network.set_edges(alex, axel)
    network.set_edges(bob, mark)
    network.set_edges(mark, tork)

    return network

if __name__ == '__main__':
    print("Hi there")

    network = generate_network()

    frnds = network.show_friends_suggestion_dfs(network.get_node_by_name("bob"))
    # Problem, When depth moved forward. How to save from pervious node validation ?
    # 3 [3, 7, 6, 8]
    # 2 [6, 9, 8, 3, 7]
    """
    ===============
Depth limit reached, ID =  6
Validation: Iterating frnd Id  3
This ID can be suggested, will move to next depth  3
Validation: Iterating frnd Id  7
This ID can be suggested, will move to next depth  7
===============
    """
