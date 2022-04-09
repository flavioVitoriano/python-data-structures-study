from __future__ import annotations
from typing import Any, Optional

from .exceptions import IsEmpty


class Element:
    value: Any
    previous: Optional[Element] = None

    def __init__(self, value) -> None:
        self.value = value


class Stack:
    top: Optional[Element] = None
    height: int = 0

    def __init__(self, initial_value: Optional[Any] = None) -> None:
        if initial_value:
            self.top = Element(initial_value)
            self.height += 1
        return

    def push(self, value: Any) -> None:
        element = Element(value)
        element.previous = self.top

        self.top = element
        self.height += 1

        return

    def pop(self) -> Element:
        element = self.top

        if not element:
            raise IsEmpty("the stack is empty")

        self.top = element.previous
        element.previous = None

        self.height -= 1

        return element
