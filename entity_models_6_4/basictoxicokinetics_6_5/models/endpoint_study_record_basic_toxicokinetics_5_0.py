from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.basictoxicokinetics_6_5.models.common_types_oecd_v5 import (
    A36,
    C13,
    C36,
    E34,
    F108,
    N64,
    N78,
    T0210,
    T24,
    T25,
    T27,
    T48,
    T115,
    T148,
    T152,
    T153,
    T284,
    T23123456,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660266,
    Td370,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0"


@dataclass
class EndpointStudyRecordBasicToxicokineticsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionBioaccessibility:
    class Meta:
        global_type = False

    bioaccessibility_testing_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BioaccessibilityTestingResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660266] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureControlAnimals:
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureRouteOfAdministration:
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureVehicle:
    class Meta:
        global_type = False

    value: Optional[T48] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[C36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsObjectiveOfStudyPick:
    class Meta:
        global_type = False

    value: Optional[C13] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[T0210] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMainAdmeResultsEntryType:
    class Meta:
        global_type = False

    value: Optional[Td370] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMetaboliteCharacterisationStudiesMetabolitesIdentified:
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParametersEntryTestNo:
    class Meta:
        global_type = False

    value: Optional[F108] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParametersEntryToxicokineticParameters:
    class Meta:
        global_type = False

    value: Optional[T115] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntryObservation:
    class Meta:
        global_type = False

    value: Optional[T153] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntryTestNo:
    class Meta:
        global_type = False

    value: Optional[F108] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntryTransferType:
    class Meta:
        global_type = False

    value: Optional[T152] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBasicToxicokineticsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBasicToxicokineticsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry:
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_species_strain_selection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    organism_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBasicToxicokineticsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMainAdmeResultsEntry:
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMainAdmeResultsEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMetaboliteCharacterisationStudies:
    class Meta:
        global_type = False

    metabolites_identified: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMetaboliteCharacterisationStudiesMetabolitesIdentified
    ] = field(
        default=None,
        metadata={
            "name": "MetabolitesIdentified",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_metabolites: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParametersEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
            "nillable": True,
        },
    )
    test_no: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParametersEntryTestNo
    ] = field(
        default=None,
        metadata={
            "name": "TestNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    toxicokinetic_parameters: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParametersEntryToxicokineticParameters
    ] = field(
        default=None,
        metadata={
            "name": "ToxicokineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
            "nillable": True,
        },
    )
    test_no: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntryTestNo
    ] = field(
        default=None,
        metadata={
            "name": "TestNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    transfer_type: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntryTransferType
    ] = field(
        default=None,
        metadata={
            "name": "TransferType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    observation: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntryObservation
    ] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMainAdmeResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMainAdmeResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParameters:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParametersEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgans:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgansEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    duration_and_frequency_of_treatment_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationAndFrequencyOfTreatmentExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    positive_control: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_dosing_and_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDosingAndSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudies:
    class Meta:
        global_type = False

    details_on_absorption: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAbsorption",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_distribution: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDistribution",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    transfer_into_organs: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesTransferIntoOrgans
    ] = field(
        default=None,
        metadata={
            "name": "TransferIntoOrgans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    details_on_excretion: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExcretion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    toxicokinetic_parameters: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudiesToxicokineticParameters
    ] = field(
        default=None,
        metadata={
            "name": "ToxicokineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsMaterialsAndMethods:
    class Meta:
        global_type = False

    objective_of_study_pick: List[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsObjectiveOfStudyPick
    ] = field(
        default_factory=list,
        metadata={
            "name": "ObjectiveOfStudyPick",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokineticsResultsAndDiscussion:
    class Meta:
        global_type = False

    preliminary_studies: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PreliminaryStudies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    main_adme_results: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMainAdmeResults
    ] = field(
        default=None,
        metadata={
            "name": "MainAdmeResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    pharmacokinetic_studies: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionPharmacokineticStudies
    ] = field(
        default=None,
        metadata={
            "name": "PharmacokineticStudies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    metabolite_characterisation_studies: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionMetaboliteCharacterisationStudies
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteCharacterisationStudies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    bioaccessibility: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionBioaccessibility
    ] = field(
        default=None,
        metadata={
            "name": "Bioaccessibility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBasicToxicokinetics:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BasicToxicokinetics"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BasicToxicokinetics/5.0"

    administrative_data: Optional[
        EndpointStudyRecordBasicToxicokineticsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordBasicToxicokineticsDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordBasicToxicokineticsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordBasicToxicokineticsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordBasicToxicokineticsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordBasicToxicokineticsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
