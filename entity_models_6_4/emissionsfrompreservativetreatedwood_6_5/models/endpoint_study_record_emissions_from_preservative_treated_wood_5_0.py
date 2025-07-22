from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.emissionsfrompreservativetreatedwood_6_5.models.common_types_oecd_v5 import (
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
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0"


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryGrowthRate:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660427] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsApplicationApplicationMethod:
    class Meta:
        global_type = False

    value: Optional[Oe70] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Oe20] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsStudyType:
    class Meta:
        global_type = False

    value: Optional[Oe90] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodSurfacePerWaterVolume:
    class Meta:
        global_type = False

    unit_code: Optional[Oe250] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodWeightPerWaterVolume:
    class Meta:
        global_type = False

    unit_code: Optional[Oe240] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryDensity:
    class Meta:
        global_type = False

    unit_code: Optional[Oe240] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryWoodSpecies:
    class Meta:
        global_type = False

    value: Optional[Oe80] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntryMeanTemp:
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestWater:
    class Meta:
        global_type = False

    value: Optional[Oe10] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeActiveIngredients:
    class Meta:
        global_type = False

    value: Optional[Oe50] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativePreservative:
    class Meta:
        global_type = False

    value: Optional[Oe40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeRetention:
    class Meta:
        global_type = False

    value: Optional[Oe60] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeTypeFormulation:
    class Meta:
        global_type = False

    value: Optional[Oe30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryEmissionRate:
    class Meta:
        global_type = False

    unit_code: Optional[Oe280] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTime:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTypeOfSpecimen:
    class Meta:
        global_type = False

    value: Optional[Oe270] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetentionEntryRetention:
    class Meta:
        global_type = False

    unit_code: Optional[Oe260] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionValidityCritFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    treat_facility: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TreatFacility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    registrant: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Registrant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    detail_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    application_date: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    formula_retention: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FormulaRetention",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    condition_procedure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConditionProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    end_sealant: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EndSealant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    subs_treat: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SubsTreat",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntry:
    class Meta:
        global_type = False

    wood_weight_per_water_volume: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodWeightPerWaterVolume
    ] = field(
        default=None,
        metadata={
            "name": "WoodWeightPerWaterVolume",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    wood_surface_per_water_volume: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditionsEntryWoodSurfacePerWaterVolume
    ] = field(
        default=None,
        metadata={
            "name": "WoodSurfacePerWaterVolume",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntry:
    class Meta:
        global_type = False

    wood_species: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryWoodSpecies
    ] = field(
        default=None,
        metadata={
            "name": "WoodSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    source_wood: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SourceWood",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    density: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryDensity
    ] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    growth_rate: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensTestSpecimensEntryGrowthRate
    ] = field(
        default=None,
        metadata={
            "name": "GrowthRate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    dimensionx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dimensionx",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    dimensiony: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dimensiony",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    dimensionz: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dimensionz",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    moisture_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoistureContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntry:
    class Meta:
        global_type = False

    ph: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    mean_temp: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamplesEntryMeanTemp
    ] = field(
        default=None,
        metadata={
            "name": "MeanTemp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    type_formulation: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeTypeFormulation
    ] = field(
        default=None,
        metadata={
            "name": "TypeFormulation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    preservative: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativePreservative
    ] = field(
        default=None,
        metadata={
            "name": "Preservative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    active_ingredients: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeActiveIngredients
    ] = field(
        default=None,
        metadata={
            "name": "ActiveIngredients",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    composition: Optional[str] = field(
        default=None,
        metadata={
            "name": "Composition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    coformulants: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Coformulants",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    retention: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservativeRetention
    ] = field(
        default=None,
        metadata={
            "name": "Retention",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntry:
    class Meta:
        global_type = False

    time: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTime
    ] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    active_ingredient: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ActiveIngredient",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    type_of_specimen: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeachingEntryTypeOfSpecimen
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfSpecimen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    specimen_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecimenNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionRetentionEntry:
    class Meta:
        global_type = False

    replicate_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReplicateNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    retention_stddev: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetentionStddev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    retention_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RetentionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    water_samples: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensWaterSamples
    ] = field(
        default=None,
        metadata={
            "name": "WaterSamples",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    loading_conditions: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimensLoadingConditions
    ] = field(
        default=None,
        metadata={
            "name": "LoadingConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    leaching: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionLeaching
    ] = field(
        default=None,
        metadata={
            "name": "Leaching",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    validity_crit_fulfilled: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionValidityCritFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCritFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    quality_criteria: List[str] = field(
        default_factory=list,
        metadata={
            "name": "QualityCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    study_type: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsStudyType
    ] = field(
        default=None,
        metadata={
            "name": "StudyType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    company_study_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyStudyNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    report_date: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReportDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    test_water: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestWater
    ] = field(
        default=None,
        metadata={
            "name": "TestWater",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    wood_preservative: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsWoodPreservative
    ] = field(
        default=None,
        metadata={
            "name": "WoodPreservative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    application: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsApplication
    ] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    test_specimens: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsTestSpecimens
    ] = field(
        default=None,
        metadata={
            "name": "TestSpecimens",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordEmissionsFromPreservativeTreatedWoodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEmissionsFromPreservativeTreatedWood:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EmissionsFromPreservativeTreatedWood"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EmissionsFromPreservativeTreatedWood/5.0"

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
