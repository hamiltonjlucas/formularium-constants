from gen.messages_pb2 import Empty
from nodes.get_m_tau import get_m_tau


def test_get_m_tau():
    spec = get_m_tau(None, Empty())
    assert spec.symbol == 'm_tau'
    assert spec.value == 1.77686
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.00012
