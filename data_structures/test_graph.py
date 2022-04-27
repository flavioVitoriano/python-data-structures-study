from data_structures.exceptions.graph import (
    NoEdgeFound,
    VertexAlreadyExist,
    VertexDoesNotExist,
)
from data_structures.graph import Graph
import pytest


def make_sut():
    return Graph()


def test_add_vertex():
    sut = make_sut()
    sut.add_vertex("test 1")

    assert sut.adjacency_list["test 1"] == []

    with pytest.raises(VertexAlreadyExist):
        sut.add_vertex("test 1")


def test_add_edge():
    sut = make_sut()

    sut.add_vertex("vertex 1")
    sut.add_vertex("vertex 2")

    sut.add_edge("vertex 1", "vertex 2")

    assert sut.adjacency_list["vertex 1"] == ["vertex 2"]
    assert sut.adjacency_list["vertex 2"] == ["vertex 1"]

    with pytest.raises(VertexDoesNotExist):
        sut.add_edge("vertex 3", "vertex 1")


def test_remove_edge():
    sut = make_sut()
    print(sut.adjacency_list.keys())

    sut.add_vertex("vertex 1")
    sut.add_vertex("vertex 2")

    sut.add_edge("vertex 1", "vertex 2")

    sut.remove_edge("vertex 1", "vertex 2")

    assert sut.adjacency_list["vertex 1"] == []
    assert sut.adjacency_list["vertex 2"] == []

    with pytest.raises(NoEdgeFound):
        sut.remove_edge("vertex 1", "vertex 2")

    with pytest.raises(VertexDoesNotExist):
        sut.remove_edge("vertex 3", "vertex 2")


def test_remove_vertex():
    sut = make_sut()

    sut.add_vertex("v1")
    sut.add_vertex("v2")

    sut.add_edge("v1", "v2")

    sut.remove_vertex("v1")

    assert sut.adjacency_list["v2"] == []
    assert list(sut.adjacency_list.keys()) == ["v2"]

    with pytest.raises(VertexDoesNotExist):
        sut.remove_vertex("v1")
