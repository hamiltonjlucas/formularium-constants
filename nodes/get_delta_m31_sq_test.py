from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_delta_m31_sq import get_delta_m31_sq


def test_get_delta_m31_sq():
    spec = get_delta_m31_sq(None, Empty())
    assert spec.symbol == 'Delta_m31_sq'
    assert spec.value == 0.002507
    assert spec.unit == 'eV^2'
    assert spec.tier == 'established'
    assert spec.source == 'NuFIT'
    assert spec.mass_dim == 2
    assert spec.uncertainty == 2.7e-05
