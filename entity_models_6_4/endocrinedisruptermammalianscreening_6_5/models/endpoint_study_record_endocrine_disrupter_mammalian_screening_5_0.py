from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.endocrinedisruptermammalianscreening_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    T24,
    T48,
    T102,
    T156,
    T285,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z38,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660234,
    Pg660307,
    Pg660443,
    Pg660444,
    Pg660445,
    Pg660446,
    Pg660447,
    Pg660448,
    Pg660449,
    Pg660450,
    Pg660453,
    Pg660464,
    Pg660465,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0"


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    observations_and_examinations_performed_and_frequency: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ObservationsAndExaminationsPerformedAndFrequency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    sacrifice_and_pathology: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SacrificeAndPathology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other_examinations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660450] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureControlAnimals:
    class Meta:
        global_type = False

    value: Optional[Pg660446] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T285] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureRouteOfAdministration:
    class Meta:
        global_type = False

    value: Optional[Pg660445] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureVehicle:
    class Meta:
        global_type = False

    value: Optional[T48] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Pg660465] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsMethodType:
    class Meta:
        global_type = False

    value: Optional[Pg660449] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[Pg660464] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsState:
    class Meta:
        global_type = False

    value: Optional[Pg660444] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[Pg660443] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660448] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660447] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T156] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEndocrineDisruptingPotential:
    class Meta:
        global_type = False

    value: Optional[Pg660453] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionMaximumToleratedDoseLevelExceeded:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservBodyweight:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservClinChem:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservClinSigns:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservFoodConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservGrpathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservHistopathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservMortality:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservOrganWeights:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservWaterConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry:
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_species_strain_selection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    state: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimalsState
    ] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_test_animals_and_environmental_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestAnimalsAndEnvironmentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminations:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_mortality: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_water_consum: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminationsObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_route_of_administration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnRouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_oral_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnOralExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    duration_of_treatment_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTreatmentExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    frequency_of_treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    positive_control: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevels:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevelsEfflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    method_type: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsMethodType
    ] = field(
        default=None,
        metadata={
            "name": "MethodType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    test_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussion:
    class Meta:
        global_type = False

    endocrine_disrupting_potential: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEndocrineDisruptingPotential
    ] = field(
        default=None,
        metadata={
            "name": "EndocrineDisruptingPotential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    maximum_tolerated_dose_level_exceeded: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionMaximumToleratedDoseLevelExceeded
    ] = field(
        default=None,
        metadata={
            "name": "MaximumToleratedDoseLevelExceeded",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    results_of_examinations: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionResultsOfExaminations
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    effect_levels: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionEffectLevels
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterMammalianScreening:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EndocrineDisrupterMammalianScreening"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterMammalianScreening/5.0"

    administrative_data: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordEndocrineDisrupterMammalianScreeningApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
