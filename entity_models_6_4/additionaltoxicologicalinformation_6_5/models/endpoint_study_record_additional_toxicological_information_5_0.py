from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.additionaltoxicologicalinformation_6_5.models.common_types_oecd_v5 import (
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
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660327,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0"


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660327] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussion:
    class Meta:
        global_type = False

    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethods:
    class Meta:
        global_type = False

    type_of_study_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfStudyInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordAdditionalToxicologicalInformation:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AdditionalToxicologicalInformation"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdditionalToxicologicalInformation/5.0"

    administrative_data: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAdditionalToxicologicalInformationApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
