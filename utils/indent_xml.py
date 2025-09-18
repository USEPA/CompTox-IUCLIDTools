"""Pretty print / indent XML for readability."""
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom


def pretty_print_xml(xml_string):
    """Pretty-prints an XML string."""
    try:
        root = ET.fromstring(xml_string)
        rough_string = ET.tostring(root, "utf-8")
        reparsed = minidom.parseString(rough_string)
        print(reparsed.toprettyxml(indent="  "))
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")


pretty_print_xml(sys.stdin.read())
