from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_r_inf import get_r_inf


def test_get_r_inf():
    spec = get_r_inf(None, Empty())
    assert spec.symbol == 'R_inf'
    assert spec.value == 10973731.568157
    assert spec.unit == 'm^-1'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 1.2e-05
