from .linked_list import LinkedList
from .exceptions.list import IsEmpty, OutOfIndex
import pytest
from typing import Optional


def make_sut(arg: Optional[str] = ""):
    if arg == "empty":
        return LinkedList()
    return LinkedList("banana")


def test_get():
    sut = make_sut()
    result = sut.get(0)

    assert result.value == "banana"

    with pytest.raises(OutOfIndex):
        sut.get(1)

    with pytest.raises(OutOfIndex):
        sut.get(2)


def test_set():
    sut = make_sut()
    sut.set(0, "apple")
    node = sut.get(0)

    assert node.value == "apple"


def test_append():
    sut = make_sut()
    sut.append("pineapple")
    result = sut.get(1)

    assert result.value == "pineapple"
    assert sut.length == 2
    assert sut.tail.value == "pineapple"
    assert sut.tail.next is None


def test_prepend():
    sut = make_sut()
    sut.prepend("apple")
    result = sut.head

    assert result.value == "apple"
    assert result.next.value == "banana"
    assert sut.length == 2


def test_insert_middle():
    sut = make_sut()
    sut.append("apple")
    sut.append("pineapple")
    sut.insert(1, "pea")

    result = sut.get(1)
    previous_node = sut.get(0)

    assert result.value == "pea"
    assert result.next.value == "apple"

    assert previous_node.next.value == "pea"
    assert sut.length == 4


def test_insert_head():
    sut = make_sut()
    sut.insert(0, "ouroboros")

    assert sut.head.value == "ouroboros"
    assert sut.head.next.value == "banana"
    assert sut.tail.value == "banana"
    assert sut.tail.next is None
    assert sut.length == 2


def test_insert_out_of_lengh():
    sut = make_sut()

    with pytest.raises(OutOfIndex):
        sut.insert(-1, "i have no mouth, but i want scream")

    with pytest.raises(OutOfIndex):
        sut.insert(2, "Monaliza overdrive")


def test_out_of_index():
    sut = make_sut()

    with pytest.raises(OutOfIndex):
        sut.get(10)


def test_str():
    expected = " ".join(["banana", "apple"])
    sut = make_sut()
    sut.append("apple")
    result = str(sut)

    assert result == expected


def test_pop_with_one_length_list():
    sut = make_sut()
    expected = "banana"
    result = sut.pop()

    assert result.value == expected
    assert sut.length == 0
    assert sut.head is None
    assert sut.tail is None


def test_pop_with_empty_list():
    sut = make_sut("empty")

    with pytest.raises(IsEmpty):
        sut.pop()


def test_pop():
    sut = make_sut()
    sut.append("apple")
    sut.append("orange")

    expected = "orange"
    result = sut.pop()

    assert result.value == expected
    assert sut.length == 2
    assert sut.head.value == "banana"
    assert sut.tail.value == "apple"
    assert sut.tail.next is None


def test_pop_first_with_one_length_list():
    sut = make_sut()
    expected = "banana"
    result = sut.pop_first()

    assert result.value == expected
    assert sut.head is None
    assert sut.tail is None
    assert sut.length == 0


def test_pop_first_with_empty_list():
    sut = make_sut("empty")

    with pytest.raises(IsEmpty):
        sut.pop_first()


def test_pop_first():
    sut = make_sut()
    sut.append("grapefruit")
    sut.append("avocado")

    expected = "banana"
    result = sut.pop_first()

    assert result.value == expected
    assert sut.head.value == "grapefruit"
    assert sut.length == 2


def test_remove():
    sut = make_sut()

    sut.append("orange")
    sut.append("grapefruit")

    removed_node = sut.remove(1)

    assert removed_node.value == "orange"
    assert sut.head.next.value == "grapefruit"
    assert sut.length == 2


def test_remove_with_empty_list():
    sut = make_sut("empty")

    with pytest.raises(IsEmpty):
        sut.remove(1)


def test_remove_out_of_length():
    sut = make_sut()

    with pytest.raises(OutOfIndex):
        sut.remove(1)

    with pytest.raises(OutOfIndex):
        sut.remove(-1)

    with pytest.raises(OutOfIndex):
        sut.remove(2)


def test_remove_in_border_index():
    sut = make_sut()

    sut.append("orange")
    sut.append("grapefruit")

    removed_node = sut.remove(0)

    assert removed_node.value == "banana"
    assert sut.head.value == "orange"
    assert sut.head.next.value == "grapefruit"
    assert sut.length == 2


def test_reverse():
    sut = make_sut("empty")

    sut.append(1)
    sut.append(2)
    sut.append(3)
    sut.append(4)

    assert sut.to_list() == [1, 2, 3, 4]

    sut.reverse()

    assert sut.to_list() == [4, 3, 2, 1]
