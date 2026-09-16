#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Define instance-related entities
"""

from .entities import Entity


class Instance(Entity):

    def __init__(self, id: str):
        Entity.__init__(self, id=id)
