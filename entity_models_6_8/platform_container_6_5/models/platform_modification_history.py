from dataclasses import field
from typing import Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/platform-modification-history/v1"
)


@dataclass
class Modification:
    """Holds the information concerning the document's modification.

    Every entry is a single operation that took place on the specific
    document and specifies the date of the action, the user that run the
    action, the submitting legal entity of the user and the modification
    remarks if any

    :ivar date: The date the action was performed on the document
    :ivar author: The userName of the user that performed the
        modification
    :ivar legal_entity: The description of the submitting legal entity
        of the user. This information contains the concatenated value of
        the LE name, city and localized country information
    :ivar remarks: The modification comment
    """

    class Meta:
        namespace = "http://iuclid6.echa.europa.eu/namespaces/platform-modification-history/v1"

    date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "required": True,
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "required": True,
        },
    )
    legal_entity: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalEntity",
            "type": "Element",
            "required": True,
        },
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "required": True,
        },
    )
