from typing import Optional


class LinkedList:
    """Basic implementation of a singly-linked list.
    Values are int.
    """

    def __init__(self, head: Optional['ListNode']):
        self.head = head

    @classmethod
    def from_list(cls, values: list[int]):
        if len(values) == 0:
            return cls(None)
        head = ListNode()
        pointer = head
        for index, value in enumerate(values):
            pointer.value = value
            if index != len(values)-1:
                pointer.next = ListNode()
                pointer = pointer.next
        return cls(head)

    # Dunder methods
    def __iter__(self):
        """Iterate over values"""
        pointer = self.head
        if pointer:
            yield pointer.value
            while pointer.next:
                yield pointer.next.value
                pointer = pointer.next

    def __str__(self) -> str:
        return str([el for el in self])

    def __repr__(self) -> str:
        return "LinkedList: " + str(self)

    def __add__(self, other: 'LinkedList') -> 'LinkedList':
        pointer = self.head
        if pointer:
            while pointer.next:
                pointer = pointer.next
            pointer.next = other.head
        else:
            self.head = other.head
        return self

    def __len__(self) -> int:
        return len([el for el in self])

    def __contains__(self, value: int) -> bool:
        return value in [el for el in self]

    # Mutable sequence emulation

    def pop(self):
        """Remove the first element.
        This doesn't return that first element.
        """
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            raise IndexError("pop from empty list")

    def reverse(self):
        raise NotImplementedError

    def count(self, item: int) -> int:
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def remove(self, item: int):
        raise NotImplementedError

    def sort(self):
        raise NotImplementedError

    def append(self, node: 'ListNode'):
        """Add node to the tail of the list"""
        pointer = self.head
        if pointer:
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
        else:
            self.head = node


class ListNode:

    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)
