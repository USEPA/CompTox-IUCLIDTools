from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from mixture_6_5.models.common_types_domain_v9 import (
    A31,
    N64,
    N78,
    Pg660585,
)
from mixture_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0"


@dataclass
class MixtureTemplates:
    class Meta:
        global_type = False

    template: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Template",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureContactPersonsEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOtherNamesEntryCountry(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOtherNamesEntryNameType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660585] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOtherNamesEntryProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOwnerLegalEntityProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureRoleInSupplyChainRoleProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureThirdPartyProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureContactPersonsEntryDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    legislation: List[MixtureContactPersonsEntryDataProtectionLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
            },
        )
    )


@dataclass
class MixtureOtherNamesEntryProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    legislation: List[MixtureOtherNamesEntryProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOwnerLegalEntityProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    legislation: List[MixtureOwnerLegalEntityProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureRoleInSupplyChainRoleProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    legislation: List[MixtureRoleInSupplyChainRoleProtectionLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
            },
        )
    )


@dataclass
class MixtureThirdPartyProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    legislation: List[MixtureThirdPartyProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureContactPersonsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[MixtureContactPersonsEntryDataProtection] = (
        field(
            default=None,
            metadata={
                "name": "DataProtection",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
            },
        )
    )
    contact_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOtherNamesEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    protection: Optional[MixtureOtherNamesEntryProtection] = field(
        default=None,
        metadata={
            "name": "Protection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    name_type: Optional[MixtureOtherNamesEntryNameType] = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    country: List[MixtureOtherNamesEntryCountry] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureRoleInSupplyChain:
    class Meta:
        global_type = False

    role_protection: Optional[MixtureRoleInSupplyChainRoleProtection] = field(
        default=None,
        metadata={
            "name": "RoleProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    manufacturer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    importer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Importer",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    only_representative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlyRepresentative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )
    downstream_user: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DownstreamUser",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureContactPersons:
    class Meta:
        global_type = False

    entry: List[MixtureContactPersonsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class MixtureOtherNames:
    class Meta:
        global_type = False

    entry: List[MixtureOtherNamesEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0",
        },
    )


@dataclass
class Mixture:
    class Meta:
        name = "MIXTURE"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/MIXTURE/9.0"

    templates: Optional[MixtureTemplates] = field(
        default=None,
        metadata={
            "name": "Templates",
            "type": "Element",
            "required": True,
        },
    )
    mixture_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MixtureName",
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
    other_names: Optional[MixtureOtherNames] = field(
        default=None,
        metadata={
            "name": "OtherNames",
            "type": "Element",
        },
    )
    owner_legal_entity_protection: Optional[
        MixtureOwnerLegalEntityProtection
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
    third_party_protection: Optional[MixtureThirdPartyProtection] = field(
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
    contact_persons: Optional[MixtureContactPersons] = field(
        default=None,
        metadata={
            "name": "ContactPersons",
            "type": "Element",
        },
    )
    role_in_supply_chain: Optional[MixtureRoleInSupplyChain] = field(
        default=None,
        metadata={
            "name": "RoleInSupplyChain",
            "type": "Element",
        },
    )
