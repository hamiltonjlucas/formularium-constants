from gen.messages_pb2 import Empty
from nodes.get_mb import get_mb


def test_get_mb():
    spec = get_mb(None, Empty())
    assert spec.symbol == 'm_b'
    assert spec.value == 4.18
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.03
