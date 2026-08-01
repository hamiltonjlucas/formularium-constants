from gen.messages_pb2 import Empty
from nodes.get_a0 import get_a0


def test_get_a0():
    spec = get_a0(None, Empty())
    assert spec.symbol == 'a_0'
    assert spec.value == 5.29177210544e-11
    assert spec.unit == 'm'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -1
    assert spec.uncertainty == 8.2e-21
