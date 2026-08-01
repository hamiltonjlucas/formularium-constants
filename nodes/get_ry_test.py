from gen.messages_pb2 import Empty
from nodes.get_ry import get_ry


def test_get_ry():
    spec = get_ry(None, Empty())
    assert spec.symbol == 'Ry'
    assert spec.value == 13.60569312299
    assert spec.unit == 'eV'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 1.5e-11
