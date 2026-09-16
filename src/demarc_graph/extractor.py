#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Extractor
"""

from .instances import Instance
from lxml import etree
from pathlib import Path
from .rdf import NS_DEMARC

XML_NAMESPACES = {"text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0"}


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

    def extract_instances(self) -> dict:
        """
        Produce a dictionary of Instance objects extracted from the XML
        """
        instance_headings = self.root.findall(
            ".//text:h[@text:style-name='treInstance']", XML_NAMESPACES
        )
        instance_ids = set()
        instances = dict()
        for instance_head in instance_headings:
            bookmark_start = instance_head.find(
                ".//text:bookmark-start", XML_NAMESPACES
            )
            if bookmark_start is not None:
                instance = None

                # extract instance ID
                instance_id = bookmark_start.get(f'{{{XML_NAMESPACES["text"]}}}name')
                if instance_id.startswith("INST"):
                    num = instance_id[4:]  # Extract the number after "INST"
                    if num.isdigit():
                        instance_id = "/instances/".join((NS_DEMARC, num))
                        if instance_id not in instance_ids:
                            instance_ids.add(instance_id)
                            instance = Instance(instance_id)
                            instances[instance_id] = instance
                        else:
                            raise RuntimeError(f"Instance ID collision")
                    else:
                        raise RuntimeError(
                            f"Malformed Instance ID in XML: {instance_id}"
                        )
                else:
                    raise RuntimeError(f"Malformed Instance ID in XML: {instance_id}")

                # extract other information about this instance
                if instance is not None:

                    # instance title (i.e., label)
                    raw_label = "".join(instance_head.itertext())
                    if not raw_label:
                        raise RuntimeError(f"Instance {instance_id} has no rawlabel")
                    label = " ".join(
                        [
                            s.strip()
                            for s in (
                                " ".join("".join(instance_head.itertext()).split())
                            ).split(":")
                            if s.strip() != instance_id
                        ]
                    )
                    if label:
                        instance.label = label
                    else:
                        raise RuntimeError(
                            f"Failed to extract a label for instance {instance_id}"
                        )

            else:
                raise RuntimeError(
                    f"Failed to match bookmark_start for instance_head='{etree.tostring(instance_head)}"
                )
        return instances
