from __future__ import annotations
import typing as t


class SllNode:

    def __init__(self, value: int):
        self.value = value
        self.next_node = None

    def set_next_node(self, node: t.Union[SllNode, None]):
        self.next_node = node

    def get_next_node(self) -> t.Union[SllNode, None]:
        return self.next_node

    def get_value(self) -> int:
        return self.value
