from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.immunotoxicity_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    P29,
    T024,
    T24,
    T25,
    T27,
    T102,
    T139,
    T166,
    T284,
    T23123456,
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
    Pg660233,
    Pg660234,
    Pg660235,
    Pg660242,
    Pg660307,
    Pg660320,
    Td390,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0"


@dataclass
class EndpointStudyRecordImmunotoxicityApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    observations_and_clinical_examinations_performed_and_frequency: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "ObservationsAndClinicalExaminationsPerformedAndFrequency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    sacrifice_and_pathology: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SacrificeAndPathology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    cell_viabilities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CellViabilities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    humoral_immunity_examinations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "HumoralImmunityExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    specific_cell_mediated_immunity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificCellMediatedImmunity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    non_specific_cell_mediated_immunity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NonSpecificCellMediatedImmunity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other_functional_activity_assays: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherFunctionalActivityAssays",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other_examinations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    positive_control: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660320] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureControlAnimals:
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter:
    class Meta:
        global_type = False

    unit_code: Optional[P29] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureRouteOfAdministration:
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureVehicle:
    class Meta:
        global_type = False

    value: Optional[Td390] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[T139] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[T024] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660233] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsImmunologicalFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservBodyweight:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservClinChem:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservClinSigns:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservDermalIrritationIfDermalStudy:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservFoodConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservFoodEfficiency:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservGrpathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservHaematol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservHistopathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservHistopatholNeoplastic:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservMortality:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservNeurobehaviour:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservNeuropathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservOphthalm:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservOrganWeights:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservUrin:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservWaterConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsOtherEffects:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsCellViabilities:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsHumoralImmunityExaminations:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsNonSpecificCellMediatedImmunity:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsOtherFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsOtherFunctionalActivityAssays:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsSpecificCellMediatedImmunity:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryCriticalEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryOrgan:
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntrySystem:
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordImmunotoxicityAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordImmunotoxicityDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordImmunotoxicityDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry:
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    organism_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordImmunotoxicityOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminations:
    class Meta:
        global_type = False

    cell_viabilities: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsCellViabilities
    ] = field(
        default=None,
        metadata={
            "name": "CellViabilities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_cell_viabilities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityCellViabilities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    humoral_immunity_examinations: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsHumoralImmunityExaminations
    ] = field(
        default=None,
        metadata={
            "name": "HumoralImmunityExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_humoral_immunity_examinations: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityHumoralImmunityExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    specific_cell_mediated_immunity: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsSpecificCellMediatedImmunity
    ] = field(
        default=None,
        metadata={
            "name": "SpecificCellMediatedImmunity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_specific_cell_mediated_immunity: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeveritySpecificCellMediatedImmunity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    non_specific_cell_mediated_immunity: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsNonSpecificCellMediatedImmunity
    ] = field(
        default=None,
        metadata={
            "name": "NonSpecificCellMediatedImmunity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_non_specific_cell_mediated_immunity: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityNonSpecificCellMediatedImmunity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other_functional_activity_assays: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsOtherFunctionalActivityAssays
    ] = field(
        default=None,
        metadata={
            "name": "OtherFunctionalActivityAssays",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_other_functional_activity_assays: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherFunctionalActivityAssays",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other_findings: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminationsOtherFindings
    ] = field(
        default=None,
        metadata={
            "name": "OtherFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_other_findings: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            "nillable": True,
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    system: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    organ: List[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminations:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_dermal_irritation_if_dermal_study: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservDermalIrritationIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "ObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_dermal_irritation_if_dermal_study: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_mortality: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            },
        )
    )
    observ_water_consum: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            },
        )
    )
    immunological_findings: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            },
        )
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsOtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    description_incidence_and_severity_other_effects: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    specific_immunotoxic_examinations: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminationsSpecificImmunotoxicExaminations
    ] = field(
        default=None,
        metadata={
            "name": "SpecificImmunotoxicExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordImmunotoxicityAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    mass_median_aerodynamic_diameter: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter
    ] = field(
        default=None,
        metadata={
            "name": "MassMedianAerodynamicDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    geometric_standard_deviation: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeometricStandardDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
            "nillable": True,
        },
    )
    remarks_on_mmad: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnMMAD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    details_on_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    duration_of_treatment_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTreatmentExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    frequency_of_treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevels:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevelsEfflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicity:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicityResultsAndDiscussion:
    class Meta:
        global_type = False

    results_of_examinations: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionResultsOfExaminations
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    effect_levels: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionEffectLevels
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    target_system_organ_toxicity: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionTargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0",
        },
    )


@dataclass
class EndpointStudyRecordImmunotoxicity:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.Immunotoxicity"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Immunotoxicity/5.0"

    administrative_data: Optional[
        EndpointStudyRecordImmunotoxicityAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordImmunotoxicityDataSource] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordImmunotoxicityMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordImmunotoxicityResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordImmunotoxicityOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordImmunotoxicityApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
