from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_7.aspectratioshape_6_5.models.common_types_oecd_v8 import (
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
    Nm13,
    Nm18,
    Nm28,
    Nm39,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660339,
    Pg661157,
)
from entity_models_6_7.aspectratioshape_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0"


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660339] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsDataGathering:
    class Meta:
        global_type = False

    instruments: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Instruments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    calibration: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    reproducibility: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Reproducibility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm13] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsMethodType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm18] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsOtherQualityAssurance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsTestMaterialsReferenceMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reference_material_nanomaterial: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterialNanomaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    sample_identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleIdentificationNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryXDimension(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryYDimension(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryZDimension(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryPercentageValue(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm28] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryShape(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm39] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryStDev(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Nm28] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAspectRatioShapeDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAspectRatioShapeDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsTestMaterialsReferenceMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsTestMaterialsReferenceMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordAspectRatioShapeOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    x_dimension: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryXDimension
    ] = field(
        default=None,
        metadata={
            "name": "xDimension",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    x_dimension_deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "xDimensionDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    y_dimension: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryYDimension
    ] = field(
        default=None,
        metadata={
            "name": "yDimension",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    y_dimension_deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "yDimensionDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    z_dimension: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryZDimension
    ] = field(
        default=None,
        metadata={
            "name": "zDimension",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    z_dimension_deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "zDimensionDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    shape: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryShape
    ] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    percentage_value: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryPercentageValue
    ] = field(
        default=None,
        metadata={
            "name": "PercentageValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    st_dev: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryStDev
    ] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    reference_material: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsTestMaterialsReferenceMaterial
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatio:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatioEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescription:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescriptionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    method_type: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsMethodType
    ] = field(
        default=None,
        metadata={
            "name": "MethodType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    details_on_methods_and_data_evaluation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMethodsAndDataEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Sampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    data_gathering: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsDataGathering
    ] = field(
        default=None,
        metadata={
            "name": "DataGathering",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAspectRatioShapeOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShapeResultsAndDiscussion:
    class Meta:
        global_type = False

    shape_description: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionShapeDescription
    ] = field(
        default=None,
        metadata={
            "name": "ShapeDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    aspect_ratio: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAspectRatio
    ] = field(
        default=None,
        metadata={
            "name": "AspectRatio",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0",
        },
    )


@dataclass
class EndpointStudyRecordAspectRatioShape:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AspectRatioShape"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AspectRatioShape/8.0"

    administrative_data: Optional[
        EndpointStudyRecordAspectRatioShapeAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordAspectRatioShapeDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAspectRatioShapeMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAspectRatioShapeResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAspectRatioShapeOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAspectRatioShapeApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
