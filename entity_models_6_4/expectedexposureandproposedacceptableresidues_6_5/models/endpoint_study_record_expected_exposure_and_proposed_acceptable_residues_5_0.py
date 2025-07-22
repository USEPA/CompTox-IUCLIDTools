from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.expectedexposureandproposedacceptableresidues_6_5.models.common_types_oecd_v5 import (
    A36,
    C1113,
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
    Pg660354,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0"


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    further_details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FurtherDetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660354] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsProductType:
    class Meta:
        global_type = False

    value: Optional[C1113] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesResultsAndDiscussion:
    class Meta:
        global_type = False

    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethods:
    class Meta:
        global_type = False

    background_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    product_type: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0",
        },
    )


@dataclass
class EndpointStudyRecordExpectedExposureAndProposedAcceptableResidues:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ExpectedExposureAndProposedAcceptableResidues"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ExpectedExposureAndProposedAcceptableResidues/5.0"

    administrative_data: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordExpectedExposureAndProposedAcceptableResiduesApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
