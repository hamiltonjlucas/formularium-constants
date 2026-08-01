from gen.messages_pb2 import Empty
from nodes.get_m_pl import get_m_pl


def test_get_m_pl():
    spec = get_m_pl(None, Empty())
    assert spec.symbol == 'M_Pl'
    assert spec.value == 1.22089e+19
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 1
