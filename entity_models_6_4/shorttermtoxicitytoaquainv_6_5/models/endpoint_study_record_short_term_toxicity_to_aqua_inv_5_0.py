from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.shorttermtoxicitytoaquainv_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E01,
    E04,
    E05,
    E06,
    E07,
    E15,
    E35,
    E102,
    E103,
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
    Pg660223,
    Pg660224,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0"


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660224] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660223] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[E07] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignTestType:
    class Meta:
        global_type = False

    value: Optional[E01] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignTotalExposureDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignWaterMediaType:
    class Meta:
        global_type = False

    value: Optional[E102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[E06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestSolutionsVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToAquaInvOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryBasisForEffect:
    class Meta:
        global_type = False

    value: Optional[E103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryConcBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryEffectConc:
    class Meta:
        global_type = False

    unit_code: Optional[E05] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[E104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryNominalMeasured:
    class Meta:
        global_type = False

    value: Optional[E35] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    test_type: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    water_media_type: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignWaterMediaType
    ] = field(
        default=None,
        metadata={
            "name": "WaterMediaType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks_on_exposure_duration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    post_exposure_observation_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostExposureObservationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    hardness: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    ph: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    dissolved_oxygen: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DissolvedOxygen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    salinity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    conductivity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestSolutions:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestSolutionsVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    details_on_test_solutions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
            "nillable": True,
        },
    )
    duration: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    effect_conc: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryEffectConc
    ] = field(
        default=None,
        metadata={
            "name": "EffectConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    nominal_measured: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryNominalMeasured
    ] = field(
        default=None,
        metadata={
            "name": "NominalMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    conc_based_on: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryConcBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    test_solutions: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestSolutions
    ] = field(
        default=None,
        metadata={
            "name": "TestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_concentrations: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionEffectConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    results_ref_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsRefSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0",
        },
    )


@dataclass
class EndpointStudyRecordShortTermToxicityToAquaInv:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ShortTermToxicityToAquaInv"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ShortTermToxicityToAquaInv/5.0"

    administrative_data: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordShortTermToxicityToAquaInvApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
