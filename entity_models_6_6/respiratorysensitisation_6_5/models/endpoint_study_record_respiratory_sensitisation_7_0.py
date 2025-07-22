from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_6.respiratorysensitisation_6_5.models.common_types_oecd_v7 import (
    A36,
    N64,
    N78,
    T0210,
    T24,
    T172,
    T173,
    T255,
    T256,
    T521,
    T23123456,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660211,
    Pg660221,
    Pg660222,
    Pg661157,
)
from entity_models_6_6.respiratorysensitisation_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0"


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660211] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660221] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationApplicantSummaryAndConclusionInterpretationOfResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660222] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimalsSex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T0210] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemNegativeControlSubstanceS(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T173] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemPositiveControlSubstances(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T172] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemRouteOfChallengeExposure(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T256] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemRouteOfInductionExposure(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T255] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T521] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    legislation: List[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    interpretation_of_results: Optional[
        EndpointStudyRecordRespiratorySensitisationApplicantSummaryAndConclusionInterpretationOfResults
    ] = field(
        default=None,
        metadata={
            "name": "InterpretationOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordRespiratorySensitisationDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordRespiratorySensitisationDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    organism_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystem:
    class Meta:
        global_type = False

    route_of_induction_exposure: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemRouteOfInductionExposure
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfInductionExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    route_of_challenge_exposure: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemRouteOfChallengeExposure
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfChallengeExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    concentration: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    no_of_animals_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    challenge_controls: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ChallengeControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    positive_control_substances: List[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemPositiveControlSubstances
    ] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControlSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    negative_control_substance_s: List[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystemNegativeControlSubstanceS
    ] = field(
        default_factory=list,
        metadata={
            "name": "NegativeControlSubstanceS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationResultsAndDiscussion:
    class Meta:
        global_type = False

    results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    pos_control_results: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PosControlResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    neg_control_results: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "NegControlResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordRespiratorySensitisationResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    test_system: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "TestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0",
        },
    )


@dataclass
class EndpointStudyRecordRespiratorySensitisation:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.RespiratorySensitisation"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RespiratorySensitisation/7.0"

    administrative_data: Optional[
        EndpointStudyRecordRespiratorySensitisationAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordRespiratorySensitisationDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordRespiratorySensitisationMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordRespiratorySensitisationResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordRespiratorySensitisationOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordRespiratorySensitisationApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
