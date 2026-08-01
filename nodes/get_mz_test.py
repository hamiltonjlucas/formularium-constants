from gen.messages_pb2 import Empty
from nodes.get_mz import get_mz


def test_get_mz():
    spec = get_mz(None, Empty())
    assert spec.symbol == 'M_Z'
    assert spec.value == 91.1876
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.0021
