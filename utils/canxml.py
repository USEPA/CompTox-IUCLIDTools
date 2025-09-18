"""Canonical XML dump to compare two XML files.

The output for each file is dumped in sequence, but can be viewed side by side in an
editor for comparison.  Equivalence of namespaces in effect is immediately apparent.

Usage: python canxml.py file1.xml file2.xml

First, both files are loaded and all the prefixes they use for namespaces in mapped.

Then each file is dumped in an indented form:

1 ../../Downloads/i6z/2b7fd258-0e8a-4d36-a575-20270310d77d_0.i6d
2 i6c:Document
3   @xsi:schemaLocation http://iuclid6.echa.europa.eu/namespaces/platform-container/v2
      platform-container-v2.xsd
4   i6c:PlatformMetadata
5     i6m:iuclidVersion
6       7.0.7
...
7   i6c:Content
8     QnF5:ENDPOINT_STUDY_RECORD.RepeatedDoseToxicityOral
9       QnF5:MaterialsAndMethods

with content by line as follows:
1 - The path to the dumped file.
2 - An element with the prefixe(s) used for its namespace by *both* source documents.
    i.e. if one document used 'i6c' and the other used 'cont', *for the same namespace*,
    the element would be shown as 'i6c|cont:Document'.
4 - An attribute of the element with its namespace and value.
6 - Text content of an element.
8 - For namespaces not assigned a prefix by either document, a short deterministic
    prefix is generated (first 4 chars. of base64 encoding of md5sum of the namespace).
"""

import base64
import hashlib
import re
import sys
from collections import defaultdict

import lxml.etree as ET
import lxml.sax

NS_NS = re.compile("^ns\\d+")  # Ignore "nsXX:" namespaces.


class GetNSprefixes(lxml.sax.ElementTreeContentHandler):
    """Collect prefixes used for namespaces."""

    def __init__(self, *args, **kwargs):
        """Set up CanXML."""
        self._prefixes = kwargs.pop("prefixes")
        super().__init__(*args, **kwargs)

    def startPrefixMapping(self, prefix, uri):
        """Handle prefix start."""
        if prefix and not NS_NS.match(prefix):
            self._prefixes[uri].add(prefix)
        return super().startPrefixMapping(prefix, uri)


class CanXML(lxml.sax.ElementTreeContentHandler):
    """CanXML SAX handler."""

    def __init__(self, *args, **kwargs):
        """Set up CanXML."""
        self._prefixes = kwargs.pop("prefixes")
        self._depth = 0
        super().__init__(*args, **kwargs)

    def startElementNS(self, name, qname, attributes=None):
        """Start element."""
        prefix = "|".join(self._prefixes[name[0]])
        if prefix:
            prefix += ":"
            ns = ""
        else:
            ns = f" (in {name[0]})"
            ns = ""
            prefix = (
                base64.b64encode(hashlib.md5(name[0].encode("utf-8")).digest())[
                    :4
                ].decode("utf-8")
                + ":"
            )
        print(f"{'  ' * self._depth}{prefix}{name[1]}{ns}")
        if attributes:
            for quat in attributes.getNames():
                prefix = "|".join(self._prefixes[quat[0]])
                value = attributes.getValue(quat)
                print(f"{'  ' * self._depth}  @{prefix}:{quat[1]} {value} {quat[0]}")
        self._depth += 1
        return super().startElementNS(name, attributes)

    def characters(self, data):
        """Handle text content."""
        if data.strip():
            text = " ".join(data.split())[:60]
            print(f"{'  ' * self._depth}{text}")
        return super().characters(data)

    def endElementNS(self, name, qname, attributes=None):
        """End element."""
        self._depth -= 1
        return super().endElementNS(name, attributes)


prefixes = defaultdict(set)

# First map namespaces.
for arg in sys.argv[1:3]:
    handler = GetNSprefixes(prefixes=prefixes)
    with open(arg) as stream:
        tree = ET.parse(stream)
    lxml.sax.saxify(tree, handler)

# Then check for conflicts.
prefix2ns = defaultdict(set)
# Uncomment to deliberately create conflict to check check:
# prefixes[list(prefixes)[1]].add(list(prefixes[list(prefixes)[0]])[0])
# Uncomment to have two prefixes for one namespace just to test:
# prefixes[list(prefixes)[0]].add("nstest")
for ns, pfxs in prefixes.items():
    for pfx in pfxs:
        if prefix2ns[pfx] and prefix2ns[pfx] != set((ns,)):
            print(f"Conflicting prefix {pfx}:")
            print(prefix2ns[pfx])
            print(ns)
            sys.exit(10)
        prefix2ns[pfx].add(ns)
for pfx, ns in prefix2ns.items():
    print(pfx, ns)

# Then compare files.
for arg in sys.argv[1:3]:
    print(arg)
    handler = CanXML(prefixes=prefixes)
    with open(arg) as stream:
        tree = ET.parse(stream)
    lxml.sax.saxify(tree, handler)
