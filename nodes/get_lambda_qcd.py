from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_types_messages_pb2 import ConstantSpec, Empty
from nodes.specs import CONSTANTS

SPEC = CONSTANTS['Lambda_QCD']


def get_lambda_qcd(ax: AxiomContext, input: Empty) -> ConstantSpec:
    """QCD scale (1-loop nf=3 estimate): 0.2445 ± 0.05 GeV (derived, derived). Returns the full spec."""
    m = ConstantSpec(
        symbol=SPEC.symbol, name=SPEC.name, value=SPEC.value, unit=SPEC.unit,
        mass_dim=SPEC.mass_dim, tier=SPEC.tier, source=SPEC.source,
        aliases=SPEC.aliases, notes=SPEC.notes,
        related_formulas=SPEC.related_formulas,
    )
    if SPEC.uncertainty is not None:
        m.uncertainty = SPEC.uncertainty
    return m
