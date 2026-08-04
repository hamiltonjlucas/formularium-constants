from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_sin2_thetaw import get_sin2_thetaw


def test_get_sin2_thetaw():
    spec = get_sin2_thetaw(None, Empty())
    assert spec.symbol == 'sin2_thetaW'
    assert spec.value == 0.23122
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'PDG'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 4e-05
