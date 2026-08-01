from gen.messages_pb2 import Empty
from nodes.get_mn import get_mn


def test_get_mn():
    spec = get_mn(None, Empty())
    assert spec.symbol == 'm_n'
    assert spec.value == 0.93956542194
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 4.8e-10
