from gen.messages_pb2 import Empty
from nodes.get_ms import get_ms


def test_get_ms():
    spec = get_ms(None, Empty())
    assert spec.symbol == 'm_s'
    assert spec.value == 0.0934
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.008
