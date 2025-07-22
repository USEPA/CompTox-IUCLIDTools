from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_8.surfacechemistry_6_5.models.common_types_oecd_v9 import (
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
    Nm09,
    Nm10,
    Nm11,
    Nm12,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660342,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Pg661700,
    Pg661701,
    Pg661702,
)
from entity_models_6_8.surfacechemistry_6_5.models.platform_fields import (
    BaseDataProtectionField,
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0"


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660342] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsDataGathering:
    class Meta:
        global_type = False

    instruments: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Instruments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    specific_details_on_instruments_and_instruments_settings_measurements: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnInstrumentsAndInstrumentsSettingsMeasurements",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    calibration: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    reproducibility: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Reproducibility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661700] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsMethodType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm09] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsOtherQualityAssurance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsTestMaterialsReferenceMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reference_material_nanomaterial: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterialNanomaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    sample_identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleIdentificationNumber",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingFunctionalisation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm10] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicCompositionEntryFraction(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicCompositionEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingCoating(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntryFraction(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntryGroup(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Nm11] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndexEntryHydrophobicityIndex(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndexEntryRemarksOnResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityQualitativeHydrophobicity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661702] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionSurfaceCharge(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661701] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordSurfaceChemistryDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordSurfaceChemistryDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsTestMaterialsReferenceMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsTestMaterialsReferenceMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordSurfaceChemistryOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicCompositionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    element: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    fraction: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicCompositionEntryFraction
    ] = field(
        default=None,
        metadata={
            "name": "Fraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicCompositionEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    group: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntryGroup
    ] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    fraction: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntryFraction
    ] = field(
        default=None,
        metadata={
            "name": "Fraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndexEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    hydrophobicity_index: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndexEntryHydrophobicityIndex
    ] = field(
        default=None,
        metadata={
            "name": "HydrophobicityIndex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    st_dev: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StDev",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndexEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    reference_material: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsTestMaterialsReferenceMaterial
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicComposition:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicCompositionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroup:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroupEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndex:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndexEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    method_type: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsMethodType
    ] = field(
        default=None,
        metadata={
            "name": "MethodType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    specific_details_on_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    details_on_methods_and_data_evaluation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMethodsAndDataEvaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Sampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    specific_details_on_sample_preparation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnSamplePreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    data_gathering: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsDataGathering
    ] = field(
        default=None,
        metadata={
            "name": "DataGathering",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordSurfaceChemistryOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoating:
    class Meta:
        global_type = False

    coating: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingCoating
    ] = field(
        default=None,
        metadata={
            "name": "Coating",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    coating_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CoatingDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    atomic_composition: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingAtomicComposition
    ] = field(
        default=None,
        metadata={
            "name": "AtomicComposition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisation:
    class Meta:
        global_type = False

    functionalisation_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "FunctionalisationDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    functional_group: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisationFunctionalGroup
    ] = field(
        default=None,
        metadata={
            "name": "FunctionalGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicity:
    class Meta:
        global_type = False

    qualitative_hydrophobicity: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityQualitativeHydrophobicity
    ] = field(
        default=None,
        metadata={
            "name": "QualitativeHydrophobicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    hydrophobicity_index: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicityHydrophobicityIndex
    ] = field(
        default=None,
        metadata={
            "name": "HydrophobicityIndex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistryResultsAndDiscussion:
    class Meta:
        global_type = False

    coating_functionalisation: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoatingFunctionalisation
    ] = field(
        default=None,
        metadata={
            "name": "CoatingFunctionalisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    surface_charge: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionSurfaceCharge
    ] = field(
        default=None,
        metadata={
            "name": "SurfaceCharge",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    coating: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionCoating
    ] = field(
        default=None,
        metadata={
            "name": "Coating",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    functionalisation: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionFunctionalisation
    ] = field(
        default=None,
        metadata={
            "name": "Functionalisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    hydrophobicity: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionHydrophobicity
    ] = field(
        default=None,
        metadata={
            "name": "Hydrophobicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0",
        },
    )


@dataclass
class EndpointStudyRecordSurfaceChemistry:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.SurfaceChemistry"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SurfaceChemistry/9.0"

    administrative_data: Optional[
        EndpointStudyRecordSurfaceChemistryAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordSurfaceChemistryDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordSurfaceChemistryMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordSurfaceChemistryResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordSurfaceChemistryOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordSurfaceChemistryApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
