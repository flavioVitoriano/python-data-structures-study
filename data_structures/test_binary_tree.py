from .binary_tree import BinaryTree


def make_sut():
    return BinaryTree()


def test_insert_root():
    sut = make_sut()
    value = 10

    sut.insert(value)

    assert sut.root.value == value


def test_insert_left():
    sut = make_sut()
    value = 10
    left_value = 9

    sut.insert(value)
    sut.insert(left_value)

    assert sut.root.left.value == left_value


def test_insert_right():
    sut = make_sut()
    value = 10
    right_value = 11

    sut.insert(value)
    sut.insert(right_value)

    assert sut.root.right.value == right_value


def test_tree_with_existent_value():
    sut = make_sut()
    root = 10

    sut.insert(root)
    result = sut.insert(10)

    assert result is False


def test_contains():
    sut = make_sut()
    sut.insert(10)
    sut.insert(20)
    sut.insert(9)
    sut.insert(5)

    expected_true = sut.contains(9)
    expected_false = sut.contains(6)

    assert expected_true is True
    assert expected_false is False


def test_min_value():
    sut = make_sut()
    sut.insert(10)
    sut.insert(14)
    sut.insert(1)
    sut.insert(4)
    sut.insert(13)

    all_tree_min_value = sut.min_value_node()
    right_side_min_value = sut.min_value_node(sut.root.right)

    assert all_tree_min_value.value == 1
    assert right_side_min_value.value == 13


def test_max_value():
    sut = make_sut()
    sut.insert(10)
    sut.insert(14)
    sut.insert(1)
    sut.insert(4)
    sut.insert(13)

    all_tree_max_value = sut.max_value_node()
    right_side_max_value = sut.max_value_node(sut.root.left)

    assert all_tree_max_value.value == 14
    assert right_side_max_value.value == 4
