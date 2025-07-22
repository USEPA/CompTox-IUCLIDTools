from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_5.natureresiduesinprocessedcommod_6_5.models.common_types_oecd_v6 import (
    A36,
    C1112,
    N64,
    N78,
    T148,
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
    Pg660487,
    Pg660488,
    Pg660490,
    Pg660491,
)
from entity_models_6_5.natureresiduesinprocessedcommod_6_5.models.platform_fields import (
    AttachmentListField,
    BaseDataProtectionField,
    BasePhysicalQuantityRangeField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    LowerQualifier,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
    UpperQualifier,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0"


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660487] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660488] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsProductType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsSamplingAndAnalyticalMethodology:
    class Meta:
        global_type = False

    details_on_sample_handling_and_storage_conditions: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleHandlingAndStorageConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    details_on_analytical_methodology: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnAnalyticalMethodology",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    test_strategies: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "TestStrategies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    experimental_procedure: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntryTrrcomponentNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntryTrrconcentration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660491] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntryTrrpercentage(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    legislation: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    trrcomponent_no: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntryTrrcomponentNo
    ] = field(
        default=None,
        metadata={
            "name": "TRRComponentNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    test_conditions: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    identity_of_trrcomponent: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfTRRComponent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    trrconcentration: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntryTrrconcentration
    ] = field(
        default=None,
        metadata={
            "name": "TRRConcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    trrpercentage: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntryTrrpercentage
    ] = field(
        default=None,
        metadata={
            "name": "TRRPercentage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    attached_study_report: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[AttachmentListField] = (
        field(
            default=None,
            metadata={
                "name": "AttachedSanitisedDocsForPublication",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrr:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrrEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethods:
    class Meta:
        global_type = False

    product_type: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    sampling_and_analytical_methodology: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsSamplingAndAnalyticalMethodology
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussion:
    class Meta:
        global_type = False

    storage_stability: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    total_radioactive_residues_trr: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionTotalRadioactiveResiduesTrr
    ] = field(
        default=None,
        metadata={
            "name": "TotalRadioactiveResiduesTRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    other_details_on_trrs: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OtherDetailsOnTRRs",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    metabolic_pathway: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "MetabolicPathway",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0",
        },
    )


@dataclass
class EndpointStudyRecordNatureResiduesInProcessedCommod:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.NatureResiduesInProcessedCommod"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-NatureResiduesInProcessedCommod/6.0"

    administrative_data: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordNatureResiduesInProcessedCommodApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
