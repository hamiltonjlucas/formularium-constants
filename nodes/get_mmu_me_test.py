from gen.messages_pb2 import Empty
from nodes.get_mmu_me import get_mmu_me


def test_get_mmu_me():
    spec = get_mmu_me(None, Empty())
    assert spec.symbol == 'mmu_me'
    assert spec.value == 206.7682827
    assert spec.unit == 'dimensionless'
    assert spec.tier == 'established'
    assert spec.source == 'derived'
    assert spec.mass_dim == 0
    assert spec.uncertainty == 4.6e-06
