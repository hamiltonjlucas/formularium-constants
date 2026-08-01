from gen.messages_pb2 import Empty
from nodes.get_r_gas import get_r_gas


def test_get_r_gas():
    spec = get_r_gas(None, Empty())
    assert spec.symbol == 'R_gas'
    assert spec.value == 8.31446261815324
    assert spec.unit == 'J/(mol*K)'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
