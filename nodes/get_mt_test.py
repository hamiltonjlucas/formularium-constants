from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_mt import get_mt


def test_get_mt():
    spec = get_mt(None, Empty())
    assert spec.symbol == 'm_t'
    assert spec.value == 172.57
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.29
