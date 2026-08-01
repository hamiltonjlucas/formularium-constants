from gen.axiom_context import AxiomContext
from gen.messages_pb2 import ConstantSpec
from gen.messages_pb2 import Empty
from nodes.specs import CONSTANTS

SPEC = CONSTANTS['V_ub']


def get_v_ub(ax: AxiomContext, input: Empty) -> ConstantSpec:
    """CKM |V_ub|: 0.00382 ± 0.0002 dimensionless (PDG, established). Returns the full spec."""
    m = ConstantSpec(
        symbol=SPEC.symbol, name=SPEC.name, value=SPEC.value, unit=SPEC.unit,
        mass_dim=SPEC.mass_dim, tier=SPEC.tier, source=SPEC.source,
        aliases=SPEC.aliases, notes=SPEC.notes,
        related_formulas=SPEC.related_formulas,
    )
    if SPEC.uncertainty is not None:
        m.uncertainty = SPEC.uncertainty
    return m
