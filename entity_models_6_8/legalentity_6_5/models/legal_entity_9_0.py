from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from legalentity_6_5.models.common_types_domain_v9 import (
    A31,
    N01,
    N02,
    N41,
    N64,
    N78,
)
from legalentity_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0"


@dataclass
class LegalEntityContactInfoContactPersonsEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoContactAddressCountry(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoContactAddressDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoLegalEntityType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N01] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoOtherNamesEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntryIdentifierType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryRegulatoryProgramme(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N41] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactPersonsEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    legislation: List[
        LegalEntityContactInfoContactPersonsEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoContactAddressDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    legislation: List[
        LegalEntityGeneralInfoContactAddressDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoOtherNamesEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    legislation: List[
        LegalEntityGeneralInfoOtherNamesEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    legislation: List[
        LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    legislation: List[
        LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    legislation: List[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactPersonsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityContactInfoContactPersonsEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    contact_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoContactAddress:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityGeneralInfoContactAddressDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    address1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    address2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    town: Optional[str] = field(
        default=None,
        metadata={
            "name": "Town",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    country: Optional[LegalEntityGeneralInfoContactAddressCountry] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    web_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "WebSite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoOtherNamesEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityGeneralInfoOtherNamesEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersExternalSystemIdentifiersEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    external_system_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalSystemDesignator",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    identifier_type: Optional[
        LegalEntityIdentifiersLegalEntityIdentifiersEntryIdentifierType
    ] = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    regulatory_programme: Optional[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryRegulatoryProgramme
    ] = field(
        default=None,
        metadata={
            "name": "RegulatoryProgramme",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactPersons:
    class Meta:
        global_type = False

    entry: List[LegalEntityContactInfoContactPersonsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoOtherNames:
    class Meta:
        global_type = False

    entry: List[LegalEntityGeneralInfoOtherNamesEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersExternalSystemIdentifiers:
    class Meta:
        global_type = False

    entry: List[LegalEntityIdentifiersExternalSystemIdentifiersEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiers:
    class Meta:
        global_type = False

    entry: List[LegalEntityIdentifiersLegalEntityIdentifiersEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiers:
    class Meta:
        global_type = False

    entry: List[LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntry] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
            },
        )
    )


@dataclass
class LegalEntityContactInfo:
    class Meta:
        global_type = False

    contact_persons: Optional[LegalEntityContactInfoContactPersons] = field(
        default=None,
        metadata={
            "name": "ContactPersons",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityGeneralInfo:
    class Meta:
        global_type = False

    legal_entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalEntityName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
            "required": True,
        },
    )
    legal_entity_type: Optional[LegalEntityGeneralInfoLegalEntityType] = field(
        default=None,
        metadata={
            "name": "LegalEntityType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    other_names: Optional[LegalEntityGeneralInfoOtherNames] = field(
        default=None,
        metadata={
            "name": "OtherNames",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    contact_address: Optional[LegalEntityGeneralInfoContactAddress] = field(
        default=None,
        metadata={
            "name": "ContactAddress",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntityIdentifiers:
    class Meta:
        global_type = False

    legal_entity_identifiers: Optional[
        LegalEntityIdentifiersLegalEntityIdentifiers
    ] = field(
        default=None,
        metadata={
            "name": "LegalEntityIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    regulatory_programme_identifiers: Optional[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiers
    ] = field(
        default=None,
        metadata={
            "name": "RegulatoryProgrammeIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )
    external_system_identifiers: Optional[
        LegalEntityIdentifiersExternalSystemIdentifiers
    ] = field(
        default=None,
        metadata={
            "name": "ExternalSystemIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0",
        },
    )


@dataclass
class LegalEntity:
    class Meta:
        name = "LEGAL_ENTITY"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/9.0"

    general_info: Optional[LegalEntityGeneralInfo] = field(
        default=None,
        metadata={
            "name": "GeneralInfo",
            "type": "Element",
            "required": True,
        },
    )
    identifiers: Optional[LegalEntityIdentifiers] = field(
        default=None,
        metadata={
            "name": "Identifiers",
            "type": "Element",
        },
    )
    contact_info: Optional[LegalEntityContactInfo] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
        },
    )
