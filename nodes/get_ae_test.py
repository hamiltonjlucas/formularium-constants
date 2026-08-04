from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_ae import get_ae


def test_get_ae():
    spec = get_ae(None, Empty())
    assert spec.symbol == 'a_e'
    assert spec.value == 0.00115965218059
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 1.3e-12
