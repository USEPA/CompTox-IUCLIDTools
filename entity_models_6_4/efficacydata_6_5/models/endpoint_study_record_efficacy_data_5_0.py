from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.efficacydata_6_5.models.common_types_oecd_v5 import (
    A36,
    C106,
    C109,
    C110,
    C112,
    C113,
    C114,
    C115,
    C116,
    C117,
    C118,
    N64,
    N78,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z36,
    Z40,
    Z52,
    Z58,
    Pg660000,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660352,
    Pg660360,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0"


@dataclass
class EndpointStudyRecordEfficacyDataApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsProductsMaterialsOrganismsOrObjectsToBeProtectedUnderStudy:
    class Meta:
        global_type = False

    organisms_to_be_protected_or_treated_materials: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OrganismsToBeProtectedOrTreatedMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryEfficacy:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660352] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataBackgroundSourceOfInformationTypeOfStudy:
    class Meta:
        global_type = False

    value: Optional[C112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsComplianceWithQualityStandards:
    class Meta:
        global_type = False

    value: Optional[Z58] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[C106] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntryCommonName:
    class Meta:
        global_type = False

    value: Optional[C110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntryDevelopmentalStage:
    class Meta:
        global_type = False

    value: Optional[C116] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntryScientificName:
    class Meta:
        global_type = False

    value: Optional[C109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsStudyDesignMethodOfApplication:
    class Meta:
        global_type = False

    value: Optional[C118] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsStudyDesignTotalExposureDurationContactTime:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsTestMaterialsAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsTestMaterialsFormulationType:
    class Meta:
        global_type = False

    value: Optional[C115] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryEfficacyParameter:
    class Meta:
        global_type = False

    value: Optional[C114] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryInterferingSubstances:
    class Meta:
        global_type = False

    value: Optional[Pg660000] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryTimeToProduceEffect:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryInterferingSubstances:
    class Meta:
        global_type = False

    value: Optional[Pg660000] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryMinimumEffectiveDose:
    class Meta:
        global_type = False

    unit_code: Optional[C117] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryTimeToProduceEffect:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionObservedLimitationsOnEfficacyIndicationOfResistance:
    class Meta:
        global_type = False

    value: Optional[Pg660360] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionObservedLimitationsOnEfficacyUndesirableOrUnintendedSideEffects:
    class Meta:
        global_type = False

    value: Optional[Pg660360] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEfficacyDataAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataBackground:
    class Meta:
        global_type = False

    background_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    objective_label_claim_addressed: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ObjectiveLabelClaimAddressed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    source_of_information_type_of_study: List[
        EndpointStudyRecordEfficacyDataBackgroundSourceOfInformationTypeOfStudy
    ] = field(
        default_factory=list,
        metadata={
            "name": "SourceOfInformationTypeOfStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEfficacyDataDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEfficacyDataDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntry:
    class Meta:
        global_type = False

    scientific_name: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntryScientificName
    ] = field(
        default=None,
        metadata={
            "name": "ScientificName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    common_name: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntryCommonName
    ] = field(
        default=None,
        metadata={
            "name": "CommonName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    developmental_stage: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntryDevelopmentalStage
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    total_exposure_duration_contact_time: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsStudyDesignTotalExposureDurationContactTime
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDurationContactTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    mode_of_efficacy_assessment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ModeOfEfficacyAssessment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    method_of_application: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsStudyDesignMethodOfApplication
    ] = field(
        default=None,
        metadata={
            "name": "MethodOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    formulation_type: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsTestMaterialsFormulationType
    ] = field(
        default=None,
        metadata={
            "name": "FormulationType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    analytical_monitoring: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsTestMaterialsAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    details_on_sampling_and_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSamplingAndAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEfficacyDataOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntry:
    class Meta:
        global_type = False

    efficacy_parameter: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryEfficacyParameter
    ] = field(
        default=None,
        metadata={
            "name": "EfficacyParameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    efficacy: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryEfficacy
    ] = field(
        default=None,
        metadata={
            "name": "Efficacy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    time_to_produce_effect: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryTimeToProduceEffect
    ] = field(
        default=None,
        metadata={
            "name": "TimeToProduceEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Treatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    interfering_substances: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryInterferingSubstances
    ] = field(
        default=None,
        metadata={
            "name": "InterferingSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntry:
    class Meta:
        global_type = False

    minimum_effective_dose: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryMinimumEffectiveDose
    ] = field(
        default=None,
        metadata={
            "name": "MinimumEffectiveDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    time_to_produce_effect: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryTimeToProduceEffect
    ] = field(
        default=None,
        metadata={
            "name": "TimeToProduceEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Treatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    interfering_substances: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryInterferingSubstances
    ] = field(
        default=None,
        metadata={
            "name": "InterferingSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionObservedLimitationsOnEfficacy:
    class Meta:
        global_type = False

    indication_of_resistance: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionObservedLimitationsOnEfficacyIndicationOfResistance
    ] = field(
        default=None,
        metadata={
            "name": "IndicationOfResistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    details_on_development_of_resistance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDevelopmentOfResistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    undesirable_or_unintended_side_effects: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionObservedLimitationsOnEfficacyUndesirableOrUnintendedSideEffects
    ] = field(
        default=None,
        metadata={
            "name": "UndesirableOrUnintendedSideEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    details_on_undesirable_or_unintended_side_effects: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnUndesirableOrUnintendedSideEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    other_limitations_observed: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherLimitationsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    relevance_of_study_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RelevanceOfStudyResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganisms:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganismsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessment:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessmentEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDose:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDoseEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEfficacyDataAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlled:
    class Meta:
        global_type = False

    test_target_organisms: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlledTestTargetOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestTargetOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    details_on_test_target_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestTargetOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataResultsAndDiscussion:
    class Meta:
        global_type = False

    efficacy_performance_assessment: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionEfficacyPerformanceAssessment
    ] = field(
        default=None,
        metadata={
            "name": "EfficacyPerformanceAssessment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    minimum_effective_dose: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionMinimumEffectiveDose
    ] = field(
        default=None,
        metadata={
            "name": "MinimumEffectiveDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    results_on_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsOnDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    observed_limitations_on_efficacy: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionObservedLimitationsOnEfficacy
    ] = field(
        default=None,
        metadata={
            "name": "ObservedLimitationsOnEfficacy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyDataMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    compliance_with_quality_standards: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsComplianceWithQualityStandards
    ] = field(
        default=None,
        metadata={
            "name": "ComplianceWithQualityStandards",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    pest_target_organisms_to_be_controlled: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsPestTargetOrganismsToBeControlled
    ] = field(
        default=None,
        metadata={
            "name": "PestTargetOrganismsToBeControlled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    products_materials_organisms_or_objects_to_be_protected_under_study: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsProductsMaterialsOrganismsOrObjectsToBeProtectedUnderStudy
    ] = field(
        default=None,
        metadata={
            "name": "ProductsMaterialsOrganismsOrObjectsToBeProtectedUnderStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEfficacyData:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EfficacyData"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EfficacyData/5.0"

    administrative_data: Optional[
        EndpointStudyRecordEfficacyDataAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordEfficacyDataDataSource] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    background: Optional[EndpointStudyRecordEfficacyDataBackground] = field(
        default=None,
        metadata={
            "name": "Background",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordEfficacyDataMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordEfficacyDataResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordEfficacyDataOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordEfficacyDataApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
