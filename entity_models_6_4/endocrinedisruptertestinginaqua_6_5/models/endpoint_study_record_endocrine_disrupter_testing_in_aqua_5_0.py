from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.endocrinedisruptertestinginaqua_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E01,
    E05,
    E15,
    E35,
    E102,
    E105,
    E115B,
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
    Pg660220,
    Pg660438,
    Pg660439,
    Pg660440,
    Pg660441,
    Pg660442,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0"


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660438] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Pg660439] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignLimitTest:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignTestType:
    class Meta:
        global_type = False

    value: Optional[E01] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignTotalExposureDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignWaterMediaType:
    class Meta:
        global_type = False

    value: Optional[E102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestOrganismsAquaticVertebrateType:
    class Meta:
        global_type = False

    value: Optional[Pg660440] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[Pg660441] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestSolutionsVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryBasisForEffect:
    class Meta:
        global_type = False

    value: Optional[Pg660442] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryConcBasedOn:
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryEffectConc:
    class Meta:
        global_type = False

    unit_code: Optional[E05] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[E115B] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryNominalMeasured:
    class Meta:
        global_type = False

    value: Optional[E35] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660220] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    test_type: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    water_media_type: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignWaterMediaType
    ] = field(
        default=None,
        metadata={
            "name": "WaterMediaType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks_on_exposure_duration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    post_exposure_observation_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostExposureObservationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    hardness: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    ph: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    dissolved_oxygen: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DissolvedOxygen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    salinity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    conductivity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    aquatic_vertebrate_type: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestOrganismsAquaticVertebrateType
    ] = field(
        default=None,
        metadata={
            "name": "AquaticVertebrateType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    test_organisms_species: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestSolutions:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestSolutionsVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    details_on_test_solutions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
            "nillable": True,
        },
    )
    duration: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    effect_conc: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryEffectConc
    ] = field(
        default=None,
        metadata={
            "name": "EffectConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    nominal_measured: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryNominalMeasured
    ] = field(
        default=None,
        metadata={
            "name": "NominalMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    conc_based_on: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryConcBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    test_solutions: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestSolutions
    ] = field(
        default=None,
        metadata={
            "name": "TestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_concentrations: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionEffectConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    results_ref_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsRefSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterTestingInAqua:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EndocrineDisrupterTestingInAqua"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterTestingInAqua/5.0"

    administrative_data: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordEndocrineDisrupterTestingInAquaApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
