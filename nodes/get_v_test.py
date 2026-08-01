from gen.messages_pb2 import Empty
from nodes.get_v import get_v


def test_get_v():
    spec = get_v(None, Empty())
    assert spec.symbol == 'v'
    assert spec.value == 246.21965
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 1
