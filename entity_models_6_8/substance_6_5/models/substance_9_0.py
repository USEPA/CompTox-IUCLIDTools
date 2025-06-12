from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from substance_6_5.models.common_types_domain_v9 import (
    A31,
    N08,
    N58,
    N64,
    N78,
    N97,
    Pg660200,
)
from substance_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0"


@dataclass
class SubstanceTemplates:
    class Meta:
        global_type = False

    template: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Template",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceContactPersonsEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNamesEntryCountry(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNamesEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNamesEntryNameType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N97] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNamesEntryRelation(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660200] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOwnerLegalEntityProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceReferenceSubstanceProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceRoleInSupplyChainRoleProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceThirdPartyProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceTypeOfSubstanceComposition(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceTypeOfSubstanceOrigin(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N58] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceContactPersonsEntryDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    legislation: List[
        SubstanceContactPersonsEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNamesEntryDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    legislation: List[SubstanceOtherNamesEntryDataProtectionLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
            },
        )
    )


@dataclass
class SubstanceOwnerLegalEntityProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    legislation: List[SubstanceOwnerLegalEntityProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceReferenceSubstanceProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    legislation: List[SubstanceReferenceSubstanceProtectionLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
            },
        )
    )


@dataclass
class SubstanceRoleInSupplyChainRoleProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    legislation: List[SubstanceRoleInSupplyChainRoleProtectionLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
            },
        )
    )


@dataclass
class SubstanceThirdPartyProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    legislation: List[SubstanceThirdPartyProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceTypeOfSubstance:
    class Meta:
        global_type = False

    composition: Optional[SubstanceTypeOfSubstanceComposition] = field(
        default=None,
        metadata={
            "name": "Composition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    origin: Optional[SubstanceTypeOfSubstanceOrigin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceContactPersonsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[SubstanceContactPersonsEntryDataProtection] = (
        field(
            default=None,
            metadata={
                "name": "DataProtection",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
            },
        )
    )
    contact_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNamesEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[SubstanceOtherNamesEntryDataProtection] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    name_type: Optional[SubstanceOtherNamesEntryNameType] = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    country: List[SubstanceOtherNamesEntryCountry] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    relation: Optional[SubstanceOtherNamesEntryRelation] = field(
        default=None,
        metadata={
            "name": "Relation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceReferenceSubstance:
    class Meta:
        global_type = False

    protection: Optional[SubstanceReferenceSubstanceProtection] = field(
        default=None,
        metadata={
            "name": "Protection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceRoleInSupplyChain:
    class Meta:
        global_type = False

    role_protection: Optional[SubstanceRoleInSupplyChainRoleProtection] = (
        field(
            default=None,
            metadata={
                "name": "RoleProtection",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
            },
        )
    )
    manufacturer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    importer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Importer",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    only_representative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlyRepresentative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )
    downstream_user: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DownstreamUser",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceContactPersons:
    class Meta:
        global_type = False

    entry: List[SubstanceContactPersonsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class SubstanceOtherNames:
    class Meta:
        global_type = False

    entry: List[SubstanceOtherNamesEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0",
        },
    )


@dataclass
class Substance:
    class Meta:
        name = "SUBSTANCE"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/SUBSTANCE/9.0"

    templates: Optional[SubstanceTemplates] = field(
        default=None,
        metadata={
            "name": "Templates",
            "type": "Element",
            "required": True,
        },
    )
    chemical_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChemicalName",
            "type": "Element",
            "required": True,
        },
    )
    public_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicName",
            "type": "Element",
        },
    )
    other_names: Optional[SubstanceOtherNames] = field(
        default=None,
        metadata={
            "name": "OtherNames",
            "type": "Element",
        },
    )
    owner_legal_entity_protection: Optional[
        SubstanceOwnerLegalEntityProtection
    ] = field(
        default=None,
        metadata={
            "name": "OwnerLegalEntityProtection",
            "type": "Element",
        },
    )
    owner_legal_entity: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnerLegalEntity",
            "type": "Element",
        },
    )
    third_party_protection: Optional[SubstanceThirdPartyProtection] = field(
        default=None,
        metadata={
            "name": "ThirdPartyProtection",
            "type": "Element",
        },
    )
    third_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThirdParty",
            "type": "Element",
        },
    )
    contact_persons: Optional[SubstanceContactPersons] = field(
        default=None,
        metadata={
            "name": "ContactPersons",
            "type": "Element",
        },
    )
    reference_substance: Optional[SubstanceReferenceSubstance] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
        },
    )
    type_of_substance: Optional[SubstanceTypeOfSubstance] = field(
        default=None,
        metadata={
            "name": "TypeOfSubstance",
            "type": "Element",
        },
    )
    role_in_supply_chain: Optional[SubstanceRoleInSupplyChain] = field(
        default=None,
        metadata={
            "name": "RoleInSupplyChain",
            "type": "Element",
        },
    )
