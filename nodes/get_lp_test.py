from gen.messages_pb2 import Empty
from nodes.get_lp import get_lp


def test_get_lp():
    spec = get_lp(None, Empty())
    assert spec.symbol == 'l_P'
    assert spec.value == 1.616255e-35
    assert spec.unit == 'm'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == -1
    assert spec.uncertainty == 1.8e-40
