from gen.messages_pb2 import Empty
from nodes.get_lambda_c import get_lambda_c


def test_get_lambda_c():
    spec = get_lambda_c(None, Empty())
    assert spec.symbol == 'lambda_C'
    assert spec.value == 2.42631023538e-12
    assert spec.unit == 'm'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == -1
    assert spec.uncertainty == 7.6e-22
