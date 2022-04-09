import pytest

from .exceptions.list import IsEmpty
from .queue import Queue


def make_sut():
    return Queue()


def test_enqueue():
    sut = make_sut()
    assert sut.first is None
    assert sut.last is None
    assert sut.length == 0

    sut.enqueue("paulo")
    assert sut.first.value == "paulo"
    assert sut.last.value == "paulo"
    assert sut.length == 1

    sut.enqueue("amanda")
    assert sut.first.value == "paulo"
    assert sut.last.value == "amanda"
    assert sut.length == 2


def test_dequeue():
    sut = make_sut()
    sut.enqueue("paulo")
    sut.enqueue("amanda")
    sut.enqueue("mario")

    el = sut.dequeue()
    assert el.value == "paulo"
    assert el.next is None

    assert sut.first.value == "amanda"
    assert sut.length == 2

    el = sut.dequeue()
    assert el.value == "amanda"
    assert el.next is None

    assert sut.first.value == "mario"
    assert sut.length == 1


def test_dequeue_with_empty_queue():
    sut = make_sut()

    with pytest.raises(IsEmpty):
        sut.dequeue()


def test_dequeue_one_length():
    sut = make_sut()
    sut.enqueue("roberto")
    el = sut.dequeue()

    assert el.value == "roberto"

    assert sut.first is None
    assert sut.last is None

    assert sut.length == 0
