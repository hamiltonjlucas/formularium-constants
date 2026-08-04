from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_b_wien import get_b_wien


def test_get_b_wien():
    spec = get_b_wien(None, Empty())
    assert spec.symbol == 'b_wien'
    assert spec.value == 0.002897771955
    assert spec.unit == 'm*K'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
