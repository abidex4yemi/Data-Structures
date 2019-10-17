# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If value to insert is equal to root node
        if self.value == value:
            return False
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return True

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.value
        return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    def iterative_df_for_each(self, cb):
        stack = []
        stack.append(self)
        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        root = node
        if root:
            self.in_order_print(node.left)
            print(root.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal
        root = node
        nodes = []
        stack = [root]
        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            nodes.append(cur_node)
            for child in cur_node:
                stack.append(child)
        return nodes

    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if root:
            print(root.val)
            pre_order_dft(root.left)
            pre_order_dft(root.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if root:
            post_order_dft(root.left)
            post_order_dft(root.right)
            print(root.val)
