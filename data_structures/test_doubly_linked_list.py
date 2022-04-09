from .doubly_linked_list import DoublyLinkedList
from .exceptions import IsEmpty, OutOfIndex
import pytest


def make_sut(arg: str = ""):
    if arg == "empty":
        return DoublyLinkedList()

    return DoublyLinkedList("pikachu")


def test_append():
    sut = make_sut()
    sut.append("charmander")

    assert sut.tail.value == "charmander"
    assert sut.tail.previous.value == "pikachu"
    assert sut.length == 2


def test_append_with_empty_list():
    sut = make_sut("empty")

    sut.append("squirtle")

    assert sut.head.value == "squirtle"
    assert sut.head.next is None
    assert sut.head.previous is None

    assert sut.tail.value == "squirtle"
    assert sut.tail.next is None
    assert sut.tail.previous is None

    assert sut.length == 1


def test_pop():
    sut = make_sut()
    sut.append("chikorita")

    node = sut.pop()
    assert node.value == "chikorita"
    assert node.next is None
    assert node.previous is None

    assert sut.tail.value == "pikachu"
    assert sut.tail.next is None

    assert sut.length == 1


def test_pop_with_empty_list():
    sut = make_sut("empty")

    with pytest.raises(IsEmpty):
        sut.pop()


def test_pop_with_one_length_list():
    sut = make_sut()
    node = sut.pop()

    assert node.value == "pikachu"
    assert node.next is None
    assert node.previous is None

    assert sut.head is None
    assert sut.tail is None

    assert sut.length == 0


def test_prepend():
    sut = make_sut()
    sut.prepend("digglet")

    assert sut.head.value == "digglet"
    assert sut.head.next.value == "pikachu"

    assert sut.tail.value == "pikachu"
    assert sut.tail.previous.value == "digglet"

    assert sut.length == 2


def test_prepend_with_empty_list():
    sut = make_sut("empty")

    sut.prepend("pidgey")

    assert sut.head.value == "pidgey"
    assert sut.tail.value == "pidgey"

    assert sut.head.next is None
    assert sut.tail.next is None

    assert sut.head.previous is None
    assert sut.tail.previous is None

    assert sut.length == 1


def test_pop_first():
    sut = make_sut()
    sut.append("charmander")
    sut.append("squirtle")

    node = sut.pop_first()

    assert node.value == "pikachu"
    assert node.next is None
    assert node.previous is None

    assert sut.head.value == "charmander"
    assert sut.head.previous is None

    assert sut.tail.value == "squirtle"
    assert sut.tail.previous.value == "charmander"

    assert sut.length == 2


def test_pop_first_with_one_length_list():
    sut = make_sut()
    node = sut.pop_first()

    assert node.value == "pikachu"
    assert node.next is None
    assert node.previous is None

    assert sut.head is None
    assert sut.tail is None

    assert sut.length == 0


def test_pop_first_with_empty_list():
    sut = make_sut("empty")

    with pytest.raises(IsEmpty):
        sut.pop_first()


def test_get():
    sut = make_sut()
    node = sut.get(0)

    assert node.value == "pikachu"

    with pytest.raises(OutOfIndex):
        sut.get(-1)

    with pytest.raises(OutOfIndex):
        sut.get(1)


def test_set():
    sut = make_sut()
    sut.append("test")
    sut.set(1, "ratata")
    node = sut.get(1)

    assert node.value == "ratata"


def test_insert_head():
    sut = make_sut()

    sut.insert(0, "charmander")
    node = sut.get(0)

    assert node.value == "charmander"
    assert node.next.value == "pikachu"
    assert node.previous is None
    assert sut.head.value == "charmander"
    assert sut.length == 2


def test_insert_middle():
    sut = make_sut("empty")
    sut.append("charmander")
    sut.append("pikachu")
    sut.append("chikorita")
    sut.insert(2, "turtwig")
    node = sut.get(2)

    assert node.value == "turtwig"
    assert node.next.value == "chikorita"
    assert node.previous.value == "pikachu"

    assert node.previous.next.value == "turtwig"
    assert node.next.previous.value == "turtwig"

    assert sut.length == 4


def test_remove_head():
    sut = make_sut()
    node = sut.remove(0)

    assert node.value == "pikachu"
    assert sut.head is None
    assert sut.tail is None

    assert sut.length == 0


def test_remove_tail():
    sut = make_sut()
    sut.append("raticate")
    sut.append("charizard")

    node = sut.remove(2)

    assert node.value == "charizard"
    assert sut.tail.value == "raticate"

    assert sut.length == 2


def test_remove_middle():
    sut = make_sut()
    sut.append("crocodile")
    sut.append("geodute")

    node = sut.remove(1)

    assert node.value == "crocodile"

    node = sut.get(1)

    assert node.value == "geodute"
    assert node.previous.value == "pikachu"
    assert node.next is None

    assert sut.length == 2
