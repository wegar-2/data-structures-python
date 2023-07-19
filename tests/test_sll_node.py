from data_structures_python import SllNode


def test_node_constructor():
    node = SllNode(value=22)
    assert isinstance(node, SllNode) is True


def test_get_value():
    node = SllNode(value=232)
    assert node.get_value() == 232


def test_set_get_next_node():
    node1 = SllNode(value=8741)
    node2 = SllNode(value=5612)
    node1.set_next_node(node=node2)
    assert node1.get_next_node().get_value() == node2.get_value()
