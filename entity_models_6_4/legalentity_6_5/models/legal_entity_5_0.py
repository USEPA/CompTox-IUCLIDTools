from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.legalentity_6_5.models.common_types_domain_v5 import (
    N01,
    N02,
    N41,
    N64,
    N78,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0"


@dataclass
class LegalEntityContactInfoContactAddressDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactPersonsEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoLegalEntityType:
    class Meta:
        global_type = False

    value: Optional[N01] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntryIdentifierType:
    class Meta:
        global_type = False

    value: Optional[N02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryRegulatoryProgramme:
    class Meta:
        global_type = False

    value: Optional[N41] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactAddressDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    legislation: List[
        LegalEntityContactInfoContactAddressDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactPersonsEntryDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    legislation: List[
        LegalEntityContactInfoContactPersonsEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoOtherNamesEntryDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    legislation: List[
        LegalEntityGeneralInfoOtherNamesEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    legislation: List[
        LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    legislation: List[
        LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    legislation: List[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactAddress:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityContactInfoContactAddressDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    contact_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactAddress",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityContactInfoContactPersonsEntry:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityContactInfoContactPersonsEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    contact_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityGeneralInfoOtherNamesEntry:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityGeneralInfoOtherNamesEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersExternalSystemIdentifiersEntry:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityIdentifiersExternalSystemIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    external_system_designator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalSystemDesignator",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersLegalEntityIdentifiersEntry:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityIdentifiersLegalEntityIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    identifier_type: Optional[
        LegalEntityIdentifiersLegalEntityIdentifiersEntryIdentifierType
    ] = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntry:
    class Meta:
        global_type = False

    data_protection: Optional[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    regulatory_programme: Optional[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiersEntryRegulatoryProgramme
    ] = field(
        default=None,
        metadata={
            "name": "RegulatoryProgramme",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    contact_address: Optional[LegalEntityContactInfoContactAddress] = field(
        default=None,
        metadata={
            "name": "ContactAddress",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
            "required": True,
        },
    )
    legal_entity_type: Optional[LegalEntityGeneralInfoLegalEntityType] = field(
        default=None,
        metadata={
            "name": "LegalEntityType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    other_names: Optional[LegalEntityGeneralInfoOtherNames] = field(
        default=None,
        metadata={
            "name": "OtherNames",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    regulatory_programme_identifiers: Optional[
        LegalEntityIdentifiersRegulatoryProgrammeIdentifiers
    ] = field(
        default=None,
        metadata={
            "name": "RegulatoryProgrammeIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )
    external_system_identifiers: Optional[
        LegalEntityIdentifiersExternalSystemIdentifiers
    ] = field(
        default=None,
        metadata={
            "name": "ExternalSystemIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0",
        },
    )


@dataclass
class LegalEntity:
    class Meta:
        name = "LEGAL_ENTITY"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/LEGAL_ENTITY/5.0"

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
