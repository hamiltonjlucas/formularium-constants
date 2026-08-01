from gen.messages_pb2 import Empty
from nodes.get_tp import get_tp


def test_get_tp():
    spec = get_tp(None, Empty())
    assert spec.symbol == 't_P'
    assert spec.value == 5.391247e-44
    assert spec.unit == 's'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == -1
    assert spec.uncertainty == 6e-49
