from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_mp_me import get_mp_me


def test_get_mp_me():
    spec = get_mp_me(None, Empty())
    assert spec.symbol == 'mp_me'
    assert spec.value == 1836.152673426
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 3.2e-08
