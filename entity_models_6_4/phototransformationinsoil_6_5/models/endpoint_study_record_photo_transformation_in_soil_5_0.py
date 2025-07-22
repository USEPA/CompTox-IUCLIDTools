from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.phototransformationinsoil_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    F023,
    F03,
    F13,
    F102,
    F112,
    F137,
    N64,
    N78,
    P116,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z36,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660044,
    Pg660159,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0"


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSpectrumWavelengthInNm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignRelativeLightIntensity:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryDegradationPercent:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660159] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[F023] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMethod:
    class Meta:
        global_type = False

    value: Optional[Pg660044] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDarkControls:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryInitialConcMeasured:
    class Meta:
        global_type = False

    unit_code: Optional[F13] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryTemp:
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSource:
    class Meta:
        global_type = False

    value: Optional[F03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignReferenceSubstance:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryTimePoint:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLifeEntryHalfLife:
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLifeEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntryNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryParameter:
    class Meta:
        global_type = False

    value: Optional[F112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryValue:
    class Meta:
        global_type = False

    unit_code: Optional[P116] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionTransformationProducts:
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordPhotoTransformationInSoilDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordPhotoTransformationInSoilDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntry:
    class Meta:
        global_type = False

    duration: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    moisture: Optional[str] = field(
        default=None,
        metadata={
            "name": "Moisture",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    temp: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    initial_conc_measured: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryInitialConcMeasured
    ] = field(
        default=None,
        metadata={
            "name": "InitialConcMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    degradation_percent: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryDegradationPercent
    ] = field(
        default=None,
        metadata={
            "name": "DegradationPercent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    st_dev: Optional[str] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    time_point: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryTimePoint
    ] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    test_condition: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestCondition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLifeEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    half_life: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLifeEntryHalfLife
    ] = field(
        default=None,
        metadata={
            "name": "HalfLife",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    test_condition: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestCondition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLifeEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntry:
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntry:
    class Meta:
        global_type = False

    parameter: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    value: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestCondition:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLife:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLifeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrum:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    analytical_method: List[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMethod
    ] = field(
        default_factory=list,
        metadata={
            "name": "AnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    details_on_soil: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    light_source: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSource
    ] = field(
        default=None,
        metadata={
            "name": "LightSource",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    light_spectrum_wavelength_in_nm: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSpectrumWavelengthInNm
    ] = field(
        default=None,
        metadata={
            "name": "LightSpectrumWavelengthInNm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    relative_light_intensity: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignRelativeLightIntensity
    ] = field(
        default=None,
        metadata={
            "name": "RelativeLightIntensity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    details_on_light_source: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnLightSource",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    duration_of_test_at_given_test_condition: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestCondition
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfTestAtGivenTestCondition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    reference_substance: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignReferenceSubstance
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    dark_controls: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDarkControls
    ] = field(
        default=None,
        metadata={
            "name": "DarkControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    computational_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ComputationalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussion:
    class Meta:
        global_type = False

    preliminary_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PreliminaryStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    test_performance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestPerformance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    spectrum: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrum
    ] = field(
        default=None,
        metadata={
            "name": "Spectrum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    degradation: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradation
    ] = field(
        default=None,
        metadata={
            "name": "Degradation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    quantum_yield: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantumYield",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
            "nillable": True,
        },
    )
    dissipation_half_life: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDissipationHalfLife
    ] = field(
        default=None,
        metadata={
            "name": "DissipationHalfLife",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    identity_transformation: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformation
    ] = field(
        default=None,
        metadata={
            "name": "IdentityTransformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    results_reference_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhotoTransformationInSoil:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.PhotoTransformationInSoil"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-PhotoTransformationInSoil/5.0"

    administrative_data: Optional[
        EndpointStudyRecordPhotoTransformationInSoilAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordPhotoTransformationInSoilDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
