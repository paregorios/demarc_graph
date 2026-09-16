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
import logging
from pathlib import Path

logging.getLogger("normalize_space").setLevel(logging.WARNING)


class TestExtractor:

    logger = logging.getLogger("TestExtractor")

    def test_init(self):
        source_path = Path("data/elliottDiss.xml").resolve()
        e = Extractor(whence=source_path)
        instances = e.extract_instances()
        self.logger.debug(f"extracted {len(instances)} instances")
        assert len(instances) == 106
        for iid, instance in instances.items():
            self.logger.debug(f"{iid}: {instance.label}")
