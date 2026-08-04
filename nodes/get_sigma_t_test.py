from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_sigma_t import get_sigma_t


def test_get_sigma_t():
    spec = get_sigma_t(None, Empty())
    assert spec.symbol == 'sigma_T'
    assert spec.value == 6.6524587051e-29
    assert spec.unit == 'm^2'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -2
    assert spec.uncertainty == 6.2e-38
