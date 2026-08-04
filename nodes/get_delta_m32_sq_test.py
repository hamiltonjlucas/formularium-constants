from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_delta_m32_sq import get_delta_m32_sq


def test_get_delta_m32_sq():
    spec = get_delta_m32_sq(None, Empty())
    assert spec.symbol == 'Delta_m32_sq'
    assert spec.value == 0.0024329
    assert spec.unit == 'eV^2'
    assert spec.tier == 'derived'
    assert spec.source == 'derived'
    assert spec.mass_dim == 2
    assert spec.uncertainty == 2.7e-05
