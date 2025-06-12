from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from emissionsfrompreservativetreatedwood_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    C113,
    F102,
    N64,
    N78,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Oe10,
    Oe20,
    Oe30,
    Oe40,
    Oe50,
    Oe60,
    Oe70,
    Oe80,
    Oe90,
    Oe240,
    Oe250,
    Oe260,
    Oe270,
    Oe280,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660427,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from emissionsfrompreservativetreatedwood_6_5.models.platform_fields import (
    AttachmentListField,
    BaseDataProtectionField,
    BasePhysicalQuantityField,
    BasePhysicalQuantityRangeField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    LowerQualifier,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
    UpperQualifier,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0"


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660427] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsApplicationApplicationMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe70] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe20] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsStudyType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe90] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodSurfacePerWaterVolume(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Oe250] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodWeightPerWaterVolume(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Oe240] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryDensity(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Oe240] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryGrowthRate(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryWoodSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe80] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntryMeanTemp(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestWater(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe10] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeActiveIngredients(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe50] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativePreservative(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeRetention(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe60] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeTypeFormulation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryEmissionRate(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Oe280] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTime(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTypeOfSpecimen(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Oe270] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetentionEntryRetention(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Oe260] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionValidityCritFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsApplication:
    class Meta:
        global_type = False

    application_method: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsApplicationApplicationMethod
    ] = field(
        default=None,
        metadata={
            "name": "ApplicationMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    treat_facility: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TreatFacility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    registrant: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Registrant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    detail_method: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "DetailMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    application_date: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    formula_retention: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "FormulaRetention",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    condition_procedure: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ConditionProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    end_sealant: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "EndSealant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    subs_treat: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SubsTreat",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    wood_weight_per_water_volume: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodWeightPerWaterVolume
    ] = field(
        default=None,
        metadata={
            "name": "WoodWeightPerWaterVolume",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    wood_surface_per_water_volume: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodSurfacePerWaterVolume
    ] = field(
        default=None,
        metadata={
            "name": "WoodSurfacePerWaterVolume",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    wood_species: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryWoodSpecies
    ] = field(
        default=None,
        metadata={
            "name": "WoodSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    source_wood: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SourceWood",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    density: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryDensity
    ] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    growth_rate: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryGrowthRate
    ] = field(
        default=None,
        metadata={
            "name": "GrowthRate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    dimensionx: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dimensionx",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    dimensiony: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dimensiony",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    dimensionz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dimensionz",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    moisture_content: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MoistureContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    ph: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    mean_temp: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntryMeanTemp
    ] = field(
        default=None,
        metadata={
            "name": "MeanTemp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservative:
    class Meta:
        global_type = False

    supplier_preserv: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierPreserv",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    type_formulation: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeTypeFormulation
    ] = field(
        default=None,
        metadata={
            "name": "TypeFormulation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    preservative: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativePreservative
    ] = field(
        default=None,
        metadata={
            "name": "Preservative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    active_ingredients: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeActiveIngredients
    ] = field(
        default=None,
        metadata={
            "name": "ActiveIngredients",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    composition: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Composition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    coformulants: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Coformulants",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    retention: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeRetention
    ] = field(
        default=None,
        metadata={
            "name": "Retention",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    time: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTime
    ] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    active_ingredient: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ActiveIngredient",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    type_of_specimen: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTypeOfSpecimen
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfSpecimen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    specimen_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecimenNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
            "nillable": True,
        },
    )
    emission_rate: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryEmissionRate
    ] = field(
        default=None,
        metadata={
            "name": "EmissionRate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetentionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    replicate_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReplicateNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
            "nillable": True,
        },
    )
    retention: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetentionEntryRetention
    ] = field(
        default=None,
        metadata={
            "name": "Retention",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    retention_stddev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RetentionStddev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    retention_remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "RetentionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditions:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimens:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamples:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeaching:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetention:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetentionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimens:
    class Meta:
        global_type = False

    test_specimens: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimens
    ] = field(
        default=None,
        metadata={
            "name": "TestSpecimens",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    water_samples: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamples
    ] = field(
        default=None,
        metadata={
            "name": "WaterSamples",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    loading_conditions: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditions
    ] = field(
        default=None,
        metadata={
            "name": "LoadingConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    kinetic_evaluation: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "KineticEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    study_type: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsStudyType
    ] = field(
        default=None,
        metadata={
            "name": "StudyType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    company_study_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyStudyNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    report_date: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ReportDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    test_water: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestWater
    ] = field(
        default=None,
        metadata={
            "name": "TestWater",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    wood_preservative: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservative
    ] = field(
        default=None,
        metadata={
            "name": "WoodPreservative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    application: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsApplication
    ] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    test_specimens: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimens
    ] = field(
        default=None,
        metadata={
            "name": "TestSpecimens",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussion:
    class Meta:
        global_type = False

    retention: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetention
    ] = field(
        default=None,
        metadata={
            "name": "Retention",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    leaching: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeaching
    ] = field(
        default=None,
        metadata={
            "name": "Leaching",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    validity_crit_fulfilled: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionValidityCritFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCritFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    quality_criteria: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "QualityCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWood:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EmissionsFromPreservativeTreatedWood"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/9.0"

    administrative_data: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
