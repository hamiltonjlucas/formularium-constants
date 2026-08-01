from gen.messages_pb2 import Empty
from nodes.get_lambda_cc import get_lambda_cc


def test_get_lambda_cc():
    spec = get_lambda_cc(None, Empty())
    assert spec.symbol == 'Lambda_cc'
    assert spec.value == 1.0904e-52
    assert spec.unit == 'm^-2'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 2
    assert spec.uncertainty == 2e-54
