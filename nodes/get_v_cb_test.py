from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_v_cb import get_v_cb


def test_get_v_cb():
    spec = get_v_cb(None, Empty())
    assert spec.symbol == 'V_cb'
    assert spec.value == 0.041
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.0014
