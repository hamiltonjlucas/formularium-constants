from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_mp import get_mp


def test_get_mp():
    spec = get_mp(None, Empty())
    assert spec.symbol == 'm_p'
    assert spec.value == 0.9382720894300001
    assert spec.unit == 'GeV'
    assert spec.tier == 'established'
    assert spec.source == 'CODATA'
    assert spec.mass_dim == 1
    assert spec.uncertainty == 2.9e-10
