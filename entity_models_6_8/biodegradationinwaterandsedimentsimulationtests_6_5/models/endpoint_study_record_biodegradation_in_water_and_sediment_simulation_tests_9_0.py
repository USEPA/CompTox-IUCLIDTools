from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from biodegradationinwaterandsedimentsimulationtests_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    E149,
    F102,
    F103,
    F110,
    F136,
    F261B,
    F272,
    F282,
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
    Pg660257,
    Pg660259,
    Pg660261,
    Pg660263,
    Pg660490,
    Pg660822,
    Pg660823,
    Pg661157,
    Pg661170,
    Pg661171,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Pg661691,
)
from biodegradationinwaterandsedimentsimulationtests_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0"


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660259] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660257] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteriaEntryValidityCriteriaFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F261B] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignDurationOfTestContactTime(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[F282] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInoculumOrTestSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F272] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignOxygenConditions(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660261] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignParameterFollowedForBiodegradationEstimation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstanceEntryReferenceSubstance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661691] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryCompartment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660263] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661170] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryTemp(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F136] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryTypeOfValue(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661171] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryPvalue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryCompartment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660823] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryDegr(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryParentProduct(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660822] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntrySamplingTime(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionEvaporationOfParentCompound(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryCo2(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryCompartment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660263] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryNonExtractable(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntrySamplingTime(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMineralizationRateInCo2(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E149] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionResidues(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProducts(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryCompartment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660263] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryIdno(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661170] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryTemp(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryTypeOfKineticsAndMethodOfCalculation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F136] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryTypeOfValue(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661171] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryPvalue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionVolatileMetabolites(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteriaEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    validity_criteria: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    observed_value: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ObservedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteriaEntryValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    initial_conc: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc
    ] = field(
        default=None,
        metadata={
            "name": "InitialConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstanceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reference_substance: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstanceEntryReferenceSubstance
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    type_value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    type_of_value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryTypeOfValue
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    chi_square2_error: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChiSquare2Error",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    pvalue: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryPvalue
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    kinetic_parameters: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "KineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    parent_product: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryParentProduct
    ] = field(
        default=None,
        metadata={
            "name": "ParentProduct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    name_or_code_for_product: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOrCodeForProduct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    sampling_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SamplingDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            "nillable": True,
        },
    )
    sampling_time: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntrySamplingTime
    ] = field(
        default=None,
        metadata={
            "name": "SamplingTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    degr: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryDegr
    ] = field(
        default=None,
        metadata={
            "name": "Degr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    sampling_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SamplingDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            "nillable": True,
        },
    )
    sampling_time: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntrySamplingTime
    ] = field(
        default=None,
        metadata={
            "name": "SamplingTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    total_extractable: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable
    ] = field(
        default=None,
        metadata={
            "name": "TotalExtractable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    non_extractable: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryNonExtractable
    ] = field(
        default=None,
        metadata={
            "name": "NonExtractable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    co2: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryCo2
    ] = field(
        default=None,
        metadata={
            "name": "CO2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    other_volatiles: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles
    ] = field(
        default=None,
        metadata={
            "name": "OtherVolatiles",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    recovery: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryRecovery
    ] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    idno: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryIdno
    ] = field(
        default=None,
        metadata={
            "name": "IDNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    identity_of_compound: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    parent_compound_s: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "ParentCompoundS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    kinetic_formation_fraction: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "KineticFormationFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    maximum_occurrence: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumOccurrence",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    timepoint_of_maximum_occurrence_observed_in_days: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimepointOfMaximumOccurrenceObservedInDays",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            "nillable": True,
        },
    )
    parameter: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    type_of_kinetics_and_method_of_calculation: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryTypeOfKineticsAndMethodOfCalculation
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfKineticsAndMethodOfCalculation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    type_of_value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryTypeOfValue
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    chi_square2_error: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChiSquare2Error",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    pvalue: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntryPvalue
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    kinetic_parameters: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "KineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteria:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteriaEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstance:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstanceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompound:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompoundEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalance:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalanceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetails:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetailsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteria
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    oxygen_conditions: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignOxygenConditions
    ] = field(
        default=None,
        metadata={
            "name": "OxygenConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    continuous_darkness: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContinuousDarkness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    inoculum_or_test_system: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInoculumOrTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InoculumOrTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_source_and_properties_of_surface_water: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSourceAndPropertiesOfSurfaceWater",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_source_and_properties_of_sediment: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSourceAndPropertiesOfSediment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_source_and_properties_of_manure: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSourceAndPropertiesOfManure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_inoculum: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnInoculum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    duration_of_test_contact_time: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignDurationOfTestContactTime
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfTestContactTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    initial_test_substance_concentration: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration
    ] = field(
        default=None,
        metadata={
            "name": "InitialTestSubstanceConcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    parameter_followed_for_biodegradation_estimation: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignParameterFollowedForBiodegradationEstimation
    ] = field(
        default_factory=list,
        metadata={
            "name": "ParameterFollowedForBiodegradationEstimation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    reference_substance: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstance
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    kinetic_evaluation: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "KineticEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussion:
    class Meta:
        global_type = False

    test_performance: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TestPerformance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    material_mass_balance: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMaterialMassBalance
    ] = field(
        default=None,
        metadata={
            "name": "MaterialMassBalance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    degradation: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradation
    ] = field(
        default=None,
        metadata={
            "name": "Degradation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    dtparent_compound: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDtparentCompound
    ] = field(
        default=None,
        metadata={
            "name": "DTParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    mineralization_rate_in_co2: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMineralizationRateInCo2
    ] = field(
        default=None,
        metadata={
            "name": "MineralizationRateInCO2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    transformation_products_details: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProductsDetails
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProductsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    transf_products_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "TransfProductsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    evaporation_of_parent_compound: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionEvaporationOfParentCompound
    ] = field(
        default=None,
        metadata={
            "name": "EvaporationOfParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    volatile_metabolites: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionVolatileMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "VolatileMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    residues: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionResidues
    ] = field(
        default=None,
        metadata={
            "name": "Residues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    results_with_reference_substance: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ResultsWithReferenceSubstance",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
            },
        )
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTests:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BiodegradationInWaterAndSedimentSimulationTests"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/9.0"

    administrative_data: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
