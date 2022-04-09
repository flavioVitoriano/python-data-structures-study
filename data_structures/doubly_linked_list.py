from __future__ import annotations
from typing import Any, Optional
from .exceptions import IsEmpty, OutOfIndex


class Node:
    value: Any
    next: Optional[Node] = None
    previous: Optional[Node] = None

    def __init__(self, value: Any):
        self.value = value


class DoublyLinkedList:
    head: Optional[Node]
    tail: Optional[Node]
    length: int = 0

    def __init__(self, value: Optional[Any] = None):
        if not value:
            self.head, self.tail = None, None
            return

        node = Node(value)
        self.head = node
        self.tail = node

        self.length = 1

    def append(self, value):
        node = Node(value)

        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return

        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1

        return

    def pop(self):
        if self.length == 0:
            raise IsEmpty("List is empty")

        elif self.length == 1:
            node = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return node

        node = self.tail
        node.previous.next = None
        self.tail = node.previous
        node.previous = None

        self.length -= 1

        return node

    def pop_first(self) -> Node:
        node: Optional[Node] = self.head

        if self.length == 0 or not node:
            raise IsEmpty("List is empty")

        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.previous = None
            node.next = None

        self.length -= 1
        return node

    def prepend(self, value: Any):
        node = Node(value)

        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        self.length += 1

    def get(self, index: int) -> Node:
        temp: Optional[Node] = None

        if index < 0 or index >= self.length:
            raise OutOfIndex("index out of list range")

        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.previous

        if temp is None:
            raise OutOfIndex("index out of list range")

        return temp

    def set(self, index: int, value: Any):
        node = self.get(index)
        node.value = value
        return

    def insert(self, index: int, value: Any):
        if index < 0 or index > self.length:
            raise OutOfIndex("The index is out of list")
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        current_node = self.get(index)
        new_node = Node(value)
        prev_node = current_node.previous

        new_node.next = current_node
        new_node.previous = prev_node

        prev_node.next = new_node
        current_node.previous = new_node

        self.length += 1

        return

    def remove(self, index: int) -> Node:
        node = self.get(index)

        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()

        prev_node = node.previous
        next_node = node.next

        prev_node.next = next_node
        next_node.previous = prev_node

        node.next = None
        node.previous = None

        self.length -= 1

        return node
