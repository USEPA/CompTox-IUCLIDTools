from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_5.biodegradationinwaterandsedimentsimulationtests_6_5.models.common_types_oecd_v6 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    E36,
    E149,
    F102,
    F103,
    F110,
    F135,
    F136,
    F137,
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
    Pg660822,
    Pg660823,
)
from entity_models_6_5.biodegradationinwaterandsedimentsimulationtests_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0"


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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstanceEntryReferenceSubstance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryCompartment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660263] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryHalfLife(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[C113] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryTemp(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F136] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionIdentityTransformationEntryNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryCo2(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryCompartment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660263] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryNonExtractable(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryOtherVolatiles(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryTotalExtractable(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionOtherKineticParameters(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F135] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    observed_value: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ObservedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsApplicantSummaryAndConclusionValidityCriteriaEntryValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    name_or_code_for_product: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOrCodeForProduct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    degr: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryDegr
    ] = field(
        default=None,
        metadata={
            "name": "Degr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    sampling_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SamplingDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50Entry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    half_life: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryHalfLife
    ] = field(
        default=None,
        metadata={
            "name": "HalfLife",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    type_value: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50EntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionIdentityTransformationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionIdentityTransformationEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    compartment: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryCompartment
    ] = field(
        default=None,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    sampling_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SamplingDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
            "nillable": True,
        },
    )
    total_extractable: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryTotalExtractable
    ] = field(
        default=None,
        metadata={
            "name": "TotalExtractable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    non_extractable: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryNonExtractable
    ] = field(
        default=None,
        metadata={
            "name": "NonExtractable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    co2: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryCo2
    ] = field(
        default=None,
        metadata={
            "name": "CO2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other_volatiles: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryOtherVolatiles
    ] = field(
        default=None,
        metadata={
            "name": "OtherVolatiles",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    attached_study_report: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[AttachmentListField] = (
        field(
            default=None,
            metadata={
                "name": "AttachedSanitisedDocsForPublication",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
            },
        )
    )
    kinetic_evaluation: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "KineticEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50Entry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionIdentityTransformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionIdentityTransformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecovery:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecoveryEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    inoculum_or_test_system: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInoculumOrTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InoculumOrTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    details_on_source_and_properties_of_surface_water: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSourceAndPropertiesOfSurfaceWater",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    details_on_source_and_properties_of_sediment: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSourceAndPropertiesOfSediment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    details_on_inoculum: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnInoculum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    duration_of_test_contact_time: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignDurationOfTestContactTime
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfTestContactTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    initial_test_substance_concentration: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration
    ] = field(
        default=None,
        metadata={
            "name": "InitialTestSubstanceConcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    parameter_followed_for_biodegradation_estimation: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignParameterFollowedForBiodegradationEstimation
    ] = field(
        default_factory=list,
        metadata={
            "name": "ParameterFollowedForBiodegradationEstimation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    reference_substance: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesignReferenceSubstance
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    mean_total_recovery: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMeanTotalRecovery
    ] = field(
        default=None,
        metadata={
            "name": "MeanTotalRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    degradation: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionDegradation
    ] = field(
        default=None,
        metadata={
            "name": "Degradation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    half_life_of_parent_compound50_disappearance_time_dt50: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionHalfLifeOfParentCompound50DisappearanceTimeDt50
    ] = field(
        default=None,
        metadata={
            "name": "HalfLifeOfParentCompound50DisappearanceTimeDT50",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    mineralization_rate_in_co2: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionMineralizationRateInCo2
    ] = field(
        default=None,
        metadata={
            "name": "MineralizationRateInCO2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    other_kinetic_parameters: List[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionOtherKineticParameters
    ] = field(
        default_factory=list,
        metadata={
            "name": "OtherKineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    identity_transformation: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionIdentityTransformation
    ] = field(
        default=None,
        metadata={
            "name": "IdentityTransformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    transf_products_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "TransfProductsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    evaporation_of_parent_compound: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionEvaporationOfParentCompound
    ] = field(
        default=None,
        metadata={
            "name": "EvaporationOfParentCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    volatile_metabolites: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionVolatileMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "VolatileMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    residues: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionResidues
    ] = field(
        default=None,
        metadata={
            "name": "Residues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    results_with_reference_substance: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ResultsWithReferenceSubstance",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
            },
        )
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTestsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0",
        },
    )


@dataclass
class EndpointStudyRecordBiodegradationInWaterAndSedimentSimulationTests:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BiodegradationInWaterAndSedimentSimulationTests"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BiodegradationInWaterAndSedimentSimulationTests/6.0"

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
