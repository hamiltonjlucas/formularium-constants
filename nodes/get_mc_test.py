from gen.messages_pb2 import Empty
from nodes.get_mc import get_mc


def test_get_mc():
    spec = get_mc(None, Empty())
    assert spec.symbol == 'm_c'
    assert spec.value == 1.27
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.02
