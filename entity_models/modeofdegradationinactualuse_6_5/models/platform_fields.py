from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from modeofdegradationinactualuse_6_5.models.xml import LangValue

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"


@dataclass
class AttachmentListField:
    """
    Holds the list of the attachment content identifiers/keys attached to the
    specific field.
    """

    class Meta:
        name = "attachmentListField"

    key: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class BaseDataProtectionField:
    """An empty complex type that is extended by the data protection fields which
    are defined inline in the auto-generated document xsds.

    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The data protection fields contain the following elements:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>confidentiality</ns1:li>
    <ns1:li>justification</ns1:li>
    <ns1:li>legislation</ns1:li>
    <ns1:ul>
    <ns1:li>value</ns1:li>
    <ns1:li>other</ns1:li>
    </ns1:ul>
    </ns1:ul>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The inline definition of the fields take place in order to:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>restrict the eligible phrase codes for the "confidentiality" and "value" element</ns1:li>
    <ns1:li>based on the field definition, properly define the multilingual behavior of the textual "justification" and "other" elements</ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "baseDataProtectionField"


@dataclass
class BasePhysicalQuantityField:
    """An empty complex type that is extended by the physical quantity fields which
    are defined inline in the auto-generated document xsds.

    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The physical quantity fields contain the following elements:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>unitCode</ns1:li>
    <ns1:li>unitOther</ns1:li>
    <ns1:li>value</ns1:li>
    </ns1:ul>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The inline definition of the fields take place in order to:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>restrict the eligible phrase codes for the "unitCode" element</ns1:li>
    <ns1:li>conditionally define or omit the "unitOther" element based on the configured phrasegroup (open, close)</ns1:li>
    <ns1:li>based on the field definition, properly define the multilingual behavior of the textual "unitOther" element</ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "basePhysicalQuantityField"


@dataclass
class BasePhysicalQuantityRangeField:
    """An empty complex type that is extended by the physical quantity range fields
    which are defined inline in the auto-generated document xsds.

    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The physical quantity range fields contain the following elements:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>unitCode</ns1:li>
    <ns1:li>unitOther</ns1:li>
    <ns1:li>lowerQualifier</ns1:li>
    <ns1:li>upperQualifier</ns1:li>
    <ns1:li>lowerValue</ns1:li>
    <ns1:li>upperValue</ns1:li>
    <ns1:li>qualifier: in case of half-bounded</ns1:li>
    <ns1:li>value: in case of half-bounded</ns1:li>
    </ns1:ul>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The inline definition of the fields take place in order to:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>restrict the eligible phrase codes for the "unitCode" element</ns1:li>
    <ns1:li>conditionally define or omit the "unitOther" element based on the configured phrasegroup (open, close)</ns1:li>
    <ns1:li>based on the field definition, properly define the multilingual behavior of the textual "unitOther" element</ns1:li>
    <ns1:li>based on the field definition, dynamically setup the bounded- or half-boudnded-related elements</ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "basePhysicalQuantityRangeField"


@dataclass
class BasePicklistField:
    """An empty complex type that is extended by the picklist fields which are
    defined inline in the auto-generated document xsds.

    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The picklist fields contain the following elements:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>value</ns1:li>
    <ns1:li>other</ns1:li>
    <ns1:li>remarks</ns1:li>
    </ns1:ul>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    <ns1:br xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1"/>
    The inline definition of the fields take place in order to:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1">
    <ns1:li>restrict the eligible phrase codes per picklist field</ns1:li>
    <ns1:li>conditionally define or omit the "other" element based on the configured phrasegroup (open, close)</ns1:li>
    <ns1:li>based on the picklist definition, properly define the multilingual behavior of the textual elements "other" and "remarks" elements </ns1:li>
    <ns1:li>based on the picklist definition, properly define the length restriction of the "remarks" elements </ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "basePicklistField"


@dataclass
class DocumentReferenceMultipleField:
    """
    Multilingual version of the document reference field.
    """

    class Meta:
        name = "documentReferenceMultipleField"

    key: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


class HalfBoundedQualifier(Enum):
    """
    Restricts the eligible values of the "halfBoundedQualifier" element.
    """

    GREATER_THAN_SIGN = ">"
    GREATER_THAN_SIGN_EQUALS_SIGN = ">="
    LESS_THAN_SIGN = "<"
    LESS_THAN_SIGN_EQUALS_SIGN = "<="
    CA = "ca."


@dataclass
class InventoryEntry:
    """
    Specifies the content of the chemical inventory field.
    """

    class Meta:
        name = "inventoryEntry"

    inventory_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "inventoryCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    number_in_inventory: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberInInventory",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )


@dataclass
class Legislation:
    """
    Elements that constitute the regulatory programme legislation information of a
    data protection field.
    """

    class Meta:
        name = "legislation"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


class LowerQualifier(Enum):
    """
    Restricts the eligible values of the "lowerQualifier" element.
    """

    GREATER_THAN_SIGN = ">"
    GREATER_THAN_SIGN_EQUALS_SIGN = ">="
    CA = "ca."


@dataclass
class PhysicalQuantityField:
    """
    Specifies the elements constituting the IUCLID6 physical quantity fields.
    """

    class Meta:
        name = "physicalQuantityField"


@dataclass
class PicklistField:
    """
    Lists the elements (phrase code and other text) constituting the IUCLID6
    picklist field.
    """

    class Meta:
        name = "picklistField"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class PicklistFieldWithLargeTextRemarks:
    """Lists the elements (phrase code, other text and remarks) constituting the IUCLID6 picklist field - remarks information can be up to 32768 characters"""

    class Meta:
        name = "picklistFieldWithLargeTextRemarks"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class PicklistFieldWithMultiLineTextRemarks:
    """Lists the elements (phrase code, other text and remarks) constituting the IUCLID6 picklist field - remarks information can be up to 2000 characters"""

    class Meta:
        name = "picklistFieldWithMultiLineTextRemarks"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class PicklistFieldWithSmallTextRemarks:
    """Lists the elements (phrase code, other text and remarks) constituting the IUCLID6 picklist field - remarks information can be up to 255 characters"""

    class Meta:
        name = "picklistFieldWithSmallTextRemarks"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class RepeatableEntryType:
    """
    Specifies the multiplicity and attribute of a repeatable block.
    """

    class Meta:
        name = "repeatableEntryType"

    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )


@dataclass
class SectionTypesFieldDocumentDefinitionIdentifier:
    class Meta:
        global_type = False

    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    document_sub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentSubType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )


class UpperQualifier(Enum):
    """
    Restricts the eligible values of the "upperQualifier" element.
    """

    LESS_THAN_SIGN = "<"
    LESS_THAN_SIGN_EQUALS_SIGN = "<="
    CA = "ca."


@dataclass
class AddressField:
    """
    Contains the elements constituting the AddressField type.
    """

    class Meta:
        name = "addressField"

    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    country: Optional[PicklistField] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    street1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    street2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    website: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    zipcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )


@dataclass
class DataProtectionField:
    """
    The elements constituting the data protection field type.
    """

    class Meta:
        name = "dataProtectionField"

    confidentiality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    justification: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    legislation: List[Legislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualTextField:
    """
    Indicates that a field holds multilingual textual content.
    """

    class Meta:
        name = "multilingualTextField"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class MultilingualTextFieldLarge:
    """
    Indicates that a field holds multilingual textual content with a maximum of
    32768 characters.
    """

    class Meta:
        name = "multilingualTextFieldLarge"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class MultilingualTextFieldMultiLine:
    """
    Indicates that a field holds multilingual textual content with a maximum of
    2000 characters.
    """

    class Meta:
        name = "multilingualTextFieldMultiLine"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class MultilingualTextFieldSmall:
    """
    Indicates that a field holds multilingual textual content with a maximum of 255
    characters.
    """

    class Meta:
        name = "multilingualTextFieldSmall"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class PhysicalQuantityHalfBoundedField:
    """
    Lists the elements constituting the decimal, hald-bounded physical quantity
    range field.
    """

    class Meta:
        name = "physicalQuantityHalfBoundedField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    qualifier: Optional[HalfBoundedQualifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class PhysicalQuantityIntegerHalfBoundedField:
    """
    Lists the elements constituting the integer, half bounded physical quantity
    range field.
    """

    class Meta:
        name = "physicalQuantityIntegerHalfBoundedField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    qualifier: Optional[HalfBoundedQualifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class PhysicalQuantityIntegerRangeField:
    """
    Lists the elements constituting the integer physical quantity range field.
    """

    class Meta:
        name = "physicalQuantityIntegerRangeField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class PhysicalQuantityRangeField:
    """
    Lists the elements constituting the decimal physical quantity range field.
    """

    class Meta:
        name = "physicalQuantityRangeField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class SectionTypesField:
    """
    Specifies the content of the section types field under Category document.
    """

    class Meta:
        name = "sectionTypesField"

    document_definition_identifier: List[
        SectionTypesFieldDocumentDefinitionIdentifier
    ] = field(
        default_factory=list,
        metadata={
            "name": "documentDefinitionIdentifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualLegislation:
    """
    The multilingual version of the legislation type.
    """

    class Meta:
        name = "multilingualLegislation"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPhysicalQuantityHalfBoundedField:
    """
    The multilingual version of the half bounded physical quantity range field.
    """

    class Meta:
        name = "multilingualPhysicalQuantityHalfBoundedField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    qualifier: Optional[HalfBoundedQualifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPhysicalQuantityIntegerHalfBoundedField:
    """
    The multilingual version of the half bounded physical quantity range field with
    integer value.
    """

    class Meta:
        name = "multilingualPhysicalQuantityIntegerHalfBoundedField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    qualifier: Optional[HalfBoundedQualifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPhysicalQuantityIntegerRangeField:
    """
    The multilingual version of the physical quantity range field with integer
    value.
    """

    class Meta:
        name = "multilingualPhysicalQuantityIntegerRangeField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPhysicalQuantityRangeField:
    """
    The multilingual version of the physical quantity range field.
    """

    class Meta:
        name = "multilingualPhysicalQuantityRangeField"

    unit_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPicklistField:
    """
    The multilingual version of the picklist field.
    """

    class Meta:
        name = "multilingualPicklistField"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPicklistFieldWithLargeTextRemarks:
    """
    The multilingual version of the picklist field including remarks information up
    to 32768 characters.
    """

    class Meta:
        name = "multilingualPicklistFieldWithLargeTextRemarks"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPicklistFieldWithMultiLineTextRemarks:
    """
    The multilingual version of the picklist field including remarks information up
    to 2000 characters.
    """

    class Meta:
        name = "multilingualPicklistFieldWithMultiLineTextRemarks"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualPicklistFieldWithSmallTextRemarks:
    """
    The multilingual version of the picklist field including remarks information up
    to 255 characters.
    """

    class Meta:
        name = "multilingualPicklistFieldWithSmallTextRemarks"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )


@dataclass
class MultilingualDataProtectionField:
    """
    The multilingual version of the data protection field type.
    """

    class Meta:
        name = "multilingualDataProtectionField"

    confidentiality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "required": True,
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
            "min_occurs": 1,
        },
    )
    legislation: List[MultilingualLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",
        },
    )
