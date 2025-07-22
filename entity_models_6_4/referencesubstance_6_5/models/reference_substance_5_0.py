from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.referencesubstance_6_5.models.common_types_domain_v5 import (
    N05,
    N64,
    N78,
    N95,
    Pg660192,
)

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0"
)


@dataclass
class ReferenceSubstanceGeneralInfo:
    class Meta:
        global_type = False

    reference_substance_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstanceName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
            "required": True,
        },
    )


@dataclass
class ReferenceSubstanceInventoryInventoryEntry:
    class Meta:
        global_type = False

    entry: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoChemicalStructureFilesEntry:
    class Meta:
        global_type = False

    structure_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "StructureFile",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    remarks_chem_struct: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksChemStruct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoMolecularWeightRange:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoCasinfo:
    class Meta:
        global_type = False

    casnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "CASNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    casname: Optional[str] = field(
        default=None,
        metadata={
            "name": "CASName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceInventory:
    class Meta:
        global_type = False

    inventory_entry: Optional[ReferenceSubstanceInventoryInventoryEntry] = (
        field(
            default=None,
            metadata={
                "name": "InventoryEntry",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
            },
        )
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoChemicalStructureFiles:
    class Meta:
        global_type = False

    entry: List[
        ReferenceSubstanceMolecularStructuralInfoChemicalStructureFilesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceNoInfoAvailableInventoryEntryJustification:
    class Meta:
        global_type = False

    value: Optional[N95] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelatedSubstancesEntryIdentifier:
    class Meta:
        global_type = False

    value: Optional[Pg660192] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelation:
    class Meta:
        global_type = False

    value: Optional[N05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoSynonymsEntryIdentifier:
    class Meta:
        global_type = False

    value: Optional[Pg660192] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    legislation: List[
        ReferenceSubstanceMolecularStructuralInfoDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceNoInfoAvailable:
    class Meta:
        global_type = False

    inventory_entry_justification: Optional[
        ReferenceSubstanceNoInfoAvailableInventoryEntryJustification
    ] = field(
        default=None,
        metadata={
            "name": "InventoryEntryJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    legislation: List[
        ReferenceSubstanceReferenceSubstanceInfoDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelatedSubstancesEntry:
    class Meta:
        global_type = False

    identifier: Optional[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelatedSubstancesEntryIdentifier
    ] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoSynonymsEntry:
    class Meta:
        global_type = False

    identifier: Optional[
        ReferenceSubstanceReferenceSubstanceInfoSynonymsEntryIdentifier
    ] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfo:
    class Meta:
        global_type = False

    data_protection: Optional[
        ReferenceSubstanceMolecularStructuralInfoDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    molecular_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "MolecularFormula",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    molecular_weight_range: Optional[
        ReferenceSubstanceMolecularStructuralInfoMolecularWeightRange
    ] = field(
        default=None,
        metadata={
            "name": "MolecularWeightRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    smiles_notation: Optional[str] = field(
        default=None,
        metadata={
            "name": "SmilesNotation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    in_chl: Optional[str] = field(
        default=None,
        metadata={
            "name": "InChl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    structural_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "StructuralFormula",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    chemical_structure_files: Optional[
        ReferenceSubstanceMolecularStructuralInfoChemicalStructureFiles
    ] = field(
        default=None,
        metadata={
            "name": "ChemicalStructureFiles",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelatedSubstances:
    class Meta:
        global_type = False

    entry: List[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelatedSubstancesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoSynonyms:
    class Meta:
        global_type = False

    entry: List[ReferenceSubstanceReferenceSubstanceInfoSynonymsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntry:
    class Meta:
        global_type = False

    related_substances: Optional[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelatedSubstances
    ] = field(
        default=None,
        metadata={
            "name": "RelatedSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    relation: Optional[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntryRelation
    ] = field(
        default=None,
        metadata={
            "name": "Relation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstances:
    class Meta:
        global_type = False

    entry: List[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstancesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfoRelatedSubstances:
    class Meta:
        global_type = False

    identifiers_of_related_substances: Optional[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstancesIdentifiersOfRelatedSubstances
    ] = field(
        default=None,
        metadata={
            "name": "IdentifiersOfRelatedSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    group_category_info: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GroupCategoryInfo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstanceReferenceSubstanceInfo:
    class Meta:
        global_type = False

    data_protection: Optional[
        ReferenceSubstanceReferenceSubstanceInfoDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    iupac_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IupacName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    synonyms: Optional[ReferenceSubstanceReferenceSubstanceInfoSynonyms] = (
        field(
            default=None,
            metadata={
                "name": "Synonyms",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
            },
        )
    )
    casinfo: Optional[ReferenceSubstanceReferenceSubstanceInfoCasinfo] = field(
        default=None,
        metadata={
            "name": "CASInfo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )
    related_substances: Optional[
        ReferenceSubstanceReferenceSubstanceInfoRelatedSubstances
    ] = field(
        default=None,
        metadata={
            "name": "RelatedSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0",
        },
    )


@dataclass
class ReferenceSubstance:
    class Meta:
        name = "REFERENCE_SUBSTANCE"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/5.0"
        )

    general_info: Optional[ReferenceSubstanceGeneralInfo] = field(
        default=None,
        metadata={
            "name": "GeneralInfo",
            "type": "Element",
            "required": True,
        },
    )
    inventory: Optional[ReferenceSubstanceInventory] = field(
        default=None,
        metadata={
            "name": "Inventory",
            "type": "Element",
        },
    )
    no_info_available: Optional[ReferenceSubstanceNoInfoAvailable] = field(
        default=None,
        metadata={
            "name": "NoInfoAvailable",
            "type": "Element",
        },
    )
    reference_substance_info: Optional[
        ReferenceSubstanceReferenceSubstanceInfo
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstanceInfo",
            "type": "Element",
        },
    )
    molecular_structural_info: Optional[
        ReferenceSubstanceMolecularStructuralInfo
    ] = field(
        default=None,
        metadata={
            "name": "MolecularStructuralInfo",
            "type": "Element",
        },
    )
