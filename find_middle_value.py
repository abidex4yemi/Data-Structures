"""How do you find and return the middle node of a singly
    linked list in one pass? You do not have access to the
    length of the list. If the list is even, you should return
    the first of the two "middle" nodes.
"""


"""
    - Traverse linked list using two pointers
    - Move one pointer by one and other by two
    - When the fast pointer reaches end
    - Slow pointer will reach middle of the linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def find_middle(self):
        middle = self
        end = self

        while end is not None:
            end = end.next
            if end:
                end = end.next
                middle = middle.next

        return f"Middle is: {middle.value}"


root = Node(3)
cur = root
cur.add(4)
print(cur)
cur = cur.next
print(cur)
cur.add(5)
cur = cur.next
cur.add(6)
cur = cur.next
cur.add(7)
cur = cur.next
print(cur.next)
print(root.find_middle())
