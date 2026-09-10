#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Extractor
"""

from lxml import etree
from pathlib import Path


class Extractor:
    """
    Extract data from the original dissertation XML
    """

    def __init__(self, whence: Path):
        self.source_path = whence
        self._load_xml()

    def _load_xml(self):
        tree = etree.parse(self.source_path)
        self.root = tree.getroot()
