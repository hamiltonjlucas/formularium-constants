from gen.messages_pb2 import Empty
from nodes.get_s_ic_triv import get_s_ic_triv


def test_get_s_ic_triv():
    spec = get_s_ic_triv(None, Empty())
    assert spec.symbol == 'S_IC_triv'
    assert spec.value == 3.265986323710904
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
