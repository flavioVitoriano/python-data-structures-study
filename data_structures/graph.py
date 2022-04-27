from __future__ import annotations
from typing import Any, Dict, List

from data_structures.exceptions.graph import (
    NoEdgeFound,
    VertexAlreadyExist,
    VertexDoesNotExist,
)


class Graph:
    adjacency_list: Dict[Any, List[str]]

    def __init__(self) -> None:
        self.adjacency_list = {}

    def __check_vertex_exists(self, vertex: Any):
        return vertex in self.adjacency_list.keys()

    def __add_unidirectional_edge(self, v1: Any, v2: Any):
        if not (self.__check_vertex_exists(v1) and self.__check_vertex_exists(v2)):
            raise VertexDoesNotExist("One or all vertexes provided does not exist")

        self.adjacency_list[v1].append(v2)
        return

    def add_vertex(self, value: Any):
        if self.__check_vertex_exists(value):
            raise VertexAlreadyExist("the provided value already exists")

        self.adjacency_list[value] = []
        return

    def add_edge(self, vertex_one: Any, vertex_two: Any):
        self.__add_unidirectional_edge(vertex_one, vertex_two)
        self.__add_unidirectional_edge(vertex_two, vertex_one)

        return

    def remove_edge(self, vertex_one: Any, vertex_two: Any):
        if not (
            self.__check_vertex_exists(vertex_one)
            and self.__check_vertex_exists(vertex_two)
        ):
            raise VertexDoesNotExist("One or all vertexes provided does not exist")

        try:
            self.adjacency_list[vertex_one].remove(vertex_two)
            self.adjacency_list[vertex_two].remove(vertex_one)
        except ValueError:
            raise NoEdgeFound("vertexes dont have an edge")

        return

    def remove_vertex(self, vertex: Any):
        for key, value in self.adjacency_list.items():
            curated_value = list(filter(lambda item: item != vertex, value))
            self.adjacency_list[key] = curated_value

        try:
            del self.adjacency_list[vertex]
        except KeyError:
            raise VertexDoesNotExist("the specified vertex does not exist")

        return
