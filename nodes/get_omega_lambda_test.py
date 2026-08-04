from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_omega_lambda import get_omega_lambda


def test_get_omega_lambda():
    spec = get_omega_lambda(None, Empty())
    assert spec.symbol == 'Omega_Lambda'
    assert spec.value == 0.6847
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'Planck'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.0073
