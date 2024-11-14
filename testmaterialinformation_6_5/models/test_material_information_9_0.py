from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from testmaterialinformation_6_5.models.common_types_domain_v9 import (
    A101,
    N24,
    Pg660011,
    Pg660016,
)
from testmaterialinformation_6_5.models.platform_fields import (
    BasePhysicalQuantityRangeField,
    BasePicklistField,
    LowerQualifier,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
    UpperQualifier,
)

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0"
)


@dataclass
class TestMaterialInformationCompositionCompositionListEntryConcentration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[N24] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )


@dataclass
class TestMaterialInformationCompositionCompositionListEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660016] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )


@dataclass
class TestMaterialInformationCompositionCompositionPurityOtherInformation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660011] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )


@dataclass
class TestMaterialInformationCompositionOtherCharacteristicsTestMaterialForm(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A101] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )


@dataclass
class TestMaterialInformationCompositionCompositionListEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        TestMaterialInformationCompositionCompositionListEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    concentration: Optional[
        TestMaterialInformationCompositionCompositionListEntryConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )


@dataclass
class TestMaterialInformationCompositionOtherCharacteristics:
    class Meta:
        global_type = False

    test_material_form: Optional[
        TestMaterialInformationCompositionOtherCharacteristicsTestMaterialForm
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterialForm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    details_on_test_material: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    confidential_details_on_test_material: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "ConfidentialDetailsOnTestMaterial",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
            },
        )
    )


@dataclass
class TestMaterialInformationCompositionCompositionList:
    class Meta:
        global_type = False

    entry: List[TestMaterialInformationCompositionCompositionListEntry] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
            },
        )
    )


@dataclass
class TestMaterialInformationComposition:
    class Meta:
        global_type = False

    composition_list: Optional[
        TestMaterialInformationCompositionCompositionList
    ] = field(
        default=None,
        metadata={
            "name": "CompositionList",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    composition_purity_other_information: Optional[
        TestMaterialInformationCompositionCompositionPurityOtherInformation
    ] = field(
        default=None,
        metadata={
            "name": "CompositionPurityOtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )
    other_characteristics: Optional[
        TestMaterialInformationCompositionOtherCharacteristics
    ] = field(
        default=None,
        metadata={
            "name": "OtherCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0",
        },
    )


@dataclass
class TestMaterialInformation:
    class Meta:
        name = "TEST_MATERIAL_INFORMATION"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/TEST_MATERIAL_INFORMATION/9.0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    composition: Optional[TestMaterialInformationComposition] = field(
        default=None,
        metadata={
            "name": "Composition",
            "type": "Element",
        },
    )
