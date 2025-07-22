from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.analyticalmethods_6_5.models.common_types_oecd_v5 import (
    A36,
    C54,
    C102,
    C104,
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
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660350,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0"


@dataclass
class EndpointStudyRecordAnalyticalMethodsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsBackground:
    class Meta:
        global_type = False

    background_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidation:
    class Meta:
        global_type = False

    independent_laboratory_validation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "IndependentLaboratoryValidation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethod:
    class Meta:
        global_type = False

    recovery_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RecoveryResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    characteristics_of_analytical_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicsOfAnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethod:
    class Meta:
        global_type = False

    recovery_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RecoveryResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    characteristics_of_enforcement_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CharacteristicsOfEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660350] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableInstrumentDetectorForConfirmatoryMethod:
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableInstrumentDetectorForEnforcementMethod:
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[C102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsMatrixMedium:
    class Meta:
        global_type = False

    value: Optional[C54] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsOtherQualityAssurance:
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsInstrumentDetector:
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussion:
    class Meta:
        global_type = False

    recovery_results_and_characteristics_of_analytical_method: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethod
    ] = field(
        default=None,
        metadata={
            "name": "RecoveryResultsAndCharacteristicsOfAnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    results_using_enforcement_method: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResultsUsingEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    independent_laboratory_validation: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidation
    ] = field(
        default=None,
        metadata={
            "name": "IndependentLaboratoryValidation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAnalyticalMethodsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAnalyticalMethodsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicable:
    class Meta:
        global_type = False

    instrument_detector_for_confirmatory_method: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableInstrumentDetectorForConfirmatoryMethod
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetectorForConfirmatoryMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    details_on_confirmatory_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnConfirmatoryMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicable:
    class Meta:
        global_type = False

    instrument_detector_for_enforcement_method: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableInstrumentDetectorForEnforcementMethod
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetectorForEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    details_on_enforcement_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethods:
    class Meta:
        global_type = False

    instrument_detector: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsInstrumentDetector
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetector",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    details_on_analytical_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    matrix_medium: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsMatrixMedium
    ] = field(
        default_factory=list,
        metadata={
            "name": "MatrixMedium",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    principles_of_analytical_methods: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethods
    ] = field(
        default=None,
        metadata={
            "name": "PrinciplesOfAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    enforcement_method_if_applicable: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "EnforcementMethodIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    confirmatory_method_if_applicable: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "ConfirmatoryMethodIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethods:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AnalyticalMethods"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/5.0"

    administrative_data: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordAnalyticalMethodsDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    background: Optional[EndpointStudyRecordAnalyticalMethodsBackground] = (
        field(
            default=None,
            metadata={
                "name": "Background",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAnalyticalMethodsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
