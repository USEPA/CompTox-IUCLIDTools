"""For a given OHT XSD file, e.g.
ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral-9.0.xsd,
return a mapping the the OHT's pick list elements to the corresponding pick
list in Phrases.xml.

NOTE: some nested elements have the same name and point to different picklists,

    "AttachedJustification/ReasonPurpose": "PG6-60009",
    "CrossReference/ReasonPurpose": "PG6-60010",

So keys are the "/" joined @name of all parent elements, e.g.
"ENDPOINT_STUDY_RECORD.RepeatedDoseToxicityOral/DataSource/DataAccess": "Z03"

E.g. from
    <xs:element minOccurs="0" name="Endpoint">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="i6:basePicklistField">
                    <xs:sequence>
                        <xs:element minOccurs="0" name="value" type="ct:PG6_60225"/>

Endpoint -> PG6_60225 which will be <PhraseGroup code="PG6-60225""> (dash not
underscore) in Phrases.xml.

WARNING: phrases_to_dict() caches about 4.8 Mb of data in memory
"""

from functools import lru_cache as cache
from pathlib import Path

from lxml import etree as ET


# def oht_xsd_to_picklist(xsd_file: str | Path) -> dict[str, str]:
@cache
def oht_xsd_to_picklist(xsd_file):
    """Parse the OHT XSD file and extract the picklist elements."""
    tree = ET.parse(xsd_file)  # noqa: S320 - we trust this data
    root = tree.getroot()

    ns = {
        "xs": "http://www.w3.org/2001/XMLSchema",
        # FIXME: import this from common location
        "i6": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
    }

    picklist_mapping = {}

    # Find the elements that contain picklist fields, we need @name from them
    for element in root.xpath(
        ".//xs:element[@name='value' and ../../@base='i6:basePicklistField']",
        namespaces=ns,
    ):
        # and then find the named parent elements
        parents = element.xpath(
            "./ancestor::xs:element[@name]",
            namespaces=ns,
        )
        key = "/".join(parent.attrib["name"] for parent in parents)
        picklist_name = element.attrib["type"].replace("ct:", "").replace("_", "-")
        if key in picklist_mapping and picklist_mapping[key] != picklist_name:
            raise ValueError(
                f"Multiple picklist mapping for {key}: "
                f"{picklist_mapping[key]} and {picklist_name}"
            )
        picklist_mapping[key] = picklist_name

    return picklist_mapping


# def phrases_to_dict(phrases_file: str | Path) -> dict[str, dict[str, str]]:
@cache
def phrases_to_dict(phrases_file):
    """Parse the Phrases.xml file and return a dictionary of codes.

    ...
    }, {"C11": {  # PhraseGroup
        "cytotoxicity": "745",  # Phrase: code
        "hematotoxicity": "832",
        }
    }, {"C12": {
    ...
    """
    tree = ET.parse(phrases_file)  # noqa: S320 - we trust this data
    root = tree.getroot()

    ns = {"pg": "http://iuclid6.echa.europa.eu/schemas/phrases"}

    phrases_dict = {}
    for phrase_group in root.xpath(".//pg:PhraseGroup", namespaces=ns):
        group_code = phrase_group.attrib["code"]
        phrases_dict[group_code] = {}
        for phrase in phrase_group.xpath("./pg:Phrase", namespaces=ns):
            code = phrase.xpath("./pg:Code/text()", namespaces=ns)[0]
            label = phrase.xpath("./pg:Label/text()", namespaces=ns)[0]
            phrases_dict[group_code][label] = code

    return phrases_dict


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:  # noqa: PLR2004
        print("Usage: python oht_xsd_to_picklist.py <xsd_file>")
        sys.exit(1)
    xsd_file = sys.argv[1]
    mapping = oht_xsd_to_picklist(xsd_file)
    for oht, picklist in mapping.items():
        print(f"{oht} -> {picklist}")
    print(json.dumps(phrases_to_dict("Phrases.xml")["PG6-60010"], indent=2))
    print(len(json.dumps(phrases_to_dict("Phrases.xml"))))
