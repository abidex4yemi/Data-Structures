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
            self.head = DoublyLinkedList(value)
            self.size += 1
        else:
            new_node = DoublyLinkedList(value)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            removedvalue = self.head.data
            self.head = self.head.next
            if self.size == 1:
                self.head = None
            else:
                self.head.prev is None
            self.size -= 1

            return removedvalue

    def len(self):
        return self.size


if __name__ == "__main__":
    # s = Stack()
    # s.push(100)
    # s.push(105)
    # s.push(110)
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.len())
    # s.push(101)
    # s.push(105)
    # self.s.pop(), 105
    # self.s.len()
    pass
