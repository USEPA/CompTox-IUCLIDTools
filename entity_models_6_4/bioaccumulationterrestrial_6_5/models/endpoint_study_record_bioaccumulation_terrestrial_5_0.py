from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.bioaccumulationterrestrial_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    E04,
    E148,
    F102,
    F119,
    F120,
    F121,
    F123,
    F133,
    F138,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660185,
    Pg660186,
    Td330,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0"


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    ph: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    toc: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TOC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    moisture: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Moisture",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    details_on_test_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660185] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Pg660186] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalDepurationDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[E148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrateVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryBasis:
    class Meta:
        global_type = False

    value: Optional[F120] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis:
    class Meta:
        global_type = False

    value: Optional[F121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryType:
    class Meta:
        global_type = False

    value: Optional[F133] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryValue:
    class Meta:
        global_type = False

    unit_code: Optional[Td330] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryDepurationTime:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryElimination:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[F123] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryLipidContent:
    class Meta:
        global_type = False

    unit_code: Optional[F119] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryTimePoint:
    class Meta:
        global_type = False

    value: Optional[F138] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    total_exposure_uptake_duration: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureUptakeDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    total_depuration_duration: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalDepurationDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalDepurationDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrate:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrateVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    details_on_preparation_and_application_of_test_substrate: List[str] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnPreparationAndApplicationOfTestSubstrate",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
            "nillable": True,
        },
    )
    type_value: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    value: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    basis: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryBasis
    ] = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    time_of_plateau: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau
    ] = field(
        default=None,
        metadata={
            "name": "TimeOfPlateau",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    calculation_basis: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis
    ] = field(
        default=None,
        metadata={
            "name": "CalculationBasis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
            "nillable": True,
        },
    )
    elimination: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryElimination
    ] = field(
        default=None,
        metadata={
            "name": "Elimination",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    depuration_time: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryDepurationTime
    ] = field(
        default=None,
        metadata={
            "name": "DepurationTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntry:
    class Meta:
        global_type = False

    lipid_content: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryLipidContent
    ] = field(
        default=None,
        metadata={
            "name": "LipidContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    time_point: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryTimePoint
    ] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactor:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepuration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContent:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    test_substrate: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrate
    ] = field(
        default=None,
        metadata={
            "name": "TestSubstrate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussion:
    class Meta:
        global_type = False

    lipid_content: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContent
    ] = field(
        default=None,
        metadata={
            "name": "LipidContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    bioaccumulation_factor: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactor
    ] = field(
        default=None,
        metadata={
            "name": "BioaccumulationFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    depuration: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepuration
    ] = field(
        default=None,
        metadata={
            "name": "Depuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    kinetic_parameters: List[str] = field(
        default_factory=list,
        metadata={
            "name": "KineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    metabolites: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Metabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    reported_statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReportedStatistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationTerrestrial:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BioaccumulationTerrestrial"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationTerrestrial/5.0"

    administrative_data: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
