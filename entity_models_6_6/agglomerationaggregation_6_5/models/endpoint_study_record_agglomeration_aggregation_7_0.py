from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_6.agglomerationaggregation_6_5.models.common_types_oecd_v7 import (
    A36,
    N64,
    N78,
    P28,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Nm13,
    Nm14,
    Nm15,
    Nm17,
    Nm19,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660328,
    Pg661157,
)
from entity_models_6_6.agglomerationaggregation_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePhysicalQuantityField,
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0"


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660328] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsDataGathering:
    class Meta:
        global_type = False

    instruments: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Instruments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    calibration: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    reproducibility: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Reproducibility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm13] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsMethodType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm14] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsOtherQualityAssurance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsTestMaterialsReferenceMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reference_material_nanomaterial: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterialNanomaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    sample_identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleIdentificationNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryMeanDiameter(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryPh(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryStDev(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryMean(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryPercentile(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[P28] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryPh(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryStDev(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntryDistribution(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm19] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntrySequenceNumber(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm17] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntrySize(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntryMean(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntryPh(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAgglomerationAggregationDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAgglomerationAggregationDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsTestMaterialsReferenceMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsTestMaterialsReferenceMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    mean_diameter: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryMeanDiameter
    ] = field(
        default=None,
        metadata={
            "name": "MeanDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    st_dev: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryStDev
    ] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    medium: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Medium",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    percentile: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryPercentile
    ] = field(
        default=None,
        metadata={
            "name": "Percentile",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    mean: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryMean
    ] = field(
        default=None,
        metadata={
            "name": "Mean",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    st_dev: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryStDev
    ] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    medium: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Medium",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    sequence_number: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntrySequenceNumber
    ] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    size: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntrySize
    ] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    distribution: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntryDistribution
    ] = field(
        default=None,
        metadata={
            "name": "Distribution",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    mean: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntryMean
    ] = field(
        default=None,
        metadata={
            "name": "Mean",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    medium: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Medium",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    reference_material: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsTestMaterialsReferenceMaterial
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameter:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameterEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSize:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSizeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassages:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassagesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndex:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndexEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    method_type: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsMethodType
    ] = field(
        default=None,
        metadata={
            "name": "MethodType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    details_on_methods_and_data_evaluation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMethodsAndDataEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Sampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    data_gathering: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsDataGathering
    ] = field(
        default=None,
        metadata={
            "name": "DataGathering",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregationResultsAndDiscussion:
    class Meta:
        global_type = False

    agglomeration_aggregation_diameter: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationDiameter
    ] = field(
        default=None,
        metadata={
            "name": "AgglomerationAggregationDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    agglomeration_aggregation_size: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAgglomerationAggregationSize
    ] = field(
        default=None,
        metadata={
            "name": "AgglomerationAggregationSize",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    distribution_different_passages: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionDistributionDifferentPassages
    ] = field(
        default=None,
        metadata={
            "name": "DistributionDifferentPassages",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    index: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionIndex
    ] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordAgglomerationAggregation:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AgglomerationAggregation"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AgglomerationAggregation/7.0"

    administrative_data: Optional[
        EndpointStudyRecordAgglomerationAggregationAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordAgglomerationAggregationDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAgglomerationAggregationMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAgglomerationAggregationResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAgglomerationAggregationOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAgglomerationAggregationApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
