#
# This file is part of demarc_graph
# by Tom Elliott
# (c) Copyright 2026 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Extractor
"""

from .bibliography import citation_reasons, works_cited_by_short_title
from .instances import Instance
import logging
from lxml import etree
from pathlib import Path
from pprint import pprint
import re
from .rdf import NS_DEMARC
from .references import Reference
from .text import norm
from urllib.parse import urlsplit, urlunsplit

XML_NAMESPACES = {"text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0"}
NS_DEMARC_PARTS = urlsplit(str(NS_DEMARC))


class Extractor:
    """
    Extract data from the original dissertation XML
    """

    def __init__(self, whence: Path):
        self.source_path = whence
        self._load_xml()
        # Burton 2000, no. 5
        self.rx_burton_reference = re.compile(r"^Burton 2000, no. (?P<number>\d+)$")
        # Date(s): 2 BC - AD 14
        self.rx_date_range = re.compile(
            r"^Date\(s\): (?P<start>(AD \d+|\d+ BC)) - (?P<end>(AD \d+|\d+ BC))$"
        )

    def _load_xml(self):
        tree = etree.parse(self.source_path)
        self.root = tree.getroot()

    def extract_instances(self) -> dict:
        """
        Produce a dictionary of Instance objects extracted from the XML
        """
        logger = logging.getLogger("Extractor.extract_instances")
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
                        uripath = [p for p in NS_DEMARC_PARTS.path.split("/") if p]
                        uripath.append(instance_id)
                        uripath = "/".join(uripath)
                        parts = list(NS_DEMARC_PARTS)
                        parts[2] = uripath
                        instance_uri = urlunsplit(parts)
                        if instance_id not in instance_ids:
                            instance_ids.add(instance_id)
                            instance = Instance(instance_uri)
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
                        instance.add_label(label)
                    else:
                        raise RuntimeError(
                            f"Failed to extract a label for instance {instance_id}"
                        )

                    # subsequent paragraphs
                    paragraphs = []
                    next_node = instance_head.getnext()
                    i = 0
                    while next_node is not None:
                        if next_node.tag == f"{{{XML_NAMESPACES['text']}}}p":
                            paragraphs.append(next_node)
                            raw_text = norm(" ".join(next_node.itertext()))
                            m = self.rx_burton_reference.fullmatch(raw_text)
                            if m:
                                logger.debug(
                                    f"Instance {instance_id} paragraph {i} matches Burton reference pattern"
                                )
                                ref_id = f"{instance_id}-REF{i+1}"
                                ref = Reference(
                                    id=NS_DEMARC[ref_id],
                                    short_title="Burton 2000",
                                    reason="citesAsRelated",
                                    context={"locator": f"number {m.group('number')}"},
                                )
                                instance.add_reference(ref)
                            else:
                                m = self.rx_date_range.fullmatch(raw_text)
                                if m:
                                    logger.debug(
                                        f"Instance {instance_id} paragraph {i} matches date range pattern"
                                    )
                                else:
                                    logger.debug(
                                        f"Instance {instance_id} paragraph {i} is general text: {' '.join(raw_text.split()[:10])}"
                                    )
                            i += 1
                        else:
                            break
                        next_node = next_node.getnext()

            else:
                raise RuntimeError(
                    f"Failed to match bookmark_start for instance_head='{etree.tostring(instance_head)}"
                )
        return instances
