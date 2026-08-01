from gen.messages_pb2 import Empty
from nodes.get_hbar import get_hbar


def test_get_hbar():
    spec = get_hbar(None, Empty())
    assert spec.symbol == 'hbar'
    assert spec.value == 1.0545718176461565e-34
    assert spec.unit == 'J*s'
    assert spec.tier == 'established'
    assert spec.source == 'definition'
    assert spec.mass_dim == 0
