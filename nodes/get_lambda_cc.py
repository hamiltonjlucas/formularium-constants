from gen.axiom_context import AxiomContext
from gen.messages_pb2 import ConstantSpec
from gen.messages_pb2 import Empty
from nodes.specs import CONSTANTS

SPEC = CONSTANTS['Lambda_cc']


def get_lambda_cc(ax: AxiomContext, input: Empty) -> ConstantSpec:
    """cosmological constant: 1.0904e-52 ± 2e-54 m^-2 (derived, established). Returns the full spec."""
    m = ConstantSpec(
        symbol=SPEC.symbol, name=SPEC.name, value=SPEC.value, unit=SPEC.unit,
        mass_dim=SPEC.mass_dim, tier=SPEC.tier, source=SPEC.source,
        aliases=SPEC.aliases, notes=SPEC.notes,
        related_formulas=SPEC.related_formulas,
    )
    if SPEC.uncertainty is not None:
        m.uncertainty = SPEC.uncertainty
    return m
