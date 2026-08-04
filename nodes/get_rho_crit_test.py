from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_rho_crit import get_rho_crit


def test_get_rho_crit():
    spec = get_rho_crit(None, Empty())
    assert spec.symbol == 'rho_crit'
    assert spec.value == 8.53e-27
    assert spec.unit == 'kg/m^3'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 4
