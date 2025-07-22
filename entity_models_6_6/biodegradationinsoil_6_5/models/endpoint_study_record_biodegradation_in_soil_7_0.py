from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_6.biodegradationinsoil_6_5.models.common_types_oecd_v7 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    F11,
    F12,
    F16,
    F17,
    F25,
    F103,
    F109,
    F110,
    F132,
    F136,
    F137,
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
    EuPpp60865,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660267,
    Pg660268,
    Pg660822,
    Pg661157,
)
from entity_models_6_6.biodegradationinsoil_6_5.models.platform_fields import (
    AttachmentListField,
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0"


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660268] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660267] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntryDuration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[F132] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignOxygenConditions(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignParameterFollowed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilClassification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F16] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryBulkDensityGcm(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryCec(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[F17] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryClay(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryMoistureContent(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryOrgC(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryPh(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySand(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySilt(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F11] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryDegr(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParentProduct(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660822] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySamplingTime(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionEvaporationOfParentCompound(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryHalfLife(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryTemp(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F136] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntryNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryCo2(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryNonExtractable(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingDays(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[EuPpp60865] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionResidues(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProducts(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionVolatileMetabolites(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBiodegradationInSoilDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBiodegradationInSoilDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    temp: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    humidity: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Humidity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    microbial_biomass: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "MicrobialBiomass",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    initial_conc: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc
    ] = field(
        default=None,
        metadata={
            "name": "InitialConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    soil_type: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilType
    ] = field(
        default=None,
        metadata={
            "name": "SoilType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    clay: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryClay
    ] = field(
        default=None,
        metadata={
            "name": "Clay",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    silt: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySilt
    ] = field(
        default=None,
        metadata={
            "name": "Silt",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    sand: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySand
    ] = field(
        default=None,
        metadata={
            "name": "Sand",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    org_c: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryOrgC
    ] = field(
        default=None,
        metadata={
            "name": "OrgC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    cec: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryCec
    ] = field(
        default=None,
        metadata={
            "name": "CEC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    bulk_density_gcm: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryBulkDensityGcm
    ] = field(
        default=None,
        metadata={
            "name": "BulkDensityGCm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    moisture_content: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryMoistureContent
    ] = field(
        default=None,
        metadata={
            "name": "MoistureContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    parent_product: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParentProduct
    ] = field(
        default=None,
        metadata={
            "name": "ParentProduct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    name_or_code_for_product: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOrCodeForProduct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    sampling_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SamplingDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
            "nillable": True,
        },
    )
    degr: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryDegr
    ] = field(
        default=None,
        metadata={
            "name": "Degr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    sampling_time: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySamplingTime
    ] = field(
        default=None,
        metadata={
            "name": "SamplingTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    half_life: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryHalfLife
    ] = field(
        default=None,
        metadata={
            "name": "HalfLife",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    type_value: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    sampling_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SamplingDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
            "nillable": True,
        },
    )
    sampling_days: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingDays
    ] = field(
        default=None,
        metadata={
            "name": "SamplingDays",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    total_extractable: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable
    ] = field(
        default=None,
        metadata={
            "name": "TotalExtractable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    non_extractable: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryNonExtractable
    ] = field(
        default=None,
        metadata={
            "name": "NonExtractable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    co2: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryCo2
    ] = field(
        default=None,
        metadata={
            "name": "CO2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    other_volatiles: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles
    ] = field(
        default=None,
        metadata={
            "name": "OtherVolatiles",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTime:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditions:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilProperties:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompound:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalance:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    oxygen_conditions: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignOxygenConditions
    ] = field(
        default=None,
        metadata={
            "name": "OxygenConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    soil_classification: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilClassification
    ] = field(
        default=None,
        metadata={
            "name": "SoilClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
            "nillable": True,
        },
    )
    soil_properties: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilProperties
    ] = field(
        default=None,
        metadata={
            "name": "SoilProperties",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    details_on_soil_characteristics: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSoilCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    duration_of_test_contact_time: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTime
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfTestContactTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    initial_test_substance_concentration: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration
    ] = field(
        default=None,
        metadata={
            "name": "InitialTestSubstanceConcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    parameter_followed: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignParameterFollowed
    ] = field(
        default_factory=list,
        metadata={
            "name": "ParameterFollowed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    experimental_conditions: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditions
    ] = field(
        default=None,
        metadata={
            "name": "ExperimentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    details_on_experimental_conditions: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnExperimentalConditions",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    kinetic_evaluation: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "KineticEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussion:
    class Meta:
        global_type = False

    material_mass_balance: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalance
    ] = field(
        default=None,
        metadata={
            "name": "MaterialMassBalance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    degradation: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradation
    ] = field(
        default=None,
        metadata={
            "name": "Degradation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    half_life_of_parent_compound: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompound
    ] = field(
        default=None,
        metadata={
            "name": "HalfLifeOfParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    identity_transformation: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformation
    ] = field(
        default=None,
        metadata={
            "name": "IdentityTransformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    transf_products_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "TransfProductsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    evaporation_of_parent_compound: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionEvaporationOfParentCompound
    ] = field(
        default=None,
        metadata={
            "name": "EvaporationOfParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    volatile_metabolites: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionVolatileMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "VolatileMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    residues: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionResidues
    ] = field(
        default=None,
        metadata={
            "name": "Residues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    results_with_reference_substance: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ResultsWithReferenceSubstance",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
            },
        )
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    test_type: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoil:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BiodegradationInSoil"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/7.0"

    administrative_data: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordBiodegradationInSoilDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordBiodegradationInSoilApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
