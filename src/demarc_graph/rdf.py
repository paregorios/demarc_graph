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

NS_BIB = Namespace("http://purl.org/net/biblio#")
NS_BIBO = Namespace("http://purl.org/ontology/bibo/")
NS_CITO = Namespace("http://purl.org/spar/cito/")
NS_DEMARC = Namespace("https://paregorios.org/demarc/")
NS_PRISM = Namespace("http://prismstandard.org/namespaces/basic/2.0/")
NS_ZOTERO = Namespace("http://www.zotero.org/namespaces/export#")
