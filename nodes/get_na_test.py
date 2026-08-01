from gen.messages_pb2 import Empty
from nodes.get_na import get_na


def test_get_na():
    spec = get_na(None, Empty())
    assert spec.symbol == 'N_A'
    assert spec.value == 6.02214076e+23
    assert spec.unit == 'mol^-1'
    assert spec.tier == 'established'
    assert spec.source == 'definition'
    assert spec.mass_dim == 0
