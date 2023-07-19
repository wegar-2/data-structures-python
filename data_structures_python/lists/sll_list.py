from data_structures_python.nodes.sll_node import SllNode
from pydantic.types import PositiveInt
import typing as t
import pandas as pd


class SllList:

    def __init__(self):
        self.head_node = None
        self.length = 0

    def get_head_node(self) -> t.Union[SllNode, None]:
        return self.head_node

    def get_tail_node(self) -> SllNode:
        node = self.head_node
        while node.get_next_node() is not None:
            node = node.get_next_node()
        return node

    def get_length(self) -> PositiveInt:
        return self.length

    def drop_value(self, value: PositiveInt):
        node = self.head_node
        while node is not None:
            if node.get_next_node().get_value() == value:
                node.set_next_node(node=node.get_next_node().get_next_node())
                break

    def drop_all_values(self, value: PositiveInt):
        node = self.head_node
        while node is not None:
            if node.get_next_node().get_value() == value:
                node.set_next_node(node=node.get_next_node().get_next_node())

    def add_node(self, node: SllNode):
        if self.length == 0:
            node.set_next_node(node=None)
        self.length += 1
        if self.head_node is None:
            self.head_node = node
        else:
            node.set_next_node(node=self.head_node)
            self.head_node = node

    def __str__(self):
        pass

    def get_counts(self) -> pd.DataFrame:
        pass
