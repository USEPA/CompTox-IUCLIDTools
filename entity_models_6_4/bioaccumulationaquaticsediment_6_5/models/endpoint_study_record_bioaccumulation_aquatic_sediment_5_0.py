from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.bioaccumulationaquaticsediment_6_5.models.common_types_oecd_v5 import (
    A03,
    A36,
    A102,
    E04,
    E147,
    F34,
    F102,
    F119,
    F120,
    F121,
    F122,
    F123,
    F138,
    F141,
    F142,
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
    Z40,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660150,
    Pg660151,
    Pg660161,
    Pg660171,
    Pg660177,
    Pg660180,
    Td330,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0"


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    details_on_sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Pg660151] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660150] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusionValidityCriteriaFulfilled:
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[F34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignJustificationForMethod:
    class Meta:
        global_type = False

    value: Optional[Pg660180] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignRouteOfExposure:
    class Meta:
        global_type = False

    value: Optional[F142] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTestType:
    class Meta:
        global_type = False

    value: Optional[F122] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalDepurationDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignWaterMediaType:
    class Meta:
        global_type = False

    value: Optional[Pg660161] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl:
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganismsTestOrganismsSpecies:
    class Meta:
        global_type = False

    value: Optional[E147] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutionsVehicle:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryBasis:
    class Meta:
        global_type = False

    value: Optional[F120] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis:
    class Meta:
        global_type = False

    value: Optional[F121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryConcInEnvironmentDose:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660171] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTemp:
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryType:
    class Meta:
        global_type = False

    value: Optional[F141] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryValue:
    class Meta:
        global_type = False

    unit_code: Optional[Td330] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryDepurationTime:
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryElimination:
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryEndpoint:
    class Meta:
        global_type = False

    value: Optional[F123] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryLipidContent:
    class Meta:
        global_type = False

    unit_code: Optional[F119] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryTimePoint:
    class Meta:
        global_type = False

    value: Optional[F138] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRateConstant:
    class Meta:
        global_type = False

    value: Optional[Pg660177] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    route_of_exposure: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignRouteOfExposure
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    justification_for_method: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignJustificationForMethod
    ] = field(
        default=None,
        metadata={
            "name": "JustificationForMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    test_type: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    water_media_type: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignWaterMediaType
    ] = field(
        default=None,
        metadata={
            "name": "WaterMediaType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    total_exposure_uptake_duration: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureUptakeDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    total_depuration_duration: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalDepurationDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalDepurationDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    hardness: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    test_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    ph: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    dissolved_oxygen: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DissolvedOxygen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    toc: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TOC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    salinity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    conductivity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    nominal_and_measured_concentrations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    details_on_estimation_of_bioconcentration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnEstimationOfBioconcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    details_on_test_organisms: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutions:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutionsVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    details_on_preparation_of_test_solutions_spiked_fish_food_or_sediment: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnPreparationOfTestSolutionsSpikedFishFoodOrSediment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    conc_in_environment_dose: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryConcInEnvironmentDose
    ] = field(
        default=None,
        metadata={
            "name": "ConcInEnvironmentDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    ph: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    type_value: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    value: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    basis: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryBasis
    ] = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    time_of_plateau: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau
    ] = field(
        default=None,
        metadata={
            "name": "TimeOfPlateau",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    calculation_basis: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis
    ] = field(
        default=None,
        metadata={
            "name": "CalculationBasis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    elimination: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryElimination
    ] = field(
        default=None,
        metadata={
            "name": "Elimination",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    depuration_time: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryDepurationTime
    ] = field(
        default=None,
        metadata={
            "name": "DepurationTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntry:
    class Meta:
        global_type = False

    lipid_content: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryLipidContent
    ] = field(
        default=None,
        metadata={
            "name": "LipidContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    time_point: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryTimePoint
    ] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    rate_constant: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRateConstant
    ] = field(
        default=None,
        metadata={
            "name": "RateConstant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactor:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepuration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContent:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstants:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    test_solutions: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutions
    ] = field(
        default=None,
        metadata={
            "name": "TestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussion:
    class Meta:
        global_type = False

    lipid_content: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContent
    ] = field(
        default=None,
        metadata={
            "name": "LipidContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    bioaccumulation_factor: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactor
    ] = field(
        default=None,
        metadata={
            "name": "BioaccumulationFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    depuration: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepuration
    ] = field(
        default=None,
        metadata={
            "name": "Depuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    rate_constants: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstants
    ] = field(
        default=None,
        metadata={
            "name": "RateConstants",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    kinetic_parameters: List[str] = field(
        default_factory=list,
        metadata={
            "name": "KineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    metabolites: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Metabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    results_with_reference_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsWithReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    details_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    reported_statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReportedStatistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSediment:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BioaccumulationAquaticSediment"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/5.0"

    administrative_data: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
