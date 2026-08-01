from gen.messages_pb2 import Empty
from nodes.get_h0 import get_h0


def test_get_h0():
    spec = get_h0(None, Empty())
    assert spec.symbol == 'H_0'
    assert spec.value == 67.4
    assert spec.unit == 'km/s/Mpc'
    assert spec.tier == 'established'
    assert spec.source == 'Planck'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.5
