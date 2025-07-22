from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.biodegradationinsoil_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    F11,
    F12,
    F13,
    F16,
    F17,
    F25,
    F103,
    F109,
    F110,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660267,
    Pg660268,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0"


@dataclass
class EndpointStudyRecordBiodegradationInSoilApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryBulkDensityGcm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryClay:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryOrgC:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryPh:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySand:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySilt:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryDegr:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660268] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660267] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[F12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn:
    class Meta:
        global_type = False

    value: Optional[F110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc:
    class Meta:
        global_type = False

    unit_code: Optional[F13] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignOxygenConditions:
    class Meta:
        global_type = False

    value: Optional[F25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignParameterFollowed:
    class Meta:
        global_type = False

    value: Optional[F103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilClassification:
    class Meta:
        global_type = False

    value: Optional[F16] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryCec:
    class Meta:
        global_type = False

    unit_code: Optional[F17] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilType:
    class Meta:
        global_type = False

    value: Optional[F109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestType:
    class Meta:
        global_type = False

    value: Optional[F11] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParameter:
    class Meta:
        global_type = False

    value: Optional[F103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySamplingTime:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionEvaporationOfParentCompound:
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryHalfLife:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryTemp:
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryType:
    class Meta:
        global_type = False

    value: Optional[F136] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntryNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionResidues:
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProducts:
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionVolatileMetabolites:
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBiodegradationInSoilDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBiodegradationInSoilDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntry:
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntry:
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    temp: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    humidity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Humidity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    microbial_biomass: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MicrobialBiomass",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry:
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    initial_conc: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc
    ] = field(
        default=None,
        metadata={
            "name": "InitialConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntry:
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    soil_type: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilType
    ] = field(
        default=None,
        metadata={
            "name": "SoilType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    clay: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryClay
    ] = field(
        default=None,
        metadata={
            "name": "Clay",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    silt: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySilt
    ] = field(
        default=None,
        metadata={
            "name": "Silt",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    sand: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySand
    ] = field(
        default=None,
        metadata={
            "name": "Sand",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    org_c: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryOrgC
    ] = field(
        default=None,
        metadata={
            "name": "OrgC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    cec: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryCec
    ] = field(
        default=None,
        metadata={
            "name": "CEC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    bulk_density_gcm: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryBulkDensityGcm
    ] = field(
        default=None,
        metadata={
            "name": "BulkDensityGCm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    degr: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryDegr
    ] = field(
        default=None,
        metadata={
            "name": "Degr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    st_dev: Optional[str] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    parameter: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    sampling_time: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySamplingTime
    ] = field(
        default=None,
        metadata={
            "name": "SamplingTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    half_life: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryHalfLife
    ] = field(
        default=None,
        metadata={
            "name": "HalfLife",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    st_dev: Optional[str] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    type_value: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompoundEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntry:
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformationEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntry:
    class Meta:
        global_type = False

    soil_no: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    recovery: Optional[str] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    st_dev: Optional[str] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    soil_classification: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilClassification
    ] = field(
        default=None,
        metadata={
            "name": "SoilClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    details_on_soil_characteristics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSoilCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    duration_of_test_contact_time: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTime
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfTestContactTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    initial_test_substance_concentration: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration
    ] = field(
        default=None,
        metadata={
            "name": "InitialTestSubstanceConcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    parameter_followed: List[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignParameterFollowed
    ] = field(
        default_factory=list,
        metadata={
            "name": "ParameterFollowed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    experimental_conditions: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditions
    ] = field(
        default=None,
        metadata={
            "name": "ExperimentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    details_on_experimental_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExperimentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    degradation: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradation
    ] = field(
        default=None,
        metadata={
            "name": "Degradation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    half_life_of_parent_compound: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionHalfLifeOfParentCompound
    ] = field(
        default=None,
        metadata={
            "name": "HalfLifeOfParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    identity_transformation: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionIdentityTransformation
    ] = field(
        default=None,
        metadata={
            "name": "IdentityTransformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    transf_products_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TransfProductsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    evaporation_of_parent_compound: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionEvaporationOfParentCompound
    ] = field(
        default=None,
        metadata={
            "name": "EvaporationOfParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    volatile_metabolites: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionVolatileMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "VolatileMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    residues: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionResidues
    ] = field(
        default=None,
        metadata={
            "name": "Residues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    results_with_reference_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsWithReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    test_type: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInSoil:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BiodegradationInSoil"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInSoil/5.0"

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
