from gen.axiom_context import AxiomContext
from gen.messages_pb2 import ConstantSpec
from gen.messages_pb2 import Empty
from nodes.specs import CONSTANTS

SPEC = CONSTANTS['Delta_m32_sq']


def get_delta_m32_sq(ax: AxiomContext, input: Empty) -> ConstantSpec:
    """Delta m^2_32 neutrino splitting: 0.0024329 ± 2.7e-05 eV^2 (derived, derived). Returns the full spec."""
    m = ConstantSpec(
        symbol=SPEC.symbol, name=SPEC.name, value=SPEC.value, unit=SPEC.unit,
        mass_dim=SPEC.mass_dim, tier=SPEC.tier, source=SPEC.source,
        aliases=SPEC.aliases, notes=SPEC.notes,
        related_formulas=SPEC.related_formulas,
    )
    if SPEC.uncertainty is not None:
        m.uncertainty = SPEC.uncertainty
    return m
