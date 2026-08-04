from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_mh import get_mh


def test_get_mh():
    spec = get_mh(None, Empty())
    assert spec.symbol == 'm_H'
    assert spec.value == 125.25
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 0.17
