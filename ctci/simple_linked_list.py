from __future__ import annotations
from typing import Optional, TypeVar, Generic, Iterable

V = TypeVar("V")


class Node(Generic[V]):
    def __init__(self, value: V, next: ListNode = None):
        self._value = value
        self._next: ListNode = next

    def value(self) -> V:
        return self._value

    def next(self) -> ListNode:
        return self._next


ListNode = Optional[Node]


class LinkedList(Generic[V]):
    """Implement a LIFO linked list."""

    def __init__(self, values: Optional[Iterable[V]] = None):
        self._head: ListNode = None
        self._len: int = 0
        for value in values or []:
            self.push(value)

    def __iter__(self):
        """Iterate over values."""
        pointer = self._head
        while pointer:
            yield pointer.value()
            pointer = pointer.next()

    def __len__(self) -> int:
        return self._len

    def head(self) -> ListNode:
        """Return head node. Raise EmptyListException if head is None."""
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: V) -> None:
        """Add a predecessor to the head node. Update length."""
        self._head = Node(value, self._head)
        self._len += 1

    def pop(self) -> V:
        """Advance head one place and return the previous head value.

        Update length.
        """
        # head() is needed to raise an exception if self._head is None
        old_value = self.head().value()
        self._head = self._head.next()
        self._len -= 1
        return old_value

    def delete(self, value: V) -> None:
        """Find the first node with given value and delete it."""
        try:
            if self.head().value() == value:
                self.pop()
                return
        except EmptyListException:
            return
        pointer = self.head()
        while pointer._next:
            if pointer._next._value == value:
                pointer._next = pointer._next._next
                return
            pointer = pointer._next
        return

    def reversed(self) -> LinkedList:
        return LinkedList(self)


class EmptyListException(Exception):
    pass
