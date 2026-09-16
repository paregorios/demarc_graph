#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Define entity base class
"""

from rdflib import URIRef, Literal
from .rdf import *
from .text import norm
from typing import Tuple
from validators import url as valid_uri


class Entity:
    """
    Base class for various entities of interest
    """

    def __init__(self, id: str):
        self._id = ""
        self.id = id
        self._label = ""

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
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, value: str):
        self._label = norm(value)

    @label.deleter
    def label(self):
        self._label = ""

    @property
    def label_rdf(self) -> Tuple[URIRef, URIRef, Literal]:
        """serialize label as an RDF triple"""
        return (URIRef(self.id), NS_RDFS.label, Literal(self.label))
