from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_alpha_s import get_alpha_s


def test_get_alpha_s():
    spec = get_alpha_s(None, Empty())
    assert spec.symbol == 'alpha_s'
    assert spec.value == 0.1179
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.001
