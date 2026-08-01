from gen.messages_pb2 import Empty
from nodes.get_me import get_me


def test_get_me():
    spec = get_me(None, Empty())
    assert spec.symbol == 'm_e'
    assert spec.value == 0.0005109989506900001
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == 1
