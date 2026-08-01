from gen.messages_pb2 import Empty
from nodes.get_mu import get_mu


def test_get_mu():
    spec = get_mu(None, Empty())
    assert spec.symbol == 'm_u'
    assert spec.value == 0.00216
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.0005
