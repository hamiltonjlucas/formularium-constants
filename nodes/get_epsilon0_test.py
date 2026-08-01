from gen.messages_pb2 import Empty
from nodes.get_epsilon0 import get_epsilon0


def test_get_epsilon0():
    spec = get_epsilon0(None, Empty())
    assert spec.symbol == 'epsilon_0'
    assert spec.value == 8.8541878188e-12
    assert spec.unit == 'F/m'
    assert spec.tier == 'established'
    assert spec.source == 'convention'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 1.4e-21
