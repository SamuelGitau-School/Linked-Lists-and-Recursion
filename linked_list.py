from __future__ import annotations
from typing import Optional


class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        # Annotated so type checkers know 'next' can hold another Node
        self.next: Optional[Node] = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        # An empty list has no head
        self.head: Optional[Node] = None

    def insert_at_front(self, data):
        # O(1): the new node points at the old head, then becomes the head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # O(n): walk to the last node, then attach the new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        return self._sum_helper(self.head)

    def _sum_helper(self, node):
        # Base case: past the end of the list, contribute 0
        if node is None:
            return 0
        # Recursive case: this node's data plus the sum of the rest
        return node.data + self._sum_helper(node.next)

    def recursive_reverse(self):
        # The helper returns the new head once the whole list is reversed
        self.head = self._reverse_helper(None, self.head)

    def _reverse_helper(self, prev, current):
        # Base case: ran off the end, so prev is the new head
        if current is None:
            return prev
        # Recursive case: save next, point current backwards, move forward
        next_node = current.next
        current.next = prev
        return self._reverse_helper(current, next_node)

    def recursive_search(self, target):
        return self._search_helper(self.head, target)

    def _search_helper(self, node, target):
        # Base case 1: reached the end without finding the target
        if node is None:
            return False
        # Base case 2: found the target
        if node.data == target:
            return True
        # Recursive case: search the rest of the list
        return self._search_helper(node.next, target)

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        print(" -> ".join(values))