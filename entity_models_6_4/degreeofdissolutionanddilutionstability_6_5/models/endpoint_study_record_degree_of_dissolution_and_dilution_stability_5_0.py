from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.degreeofdissolutionanddilutionstability_6_5.models.common_types_bpr_v5 import (
    A36,
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
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660044,
    Pg660047,
    Pg660625,
    Pg660626,
    Pg660627,
    Pg660628,
    Pg660629,
    Pg660630,
    Pg660631,
    Pg660632,
    Pg660633,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0"


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660047] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660625] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Pg660626] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsOtherQualityAssurance:
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsStudyDesignAnalyticalMethod:
    class Meta:
        global_type = False

    value: Optional[Pg660044] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolutionEntryConcentration:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660627] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolutionEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41EntryConcentration:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660629] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41EntryPresenceOfSeparatedMaterial:
    class Meta:
        global_type = False

    value: Optional[Pg660628] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41EntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryConcentration:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660627] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HPresenceOfSediment18H:
    class Meta:
        global_type = False

    value: Optional[Pg660628] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HRemarksOnResult:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HRepeatabilityR:
    class Meta:
        global_type = False

    value: Optional[Pg660631] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HReproducibilityR:
    class Meta:
        global_type = False

    value: Optional[Pg660633] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5MinPresenceOfSediment5Min:
    class Meta:
        global_type = False

    value: Optional[Pg660628] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5MinRepeatabilityR:
    class Meta:
        global_type = False

    value: Optional[Pg660630] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5MinReproducibilityR:
    class Meta:
        global_type = False

    value: Optional[Pg660632] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    analytical_method: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsStudyDesignAnalyticalMethod
    ] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    details_on_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolutionEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    flow_time_sec: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowTimeSec",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    concentration: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolutionEntryConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolutionEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41Entry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    presence_of_separated_material: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41EntryPresenceOfSeparatedMaterial
    ] = field(
        default=None,
        metadata={
            "name": "PresenceOfSeparatedMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    concentration: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41EntryConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41EntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18H:
    class Meta:
        global_type = False

    presence_of_sediment18h: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HPresenceOfSediment18H
    ] = field(
        default=None,
        metadata={
            "name": "PresenceOfSediment18h",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    amount_of_residue_g: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmountOfResidueG",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    repeatability_r: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HRepeatabilityR
    ] = field(
        default=None,
        metadata={
            "name": "RepeatabilityR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    reproducibility_r: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HReproducibilityR
    ] = field(
        default=None,
        metadata={
            "name": "ReproducibilityR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18HRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5Min:
    class Meta:
        global_type = False

    presence_of_sediment5min: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5MinPresenceOfSediment5Min
    ] = field(
        default=None,
        metadata={
            "name": "PresenceOfSediment5min",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    amount_of_residue_g: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmountOfResidueG",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    repeatability_r: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5MinRepeatabilityR
    ] = field(
        default=None,
        metadata={
            "name": "RepeatabilityR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    reproducibility_r: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5MinReproducibilityR
    ] = field(
        default=None,
        metadata={
            "name": "ReproducibilityR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolution:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolutionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41Entry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    concentration: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    test5_min: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest5Min
    ] = field(
        default=None,
        metadata={
            "name": "Test5Min",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    test18_h: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntryTest18H
    ] = field(
        default=None,
        metadata={
            "name": "Test18H",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStability:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussion:
    class Meta:
        global_type = False

    degree_of_dissolution: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDegreeOfDissolution
    ] = field(
        default=None,
        metadata={
            "name": "DegreeOfDissolution",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    dilution_stability_mt41: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStabilityMt41
    ] = field(
        default=None,
        metadata={
            "name": "DilutionStabilityMT41",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    dilution_stability: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionDilutionStability
    ] = field(
        default=None,
        metadata={
            "name": "DilutionStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0",
        },
    )


@dataclass
class EndpointStudyRecordDegreeOfDissolutionAndDilutionStability:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.DegreeOfDissolutionAndDilutionStability"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DegreeOfDissolutionAndDilutionStability/5.0"

    administrative_data: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordDegreeOfDissolutionAndDilutionStabilityApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
