from gen.messages_pb2 import Empty
from nodes.get_mu_b import get_mu_b


def test_get_mu_b():
    spec = get_mu_b(None, Empty())
    assert spec.symbol == 'mu_B'
    assert spec.value == 9.2740100657e-24
    assert spec.unit == 'J/T'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -1
    assert spec.uncertainty == 2.9e-33
