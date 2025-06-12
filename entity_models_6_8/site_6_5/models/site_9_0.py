from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from site_6_5.models.common_types_domain_v9 import (
    A31,
    N64,
    N78,
)
from site_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0"


@dataclass
class SiteConfidentialityInfoDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteContactAddressCountry(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteContactAddressDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteGeneralInfoExternalSystemIdentifiersEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteConfidentialityInfoDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    legislation: List[SiteConfidentialityInfoDataProtectionLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
            },
        )
    )


@dataclass
class SiteContactAddressDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    legislation: List[SiteContactAddressDataProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteGeneralInfoExternalSystemIdentifiersEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    legislation: List[
        SiteGeneralInfoExternalSystemIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteConfidentialityInfo:
    class Meta:
        global_type = False

    data_protection: Optional[SiteConfidentialityInfoDataProtection] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteContactAddress:
    class Meta:
        global_type = False

    data_protection: Optional[SiteContactAddressDataProtection] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    address1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    address2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    town: Optional[str] = field(
        default=None,
        metadata={
            "name": "Town",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    country: Optional[SiteContactAddressCountry] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    web_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "WebSite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteGeneralInfoExternalSystemIdentifiersEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[
        SiteGeneralInfoExternalSystemIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    external_system_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalSystemDesignator",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteGeneralInfoExternalSystemIdentifiers:
    class Meta:
        global_type = False

    entry: List[SiteGeneralInfoExternalSystemIdentifiersEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class SiteGeneralInfo:
    class Meta:
        global_type = False

    site_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SiteName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
            "required": True,
        },
    )
    owner_legal_entity: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnerLegalEntity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    other_legal_entity_owners: Optional[DocumentReferenceMultipleField] = (
        field(
            default=None,
            metadata={
                "name": "OtherLegalEntityOwners",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
            },
        )
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )
    external_system_identifiers: Optional[
        SiteGeneralInfoExternalSystemIdentifiers
    ] = field(
        default=None,
        metadata={
            "name": "ExternalSystemIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0",
        },
    )


@dataclass
class Site:
    class Meta:
        name = "SITE"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/SITE/9.0"

    confidentiality_info: Optional[SiteConfidentialityInfo] = field(
        default=None,
        metadata={
            "name": "ConfidentialityInfo",
            "type": "Element",
        },
    )
    general_info: Optional[SiteGeneralInfo] = field(
        default=None,
        metadata={
            "name": "GeneralInfo",
            "type": "Element",
            "required": True,
        },
    )
    contact_address: Optional[SiteContactAddress] = field(
        default=None,
        metadata={
            "name": "ContactAddress",
            "type": "Element",
        },
    )
