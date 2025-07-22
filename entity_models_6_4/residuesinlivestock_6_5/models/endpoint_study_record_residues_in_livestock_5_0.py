from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.residuesinlivestock_6_5.models.common_types_oecd_v5 import (
    A36,
    C1112,
    N64,
    N78,
    T163,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z21,
    Z28,
    Z29,
    Z30,
    Z40,
    Z41,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660291,
    Pg660490,
    Pg660498,
    Pg6604961,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0"


@dataclass
class EndpointStudyRecordResiduesInLivestockApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsFurtherDetailsOnStudyDesign:
    class Meta:
        global_type = False

    further_details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FurtherDetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    details_on_sampling_and_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSamplingAndAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660291] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAdministrationExposureControlAnimals:
    class Meta:
        global_type = False

    value: Optional[T163] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAdministrationExposureTreatmentTypeRouteOfExposure:
    class Meta:
        global_type = False

    value: Optional[Z21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Z29] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsProductType:
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[Z28] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTypeOfStudy:
    class Meta:
        global_type = False

    value: Optional[Z41] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryMatrixTissueSampled:
    class Meta:
        global_type = False

    value: Optional[Pg660498] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntryResidueLevelCalculated:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntryResidueLevelCorrected:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntryResidueLevelMeasured:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntrySamplingNo:
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryTotalMean:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordResiduesInLivestockDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordResiduesInLivestockDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    treatment_type_route_of_exposure: List[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAdministrationExposureTreatmentTypeRouteOfExposure
    ] = field(
        default_factory=list,
        metadata={
            "name": "TreatmentTypeRouteOfExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    duration_and_frequency_of_dosing: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationAndFrequencyOfDosing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    doses_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    details_on_dosing: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDosing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    no_of_animals_per_dose_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDoseGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: List[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    details_on_housing_conditions_and_test_animals: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnHousingConditionsAndTestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    details_on_dietary_regime: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDietaryRegime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordResiduesInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntry:
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    residue_level_measured: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntryResidueLevelMeasured
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    residue_level_calculated: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntryResidueLevelCalculated
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    residue_level_corrected: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntryResidueLevelCorrected
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCorrected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevels:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevelsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockMaterialsAndMethods:
    class Meta:
        global_type = False

    background_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    product_type: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    type_of_study: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTypeOfStudy
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    further_details_on_study_design: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsFurtherDetailsOnStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "FurtherDetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntry:
    class Meta:
        global_type = False

    sampling_no: List[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntrySamplingNo
    ] = field(
        default_factory=list,
        metadata={
            "name": "SamplingNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    matrix_tissue_sampled: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryMatrixTissueSampled
    ] = field(
        default=None,
        metadata={
            "name": "MatrixTissueSampled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    sampling_time: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SamplingTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    dose_feeding_level: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DoseFeedingLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    residue_levels: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryResidueLevels
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    total_mean: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntryTotalMean
    ] = field(
        default=None,
        metadata={
            "name": "TotalMean",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestockResultsAndDiscussion:
    class Meta:
        global_type = False

    storage_stability: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    residue_data: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionResidueData
    ] = field(
        default=None,
        metadata={
            "name": "ResidueData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    recoveries: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Recoveries",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    depuration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Depuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    residue_transfer: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResidueTransfer",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInLivestock:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ResiduesInLivestock"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInLivestock/5.0"

    administrative_data: Optional[
        EndpointStudyRecordResiduesInLivestockAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordResiduesInLivestockDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordResiduesInLivestockMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordResiduesInLivestockResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordResiduesInLivestockOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordResiduesInLivestockApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
