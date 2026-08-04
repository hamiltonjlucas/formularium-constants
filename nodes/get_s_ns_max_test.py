from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_s_ns_max import get_s_ns_max


def test_get_s_ns_max():
    spec = get_s_ns_max(None, Empty())
    assert spec.symbol == 'S_NS_max'
    assert spec.value == 4.0
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
