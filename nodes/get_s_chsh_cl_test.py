from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_s_chsh_cl import get_s_chsh_cl


def test_get_s_chsh_cl():
    spec = get_s_chsh_cl(None, Empty())
    assert spec.symbol == 'S_CHSH_cl'
    assert spec.value == 2.0
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
