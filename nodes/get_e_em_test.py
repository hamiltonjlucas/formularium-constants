from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_e_em import get_e_em


def test_get_e_em():
    spec = get_e_em(None, Empty())
    assert spec.symbol == 'e_em'
    assert spec.value == 0.3028221207683449
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
