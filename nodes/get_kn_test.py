from gen.messages_pb2 import Empty
from nodes.get_kn import get_kn


def test_get_kn():
    spec = get_kn(None, Empty())
    assert spec.symbol == 'k_N'
    assert spec.value == 3.842
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'derived'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.5
