"""Validate and .i6d file.

Usage: python validate_i6d.py <xsd_folder> <file.i6d>

Removes the content of the Content element, validates what's left, then tries
to validate the Content element separately.
"""

# ruff: noqa: ANN101 - not annotating 'self'

import sys
from pathlib import Path

# Uncomment to use xmlschema instead of / as well as lxml
# import xmlschema
from lxml import etree as ET

xsd_folder = Path(sys.argv[1])
i6d_file = Path(sys.argv[2])

XSI = "http://www.w3.org/2001/XMLSchema-instance"
NS = {"xsi": XSI}


class XMLSchema:
    """Wrapper for XMLSchema validation."""

    pass


class LXMLSchema(XMLSchema):
    """Wrapper for lxml's XMLSchema validation."""

    def __init__(self, schema_path: Path):
        """Initialize the schema from a file."""
        self.schema = ET.XMLSchema(ET.parse(schema_path))  # noqa: S320 - we trust this data

    def is_valid(self, tree: ET._ElementTree) -> bool:
        """Test if the XML tree is valid against the schema."""
        return self.schema.validate(tree)

    def explain(self) -> None:
        """Print the validation errors."""
        print(self.schema.error_log)


# Uncomment to use xmlschema instead of / as well as lxml
xmlschema = None


class XMLSchemaSchema(XMLSchema):
    """Wrapper for xmlschema's XMLSchema validation."""

    def __init__(self, schema_path: Path):
        """Initialize the schema from a file."""
        self.schema = xmlschema.XMLSchema(schema_path)

    def is_valid(self, tree: ET._ElementTree) -> bool:
        """Test if the XML tree is valid against the schema."""
        self.tree = tree
        return self.schema.is_valid(tree)

    def explain(self) -> None:
        """Print the validation errors."""
        self.schema.validate(self.tree)


def validate_i6d(schema_cls: XMLSchema, xsd_folder: Path, i6d_file: Path) -> bool:
    """Validate an .i6d file against the XSD schema.

    This version uses lxml.
    """
    i6d_tree = ET.XML(i6d_file.read_bytes())
    schema = i6d_tree.get(f"{{{XSI}}}schemaLocation")
    if schema:
        schema = schema.split()[-1]
        print(f"Schema from file: {schema}")
    else:
        ns = i6d_tree.xpath("namespace-uri()")
        schema = "platform-container-v2.xsd" if "v2" in ns else "platform-container.xsd"
    # Get the most recent schema
    schema_path = sorted(xsd_folder.glob(f"**/{schema}"))[-1]
    print(f"Using schema: {schema_path}")

    schema = schema_cls(schema_path)
    if schema.is_valid(i6d_tree):
        print("Validation for full file succeeded.")
        return True

    print("Validation for full file failed:")
    print("Trying again with Content element removed...")
    # Remove the Content element
    ns = i6d_tree.xpath("namespace-uri()")
    xpath = f".//{{{ns}}}Content"
    print(f"XPath for Content element: {xpath}")
    content = i6d_tree.find(xpath)[0]
    content.getparent().remove(content)
    if not schema.is_valid(i6d_tree):
        print("Validation for file without Content element failed:")
        schema.explain()
    else:
        print("Validation for file without Content element succeeded.")

    if content is None:
        print("No Content element to validate separately.")
        return True

    Path("content.xml").write_text(ET.tostring(content, encoding="unicode"))

    schema = content.get(f"{{{XSI}}}schemaLocation")
    if schema:
        schema = schema.split()[-1]
        print(f"Schema from file: {schema}")
    else:
        ns = content.xpath("namespace-uri()")
        schema = "-".join(ns.split("/")[-2:]) + ".xsd"
        print(f"Schema implied by namespace: {schema}")
    # Get the most recent schema, probably only one choice
    schema_path = sorted(xsd_folder.glob(f"**/{schema}"))[-1]
    print(f"Using schema: {schema_path}")

    schema = schema_cls(schema_path)
    if schema.is_valid(content):
        print("Validation for Content element succeeded.")
        return True

    print("Validation for Content element failed:")
    schema.explain()
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:  # noqa: PLR2004
        print("Usage: python validate_i6d.py <xsd_folder> <file.i6d>")
        sys.exit(1)

    xsd_folder = Path(sys.argv[1])
    i6d_file = Path(sys.argv[2])

    if not xsd_folder.is_dir():
        print(f"Error: {xsd_folder} is not a directory.")
        sys.exit(1)
    if not i6d_file.is_file():
        print(f"Error: {i6d_file} is not a file.")
        sys.exit(1)

    schema_cls = XMLSchemaSchema
    schema_cls = LXMLSchema
    validate_i6d(schema_cls, xsd_folder, i6d_file)
