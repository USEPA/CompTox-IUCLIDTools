from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from contact_6_5.models.common_types_domain_v9 import (
    A31,
    A37,
)
from contact_6_5.models.platform_fields import (
    BasePicklistField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0"


@dataclass
class ContactGeneralInfoContactType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A37] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )


@dataclass
class ContactGeneralInfoCountry(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )


@dataclass
class ContactGeneralInfo:
    class Meta:
        global_type = False

    contact_type: Optional[ContactGeneralInfoContactType] = field(
        default=None,
        metadata={
            "name": "ContactType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
            "required": True,
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    organisation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
            "required": True,
        },
    )
    department: Optional[str] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    mobile: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mobile",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    address1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    address2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    town: Optional[str] = field(
        default=None,
        metadata={
            "name": "Town",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    country: Optional[ContactGeneralInfoCountry] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0",
        },
    )


@dataclass
class Contact:
    class Meta:
        name = "CONTACT"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/CONTACT/9.0"

    general_info: Optional[ContactGeneralInfo] = field(
        default=None,
        metadata={
            "name": "GeneralInfo",
            "type": "Element",
            "required": True,
        },
    )
