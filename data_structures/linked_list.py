from __future__ import annotations
from typing import Any, List, Optional
from .exceptions import IsEmpty, OutOfIndex


class Node:
    value: Any
    next: Optional[Node] = None

    def __init__(self, value: Any):
        self.value = value


class LinkedList:
    head: Node
    tail: Node
    length: int = 0

    def __init__(self, value: Any = None):
        if not value:
            return
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __str__(self) -> str:
        temp = self.head
        return_str = ""

        while temp is not None:
            return_str += f" {temp.value}"
            temp = temp.next

        return return_str.strip()

    def append(self, value: Any):
        node = Node(value)

        if self.length > 0:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.length += 1
        return

    def prepend(self, value: Any):
        if self.length == 0:
            return self.append(value)

        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        return

    def get(self, index: int) -> Node:
        counter = 0
        current = self.head
        exception = OutOfIndex("The index is out of list")

        if index < 0 or index > self.length:
            raise exception

        while counter < index:
            try:
                current = current.next
                counter += 1
            except AttributeError:
                raise exception

        if current is None:
            raise exception

        return current

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

        previous_node = self.get(index - 1)
        current_node = previous_node.next

        new_node = Node(value)
        new_node.next = current_node
        previous_node.next = new_node

        self.length += 1
        return

    def pop(self) -> Node:
        if self.length == 0:
            raise IsEmpty("The list is empty")
        elif self.length == 1:
            node = self.get(0)
            self.head = None
            self.tail = None
        else:
            prev_node = self.get(self.length - 2)
            node = self.get(self.length - 1)
            prev_node.next = None
            self.tail = prev_node

        self.length -= 1
        return node

    def pop_first(self) -> Node:
        if self.length == 0:
            raise IsEmpty("The list is empty")
        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = node.next
            node.next = None

        self.length -= 1
        return node

    def remove(self, index) -> Node:
        if self.length == 0:
            raise IsEmpty("The list is empty")

        if index < 0 or index >= self.length:
            raise OutOfIndex("The index is out of list")
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()

        previous_node = self.get(index - 1)
        to_remove_node = previous_node.next
        next_node = to_remove_node.next

        previous_node.next = next_node
        to_remove_node.next = None

        self.length -= 1

        return to_remove_node

    def reverse(self):
        temp_node = self.head
        self.tail, self.head = self.head, self.tail

        before_node = None
        after_node = None

        for _ in range(self.length):
            after_node = temp_node.next
            temp_node.next = before_node
            before_node = temp_node
            temp_node = after_node

        return

    def to_list(self) -> List[Any]:
        temp = self.head
        return_lst = []

        while temp is not None:
            return_lst.append(temp.value)
            temp = temp.next

        return return_lst
