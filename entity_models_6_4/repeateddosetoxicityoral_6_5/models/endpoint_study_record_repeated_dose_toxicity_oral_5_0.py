from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.repeateddosetoxicityoral_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    T023,
    T24,
    T27,
    T48,
    T102,
    T156,
    T251,
    T261,
    T281,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660225,
    Pg660226,
    Pg660233,
    Pg660234,
    Pg660235,
    Pg660242,
    Pg660307,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0"


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    observations_and_examinations_performed_and_frequency: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ObservationsAndExaminationsPerformedAndFrequency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    sacrifice_and_pathology: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SacrificeAndPathology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other_examinations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660226] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660225] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureControlAnimals:
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureRouteOfAdministration:
    class Meta:
        global_type = False

    value: Optional[T251] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureVehicle:
    class Meta:
        global_type = False

    value: Optional[T48] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[T261] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[T023] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryBasis:
    class Meta:
        global_type = False

    value: Optional[Pg660233] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[T156] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsImmunologicalFindings:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservBodyweight:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservClinChem:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservClinSigns:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservFoodConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservFoodEfficiency:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservGrpathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservHaematol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservHistopathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservHistopatholNeoplastic:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservMortality:
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservNeurobehaviour:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservNeuropathol:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservOphthalm:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservOrganWeights:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservUrin:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservWaterConsum:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsOtherEffects:
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryCriticalEffectsObserved:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryDoseResponseRelationship:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryLowestEffectiveDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryOrgan:
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryRelevantForHumans:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntrySystem:
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryTreatmentRelated:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry:
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    details_on_species_strain_selection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    organism_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            "nillable": True,
        },
    )
    endpoint: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    basis: List[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminations:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_mortality: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            },
        )
    )
    observ_water_consum: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            },
        )
    )
    immunological_findings: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            },
        )
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminationsOtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    description_incidence_and_severity_other_effects: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            "nillable": True,
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    system: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    organ: List[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    details_on_route_of_administration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnRouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    details_on_oral_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnOralExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    duration_of_treatment_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTreatmentExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    frequency_of_treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    positive_control: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevels:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevelsEfflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicity:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussion:
    class Meta:
        global_type = False

    results_of_examinations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionResultsOfExaminations
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    effect_levels: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionEffectLevels
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    target_system_organ_toxicity: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionTargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityOral:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.RepeatedDoseToxicityOral"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityOral/5.0"

    administrative_data: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordRepeatedDoseToxicityOralApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
