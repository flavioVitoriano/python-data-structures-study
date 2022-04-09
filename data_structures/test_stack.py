import pytest
from .stack import Stack
from .exceptions import IsEmpty


def make_sut():
    return Stack()


def test_push():
    sut = make_sut()
    assert sut.top is None
    assert sut.height == 0

    sut.push("one")
    assert sut.top.value == "one"
    assert sut.height == 1

    sut.push("two")
    assert sut.top.value == "two"
    assert sut.height == 2


def test_pop():
    sut = make_sut()
    sut.push("one")
    sut.push("two")

    el = sut.pop()

    assert el.value == "two"
    assert el.previous is None

    assert sut.top.value == "one"
    assert sut.height == 1


def test_pop_empty_stack():
    sut = make_sut()
    sut.push("one")
    sut.pop()

    with pytest.raises(IsEmpty):
        sut.pop()
