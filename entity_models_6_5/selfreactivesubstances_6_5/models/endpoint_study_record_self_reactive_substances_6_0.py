from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_5.selfreactivesubstances_6_5.models.common_types_oecd_v6 import (
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
    Pg660108,
    Pg660109,
    Pg660119,
    Pg660121,
    Pg660124,
    Pg660127,
    Pg660129,
    Pg660138,
    Pg660142,
    Pg660145,
)
from entity_models_6_5.selfreactivesubstances_6_5.models.platform_fields import (
    AttachmentListField,
    BaseDataProtectionField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0"


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660119] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesApplicantSummaryAndConclusionInterpretationOfResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660145] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660124] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsOtherQualityAssurance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryQualitativeParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660138] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryQualitativeResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660142] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660127] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryTestSeries(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660129] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTestsEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660108] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTestsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    interpretation_of_results: Optional[
        EndpointStudyRecordSelfReactiveSubstancesApplicantSummaryAndConclusionInterpretationOfResults
    ] = field(
        default=None,
        metadata={
            "name": "InterpretationOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordSelfReactiveSubstancesDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordSelfReactiveSubstancesDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSelfReactiveSubstancesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    test_series: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryTestSeries
    ] = field(
        default=None,
        metadata={
            "name": "TestSeries",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    quantitative_result: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "QuantitativeResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    qualitative_parameter: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryQualitativeParameter
    ] = field(
        default=None,
        metadata={
            "name": "QualitativeParameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    qualitative_result: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryQualitativeResult
    ] = field(
        default=None,
        metadata={
            "name": "QualitativeResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTestsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTestsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    number_of_fragments: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NumberOfFragments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTestsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordSelfReactiveSubstancesOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    attached_study_report: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[AttachmentListField] = (
        field(
            default=None,
            metadata={
                "name": "AttachedSanitisedDocsForPublication",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstances:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstancesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTests:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTestsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussion:
    class Meta:
        global_type = False

    small_scale_preliminary_tests: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionSmallScalePreliminaryTests
    ] = field(
        default=None,
        metadata={
            "name": "SmallScalePreliminaryTests",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    results_of_test_series_for_self_reactive_substances: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionResultsOfTestSeriesForSelfReactiveSubstances
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfTestSeriesForSelfReactiveSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0",
        },
    )


@dataclass
class EndpointStudyRecordSelfReactiveSubstances:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.SelfReactiveSubstances"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SelfReactiveSubstances/6.0"

    administrative_data: Optional[
        EndpointStudyRecordSelfReactiveSubstancesAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordSelfReactiveSubstancesDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordSelfReactiveSubstancesMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordSelfReactiveSubstancesResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordSelfReactiveSubstancesOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordSelfReactiveSubstancesApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
