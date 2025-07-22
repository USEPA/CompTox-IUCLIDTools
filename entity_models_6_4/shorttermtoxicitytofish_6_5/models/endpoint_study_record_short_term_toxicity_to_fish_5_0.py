from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.shorttermtoxicitytofish_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E01,
    E02,
    E031,
    E04,
    E05,
    E15,
    E35,
    E102,
    E104,
    E105,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660212,
    Pg660213,
    Pg660466,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0"


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660213] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660212] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[E031] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignTestType:
    class Meta:
        global_type = False

    value: Optional[E01] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignTotalExposureDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignWaterMediaType:
    class Meta:
        global_type = False

    value: Optional[E102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[E02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestSolutionsVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToFishOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryBasisForEffect:
    class Meta:
        global_type = False

    value: Optional[Pg660466] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryConcBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryEffectConc:
    class Meta:
        global_type = False

    unit_code: Optional[E05] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[E104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryNominalMeasured:
    class Meta:
        global_type = False

    value: Optional[E35] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordShortTermToxicityToFishApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordShortTermToxicityToFishDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordShortTermToxicityToFishDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    test_type: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    water_media_type: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignWaterMediaType
    ] = field(
        default=None,
        metadata={
            "name": "WaterMediaType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks_on_exposure_duration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    post_exposure_observation_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostExposureObservationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    hardness: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    ph: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    dissolved_oxygen: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DissolvedOxygen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    salinity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    conductivity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestSolutions:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestSolutionsVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    details_on_test_solutions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordShortTermToxicityToFishOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
            "nillable": True,
        },
    )
    duration: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    effect_conc: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryEffectConc
    ] = field(
        default=None,
        metadata={
            "name": "EffectConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    nominal_measured: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryNominalMeasured
    ] = field(
        default=None,
        metadata={
            "name": "NominalMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    conc_based_on: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryConcBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    test_solutions: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestSolutions
    ] = field(
        default=None,
        metadata={
            "name": "TestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_concentrations: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionEffectConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    results_ref_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsRefSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToFish:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ShortTermToxicityToFish"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToFish/5.0"

    administrative_data: Optional[
        EndpointStudyRecordShortTermToxicityToFishAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordShortTermToxicityToFishDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordShortTermToxicityToFishMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordShortTermToxicityToFishResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordShortTermToxicityToFishOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordShortTermToxicityToFishApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
