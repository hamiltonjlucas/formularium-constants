from gen.messages_pb2 import Empty
from nodes.get_a_wolf import get_a_wolf


def test_get_a_wolf():
    spec = get_a_wolf(None, Empty())
    assert spec.symbol == 'A_wolf'
    assert spec.value == 0.826
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.012
