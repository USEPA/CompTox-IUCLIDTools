from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.toxicityreproduction_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    P29,
    T027,
    T24,
    T25,
    T27,
    T40,
    T102,
    T112,
    T166,
    T281,
    T284,
    T2312346,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z38,
    Z40,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660234,
    Pg660235,
    Pg660242,
    Pg660275,
    Pg660288,
    Pg660294,
    Pg660295,
    Pg660306,
    Pg660307,
    Pg660316,
    Pg660329,
    Td390,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0"


@dataclass
class EndpointStudyRecordToxicityReproductionApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    parental_animals_observations_and_examinations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ParentalAnimalsObservationsAndExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    estrous_cyclicity_parental_animals: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EstrousCyclicityParentalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    sperm_parameters_parental_animals: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpermParametersParentalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    litter_observations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LitterObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    postmortem_examinations_parental_animals: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostmortemExaminationsParentalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    postmortem_examinations_offspring: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostmortemExaminationsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reproductive_indices: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReproductiveIndices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    offspring_viability_indices: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OffspringViabilityIndices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDetailsOnResultsF2:
    class Meta:
        global_type = False

    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDetailsOnResultsF1:
    class Meta:
        global_type = False

    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationDetailsOnResultsP0:
    class Meta:
        global_type = False

    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationDetailsOnResultsP1:
    class Meta:
        global_type = False

    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660306] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660275] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureControlAnimals:
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter:
    class Meta:
        global_type = False

    unit_code: Optional[P29] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureRouteOfAdministration:
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposureIfApplicable:
    class Meta:
        global_type = False

    value: Optional[T112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureVehicle:
    class Meta:
        global_type = False

    value: Optional[Td390] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[T40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[T027] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[T2312346] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelationToOtherToxicEffects:
    class Meta:
        global_type = False

    value: Optional[Pg660294] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryReproductiveEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1GenerationDevelopmentalImmunotoxicity:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1GenerationBehaviourFunctionalFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660288] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryGeneration:
    class Meta:
        global_type = False

    value: Optional[Pg660316] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2AnogenitalDistance:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2DermalIrritationOffspringIfDermalStudy:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2NippleRetentionInMalePups:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservBodyweightOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinChemOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodConsumOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodEfficiencyOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservGrpatholOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHaematolOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHistopatholOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservMaturationOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOphthalmOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOrganWeightsOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservUrinOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservViabilityOffspring:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservWaterConsumOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2OtherEffectsOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryCriticalEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryOrgan:
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntrySystem:
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1DevelopmentalImmunotoxicity:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1BehaviourFunctionalFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660288] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryGeneration:
    class Meta:
        global_type = False

    value: Optional[Pg660295] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1AnogenitalDistance:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1DermalIrritationOffspringIfDermalStudy:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1NippleRetentionInMalePups:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservBodyweightOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinChemOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodConsumOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodEfficiencyOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservGrpatholOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHaematolOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHistopatholOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservMaturationOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOphthalmOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOrganWeightsOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservUrinOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservViabilityOffspring:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservWaterConsumOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1OtherEffectsOffspring:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryCriticalEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryOrgan:
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntrySystem:
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660329] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ImmunologicalFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservBodyweight:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinChem:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinSigns:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservDermalIrritationIfDermalStudy:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodEfficiency:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservGrpathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHaematol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopatholNeoplastic:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservMortality:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeurobehaviour:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeuropathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOphthalm:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOrganWeights:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservUrin:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservWaterConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0OtherEffects:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservEstrousParent:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservReproPerformParent:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservSpermParent:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryCriticalEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryOrgan:
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntrySystem:
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660329] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ImmunologicalFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservBodyweight:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinChem:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinSigns:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservDermalIrritationIfDermalStudy:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodEfficiency:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservGrpathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHaematol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopatholNeoplastic:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservMortality:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeurobehaviour:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeuropathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOphthalm:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOrganWeights:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservUrin:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservWaterConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1OtherEffects:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionEstrousCycle:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionSpermMeasures:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductivePerformance:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryCriticalEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryOrgan:
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntrySystem:
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordToxicityReproductionDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordToxicityReproductionDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry:
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_species_strain_selection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    organism_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    reproductive_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryReproductiveEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    relation_to_other_toxic_effects: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelationToOtherToxicEffects
    ] = field(
        default=None,
        metadata={
            "name": "RelationToOtherToxicEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1Generation:
    class Meta:
        global_type = False

    developmental_immunotoxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1GenerationDevelopmentalImmunotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_developmental_immunotoxicity: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1Generation:
    class Meta:
        global_type = False

    behaviour_functional_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1GenerationBehaviourFunctionalFindings
    ] = field(
        default=None,
        metadata={
            "name": "BehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_behaviour_functional_findings: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityBehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryGeneration
    ] = field(
        default=None,
        metadata={
            "name": "Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2:
    class Meta:
        global_type = False

    observ_clin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservClinOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    dermal_irritation_offspring_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2DermalIrritationOffspringIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "DermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_dermal_irritation_offspring_if_dermal_study: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_viability_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservViabilityOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_viability_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_bodyweight_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservBodyweightOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_efficiency_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodEfficiencyOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_water_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservWaterConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_ophthalm_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOphthalmOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalmOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservOphthalmOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_haematol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHaematolOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematolOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_haematol_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservHaematolOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_clin_chem_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinChemOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_urin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservUrinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_urin_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservUrinOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_maturation_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservMaturationOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_maturation_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    anogenital_distance: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2AnogenitalDistance
    ] = field(
        default=None,
        metadata={
            "name": "AnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_anogenital_distance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityAnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    nipple_retention_in_male_pups: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2NippleRetentionInMalePups
    ] = field(
        default=None,
        metadata={
            "name": "NippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_nipple_retention_in_male_pups: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityNippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_organ_weights_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOrganWeightsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_grpathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservGrpatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservGrpatholOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_histopathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHistopatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other_effects_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2OtherEffectsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffectsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_other_effects_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityOtherEffectsOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1:
    class Meta:
        global_type = False

    developmental_immunotoxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1DevelopmentalImmunotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_developmental_immunotoxicity: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1:
    class Meta:
        global_type = False

    behaviour_functional_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1BehaviourFunctionalFindings
    ] = field(
        default=None,
        metadata={
            "name": "BehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_behaviour_functional_findings: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityBehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryGeneration
    ] = field(
        default=None,
        metadata={
            "name": "Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1:
    class Meta:
        global_type = False

    observ_clin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservClinOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    dermal_irritation_offspring_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1DermalIrritationOffspringIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "DermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_dermal_irritation_offspring_if_dermal_study: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_viability_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservViabilityOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_viability_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_bodyweight_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservBodyweightOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_efficiency_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodEfficiencyOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_water_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservWaterConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_ophthalm_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOphthalmOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalmOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservOphthalmOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_haematol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHaematolOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematolOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_haematol_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservHaematolOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_clin_chem_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinChemOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_urin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservUrinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_urin_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservUrinOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_maturation_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservMaturationOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_maturation_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    anogenital_distance: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1AnogenitalDistance
    ] = field(
        default=None,
        metadata={
            "name": "AnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_anogenital_distance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityAnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    nipple_retention_in_male_pups: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1NippleRetentionInMalePups
    ] = field(
        default=None,
        metadata={
            "name": "NippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_nipple_retention_in_male_pups: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityNippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_organ_weights_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOrganWeightsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_grpathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservGrpatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservGrpatholOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_histopathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHistopatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_offspring: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other_effects_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1OtherEffectsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffectsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_other_effects_offspring: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityOtherEffectsOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_dermal_irritation_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservDermalIrritationIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "ObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_dermal_irritation_if_dermal_study: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_mortality: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_water_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    immunological_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0OtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_other_effects: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0:
    class Meta:
        global_type = False

    observ_estrous_parent: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservEstrousParent
    ] = field(
        default=None,
        metadata={
            "name": "ObservEstrousParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_estrous_parent: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservEstrousParent",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_sperm_parent: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservSpermParent
    ] = field(
        default=None,
        metadata={
            "name": "ObservSpermParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_sperm_parent: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservSpermParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_repro_perform_parent: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservReproPerformParent
    ] = field(
        default=None,
        metadata={
            "name": "ObservReproPerformParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_repro_perform_parent: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservReproPerformParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_dermal_irritation_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservDermalIrritationIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "ObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_dermal_irritation_if_dermal_study: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_mortality: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_water_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    immunological_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1OtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_other_effects: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1:
    class Meta:
        global_type = False

    reproductive_function_estrous_cycle: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionEstrousCycle
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionEstrousCycle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_reproductive_function_estrous_cycle: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityReproductiveFunctionEstrousCycle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reproductive_function_sperm_measures: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionSpermMeasures
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionSpermMeasures",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_reproductive_function_sperm_measures: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityReproductiveFunctionSpermMeasures",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reproductive_performance: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductivePerformance
    ] = field(
        default=None,
        metadata={
            "name": "ReproductivePerformance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    description_incidence_and_severity_reproductive_performance: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityReproductivePerformance",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    type_of_inhalation_exposure_if_applicable: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposureIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfInhalationExposureIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    mass_median_aerodynamic_diameter: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter
    ] = field(
        default=None,
        metadata={
            "name": "MassMedianAerodynamicDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    geometric_standard_deviation: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeometricStandardDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
            "nillable": True,
        },
    )
    remarks_on_mmad: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnMMAD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_mating_procedure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMatingProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    duration_of_treatment_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTreatmentExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    frequency_of_treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_study_schedule: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudySchedule",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    positive_control: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicity:
    class Meta:
        global_type = False

    reproductive_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicity
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    justification_for_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2Generation:
    class Meta:
        global_type = False

    general_toxicity_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    developmental_neurotoxicity_of_f1_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1Generation
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalNeurotoxicityOfF1Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    developmental_immunotoxicity_of_f1_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1Generation
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicityOfF1Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_results_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDetailsOnResultsF2
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_levels_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    target_system_organ_toxicity_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspring:
    class Meta:
        global_type = False

    general_toxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    developmental_neurotoxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalNeurotoxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    developmental_immunotoxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_results_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDetailsOnResultsF1
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_levels_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    target_system_organ_toxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGeneration:
    class Meta:
        global_type = False

    general_toxicity_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reproductive_function_performance_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionPerformanceP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_results_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationDetailsOnResultsP0
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_levels_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    target_system_organ_toxicity_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGeneration:
    class Meta:
        global_type = False

    general_toxicity_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reproductive_function_performance_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionPerformanceP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    details_on_results_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationDetailsOnResultsP1
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    effect_levels_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    target_system_organ_toxicity_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussion:
    class Meta:
        global_type = False

    results_of_examinations_parental_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGeneration
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminationsParentalGeneration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    results_p1_second_parental_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGeneration
    ] = field(
        default=None,
        metadata={
            "name": "ResultsP1SecondParentalGeneration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    results_of_examinations_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminationsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    results_f2_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2Generation
    ] = field(
        default=None,
        metadata={
            "name": "ResultsF2Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    reproductive_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicity
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproduction:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ToxicityReproduction"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/5.0"

    administrative_data: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordToxicityReproductionDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordToxicityReproductionApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
