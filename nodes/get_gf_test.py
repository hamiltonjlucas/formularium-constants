from gen.messages_pb2 import Empty
from nodes.get_gf import get_gf


def test_get_gf():
    spec = get_gf(None, Empty())
    assert spec.symbol == 'G_F'
    assert spec.value == 1.1663787e-05
    assert spec.unit == 'GeV^-2'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -2
    assert spec.uncertainty == 6e-12
