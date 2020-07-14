"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value=None, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        next_node = "None" if self.next is None else f"{self.next.value} at {hex(id(self.next))}"
        prev_node = "None" if self.prev is None else f"{self.prev.value} at {hex(id(self.prev))}"
        return f"<ListNode\n  value: {self.value} at {hex(id(self))}\n  next: {next_node}\n  prev: {prev_node}\n>"


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        curr = self.head
        string = ""
        while curr:
            string += str(curr) + "\n"
            curr = curr.next
        return string

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        node = ListNode(value)
        if len(self) == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1
        return node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if len(self) == 0:
            return None

        old_head = self.head
        self.head = self.head.next
        if old_head is self.tail:
            self.tail = None
        else:
            self.head.prev = None
        self.length -= 1

        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        node = ListNode(value)
        if len(self) == 0:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1
        return node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if len(self) == 0:
            return None

        old_tail = self.tail
        self.tail = old_tail.prev
        if old_tail is self.head:
            self.head = None
        self.length -= 1

        return old_tail.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return node

        # remove node from its current position
        node.prev.next = node.next
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        # then add to head
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
        return node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return node

        # remove node from its current position
        node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next

        # then add to tail
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node
        return node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.length -= 1
        return node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if len(self) == 0:
            return None

        max_value = self.head.value
        curr = self.head.next

        while curr:
            if curr.value > max_value:
                max_value = curr.value
            curr = curr.next

        return max_value

    def reverse(self):
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next, curr.prev = curr.prev, curr.next
            curr = next_node

        self.tail, self.head = self.head, self.tail
        return self


dll = DoublyLinkedList(ListNode(1))
dll.add_to_tail(2)
third = dll.add_to_tail(3)
dll.add_to_tail(4)
dll.add_to_tail(5)
