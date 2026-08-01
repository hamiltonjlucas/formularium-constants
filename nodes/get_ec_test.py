from gen.messages_pb2 import Empty
from nodes.get_ec import get_ec


def test_get_ec():
    spec = get_ec(None, Empty())
    assert spec.symbol == 'e_C'
    assert spec.value == 1.602176634e-19
    assert spec.unit == 'C'
    assert spec.tier == 'established'
    assert spec.source == 'definition'
    assert spec.mass_dim == 0
