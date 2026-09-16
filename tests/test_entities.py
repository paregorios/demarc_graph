#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
from demarc_graph.entities import Entity
from demarc_graph.rdf import NS_RDFS
from pytest import raises
from rdflib import URIRef, Literal

"""
Test the entities module
"""


class TestEntity:
    def test_init(self):
        e = Entity("https://example.com/8675309")
        assert e.id == "https://example.com/8675309"

    def test_id_bad(self):
        with raises(ValueError):
            Entity("8675309")

    def test_label(self):
        e = Entity("https://example.com/8675309")
        assert e.label == ""
        e.label = "Jenni"
        assert e.label == "Jenni"
        assert e.label_rdf == (
            URIRef("https://example.com/8675309"),
            NS_RDFS.label,
            Literal("Jenni"),
        )
        del e.label
        assert e.label == ""
