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
        return self

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if len(self) == 0:
            return None

        old_head = self.head
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head
        if old_head is self.tail:
            self.tail = new_head
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
        return self

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass


dll = DoublyLinkedList(ListNode(1))
# dll.add_to_tail(2)
# dll.add_to_tail(3)
# dll.add_to_tail(4)
# dll.add_to_tail(5)
