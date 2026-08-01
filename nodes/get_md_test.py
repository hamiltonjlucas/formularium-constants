from gen.messages_pb2 import Empty
from nodes.get_md import get_md


def test_get_md():
    spec = get_md(None, Empty())
    assert spec.symbol == 'm_d'
    assert spec.value == 0.00467
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.0005
