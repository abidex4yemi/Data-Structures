
# from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        """
        The main benefit of using Doubly Linked List as our storage
        over list for implementing stack is the dynamic allocation of data
        and to avoid the effect of stackoverflow due to the stack of size
        restricted when list is used
        """
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self):
        pass

    def len(self):
        pass


Node(1)
Node(1)
Node(1)

print(Node(1).data)
