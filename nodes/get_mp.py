from gen.axiom_context import AxiomContext
from gen.messages_pb2 import ConstantSpec
from gen.messages_pb2 import Empty
from nodes.specs import CONSTANTS

SPEC = CONSTANTS['m_p']


def get_mp(ax: AxiomContext, input: Empty) -> ConstantSpec:
    """proton mass: 0.938272 ± 2.9e-10 GeV (CODATA, established). Returns the full spec."""
    m = ConstantSpec(
        symbol=SPEC.symbol, name=SPEC.name, value=SPEC.value, unit=SPEC.unit,
        mass_dim=SPEC.mass_dim, tier=SPEC.tier, source=SPEC.source,
        aliases=SPEC.aliases, notes=SPEC.notes,
        related_formulas=SPEC.related_formulas,
    )
    if SPEC.uncertainty is not None:
        m.uncertainty = SPEC.uncertainty
    return m
