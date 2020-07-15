"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # https://codereview.stackexchange.com/a/109410
    def __repr__(self):
        if self.right is not None:
            fmt = '{}({value!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({value!r}, {left!r})'
        else:
            fmt = '{}({value!r})'
        return fmt.format(type(self).__name__, **vars(self))

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is a node
        # if not, create the node and return
        if self is None:
            self = BSTNode(value)
            return

        # if there is a node,
        # check if the value to insert is less than the current node
        if value < self.value:
            # if it is less than the current node's value,
            # call insert again if there is already a node present
            if self.left:
                self.left.insert(value)
            # otherwise, create the node here
            else:
                self.left = BSTNode(value)
        else:
            # if the value is gte the current node's value,
            # call insert again if there is already a node present
            if self.right:
                self.right.insert(value)
            # otherwise, create the node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BSTNode(5)
# bst.insert(2)
# bst.insert(3)
# bst.insert(7)
# bst.insert(6)

bst = BSTNode(74)
bst.insert(64)
bst.insert(93)
bst.insert(69)
bst.insert(68)
bst.insert(90)
