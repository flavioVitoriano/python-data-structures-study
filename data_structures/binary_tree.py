from __future__ import annotations
from typing import Any, Optional
from enum import Enum


class Directions(str, Enum):
    LEFT = "left"
    RIGHT = "right"


class Node:
    value: int | float
    left: Optional[Node] = None
    right: Optional[Node] = None

    def __init__(self, value: Any) -> None:
        self.value = value
        return


class BinaryTree:
    root: Optional[Node] = None

    def insert(self, value: int | float) -> bool:
        new_node = Node(value)
        next_node = self.root

        if next_node is None:
            self.root = new_node
            return True

        while True:
            if next_node.value == value:
                return False

            if value < next_node.value:
                if next_node.left is None:
                    next_node.left = new_node
                    return True
                next_node = next_node.left

            else:
                if next_node.right is None:
                    next_node.right = new_node
                    return True
                next_node = next_node.right

    def contains(self, value: int | float) -> bool:
        next_node = self.root

        while True:
            if next_node is None:
                return False
            if next_node.value == value:
                return True

            if value < next_node.value:
                next_node = next_node.left
            else:
                next_node = next_node.right

    def min_value_node(self, current_node: Optional[Node] = None) -> Node:
        temp = current_node

        if not current_node:
            temp = self.root

        if not self.contains(temp.value):
            return None

        while temp.left is not None:
            temp = temp.left

        return temp

    def max_value_node(self, current_node: Optional[Node] = None) -> Node:
        temp = current_node

        if not current_node:
            temp = self.root

        if not self.contains(temp.value):
            return None

        while temp.right is not None:
            temp = temp.right

        return temp