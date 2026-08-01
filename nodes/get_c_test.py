from gen.messages_pb2 import Empty
from nodes.get_c import get_c


def test_get_c():
    spec = get_c(None, Empty())
    assert spec.symbol == 'c'
    assert spec.value == 299792458.0
    assert spec.unit == 'm/s'
    assert spec.tier == 'established'
    assert spec.source == 'definition'
    assert spec.mass_dim == 0
