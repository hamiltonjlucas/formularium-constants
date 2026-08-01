from gen.messages_pb2 import Empty
from nodes.get_re import get_re


def test_get_re():
    spec = get_re(None, Empty())
    assert spec.symbol == 'r_e'
    assert spec.value == 2.8179403205e-15
    assert spec.unit == 'm'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -1
    assert spec.uncertainty == 1.3e-24
