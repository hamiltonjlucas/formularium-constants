from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_n_ds import get_n_ds


def test_get_n_ds():
    spec = get_n_ds(None, Empty())
    assert spec.symbol == 'N_dS'
    assert spec.value == 3.309e+122
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 6e+120
