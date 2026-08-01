from gen.messages_pb2 import Empty
from nodes.get_mw import get_mw


def test_get_mw():
    spec = get_mw(None, Empty())
    assert spec.symbol == 'M_W'
    assert spec.value == 80.377
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.012
