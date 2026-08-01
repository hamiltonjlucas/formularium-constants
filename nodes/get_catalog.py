from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_types_messages_pb2 import Catalog
from gen.messages_pb2 import Empty
from nodes.specs import CONSTANTS


def get_catalog(ax: AxiomContext, input: Empty) -> Catalog:
    """Every Formularium constant spec, as a Catalog (domain slices left to the domain packages)."""
    m = Catalog()
    for c in CONSTANTS.values():
        entry = m.constants.add(
            symbol=c.symbol, name=c.name, value=c.value, unit=c.unit,
            mass_dim=c.mass_dim, tier=c.tier, source=c.source,
            aliases=c.aliases, notes=c.notes,
            related_formulas=c.related_formulas,
        )
        if c.uncertainty is not None:
            entry.uncertainty = c.uncertainty
    return m
