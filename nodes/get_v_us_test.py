from gen.messages_pb2 import Empty
from nodes.get_v_us import get_v_us


def test_get_v_us():
    spec = get_v_us(None, Empty())
    assert spec.symbol == 'V_us'
    assert spec.value == 0.2243
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.0008
