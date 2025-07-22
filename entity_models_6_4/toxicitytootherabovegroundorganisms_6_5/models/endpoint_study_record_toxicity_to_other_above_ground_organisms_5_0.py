from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.toxicitytootherabovegroundorganisms_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E04,
    E15,
    E35,
    E105,
    E132,
    E141,
    E262,
    E273,
    E281,
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
    Pg660258,
    Td350,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0"


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660258] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[E273] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesignLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesignStudyType:
    class Meta:
        global_type = False

    value: Optional[E141] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesignTotalExposureDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[E262] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestSubstrateVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect:
    class Meta:
        global_type = False

    value: Optional[E281] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryEffectConc:
    class Meta:
        global_type = False

    unit_code: Optional[Td350] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[E132] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured:
    class Meta:
        global_type = False

    value: Optional[E35] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    study_type: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesignStudyType
    ] = field(
        default=None,
        metadata={
            "name": "StudyType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    post_exposure_observation_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostExposureObservationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    humidity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Humidity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    photoperiod_and_lighting: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhotoperiodAndLighting",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestSubstrate:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestSubstrateVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    details_on_preparation_and_application_of_test_substrate: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnPreparationAndApplicationOfTestSubstrate",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
            "nillable": True,
        },
    )
    duration: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    effect_conc: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryEffectConc
    ] = field(
        default=None,
        metadata={
            "name": "EffectConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    nominal_measured: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured
    ] = field(
        default=None,
        metadata={
            "name": "NominalMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    conc_based_on: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    test_substrate: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestSubstrate
    ] = field(
        default=None,
        metadata={
            "name": "TestSubstrate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_concentrations: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionEffectConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    results_ref_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsRefSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToOtherAboveGroundOrganisms:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ToxicityToOtherAboveGroundOrganisms"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToOtherAboveGroundOrganisms/5.0"

    administrative_data: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordToxicityToOtherAboveGroundOrganismsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
