from gen.messages_pb2 import Empty
from nodes.get_lambda_qcd import get_lambda_qcd


def test_get_lambda_qcd():
    spec = get_lambda_qcd(None, Empty())
    assert spec.symbol == 'Lambda_QCD'
    assert spec.value == 0.2445
    assert spec.unit == 'GeV'
    assert spec.tier == 'derived'
    assert spec.source == 'derived'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.05
