#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Test the extractor module
"""

from demarc_graph.extractor import Extractor
from pathlib import Path


class TestExtractor:

    def test_init(self):
        source_path = Path("data/elliottDiss.xml").resolve()
        e = Extractor(whence=source_path)
