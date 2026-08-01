from gen.messages_pb2 import Empty
from nodes.get_beta0_qcd import get_beta0_qcd


def test_get_beta0_qcd():
    spec = get_beta0_qcd(None, Empty())
    assert spec.symbol == 'beta0_QCD'
    assert spec.value == 9.0
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'definition'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.0
