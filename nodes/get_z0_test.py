from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_z0 import get_z0


def test_get_z0():
    spec = get_z0(None, Empty())
    assert spec.symbol == 'Z_0'
    assert spec.value == 376.730313412
    assert spec.unit == 'ohm'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 5.9e-08
