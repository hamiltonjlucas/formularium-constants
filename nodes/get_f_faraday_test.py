from gen.messages_pb2 import Empty
from nodes.get_f_faraday import get_f_faraday


def test_get_f_faraday():
    spec = get_f_faraday(None, Empty())
    assert spec.symbol == 'F_faraday'
    assert spec.value == 96485.33212331001
    assert spec.unit == 'C/mol'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
