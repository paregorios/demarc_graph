#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Define bibliographic references
"""

from .bibliography import (
    citation_contexts,
    citation_reasons,
    works_cited_by_short_title,
)
from pprint import pformat
from .rdf import NS_CITO, NS_DCTERMS, NS_DEMARC, NS_RDF
from rdflib import URIRef, Literal, Graph
from typing import List, Tuple
from uuid import uuid4


class Reference:

    def __init__(self, id: str, short_title: str, reason: str, context: dict = {}):
        self.id = id
        self.type = NS_DEMARC["Reference"]

        try:
            work_uri = works_cited_by_short_title[short_title]
        except KeyError:
            raise ValueError(
                f"Short title '{short_title}' not found in works cited:\n{pformat(works_cited_by_short_title, indent=2)}"
            )
        self.work_uri = work_uri

        if reason not in citation_reasons:
            raise ValueError(f"Invalid citation reason: {reason}")
        self.reason = reason

        self.contexts = {}
        for context_key, context_value in context.items():
            try:
                context_uri = citation_contexts[context_key]
            except KeyError:
                raise ValueError(f"Invalid citation context: {context_key}")
            self.contexts[context_key] = context_value

    def rdf(self) -> List[Tuple[None | URIRef, URIRef, URIRef | Literal]]:
        """returns predicate and object, but reference doesn't know the ID"""
        self_uri = URIRef(self.id)

        results = [
            (None, NS_DCTERMS["references"], self_uri),
            self.type_rdf,
            (self_uri, citation_reasons[self.reason], URIRef(self.work_uri)),
        ]
        for context_key, context_value in self.contexts.items():
            results.append(
                (self_uri, citation_contexts[context_key], Literal(context_value))
            )
        return results

    @property
    def type_rdf(self) -> Tuple[URIRef, URIRef, URIRef]:
        return (URIRef(self.id), NS_RDF.type, URIRef(self.type))
