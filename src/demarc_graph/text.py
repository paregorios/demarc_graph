#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

from textnorm import normalize_space, normalize_unicode

"""
work with text strings
"""


def norm(value: str) -> str:
    """normalize unicode and whitespace in string"""
    return normalize_space(normalize_unicode(value))
