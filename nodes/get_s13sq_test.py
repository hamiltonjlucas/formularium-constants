from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_s13sq import get_s13sq


def test_get_s13sq():
    spec = get_s13sq(None, Empty())
    assert spec.symbol == 's13sq'
    assert spec.value == 0.02225
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'NuFIT'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.00059
