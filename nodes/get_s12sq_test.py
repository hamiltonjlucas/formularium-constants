from gen.messages_pb2 import Empty
from nodes.get_s12sq import get_s12sq


def test_get_s12sq():
    spec = get_s12sq(None, Empty())
    assert spec.symbol == 's12sq'
    assert spec.value == 0.303
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'NuFIT'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 0.012
