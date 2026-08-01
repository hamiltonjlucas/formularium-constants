from gen.messages_pb2 import Empty
from nodes.get_s23sq import get_s23sq


def test_get_s23sq():
    spec = get_s23sq(None, Empty())
    assert spec.symbol == 's23sq'
    assert spec.value == 0.451
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'NuFIT'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.019
