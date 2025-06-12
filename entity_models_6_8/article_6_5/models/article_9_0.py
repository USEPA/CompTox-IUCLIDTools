from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from article_6_5.models.common_types_domain_v9 import (
    Pg660564,
    Pg660567,
    Pg660741,
    Pg660742,
    Pg660746,
    Pg660753,
    Pg660757,
    Pg660759,
    Pg660760,
    Pg660761,
    Pg660762,
    Pg660766,
    Pg660768,
    Pg661607,
)
from article_6_5.models.platform_fields import (
    BasePhysicalQuantityField,
    BasePhysicalQuantityRangeField,
    BasePicklistField,
    LowerQualifier,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
    UpperQualifier,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0"


@dataclass
class ArticleCategorisationArticleCategory(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660768] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCategorisationEuproductionFlag(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660742] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsColour(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg661607] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsDensity(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660760] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsDiameter(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660759] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsHeight(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660759] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsLength(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660759] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsOtherCharacteristicsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    other_characteristic: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "OtherCharacteristic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsPictureEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    picture: Optional[str] = field(
        default=None,
        metadata={
            "name": "Picture",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsVolume(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660762] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsWeight(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660761] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsWidth(BasePhysicalQuantityField):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660759] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleComplexObjectComponentsComplexObjectComponentsEntryNumberOfUnits(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsCandidateListSubstanceNoLongerPresentEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    candidate_list_substance_no_longer_present: Optional[str] = field(
        default=None,
        metadata={
            "name": "CandidateListSubstanceNoLongerPresent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElementEntryConcentrationRange(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660757] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElementEntryMaterialCategoriesEntryAdditionalMaterialCharacteristics(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660766] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElementEntryMaterialCategoriesEntryMaterialCategory(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660753] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElementEntryMixtureCategoryEupcs(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660567] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersOtherArticleIdEntryType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660746] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersOtherNamesEntryType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660741] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersPrimaryArticleIdentifierType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg660746] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleSafeUseInstructionsDisassemblingInstructionsListEntryLanguage(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660564] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleSafeUseInstructionsSafeUseInstructionsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    safe_use_instruction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SafeUseInstruction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCategorisation:
    class Meta:
        global_type = False

    article_category: List[ArticleCategorisationArticleCategory] = field(
        default_factory=list,
        metadata={
            "name": "ArticleCategory",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    euproduction_flag: Optional[ArticleCategorisationEuproductionFlag] = field(
        default=None,
        metadata={
            "name": "EUProductionFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsOtherCharacteristics:
    class Meta:
        global_type = False

    entry: List[ArticleCharacteristicsOtherCharacteristicsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristicsPicture:
    class Meta:
        global_type = False

    entry: List[ArticleCharacteristicsPictureEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleComplexObjectComponentsComplexObjectComponentsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    article_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArticleLink",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    number_of_units: Optional[
        ArticleComplexObjectComponentsComplexObjectComponentsEntryNumberOfUnits
    ] = field(
        default=None,
        metadata={
            "name": "NumberOfUnits",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsCandidateListSubstanceNoLongerPresent:
    class Meta:
        global_type = False

    entry: List[
        ArticleConcernElementsCandidateListSubstanceNoLongerPresentEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElementEntryMaterialCategoriesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    material_category: Optional[
        ArticleConcernElementsConcernElementEntryMaterialCategoriesEntryMaterialCategory
    ] = field(
        default=None,
        metadata={
            "name": "MaterialCategory",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    additional_material_characteristics: List[
        ArticleConcernElementsConcernElementEntryMaterialCategoriesEntryAdditionalMaterialCharacteristics
    ] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalMaterialCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersOtherArticleIdEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    type_value: Optional[ArticleIdentifiersOtherArticleIdEntryType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersOtherNamesEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    type_value: Optional[ArticleIdentifiersOtherNamesEntryType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleSafeUseInstructionsDisassemblingInstructionsListEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    language: Optional[
        ArticleSafeUseInstructionsDisassemblingInstructionsListEntryLanguage
    ] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleSafeUseInstructionsSafeUseInstructions:
    class Meta:
        global_type = False

    entry: List[ArticleSafeUseInstructionsSafeUseInstructionsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleCharacteristics:
    class Meta:
        global_type = False

    picture: Optional[ArticleCharacteristicsPicture] = field(
        default=None,
        metadata={
            "name": "Picture",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    height: Optional[ArticleCharacteristicsHeight] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    length: Optional[ArticleCharacteristicsLength] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    width: Optional[ArticleCharacteristicsWidth] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    diameter: Optional[ArticleCharacteristicsDiameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    density: Optional[ArticleCharacteristicsDensity] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    weight: Optional[ArticleCharacteristicsWeight] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    volume: Optional[ArticleCharacteristicsVolume] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    colour: List[ArticleCharacteristicsColour] = field(
        default_factory=list,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    other_characteristics: Optional[
        ArticleCharacteristicsOtherCharacteristics
    ] = field(
        default=None,
        metadata={
            "name": "OtherCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleComplexObjectComponentsComplexObjectComponents:
    class Meta:
        global_type = False

    entry: List[ArticleComplexObjectComponentsComplexObjectComponentsEntry] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
            },
        )
    )


@dataclass
class ArticleConcernElementsConcernElementEntryMaterialCategories:
    class Meta:
        global_type = False

    entry: List[
        ArticleConcernElementsConcernElementEntryMaterialCategoriesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersOtherArticleId:
    class Meta:
        global_type = False

    entry: List[ArticleIdentifiersOtherArticleIdEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiersOtherNames:
    class Meta:
        global_type = False

    entry: List[ArticleIdentifiersOtherNamesEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleSafeUseInstructionsDisassemblingInstructionsList:
    class Meta:
        global_type = False

    entry: List[
        ArticleSafeUseInstructionsDisassemblingInstructionsListEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleComplexObjectComponents:
    class Meta:
        global_type = False

    complex_object_components: Optional[
        ArticleComplexObjectComponentsComplexObjectComponents
    ] = field(
        default=None,
        metadata={
            "name": "ComplexObjectComponents",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElementEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    candidate_list_substance_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "CandidateListSubstanceLink",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    concentration_range: Optional[
        ArticleConcernElementsConcernElementEntryConcentrationRange
    ] = field(
        default=None,
        metadata={
            "name": "ConcentrationRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    material_categories: Optional[
        ArticleConcernElementsConcernElementEntryMaterialCategories
    ] = field(
        default=None,
        metadata={
            "name": "MaterialCategories",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    mixture_category_eupcs: List[
        ArticleConcernElementsConcernElementEntryMixtureCategoryEupcs
    ] = field(
        default_factory=list,
        metadata={
            "name": "MixtureCategoryEUPCS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleIdentifiers:
    class Meta:
        global_type = False

    article_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArticleName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
            "required": True,
        },
    )
    other_names: Optional[ArticleIdentifiersOtherNames] = field(
        default=None,
        metadata={
            "name": "OtherNames",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    primary_article_identifier_type: Optional[
        ArticleIdentifiersPrimaryArticleIdentifierType
    ] = field(
        default=None,
        metadata={
            "name": "PrimaryArticleIdentifierType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    primary_article_identifier_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryArticleIdentifierValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
            "required": True,
        },
    )
    other_article_id: Optional[ArticleIdentifiersOtherArticleId] = field(
        default=None,
        metadata={
            "name": "OtherArticleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleSafeUseInstructions:
    class Meta:
        global_type = False

    no_safe_use_instructions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoSafeUseInstructions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    safe_use_instructions: Optional[
        ArticleSafeUseInstructionsSafeUseInstructions
    ] = field(
        default=None,
        metadata={
            "name": "SafeUseInstructions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    disassembling_instructions_list: Optional[
        ArticleSafeUseInstructionsDisassemblingInstructionsList
    ] = field(
        default=None,
        metadata={
            "name": "DisassemblingInstructionsList",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElementsConcernElement:
    class Meta:
        global_type = False

    entry: List[ArticleConcernElementsConcernElementEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class ArticleConcernElements:
    class Meta:
        global_type = False

    concern_element: Optional[ArticleConcernElementsConcernElement] = field(
        default=None,
        metadata={
            "name": "ConcernElement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )
    candidate_list_substance_no_longer_present: Optional[
        ArticleConcernElementsCandidateListSubstanceNoLongerPresent
    ] = field(
        default=None,
        metadata={
            "name": "CandidateListSubstanceNoLongerPresent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0",
        },
    )


@dataclass
class Article:
    class Meta:
        name = "ARTICLE"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ARTICLE/9.0"

    identifiers: Optional[ArticleIdentifiers] = field(
        default=None,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "required": True,
        },
    )
    categorisation: Optional[ArticleCategorisation] = field(
        default=None,
        metadata={
            "name": "Categorisation",
            "type": "Element",
        },
    )
    characteristics: Optional[ArticleCharacteristics] = field(
        default=None,
        metadata={
            "name": "Characteristics",
            "type": "Element",
        },
    )
    safe_use_instructions: Optional[ArticleSafeUseInstructions] = field(
        default=None,
        metadata={
            "name": "SafeUseInstructions",
            "type": "Element",
        },
    )
    complex_object_components: Optional[ArticleComplexObjectComponents] = (
        field(
            default=None,
            metadata={
                "name": "ComplexObjectComponents",
                "type": "Element",
            },
        )
    )
    concern_elements: Optional[ArticleConcernElements] = field(
        default=None,
        metadata={
            "name": "ConcernElements",
            "type": "Element",
        },
    )
