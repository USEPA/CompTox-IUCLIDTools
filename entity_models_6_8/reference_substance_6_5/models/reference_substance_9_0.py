from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from reference_substance_6_5.models.common_types_domain_v9 import (
    N05,
    N64,
    N78,
    N95,
    Pg660192,
)
from reference_substance_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePhysicalQuantityRangeField,
    BasePicklistField,
    InventoryEntry,
    LowerQualifier,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
    UpperQualifier,
)

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0"
)


@dataclass
class ReferenceSubstanceDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceInventoryInventoryEntry:
    class Meta:
        global_type = False

    entry: List[InventoryEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceInventoryInventoryEntryJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N95] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoChemicalStructureFilesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    structure_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "StructureFile",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    remarks_chem_struct: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "RemarksChemStruct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoMolecularWeightRange(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceRelatedSubstancesRelatedSubstancesEntryIdentifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660192] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceRelatedSubstancesRelatedSubstancesEntryRelation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceSynonymsSynonymsEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceSynonymsSynonymsEntryIdentifier(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660192] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    legislation: List[ReferenceSubstanceDataProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
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
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
            },
        )
    )
    inventory_entry_justification: Optional[
        ReferenceSubstanceInventoryInventoryEntryJustification
    ] = field(
        default=None,
        metadata={
            "name": "InventoryEntryJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    casnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "CASNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    casname: Optional[str] = field(
        default=None,
        metadata={
            "name": "CASName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceMolecularStructuralInfoDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    legislation: List[
        ReferenceSubstanceMolecularStructuralInfoDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceRelatedSubstancesRelatedSubstancesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    identifier: Optional[
        ReferenceSubstanceRelatedSubstancesRelatedSubstancesEntryIdentifier
    ] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    relation: Optional[
        ReferenceSubstanceRelatedSubstancesRelatedSubstancesEntryRelation
    ] = field(
        default=None,
        metadata={
            "name": "Relation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceSynonymsSynonymsEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    legislation: List[
        ReferenceSubstanceSynonymsSynonymsEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    molecular_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "MolecularFormula",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    molecular_weight_range: Optional[
        ReferenceSubstanceMolecularStructuralInfoMolecularWeightRange
    ] = field(
        default=None,
        metadata={
            "name": "MolecularWeightRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    smiles_notation: Optional[str] = field(
        default=None,
        metadata={
            "name": "SmilesNotation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    in_chl: Optional[str] = field(
        default=None,
        metadata={
            "name": "InChl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    in_ch_ikey: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "InChIKey",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    structural_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "StructuralFormula",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    chemical_structure_files: Optional[
        ReferenceSubstanceMolecularStructuralInfoChemicalStructureFiles
    ] = field(
        default=None,
        metadata={
            "name": "ChemicalStructureFiles",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceRelatedSubstancesRelatedSubstances:
    class Meta:
        global_type = False

    entry: List[ReferenceSubstanceRelatedSubstancesRelatedSubstancesEntry] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
            },
        )
    )


@dataclass
class ReferenceSubstanceSynonymsSynonymsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    data_protection: Optional[
        ReferenceSubstanceSynonymsSynonymsEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    identifier: Optional[ReferenceSubstanceSynonymsSynonymsEntryIdentifier] = (
        field(
            default=None,
            metadata={
                "name": "Identifier",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
            },
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceRelatedSubstances:
    class Meta:
        global_type = False

    related_substances: Optional[
        ReferenceSubstanceRelatedSubstancesRelatedSubstances
    ] = field(
        default=None,
        metadata={
            "name": "RelatedSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )
    group_category_info: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "GroupCategoryInfo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceSynonymsSynonyms:
    class Meta:
        global_type = False

    entry: List[ReferenceSubstanceSynonymsSynonymsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstanceSynonyms:
    class Meta:
        global_type = False

    synonyms: Optional[ReferenceSubstanceSynonymsSynonyms] = field(
        default=None,
        metadata={
            "name": "Synonyms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0",
        },
    )


@dataclass
class ReferenceSubstance:
    class Meta:
        name = "REFERENCE_SUBSTANCE"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/REFERENCE_SUBSTANCE/9.0"
        )

    data_protection: Optional[ReferenceSubstanceDataProtection] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
        },
    )
    reference_substance_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstanceName",
            "type": "Element",
            "required": True,
        },
    )
    iupac_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IupacName",
            "type": "Element",
        },
    )
    description: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    inventory: Optional[ReferenceSubstanceInventory] = field(
        default=None,
        metadata={
            "name": "Inventory",
            "type": "Element",
        },
    )
    synonyms: Optional[ReferenceSubstanceSynonyms] = field(
        default=None,
        metadata={
            "name": "Synonyms",
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
    related_substances: Optional[ReferenceSubstanceRelatedSubstances] = field(
        default=None,
        metadata={
            "name": "RelatedSubstances",
            "type": "Element",
        },
    )
