from .hash_table import HashTable


def make_sut():
    return HashTable()


def test_hash_table():
    sut = make_sut()
    key = "test_key"

    sut.set(key, "some_value")
    value = sut.get(key)

    assert value == "some_value"


def test_multiple_items():
    sut = make_sut()
    sut.set("hello", "world")
    sut.set("foo", "bar")
    sut.set("elden", "ring")
    sut.set("thank", "you")

    assert sut.get("hello") == "world"
    assert sut.get("foo") == "bar"
    assert sut.get("elden") == "ring"
    assert sut.get("thank") == "you"


def test_keys():
    sut = make_sut()
    sut.set("hello", "world")
    sut.set("foo", "bar")

    result = sut.keys()
    expected = ["hello", "foo"]

    for item in expected:
        assert item in result
