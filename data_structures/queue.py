from __future__ import annotations
from typing import Any, Optional

from .exceptions.list import IsEmpty


class Element:
    next: Optional[Element]
    value: Any

    def __init__(self, value: Any) -> None:
        self.value = value


class Queue:
    first: Element = None
    last: Element = None
    length: int = 0

    def __init__(self, value: Optional[Any] = None):
        if not value:
            return
        el = Element(value)
        self.first = el
        self.last = el
        self.length = 1

    def enqueue(self, value):
        el = Element(value)

        if self.length == 0:
            self.first = el
            self.last = el
        else:
            self.last.next = el
            self.last = el

        self.length += 1

    def dequeue(self) -> Element:
        el = self.first

        if self.length == 0:
            raise IsEmpty("Queue is empty")

        elif self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = el.next
            el.next = None

        self.length -= 1

        return el
