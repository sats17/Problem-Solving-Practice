# class Node:
#     def __init__(self, value, next_node, previous_node):
#         self.value = value
#         self.next_node = next_node
#         self.previous_node = previous_node
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, value):
#         head = self.head
#         if head is None:
#             self.head = Node(value, None, None)
#             head = None
#         while head is not None:
#             # print(value)
#             if head.value < value:
#                 current_node = head
#                 head = head.next_node
#                 if head is None:
#                     new_node = Node(value, None, current_node)
#                     current_node.next_node = new_node
#                     head = None
#             else:
#                 previous_node = head.previous_node
#                 # print(previous_node)
#                 if previous_node is not None:
#                     new_node = Node(value, head, previous_node)
#                     head.previous_node = new_node
#                     previous_node.next_node = new_node
#                     head = None
#                 else:
#                     new_node = Node(value, head, None)
#                     head.previous_node = new_node
#                     self.head = new_node
#                     head = None
#
#
#     def print_list(self):
#         head = self.head
#         while head is not None:
#             # print("Inside whil of print")
#             print(head.value)
#             head = head.next_node
#             # print("Next node ",head)


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value) + " " + str(self.next_node)


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert_v2(self, value):
        head = self.head
        if head is None:
            self.head = Node(value, None)
        else:
            while head is not None:
                if head.value < value:
                    if head.next_node is None:
                        new_node = Node(value, None)
                        head.next_node = new_node
                        head = None
                    elif head.next_node.value > value:
                        new_node = Node(value, head.next_node)
                        head.next_node = new_node
                        head = None
                    else:
                        head = head.next_node
                elif head.value == value:
                    print("Value already exists")
                    head = None
                else:
                    new_node = Node(value, head)
                    self.head = new_node
                    head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value, None)
        elif self.head.value == value:
            print("Do nothing")
        elif self.head.value > value:
            new_node = Node(value, self.head)
            self.head = new_node
        else:
            current_head = self.head
            while current_head.next_node is not None and current_head.next_node.value < value:
                current_head = current_head.next_node
            if current_head.next_node is not None and current_head.next_node.value == value:
                return
            new_node = Node(value, current_head.next_node)
            current_head.next_node = new_node
            # Commenting another logic, which is ignored due to extra loop iteration
            # while current_head.next_node is not None and current_head.next_node.value <= value:
            #     current_head = current_head.next_node
            # if current_head.value != value:
            #     new_node = Node(value, current_head.next_node)
            #     current_head.next_node = new_node

    def search(self, value):
        # head = self.head
        # while head is not None and head.value != value:
        #     head = head.next_node
        # if head is not None:
        #     return True
        # return False

        head = self.head
        while head is not None:
            print("Iteration")
            if head.value == value:
                return True
            elif head.value > value:
                return False
            head = head.next_node
        return False

    def delete(self, value):
        if self.head is None:
            return
        elif self.head is not None and self.head.value == value:
            self.head = self.head.next_node
            return
        else:
            head = self.head
            while head.next_node is not None:
                print("Iteration")
                if head.next_node.value == value:
                    head.next_node = head.next_node.next_node
                    return
                elif head.value > value:
                    return
                head = head.next_node
            return

    def print_list(self):
        head = self.head
        while head is not None:
            # print("Inside whil of print")
            print(head.value)
            head = head.next_node
            # print("Next node ",head)


if __name__ == '__main__':
    print("Started")
    print(10 < 10)
    list = SortedLinkedList()
    list.insert(5)
    list.insert(10)
    list.insert(11)
    list.insert(8)
    list.insert(1)
    list.insert(2)
    list.insert(2)
    list.insert(11)
    list.insert(12)
    print("################################")
    list.print_list()
    print("################################")
    # print(list.search(0))
    list.delete(3)
    print("################################")
    list.print_list()
