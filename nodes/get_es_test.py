from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_es import get_es


def test_get_es():
    spec = get_es(None, Empty())
    assert spec.symbol == 'E_S'
    assert spec.value == 1.32328e+18
    assert spec.unit == 'V/m'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 2
    assert spec.uncertainty == 800000000.0
