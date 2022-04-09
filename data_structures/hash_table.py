from typing import List, Any


class HashTable:
    data_map: List

    def __init__(self, size: int = 7):
        self.data_map = [None] * size

    def __hash(self, key: str) -> int:
        final_hash = 0

        for char in key:
            final_hash = (final_hash + ord(char) * 31) % len(self.data_map)

        return final_hash

    def __find_key(self, space_list: list[Any], key: str) -> int:
        keys = map(lambda item: item[0], space_list)

        if key not in keys:
            return None

        for index, item in enumerate(space_list):
            if item[0] == key:
                return index
        return None

    def set(self, key: str, value: Any):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        space_index = self.__find_key(self.data_map[index], key)

        if space_index is None:
            self.data_map[index].append((key, value))
            return

        self.data_map[index][space_index] = (key, value)
        return

    def get(self, key: str) -> Any:
        index = self.__hash(key)

        if self.data_map[index] is None:
            return None

        space_index = self.__find_key(self.data_map[index], key)

        if space_index is None:
            return None

        return self.data_map[index][space_index][1]

    def keys(self):
        keys = []

        for space in self.data_map:
            if space is None:
                continue

            space_keys = list(map(lambda pair: pair[0], space))
            keys.extend(space_keys)

        return keys
