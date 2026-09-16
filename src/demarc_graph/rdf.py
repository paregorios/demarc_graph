#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
RDF-related customization and utilities for demarc
"""

from rdflib.namespace import (
    RDF as NS_RDF,
    RDFS as NS_RDFS,
    XSD as NS_XSD,
    DCTERMS as NS_DCTERMS,
    FOAF as NS_FOAF,
)
from rdflib import Namespace

NS_DEMARC = Namespace("https://paregorios.org/demarc/")
