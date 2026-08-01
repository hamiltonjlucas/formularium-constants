from gen.messages_pb2 import Empty
from nodes.get_sigma_sb import get_sigma_sb


def test_get_sigma_sb():
    spec = get_sigma_sb(None, Empty())
    assert spec.symbol == 'sigma_SB'
    assert spec.value == 5.6703744191844314e-08
    assert spec.unit == 'W/(m^2*K^4)'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
