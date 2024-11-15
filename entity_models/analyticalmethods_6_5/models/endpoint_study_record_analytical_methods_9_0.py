from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from analyticalmethods_6_5.models.common_types_oecd_v9 import (
    A36,
    C54,
    C102,
    C104,
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
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660350,
    Pg661017,
    Pg661224,
    Pg661225,
    Pg661226,
    Pg661227,
    Pg661228,
    Pg661229,
    Pg661230,
)
from analyticalmethods_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0"


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660350] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsApplicantSummaryAndConclusionValidityCriteriaFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsBackgroundMethodClass(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661224] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableExtractionAndCleanUp(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661226] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableInstrumentDetectorForConfirmatoryMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableResidueMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661225] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableSuitabilityOfTheMethodForConfirmation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661227] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableExtractionAndCleanUp(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661226] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableInstrumentDetectorForEnforcementMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableResidueMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661225] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicableExtractionAndCleanUp(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661226] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicableInstrumentDetector(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicableResidueMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661225] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsMatrixMedium(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C54] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsOtherQualityAssurance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsExtractionAndCleanUp(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661226] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsInstrumentDetector(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsResidueMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661225] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661230] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryCalibrationRange(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryStandards(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661229] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationIndependentLaboratoryValidationList(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661228] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryLimitOfDetection(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryLimitOfQuantification(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryFortificationLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryMeanRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryRangeRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatabilityEntryField6852Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryCalibrationRange(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryStandards(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661229] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryLimitOfDetection(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryLimitOfQuantification(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryFortificationLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryMeanRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryRangeRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatabilityEntryField6852Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryCalibrationRange(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryStandards(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661229] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryLimitOfDetection(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryLimitOfQuantification(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryFortificationLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryMeanRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryRangeRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatabilityEntryField6852Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryCalibrationRange(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryStandards(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661229] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryLimitOfDetection(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryLimitOfQuantification(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryFortificationLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661017] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryMrmmz(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryMeanRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryRangeRecovery(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatabilityEntryField6852Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordAnalyticalMethodsApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsBackground:
    class Meta:
        global_type = False

    background_information: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    method_class: List[
        EndpointStudyRecordAnalyticalMethodsBackgroundMethodClass
    ] = field(
        default_factory=list,
        metadata={
            "name": "MethodClass",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAnalyticalMethodsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAnalyticalMethodsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicable:
    class Meta:
        global_type = False

    instrument_detector_for_confirmatory_method: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableInstrumentDetectorForConfirmatoryMethod
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetectorForConfirmatoryMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    residue_method: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableResidueMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResidueMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    extraction_and_clean_up: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableExtractionAndCleanUp
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionAndCleanUp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    suitability_of_the_method_for_confirmation: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicableSuitabilityOfTheMethodForConfirmation
    ] = field(
        default_factory=list,
        metadata={
            "name": "SuitabilityOfTheMethodForConfirmation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    details_on_confirmatory_method: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnConfirmatoryMethod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicable:
    class Meta:
        global_type = False

    instrument_detector_for_enforcement_method: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableInstrumentDetectorForEnforcementMethod
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetectorForEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    residue_method: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableResidueMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResidueMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    extraction_and_clean_up: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicableExtractionAndCleanUp
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionAndCleanUp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    flow_diagram: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowDiagram",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    details_on_enforcement_method: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicable:
    class Meta:
        global_type = False

    instrument_detector: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicableInstrumentDetector
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetector",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    residue_method: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicableResidueMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResidueMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    extraction_and_clean_up: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicableExtractionAndCleanUp
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionAndCleanUp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    flow_diagram: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowDiagram",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    details_on_ilv: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnILV",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethods:
    class Meta:
        global_type = False

    instrument_detector: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsInstrumentDetector
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentDetector",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    residue_method: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsResidueMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResidueMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    extraction_and_clean_up: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethodsExtractionAndCleanUp
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionAndCleanUp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    flow_diagram: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowDiagram",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    details_on_analytical_method: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatabilityEntryField6852(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatabilityEntryField6852Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatabilityEntryField6852(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatabilityEntryField6852Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatabilityEntryField6852(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatabilityEntryField6852Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatabilityEntryField6852(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatabilityEntryField6852Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    standards: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryStandards
    ] = field(
        default_factory=list,
        metadata={
            "name": "Standards",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_range: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntryCalibrationRange
    ] = field(
        default=None,
        metadata={
            "name": "CalibrationRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_equation: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "CalibrationEquation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_quantification: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryLimitOfQuantification
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfQuantification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_detection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntryLimitOfDetection
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfDetection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    fortification_level: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryFortificationLevel
    ] = field(
        default=None,
        metadata={
            "name": "FortificationLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    range_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryRangeRecovery
    ] = field(
        default=None,
        metadata={
            "name": "RangeRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mean_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntryMeanRecovery
    ] = field(
        default=None,
        metadata={
            "name": "MeanRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatabilityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field6852: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatabilityEntryField6852
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    mean_content: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MeanContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsdr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSDr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    horrat_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HorratValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    standards: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryStandards
    ] = field(
        default_factory=list,
        metadata={
            "name": "Standards",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_range: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntryCalibrationRange
    ] = field(
        default=None,
        metadata={
            "name": "CalibrationRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_equation: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "CalibrationEquation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_quantification: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryLimitOfQuantification
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfQuantification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_detection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntryLimitOfDetection
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfDetection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    fortification_level: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryFortificationLevel
    ] = field(
        default=None,
        metadata={
            "name": "FortificationLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    range_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryRangeRecovery
    ] = field(
        default=None,
        metadata={
            "name": "RangeRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mean_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntryMeanRecovery
    ] = field(
        default=None,
        metadata={
            "name": "MeanRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatabilityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field6852: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatabilityEntryField6852
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    mean_content: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MeanContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsdr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSDr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    horrat_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HorratValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    standards: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryStandards
    ] = field(
        default_factory=list,
        metadata={
            "name": "Standards",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_range: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntryCalibrationRange
    ] = field(
        default=None,
        metadata={
            "name": "CalibrationRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_equation: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "CalibrationEquation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_quantification: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryLimitOfQuantification
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfQuantification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_detection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntryLimitOfDetection
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfDetection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    fortification_level: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryFortificationLevel
    ] = field(
        default=None,
        metadata={
            "name": "FortificationLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    range_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryRangeRecovery
    ] = field(
        default=None,
        metadata={
            "name": "RangeRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mean_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntryMeanRecovery
    ] = field(
        default=None,
        metadata={
            "name": "MeanRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatabilityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field6852: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatabilityEntryField6852
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    mean_content: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MeanContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsdr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSDr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    horrat_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HorratValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    standards: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryStandards
    ] = field(
        default_factory=list,
        metadata={
            "name": "Standards",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_range: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntryCalibrationRange
    ] = field(
        default=None,
        metadata={
            "name": "CalibrationRange",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration_equation: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "CalibrationEquation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    correlation_coefficient_r2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorrelationCoefficientR2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_quantification: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryLimitOfQuantification
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfQuantification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    limit_of_detection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntryLimitOfDetection
    ] = field(
        default=None,
        metadata={
            "name": "LimitOfDetection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mrmmz: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryMrmmz
    ] = field(
        default=None,
        metadata={
            "name": "MRMMZ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    fortification_level: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryFortificationLevel
    ] = field(
        default=None,
        metadata={
            "name": "FortificationLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    range_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryRangeRecovery
    ] = field(
        default=None,
        metadata={
            "name": "RangeRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    mean_recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntryMeanRecovery
    ] = field(
        default=None,
        metadata={
            "name": "MeanRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatabilityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field6852: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatabilityEntryField6852
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    analyte: Optional[str] = field(
        default=None,
        metadata={
            "name": "Analyte",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    number_replicates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    mean_content: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MeanContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rsdr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RSDr",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    horrat_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HorratValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_medium: List[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsMatrixMedium
    ] = field(
        default_factory=list,
        metadata={
            "name": "MatrixMedium",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    principles_of_analytical_methods: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsPrinciplesOfAnalyticalMethods
    ] = field(
        default=None,
        metadata={
            "name": "PrinciplesOfAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    enforcement_method_if_applicable: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsEnforcementMethodIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "EnforcementMethodIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    confirmatory_method_if_applicable: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsConfirmatoryMethodIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "ConfirmatoryMethodIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    independent_laboratory_validation_ilvif_applicable: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsIndependentLaboratoryValidationIlvifApplicable
    ] = field(
        default=None,
        metadata={
            "name": "IndependentLaboratoryValidationILVIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecovery:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecoveryEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatability:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatabilityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecovery:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecoveryEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatability:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatabilityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecovery:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecoveryEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatability:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatabilityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibrationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecovery:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecoveryEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatability:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatabilityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidation:
    class Meta:
        global_type = False

    recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRecovery
    ] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    repeatability: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationRepeatability
    ] = field(
        default=None,
        metadata={
            "name": "Repeatability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    loqlod: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationLoqlod
    ] = field(
        default=None,
        metadata={
            "name": "LOQLOD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationCalibration
    ] = field(
        default=None,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MatrixEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "MatrixEffectsRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    independent_laboratory_validation_list: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidationIndependentLaboratoryValidationList
    ] = field(
        default=None,
        metadata={
            "name": "IndependentLaboratoryValidationList",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    independent_laboratory_validation: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "IndependentLaboratoryValidation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethod:
    class Meta:
        global_type = False

    recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRecovery
    ] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    recovery_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "RecoveryResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    repeatability: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodRepeatability
    ] = field(
        default=None,
        metadata={
            "name": "Repeatability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    loqlod: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodLoqlod
    ] = field(
        default=None,
        metadata={
            "name": "LOQLOD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethodCalibration
    ] = field(
        default=None,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MatrixEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "MatrixEffectsRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    characteristics_of_analytical_method: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "CharacteristicsOfAnalyticalMethod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicable:
    class Meta:
        global_type = False

    recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRecovery
    ] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    repeatability: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableRepeatability
    ] = field(
        default=None,
        metadata={
            "name": "Repeatability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    loqlod: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableLoqlod
    ] = field(
        default=None,
        metadata={
            "name": "LOQLOD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicableCalibration
    ] = field(
        default=None,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MatrixEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "MatrixEffectsRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    additional_details_on_confirmatory_method: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDetailsOnConfirmatoryMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethod:
    class Meta:
        global_type = False

    recovery: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRecovery
    ] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    recovery_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "RecoveryResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    repeatability: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodRepeatability
    ] = field(
        default=None,
        metadata={
            "name": "Repeatability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    loqlod: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodLoqlod
    ] = field(
        default=None,
        metadata={
            "name": "LOQLOD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    calibration: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethodCalibration
    ] = field(
        default=None,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MatrixEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    matrix_effects_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "MatrixEffectsRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    characteristics_of_enforcement_method: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "CharacteristicsOfEnforcementMethod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordAnalyticalMethodsResultsAndDiscussion:
    class Meta:
        global_type = False

    recovery_results_and_characteristics_of_analytical_method: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionRecoveryResultsAndCharacteristicsOfAnalyticalMethod
    ] = field(
        default=None,
        metadata={
            "name": "RecoveryResultsAndCharacteristicsOfAnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    results_using_enforcement_method: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingEnforcementMethod
    ] = field(
        default=None,
        metadata={
            "name": "ResultsUsingEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    results_using_confirmatory_method_if_applicable: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionResultsUsingConfirmatoryMethodIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "ResultsUsingConfirmatoryMethodIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    independent_laboratory_validation: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionIndependentLaboratoryValidation
    ] = field(
        default=None,
        metadata={
            "name": "IndependentLaboratoryValidation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAnalyticalMethods:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AnalyticalMethods"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AnalyticalMethods/9.0"

    administrative_data: Optional[
        EndpointStudyRecordAnalyticalMethodsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordAnalyticalMethodsDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    background: Optional[EndpointStudyRecordAnalyticalMethodsBackground] = (
        field(
            default=None,
            metadata={
                "name": "Background",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAnalyticalMethodsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAnalyticalMethodsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAnalyticalMethodsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAnalyticalMethodsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
