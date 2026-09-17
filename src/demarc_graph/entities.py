#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Define entity base class
"""

from language_tags import tags
import logging
from pprint import pformat
from rdflib import URIRef, Literal, Graph
from .rdf import *
from .references import Reference
from .text import norm
from typing import List, Tuple
from validators import url as valid_uri


class Label:
    """
    Base class for an RDFS label
    """

    def __init__(self, value: str, lang: str = "en"):
        self._value = ""
        self._lang = ""
        self.value = value
        self.lang = lang

    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        clean_value = norm(val)
        if not clean_value:
            raise ValueError(
                f"Label cannot be zero length string after whitespace normalization. Original value: '{val}'"
            )
        self._value = clean_value

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, value: str):
        logger = logging.getLogger("Label::lang.setter")
        clean_value = norm(value)
        if tags.check(clean_value):
            self._lang = clean_value
        else:
            raise ValueError(
                f"Invalid lang tag {clean_value}: {"; ".join([err.message.strip() for err in tags.tag(value).errors if err.message.strip()])}"
            )

    def rdf(self) -> Tuple[URIRef, Literal]:
        """returns predicate and object, but label doesn't know the ID"""
        return (NS_RDFS.label, Literal(self.value, lang=self.lang))


class Entity:
    """
    Base class for various entities of interest
    """

    def __init__(self, id: str, type: str):
        self._id = ""
        self.id = id
        if not valid_uri(type):
            raise ValueError(f"entity type must be an HTTPs URI, but '{type}' is not.")
        self._type = type
        self._labels = dict()  # by language tag
        self._references = list()  # references to external works

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        if valid_uri(value):
            self._id = value
        else:
            raise ValueError(f"entity ID must be an HTTPs URI, but '{value}' is not.")

    @property
    def labels(self) -> list:
        result = set()
        for some_labels in self._labels.values():
            result.update([label.value for label in some_labels])
        return list(result)

    def add_label(self, value: str, lang: str = "en"):
        label = Label(value, lang)
        try:
            self._labels[lang]
        except KeyError:
            self._labels[lang] = []
        self._labels[lang].append(label)

    def get_labels(self, lang: str = "") -> list:
        results = list()
        if not lang:
            for lang_key, labels in self._labels.items():
                results.extend([l.value for l in labels])
            return results

        if not tags.check(lang):
            raise ValueError(
                f"Invalid lang tag {lang}: {"; ".join(tags.tag(lang).errors)}"
            )
        try:
            labels = self._labels[lang]
        except KeyError:
            return []
        return [l.value for l in labels]

    @property
    def labels_rdf(self) -> List[Tuple[URIRef, URIRef, Literal]]:
        """serialize labels as RDF triples"""
        logger = logging.getLogger("Entity.labels_rdf")
        results = []
        for labels in self._labels.values():
            for label in labels:
                results.append(
                    (
                        URIRef(self.id),
                        NS_RDFS.label,
                        Literal(label.value, lang=label.lang),
                    )
                )
        return results

    @property
    def rdf(self) -> List[Tuple[URIRef, URIRef, URIRef | Literal]]:
        """returns a list of RDF triples for this entity"""
        results = [self.type_rdf]
        results.extend(self.labels_rdf)  # type: ignore
        results.extend(self.references_rdf)  # type: ignore
        return results  # type: ignore

    @property
    def references(self) -> List[Reference]:
        """returns a list of references that cite this entity"""
        return self._references

    def add_reference(self, reference: Reference):
        self._references.append(reference)

    @property
    def references_rdf(self) -> List[Tuple[URIRef, URIRef, URIRef | Literal]]:
        reference_triples = []
        for reference in self._references:
            these_triples = reference.rdf()
            if these_triples[0][0] is None:
                # the reference doesn't know the ID of the entity it cites, so we add it here
                these_triples[0] = (
                    URIRef(self.id),
                    these_triples[0][1],
                    these_triples[0][2],
                )
            reference_triples.extend(these_triples)
        return reference_triples

    @property
    def type(self) -> str:
        return self._type

    @property
    def type_rdf(self) -> Tuple[URIRef, URIRef, URIRef]:
        return (URIRef(self.id), NS_RDF.type, URIRef(self.type))
