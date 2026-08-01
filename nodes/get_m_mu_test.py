from gen.messages_pb2 import Empty
from nodes.get_m_mu import get_m_mu


def test_get_m_mu():
    spec = get_m_mu(None, Empty())
    assert spec.symbol == 'm_mu'
    assert spec.value == 0.1056583755
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
