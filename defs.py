"""Simple low level definitions for the project."""

DEFVER = "9.0"  # definitionVersion in the .i6d
I6C = "http://iuclid6.echa.europa.eu/namespaces/platform-container/v2"
I6CXSD = "platform-container.xsd"
I6M = "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
I6MAN = "http://iuclid6.echa.europa.eu/namespaces/manifest/v1"
I6 = "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"
XML_NS = "http://www.w3.org/XML/1998/namespace"  # add _NS to avoid conflicts
XSI = "http://www.w3.org/2001/XMLSchema-instance"


def truthy(value: bool | str | int | float) -> bool:
    """Convert a value to a boolean.

    Caller should do something like truthy(os.environ.get("VAR") or "Y") to
    provide a default.

    Strings like "7" and "Of course" are False.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.strip():
        return value.strip().lower()[0] in "1ty"  # 1, T(rue), Y(es)
    if isinstance(value, (int, float)):
        return bool(value)
    return False
