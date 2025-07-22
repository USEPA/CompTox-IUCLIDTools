from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_5.toxicitytobirds_6_5.models.common_types_oecd_v6 import (
    A03,
    A36,
    E30,
    E105,
    E136,
    E137,
    E138,
    E139,
    E261,
    E271,
    E282,
    F102,
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
    Z38,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660256,
)
from entity_models_6_5.toxicitytobirds_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0"


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660256] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusionValidityCriteriaFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminationsReferenceSubstancePositiveControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E271] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignControlAnimals(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignLimitTest(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignTotalExposureDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E30] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsAnalyticalMonitoring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsDoseMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E136] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E261] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryBasisForEffect(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E282] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryConcDoseBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E30] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[E139] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E138] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordToxicityToBirdsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordToxicityToBirdsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    details_on_examinations_and_observations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExaminationsAndObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    details_on_reproductive_parameters: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnReproductiveParameters",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
            },
        )
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminationsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    limit_test: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    post_exposure_observation_period: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "PostExposureObservationPeriod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
            },
        )
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    nominal_and_measured_doses_concentrations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredDosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    details_on_test_conditions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    dose_method: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsDoseMethod
    ] = field(
        default=None,
        metadata={
            "name": "DoseMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    analytical_monitoring: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    details_on_preparation_and_analysis_of_diet: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnPreparationAndAnalysisOfDiet",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    details_on_test_organisms: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    conc_dose_based_on: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryConcDoseBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcDoseBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    attached_study_report: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[AttachmentListField] = (
        field(
            default=None,
            metadata={
                "name": "AttachedSanitisedDocsForPublication",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevels:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirdsResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_levels: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevels
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    repellency_factors: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "RepellencyFactors",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    mortality_and_sub_lethal_effects: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MortalityAndSubLethalEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    effects_on_reproduction: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "EffectsOnReproduction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    results_with_reference_substance: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ResultsWithReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    further_details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "FurtherDetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    reported_statistics_and_error_estimates: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "ReportedStatisticsAndErrorEstimates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToBirds:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ToxicityToBirds"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToBirds/6.0"

    administrative_data: Optional[
        EndpointStudyRecordToxicityToBirdsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordToxicityToBirdsDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordToxicityToBirdsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordToxicityToBirdsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordToxicityToBirdsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
