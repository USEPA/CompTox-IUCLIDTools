from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.radicalformationpotential_6_5.models.common_types_oecd_v5 import (
    A36,
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
    Nm33,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660347,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0"


@dataclass
class EndpointStudyRecordRadicalFormationPotentialApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsDataGathering:
    class Meta:
        global_type = False

    instruments: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Instruments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    calibration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    reproducibility: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Reproducibility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsTestMaterialsReferenceMaterialEntry:
    class Meta:
        global_type = False

    reference_material_nanomaterial: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterialNanomaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    sample_identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleIdentificationNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussionRadicalFormationPotentialEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
            "nillable": True,
        },
    )
    description_observations: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    quantitative_description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "QuantitativeDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660347] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsMethodType:
    class Meta:
        global_type = False

    value: Optional[Nm33] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsOtherQualityAssurance:
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsTestMaterialsReferenceMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsTestMaterialsReferenceMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRadicalFormationPotentialOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussionRadicalFormationPotential:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussionRadicalFormationPotentialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordRadicalFormationPotentialDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordRadicalFormationPotentialDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    reference_material: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsTestMaterialsReferenceMaterial
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordRadicalFormationPotentialOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussion:
    class Meta:
        global_type = False

    radical_formation_potential: Optional[
        EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussionRadicalFormationPotential
    ] = field(
        default=None,
        metadata={
            "name": "RadicalFormationPotential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    method_type: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsMethodType
    ] = field(
        default=None,
        metadata={
            "name": "MethodType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    details_on_methods_and_data_evaluation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMethodsAndDataEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    sampling: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Sampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    data_gathering: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsDataGathering
    ] = field(
        default=None,
        metadata={
            "name": "DataGathering",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0",
        },
    )


@dataclass
class EndpointStudyRecordRadicalFormationPotential:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.RadicalFormationPotential"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RadicalFormationPotential/5.0"

    administrative_data: Optional[
        EndpointStudyRecordRadicalFormationPotentialAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordRadicalFormationPotentialDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordRadicalFormationPotentialMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordRadicalFormationPotentialResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordRadicalFormationPotentialOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordRadicalFormationPotentialApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
