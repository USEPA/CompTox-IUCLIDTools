from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_4.stabilityofresiduesinstoredcommod_6_5.models.common_types_oecd_v5 import (
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
    Pg660492,
    Pg660494,
    Pg660496,
    Pg660561,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0"


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsSamplingAndAnalyticalMethodology:
    class Meta:
        global_type = False

    details_on_sample_collection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    details_on_sample_handling_and_preparation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleHandlingAndPreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    details_on_analytical_methodology: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryProceduralRecoveryControl:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevelOfNominalSpikingLevel:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660492] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Pg660494] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsProductType:
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignCommodity:
    class Meta:
        global_type = False

    value: Optional[Pg660561] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryMeanResidueLevel:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660496] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevel:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660496] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryTestCommodity:
    class Meta:
        global_type = False

    value: Optional[Pg660561] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    commodity: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignCommodity
    ] = field(
        default_factory=list,
        metadata={
            "name": "Commodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    details_on_stored_commodities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStoredCommodities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    storage_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StorageConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntry:
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    residue_level: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevel
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    mean_residue_level: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryMeanResidueLevel
    ] = field(
        default=None,
        metadata={
            "name": "MeanResidueLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    residue_level_of_nominal_spiking_level: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevelOfNominalSpikingLevel
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelOfNominalSpikingLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    mean_residue_level_of_nominal_spiking_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeanResidueLevelOfNominalSpikingLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    procedural_recovery_control: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryProceduralRecoveryControl
    ] = field(
        default=None,
        metadata={
            "name": "ProceduralRecoveryControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    mean_procedural_recovery_control: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeanProceduralRecoveryControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasured:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethods:
    class Meta:
        global_type = False

    product_type: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    sampling_and_analytical_methodology: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsSamplingAndAnalyticalMethodology
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntry:
    class Meta:
        global_type = False

    test_commodity: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryTestCommodity
    ] = field(
        default=None,
        metadata={
            "name": "TestCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    other_details_on_test_commodity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherDetailsOnTestCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    date_of_sample: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
            "nillable": True,
        },
    )
    analysis_sample_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    analysis_sample_description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisSampleDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    analyte_measured: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasured
    ] = field(
        default=None,
        metadata={
            "name": "AnalyteMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevels:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussion:
    class Meta:
        global_type = False

    residue_levels: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevels
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    storage_stability: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommod:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.StabilityOfResiduesInStoredCommod"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/5.0"

    administrative_data: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
