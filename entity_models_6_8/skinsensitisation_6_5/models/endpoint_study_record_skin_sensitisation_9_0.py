from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from skinsensitisation_6_5.models.common_types_oecd_v9 import (
    A36,
    F137,
    N64,
    N78,
    T026,
    T18,
    T20,
    T24,
    T54,
    T109,
    T110,
    T111,
    T144,
    T521,
    T522,
    T23234,
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
    Pg660210,
    Pg660211,
    Pg660214,
    Pg660215,
    Pg660216,
    Pg660217,
    Pg660218,
    Pg660332,
    Pg661121,
    Pg661157,
    Pg661239,
    Pg661240,
    Pg661241,
    Pg661242,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    SkinSens61022,
    SkinSens61023,
    SkinSens61024,
    SkinSens61025,
    SkinSens61026,
    SkinSens61027,
    SkinSens61028,
    SkinSens61029,
    SkinSens61030,
    SkinSens61031,
    SkinSens61032,
    SkinSens61033,
    SkinSens61034,
    SkinSens61035,
)
from skinsensitisation_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0"


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660211] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660210] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationApplicantSummaryAndConclusionInterpretationOfResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660218] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T20] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystemDetailsTestSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61026] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystemPositiveControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61028] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystemVehicleSolvent(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61027] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInSilicoTestSystemDetailsOfTestSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661239] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemDetailsTestSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61022] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemNegativeControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61024] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemPositiveControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61025] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemVehicleSolventControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61023] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaPositiveControlSubstances(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T522] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryAdequacyOfChallenge(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660215] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryRoute(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T54] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T521] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryAdequacyOfInduction(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660214] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryRoute(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T54] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T521] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaPositiveControlSubstances(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T026] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T23234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTypeOfStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T18] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoOutcomeOfThePredictionModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryGroup(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61029] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661240] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryRemarksOnResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61034] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryValue(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661241] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoPredictionModelOutcome(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61035] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryAtConcentration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[SkinSens61033] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryGroup(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61029] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryNegativeControlsValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61031] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryPositiveControlsValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61034] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryRunExperiment(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SkinSens61030] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryValue(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[SkinSens61032] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryVehicleControlsValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660217] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660332] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryGroup(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T111] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryReading(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660216] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    interpretation_of_results: Optional[
        EndpointStudyRecordSkinSensitisationApplicantSummaryAndConclusionInterpretationOfResults
    ] = field(
        default=None,
        metadata={
            "name": "InterpretationOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordSkinSensitisationDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordSkinSensitisationDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystem:
    class Meta:
        global_type = False

    details_test_system: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystemDetailsTestSystem
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    vehicle_solvent: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystemVehicleSolvent
    ] = field(
        default=None,
        metadata={
            "name": "VehicleSolvent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    positive_control: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystemPositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInSilicoTestSystem:
    class Meta:
        global_type = False

    details_of_test_system: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInSilicoTestSystemDetailsOfTestSystem
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOfTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    details_on_the_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTheStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystem:
    class Meta:
        global_type = False

    details_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemDetailsTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "DetailsTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    vehicle_solvent_control: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemVehicleSolventControl
    ] = field(
        default=None,
        metadata={
            "name": "VehicleSolventControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    negative_control: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemNegativeControl
    ] = field(
        default=None,
        metadata={
            "name": "NegativeControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    positive_control: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystemPositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlna:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    concentration: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    no_of_animals_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    positive_control_substances: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaPositiveControlSubstances
    ] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControlSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    route: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryRoute
    ] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    concentration_amount: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationAmount",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    day_sduration: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "DaySDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    adequacy_of_challenge: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryAdequacyOfChallenge
    ] = field(
        default=None,
        metadata={
            "name": "AdequacyOfChallenge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    route: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryRoute
    ] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    concentration_amount: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationAmount",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    day_sduration: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "DaySDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    adequacy_of_induction: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryAdequacyOfInduction
    ] = field(
        default=None,
        metadata={
            "name": "AdequacyOfInduction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    details_on_test_animals_and_environmental_conditions: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestAnimalsAndEnvironmentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    group: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryGroup
    ] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    group: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryGroup
    ] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    run_experiment: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryRunExperiment
    ] = field(
        default=None,
        metadata={
            "name": "RunExperiment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    at_concentration: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryAtConcentration
    ] = field(
        default=None,
        metadata={
            "name": "AtConcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    cell_viability: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "CellViability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    vehicle_controls_valid: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryVehicleControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "VehicleControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    negative_controls_valid: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryNegativeControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "NegativeControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    positive_controls_valid: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryPositiveControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    variability: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Variability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    test_group_remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TestGroupRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    reading: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryReading
    ] = field(
        default=None,
        metadata={
            "name": "Reading",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    hours_after_challenge: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HoursAfterChallenge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    group: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryGroup
    ] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    dose_level: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "DoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    no_with_reactions: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoWithReactions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            "nillable": True,
        },
    )
    total_no_in_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalNoInGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            "nillable": True,
        },
    )
    clinical_observations: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ClinicalObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallenge:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInduction:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTest:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlna:
    class Meta:
        global_type = False

    induction: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInduction
    ] = field(
        default=None,
        metadata={
            "name": "Induction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    challenge: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallenge
    ] = field(
        default=None,
        metadata={
            "name": "Challenge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    no_of_animals_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    challenge_controls: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ChallengeControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    positive_control_substances: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaPositiveControlSubstances
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControlSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilico:
    class Meta:
        global_type = False

    results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoResults
    ] = field(
        default=None,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    outcome_of_the_prediction_model: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilicoOutcomeOfThePredictionModel
    ] = field(
        default=None,
        metadata={
            "name": "OutcomeOfThePredictionModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemico:
    class Meta:
        global_type = False

    results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResults
    ] = field(
        default=None,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    prediction_model_outcome: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoPredictionModelOutcome
    ] = field(
        default=None,
        metadata={
            "name": "PredictionModelOutcome",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    other_effects_acceptance_of_results: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "OtherEffectsAcceptanceOfResults",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlna:
    class Meta:
        global_type = False

    results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResults
    ] = field(
        default=None,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    cellular_proliferation_data_observations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "CellularProliferationDataObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTest:
    class Meta:
        global_type = False

    results_of_test: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTest
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystem:
    class Meta:
        global_type = False

    test_animals: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    study_design_in_vivo_non_llna: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlna
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesignInVivoNonLLNA",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    study_design_in_vivo_llna: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlna
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesignInVivoLLNA",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    type_of_study: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTypeOfStudy
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    justification_for_non_llnamethod: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForNonLLNAMethod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
            },
        )
    )
    test_materials: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_vitro_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InVitroTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_chemico_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InChemicoTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_silico_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInSilicoTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InSilicoTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_vivo_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InVivoTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussion:
    class Meta:
        global_type = False

    positive_control_results: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControlResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_vitro_in_chemico: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemico
    ] = field(
        default=None,
        metadata={
            "name": "InVitroInChemico",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_silico: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInSilico
    ] = field(
        default=None,
        metadata={
            "name": "InSilico",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    traditional_sensitisation_test: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTest
    ] = field(
        default=None,
        metadata={
            "name": "TraditionalSensitisationTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    in_vivo_llna: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlna
    ] = field(
        default=None,
        metadata={
            "name": "InVivoLLNA",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisation:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.SkinSensitisation"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/9.0"

    administrative_data: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordSkinSensitisationDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordSkinSensitisationOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordSkinSensitisationApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
