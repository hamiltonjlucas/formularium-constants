from gen.axiom_context import AxiomContext
from gen.messages_pb2 import ConstantSpec
from gen.messages_pb2 import Empty
from nodes.specs import CONSTANTS

SPEC = CONSTANTS['S_NS_max']


def get_s_ns_max(ax: AxiomContext, input: Empty) -> ConstantSpec:
    """no-signaling CHSH maximum (PR box): 4 dimensionless (derived, established). Returns the full spec."""
    m = ConstantSpec(
        symbol=SPEC.symbol, name=SPEC.name, value=SPEC.value, unit=SPEC.unit,
        mass_dim=SPEC.mass_dim, tier=SPEC.tier, source=SPEC.source,
        aliases=SPEC.aliases, notes=SPEC.notes,
        related_formulas=SPEC.related_formulas,
    )
    if SPEC.uncertainty is not None:
        m.uncertainty = SPEC.uncertainty
    return m
