from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.skinsensitisation_6_5.models.common_types_oecd_v5 import (
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
    Z52,
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
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0"


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystem:
    class Meta:
        global_type = False

    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystem:
    class Meta:
        global_type = False

    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryValue:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryValue:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660211] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660210] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationApplicantSummaryAndConclusionInterpretationOfResults:
    class Meta:
        global_type = False

    value: Optional[Pg660218] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[T20] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaPositiveControlSubstances:
    class Meta:
        global_type = False

    value: Optional[T109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaVehicle:
    class Meta:
        global_type = False

    value: Optional[T522] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryAdequacyOfChallenge:
    class Meta:
        global_type = False

    value: Optional[Pg660215] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryRoute:
    class Meta:
        global_type = False

    value: Optional[T54] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryVehicle:
    class Meta:
        global_type = False

    value: Optional[T521] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryAdequacyOfInduction:
    class Meta:
        global_type = False

    value: Optional[Pg660214] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryRoute:
    class Meta:
        global_type = False

    value: Optional[T54] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryVehicle:
    class Meta:
        global_type = False

    value: Optional[T521] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaPositiveControlSubstances:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[T026] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[T23234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTypeOfStudy:
    class Meta:
        global_type = False

    value: Optional[T18] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryNegativeControlsValid:
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryParameter:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryPositiveControlsValid:
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660216] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryVehicleControlsValid:
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryParameter:
    class Meta:
        global_type = False

    value: Optional[Pg660217] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660332] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryGroup:
    class Meta:
        global_type = False

    value: Optional[T111] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryReading:
    class Meta:
        global_type = False

    value: Optional[T110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660216] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordSkinSensitisationDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordSkinSensitisationDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    concentration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    no_of_animals_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    positive_control_substances: List[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlnaPositiveControlSubstances
    ] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControlSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntry:
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    route: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryRoute
    ] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    concentration_amount: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationAmount",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    day_sduration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DaySDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    adequacy_of_challenge: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallengeEntryAdequacyOfChallenge
    ] = field(
        default=None,
        metadata={
            "name": "AdequacyOfChallenge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntry:
    class Meta:
        global_type = False

    route: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryRoute
    ] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    concentration_amount: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationAmount",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    day_sduration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DaySDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    adequacy_of_induction: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaInductionEntryAdequacyOfInduction
    ] = field(
        default=None,
        metadata={
            "name": "AdequacyOfInduction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    details_on_test_animals_and_environmental_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestAnimalsAndEnvironmentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordSkinSensitisationOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    parameter: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    run_experiment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RunExperiment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    value: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    vehicle_controls_valid: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryVehicleControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "VehicleControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    negative_controls_valid: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryNegativeControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "NegativeControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    positive_controls_valid: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryPositiveControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemicoResultsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    parameter: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    value: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    variability: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Variability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    test_group_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestGroupRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlnaResultsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    reading: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryReading
    ] = field(
        default=None,
        metadata={
            "name": "Reading",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    hours_after_challenge: Optional[str] = field(
        default=None,
        metadata={
            "name": "HoursAfterChallenge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    group: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryGroup
    ] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    dose_level: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    no_with_reactions: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoWithReactions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    total_no_in_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalNoInGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    clinical_observations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ClinicalObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTestResultsOfTestEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordSkinSensitisationAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordSkinSensitisationAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    challenge: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaChallenge
    ] = field(
        default=None,
        metadata={
            "name": "Challenge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    no_of_animals_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    challenge_controls: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ChallengeControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    positive_control_substances: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlnaPositiveControlSubstances
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControlSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    other_effects_acceptance_of_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherEffectsAcceptanceOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    cellular_proliferation_data_observations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CellularProliferationDataObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    study_design_in_vivo_non_llna: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoNonLlna
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesignInVivoNonLLNA",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    study_design_in_vivo_llna: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystemStudyDesignInVivoLlna
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesignInVivoLLNA",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisationResultsAndDiscussion:
    class Meta:
        global_type = False

    positive_control_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControlResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    in_vitro_in_chemico: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVitroInChemico
    ] = field(
        default=None,
        metadata={
            "name": "InVitroInChemico",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    traditional_sensitisation_test: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionTraditionalSensitisationTest
    ] = field(
        default=None,
        metadata={
            "name": "TraditionalSensitisationTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    in_vivo_llna: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionInVivoLlna
    ] = field(
        default=None,
        metadata={
            "name": "InVivoLLNA",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordSkinSensitisationResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    type_of_study: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTypeOfStudy
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    justification_for_non_llnamethod: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForNonLLNAMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    in_vitro_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVitroTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InVitroTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    in_chemico_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInChemicoTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InChemicoTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    in_vivo_test_system: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsInVivoTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InVivoTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordSkinSensitisationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinSensitisation:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.SkinSensitisation"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinSensitisation/5.0"

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
