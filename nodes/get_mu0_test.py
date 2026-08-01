from gen.messages_pb2 import Empty
from nodes.get_mu0 import get_mu0


def test_get_mu0():
    spec = get_mu0(None, Empty())
    assert spec.symbol == 'mu_0'
    assert spec.value == 1.25663706127e-06
    assert spec.unit == 'N/A^2'
    assert spec.tier == 'established'
    assert spec.source == 'convention'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 2e-16
