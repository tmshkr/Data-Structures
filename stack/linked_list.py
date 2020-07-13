"""
Node class

Data:
Stores two pieces of data:
1. the value
2. the next node

Methods/Behavior/Operations:
1. get value
2. set value
3. get next
4. set next
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"<Node value: {self.value}>"


"""
Linked List class

Data:
1. reference to the head node
2. reference to the tail node

Methods:
1. append (add a new node at the tail)
2. prepend (add a new node at the head)
3. remove_head
4. remove_tail
5. contains
6. get_maximum
"""


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return

        curr = self.head
        while curr.next_node is not None:
            self.tail = curr
            curr = curr.next_node

        self.tail.next_node = None
        return curr.value

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None

        # LL with one Node
        if self.head.next_node is None:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head

        old_head = self.head
        self.head = self.head.next_node
        return old_head
