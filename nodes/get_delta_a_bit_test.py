from gen.messages_pb2 import Empty
from nodes.get_delta_a_bit import get_delta_a_bit


def test_get_delta_a_bit():
    spec = get_delta_a_bit(None, Empty())
    assert spec.symbol == 'Delta_A_bit'
    assert spec.value == 7.2428e-70
    assert spec.unit == 'm^2'
    assert spec.tier == 'conjecture'
    assert spec.source == 'derived'
    assert spec.mass_dim == -2
    assert spec.uncertainty == 1.6e-74
