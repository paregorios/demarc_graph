#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
from demarc_graph.entities import Entity, Label
from demarc_graph.rdf import NS_RDFS
import logging
from pytest import raises
from rdflib import URIRef, Literal

"""
Test the entities module
"""

logging.getLogger("normalize_space").setLevel(logging.WARNING)


class TestLabel:
    def test_label(self):
        label = Label("Jenni")
        assert label.value == "Jenni"
        assert label.lang == "en"

    def test_label_fr(self):
        label = Label("Henri", lang="fr")
        assert label.value == "Henri"
        assert label.lang == "fr"

    def test_label_bad_lang(self):
        with raises(ValueError):
            Label("Frank", lang="foobar")


class TestEntity:
    def test_init(self):
        e = Entity("https://example.com/8675309")
        assert e.id == "https://example.com/8675309"

    def test_id_bad(self):
        with raises(ValueError):
            Entity("8675309")

    def test_label(self):
        e = Entity("https://example.com/8675309")
        assert e.labels == []
        e.add_label("Jenni")
        assert len(e.labels) == 1
        assert e.labels[0] == "Jenni"

    def test_labels(self):
        e = Entity("https://example.com/8675309")
        e.add_label("Jenni")
        e.add_label("Henri", "fr")
        assert len(e.labels) == 2
        assert set(e.labels) == {"Jenni", "Henri"}
        assert len(e.labels_rdf) == 2
