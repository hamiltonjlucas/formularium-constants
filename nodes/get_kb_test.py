from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_kb import get_kb


def test_get_kb():
    spec = get_kb(None, Empty())
    assert spec.symbol == 'k_B'
    assert spec.value == 1.380649e-23
    assert spec.unit == 'J/K'
    assert spec.tier == 'established'
    assert spec.source == 'definition'
    assert spec.mass_dim == 0
