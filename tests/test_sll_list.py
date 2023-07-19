from data_structures_python import SllList
from data_structures_python import SllNode


def test_sll_list_constructor():
    empty_sll_list = SllList()
    assert isinstance(empty_sll_list, SllList) is True


def test_add_nodes():
    sll_list = SllList()
    node1 = SllNode(value=23)
    node2 = SllNode(value=111)
    sll_list.add_node(node=node1)
    sll_list.add_node(node=node2)
    assert sll_list.get_length() == 2


def test_head_tail_getters():
    sll_list = SllList()
    node1 = SllNode(value=23)
    node2 = SllNode(value=111)
    node3 = SllNode(value=901)
    sll_list.add_node(node=node1)
    sll_list.add_node(node=node2)
    sll_list.add_node(node=node3)
    assert sll_list.get_head_node().get_value() == 901
    assert sll_list.get_tail_node().get_value() == 23
    assert sll_list.get_length() == 3


def test_drop_value():
    pass


def test_drop_all_values():
    pass
