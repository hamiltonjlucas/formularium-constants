from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_s_tsirelson import get_s_tsirelson


def test_get_s_tsirelson():
    spec = get_s_tsirelson(None, Empty())
    assert spec.symbol == 'S_Tsirelson'
    assert spec.value == 2.8284271247461903
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
