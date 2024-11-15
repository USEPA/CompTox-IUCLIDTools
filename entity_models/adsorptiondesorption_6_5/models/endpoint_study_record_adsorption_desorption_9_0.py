from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from adsorptiondesorption_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    F17,
    F21,
    F102,
    F109,
    F116,
    F132,
    F137,
    F221,
    N64,
    N78,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z36,
    Z40,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660189,
    Pg660190,
    Pg660194,
    Pg660195,
    Pg660196,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td470,
    Td480,
)
from adsorptiondesorption_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0"


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660190] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660189] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionApplicantSummaryAndConclusionValidityCriteriaFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsMedia(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F221] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsMethodType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F132] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodAnalyticalMonitoring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntryDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntryInitialConcMeasured(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[F116] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntrySampleNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntryTemp(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntryConcOfAdsorbedTestMat(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[F116] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntryDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntrySampleNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntryTemp(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryBulkDensityGcm(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryCec(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[F17] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryClay(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryMatrixNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryMatrixType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryOrgCarbon(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryPh(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntrySand(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntrySilt(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignHplcmethod:
    class Meta:
        global_type = False

    details_on_study_design_hplc_method: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnStudyDesignHplcMethod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryPercentageOfOrganicCarbon(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntrySampleNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryTemp(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Td470] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Td480] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryOrgCarbon(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryPhaseSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660194] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntrySampleNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryTemp(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660195] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660196] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodIdentityTransformationEntryNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntryAdsorptionPercentage(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntryDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntrySampleNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntryDesorptionPercentage(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntryDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntrySampleNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodTransformationProducts(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsHplcMethod:
    class Meta:
        global_type = False

    details_on_results_hplc_method: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResultsHplcMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordAdsorptionDesorptionApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAdsorptionDesorptionDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAdsorptionDesorptionDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    sample_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntrySampleNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    initial_conc_measured: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntryInitialConcMeasured
    ] = field(
        default=None,
        metadata={
            "name": "InitialConcMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    ph: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    sample_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntrySampleNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    conc_of_adsorbed_test_mat: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntryConcOfAdsorbedTestMat
    ] = field(
        default=None,
        metadata={
            "name": "ConcOfAdsorbedTestMat",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    ph: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    matrix_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryMatrixNo
    ] = field(
        default=None,
        metadata={
            "name": "MatrixNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    matrix_type: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryMatrixType
    ] = field(
        default=None,
        metadata={
            "name": "MatrixType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    clay: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryClay
    ] = field(
        default=None,
        metadata={
            "name": "Clay",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    silt: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntrySilt
    ] = field(
        default=None,
        metadata={
            "name": "Silt",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    sand: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntrySand
    ] = field(
        default=None,
        metadata={
            "name": "Sand",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    org_carbon: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryOrgCarbon
    ] = field(
        default=None,
        metadata={
            "name": "OrgCarbon",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    cec: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryCec
    ] = field(
        default=None,
        metadata={
            "name": "CEC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    bulk_density_gcm: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntryBulkDensityGcm
    ] = field(
        default=None,
        metadata={
            "name": "BulkDensityGCm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    sample_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntrySampleNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    type_value: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    ph: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    percentage_of_organic_carbon: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryPercentageOfOrganicCarbon
    ] = field(
        default=None,
        metadata={
            "name": "PercentageOfOrganicCarbon",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    sample_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntrySampleNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    phase_system: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryPhaseSystem
    ] = field(
        default=None,
        metadata={
            "name": "PhaseSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    type_value: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    ph: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    org_carbon: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryOrgCarbon
    ] = field(
        default=None,
        metadata={
            "name": "OrgCarbon",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodIdentityTransformationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodIdentityTransformationEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    parent_compound_s: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "ParentCompoundS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    sample_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntrySampleNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    adsorption_percentage: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntryAdsorptionPercentage
    ] = field(
        default=None,
        metadata={
            "name": "AdsorptionPercentage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    sample_no: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntrySampleNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    desorption_percentage: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntryDesorptionPercentage
    ] = field(
        default=None,
        metadata={
            "name": "DesorptionPercentage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixProperties:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixPropertiesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficient:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficientEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOther:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOtherEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodIdentityTransformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodIdentityTransformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhase:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhaseEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhase:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhaseEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethod:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    details_on_sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    matrix_properties: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodMatrixProperties
    ] = field(
        default=None,
        metadata={
            "name": "MatrixProperties",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    details_on_matrix: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMatrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    details_on_test_conditions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    duration_of_adsorption_equilibration: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfAdsorptionEquilibration
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfAdsorptionEquilibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    duration_of_desorption_equilibration: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethodDurationOfDesorptionEquilibration
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfDesorptionEquilibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    computational_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ComputationalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethod:
    class Meta:
        global_type = False

    adsorption_and_desorption_constants: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "AdsorptionAndDesorptionConstants",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    recovery_of_test_material: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "RecoveryOfTestMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    concentration_of_test_substance_at_end_of_adsorption_equilibration_period: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationOfTestSubstanceAtEndOfAdsorptionEquilibrationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    concentration_of_test_substance_at_end_of_desorption_equilibration_period: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationOfTestSubstanceAtEndOfDesorptionEquilibrationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    mass_balance_at_end_of_adsorption_phase: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfAdsorptionPhase
    ] = field(
        default=None,
        metadata={
            "name": "MassBalanceAtEndOfAdsorptionPhase",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    mass_balance_at_end_of_desorption_phase: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodMassBalanceAtEndOfDesorptionPhase
    ] = field(
        default=None,
        metadata={
            "name": "MassBalanceAtEndOfDesorptionPhase",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    identity_transformation: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethodIdentityTransformation
    ] = field(
        default=None,
        metadata={
            "name": "IdentityTransformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    details_on_results_batch_equilibrium_method: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResultsBatchEquilibriumMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    test_temperature: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    hplcmethod: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignHplcmethod
    ] = field(
        default=None,
        metadata={
            "name": "HPLCMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    batch_equilibrium_or_other_method: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesignBatchEquilibriumOrOtherMethod
    ] = field(
        default=None,
        metadata={
            "name": "BatchEquilibriumOrOtherMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    method_type: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsMethodType
    ] = field(
        default=None,
        metadata={
            "name": "MethodType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    media: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsMedia
    ] = field(
        default=None,
        metadata={
            "name": "Media",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussion:
    class Meta:
        global_type = False

    adsorption_coefficient: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionCoefficient
    ] = field(
        default=None,
        metadata={
            "name": "AdsorptionCoefficient",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    adsorption_other: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdsorptionOther
    ] = field(
        default=None,
        metadata={
            "name": "AdsorptionOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    results_hplc_method: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsHplcMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResultsHplcMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    results_batch_equilibrium_or_other_method: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionResultsBatchEquilibriumOrOtherMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResultsBatchEquilibriumOrOtherMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAdsorptionDesorption:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AdsorptionDesorption"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AdsorptionDesorption/9.0"

    administrative_data: Optional[
        EndpointStudyRecordAdsorptionDesorptionAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordAdsorptionDesorptionDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAdsorptionDesorptionMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAdsorptionDesorptionResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAdsorptionDesorptionOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAdsorptionDesorptionApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
