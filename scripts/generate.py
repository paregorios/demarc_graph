#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Script to Generate RDF
"""

from airtight.cli import configure_commandline
from demarc_graph.extractor import Extractor
from demarc_graph.rdf import NS_DEMARC
import logging
from pathlib import Path
from rdflib import Graph
import sys

logger = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = logging.WARNING
DEFAULT_INPUTPATH = Path("data/elliottDiss.xml").resolve()
OPTIONAL_ARGUMENTS = [
    [
        "-l",
        "--loglevel",
        "NOTSET",
        "desired logging level ("
        + "case-insensitive string: DEBUG, INFO, WARNING, or ERROR",
        False,
    ],
    ["-v", "--verbose", False, "verbose output (logging level == INFO)", False],
    [
        "-w",
        "--veryverbose",
        False,
        "very verbose output (logging level == DEBUG)",
        False,
    ],
    ["-i", "--input", str(DEFAULT_INPUTPATH), "path to input xml file", False],
]
POSITIONAL_ARGUMENTS = [
    # each row is a list with 3 elements: name, type, help
]

EXIT_SUCCESS = 0
EXIT_ERROR = 1


def main(**kwargs):
    """
    main function
    """
    # logger = logging.getLogger(sys._getframe().f_code.co_name)
    # code here
    # when all is done and goes well
    logging.getLogger("normalize_space").setLevel(logging.WARNING)
    whence = Path(kwargs["input"]).expanduser().resolve()
    e = Extractor(whence)
    instances = e.extract_instances()
    g = Graph()
    for instance in instances.values():
        logger.debug(f"instance id {instance.id}")
        g.add(instance.type_rdf)
        for label_triple in instance.labels_rdf:
            g.add(label_triple)
    g.bind("demarc", NS_DEMARC)
    print(g.serialize(format="turtle"))
    sys.exit(EXIT_SUCCESS)  # if error, sys.exit(EXIT_ERROR)


if __name__ == "__main__":
    main(
        **configure_commandline(
            OPTIONAL_ARGUMENTS, POSITIONAL_ARGUMENTS, DEFAULT_LOG_LEVEL
        )
    )
