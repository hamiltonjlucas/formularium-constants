from gen.messages_pb2 import Empty
from nodes.get_v_ub import get_v_ub


def test_get_v_ub():
    spec = get_v_ub(None, Empty())
    assert spec.symbol == 'V_ub'
    assert spec.value == 0.00382
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.0002
