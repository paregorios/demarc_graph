#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Bibliography
"""

from pathlib import Path
from .rdf import NS_BIBO, NS_CITO, NS_ZOTERO
from rdflib import Graph

works_cited_path = Path(__file__).parent.parent.parent / "data" / "works_cited"
works_cited_graph = Graph()
for rdf_file in works_cited_path.glob("*.rdf"):
    works_cited_graph.parse(rdf_file)
works_cited_by_short_title = dict()
for s, p, o in works_cited_graph.triples((None, NS_ZOTERO["shortTitle"], None)):
    works_cited_by_short_title[str(o)] = str(s)

citation_reasons = {
    "citesAsRelated": NS_CITO["citesAsRelated"],
}

citation_contexts = {
    "locator": NS_BIBO["locator"],
    "pageStart": NS_BIBO["pageStart"],
    "pageEnd": NS_BIBO["pageEnd"],
}
