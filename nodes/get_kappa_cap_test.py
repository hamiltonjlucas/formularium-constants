from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_kappa_cap import get_kappa_cap


def test_get_kappa_cap():
    spec = get_kappa_cap(None, Empty())
    assert spec.symbol == 'kappa_cap'
    assert spec.value == 9.5702e+68
    assert spec.unit == 'm^-2'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 2
    assert spec.uncertainty == 2.2e+64
