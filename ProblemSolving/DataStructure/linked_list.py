class Node:
    def __init__(self, value, next_node, previous_node):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        head = self.head
        if head is None:
            self.head = Node(value, None, None)
            head = None
        while head is not None:
            # print(value)
            if head.value < value:
                current_node = head
                head = head.next_node
                if head is None:
                    new_node = Node(value, None, current_node)
                    current_node.next_node = new_node
                    head = None
            else:
                previous_node = head.previous_node
                # print(previous_node)
                if previous_node is not None:
                    new_node = Node(value, head, previous_node)
                    head.previous_node = new_node
                    previous_node.next_node = new_node
                    head = None
                else:
                    new_node = Node(value, head, None)
                    head.previous_node = new_node
                    self.head = new_node
                    head = None


    def print_list(self):
        head = self.head
        while head is not None:
            # print("Inside whil of print")
            print(head.value)
            head = head.next_node
            # print("Next node ",head)


if __name__ == '__main__':
    list = LinkedList()
    list.insert(5)
    list.insert(10)
    list.insert(11)
    list.insert(8)
    list.insert(1)
    list.print_list()
