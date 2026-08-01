from gen.messages_pb2 import Empty
from nodes.get_gn import get_gn


def test_get_gn():
    spec = get_gn(None, Empty())
    assert spec.symbol == 'G_N'
    assert spec.value == 6.6743e-11
    assert spec.unit == 'm^3/(kg*s^2)'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -2
    assert spec.uncertainty == 1.5e-15
