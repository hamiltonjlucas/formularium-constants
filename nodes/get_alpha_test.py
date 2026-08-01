from gen.messages_pb2 import Empty
from nodes.get_alpha import get_alpha


def test_get_alpha():
    spec = get_alpha(None, Empty())
    assert spec.symbol == 'alpha'
    assert spec.value == 0.0072973525643
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 1.1e-12
