from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_delta_m21_sq import get_delta_m21_sq


def test_get_delta_m21_sq():
    spec = get_delta_m21_sq(None, Empty())
    assert spec.symbol == 'Delta_m21_sq'
    assert spec.value == 7.41e-05
    assert spec.unit == 'eV^2'
    assert spec.tier == 'established'
    assert spec.source == 'NuFIT'
    assert spec.mass_dim == 2
    assert spec.uncertainty == 2.1e-06
