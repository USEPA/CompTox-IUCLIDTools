from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.toxicitytoterrestrialarthropods_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E04,
    E15,
    E22,
    E35,
    E105,
    E118,
    E130,
    E141,
    E144,
    E202,
    E272,
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
    Pg660240,
    Pg660247,
    Td350,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0"


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660240] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660247] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsApplicationMethod:
    class Meta:
        global_type = False

    value: Optional[E144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[E272] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesignLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesignStudyType:
    class Meta:
        global_type = False

    value: Optional[E141] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesignTotalExposureDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestOrganismsAnimalGroup:
    class Meta:
        global_type = False

    value: Optional[E130] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[E202] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestSubstrateVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect:
    class Meta:
        global_type = False

    value: Optional[E22] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryEffectConc:
    class Meta:
        global_type = False

    unit_code: Optional[Td350] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[E118] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured:
    class Meta:
        global_type = False

    value: Optional[E35] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    study_type: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesignStudyType
    ] = field(
        default=None,
        metadata={
            "name": "StudyType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    post_exposure_observation_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostExposureObservationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    ph_if_soil_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhIfSoilStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    humidity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Humidity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    photoperiod_and_lighting: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhotoperiodAndLighting",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    animal_group: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestOrganismsAnimalGroup
    ] = field(
        default=None,
        metadata={
            "name": "AnimalGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestSubstrate:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestSubstrateVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    details_on_preparation_and_application_of_test_substrate: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnPreparationAndApplicationOfTestSubstrate",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
            "nillable": True,
        },
    )
    duration: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    effect_conc: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryEffectConc
    ] = field(
        default=None,
        metadata={
            "name": "EffectConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    nominal_measured: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured
    ] = field(
        default=None,
        metadata={
            "name": "NominalMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    conc_based_on: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    application_method: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsApplicationMethod
    ] = field(
        default=None,
        metadata={
            "name": "ApplicationMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    test_substrate: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestSubstrate
    ] = field(
        default=None,
        metadata={
            "name": "TestSubstrate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_concentrations: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionEffectConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    results_ref_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsRefSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToTerrestrialArthropods:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ToxicityToTerrestrialArthropods"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToTerrestrialArthropods/5.0"

    administrative_data: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordToxicityToTerrestrialArthropodsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
