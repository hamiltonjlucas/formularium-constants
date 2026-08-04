from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_catalog import get_catalog


def test_get_catalog():
    m = get_catalog(None, Empty())
    assert len(m.constants) == 71
    assert len(m.domains) == 0
    symbols = {c.symbol for c in m.constants}
    assert len(symbols) == 71
