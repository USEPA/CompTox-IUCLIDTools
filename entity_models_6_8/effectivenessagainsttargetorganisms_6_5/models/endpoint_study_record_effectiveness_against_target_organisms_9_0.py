from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from effectivenessagainsttargetorganisms_6_5.models.common_types_oecd_v9 import (
    A36,
    C70,
    C109,
    C110,
    C116,
    C118,
    C119,
    C1112,
    N64,
    N78,
    Y143,
    Z02,
    Z03,
    Z05,
    Z30,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660351,
    Pg660860,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from effectivenessagainsttargetorganisms_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0"


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660351] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationGeneralInformationOnEffectivenessModeAction(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C119] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnApplicationOfProductMethodOfApplication(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C118] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnIntendedUseAndApplicationFunctionAddressed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C70] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnIntendedUseAndApplicationProductType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryCommonName(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C110] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryDevelopmentalStage(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C116] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryDevelopmentalStageOfTargetPlant(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660860] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryScientificName(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C109] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationProductsOrganismsOrObjectsToBeProtectedUnderStudy:
    class Meta:
        global_type = False

    organisms_to_be_protected_or_treated_materials: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "OrganismsToBeProtectedOrTreatedMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationGeneralInformationOnEffectiveness:
    class Meta:
        global_type = False

    effects_on_target_organisms: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "EffectsOnTargetOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    mode_action: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationGeneralInformationOnEffectivenessModeAction
    ] = field(
        default=None,
        metadata={
            "name": "ModeAction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    details_on_mode_of_action: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnModeOfAction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    possible_occurrence_of_resistance: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "PossibleOccurrenceOfResistance",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
            },
        )
    )
    management_strategies_to_avoid_resistance: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ManagementStrategiesToAvoidResistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    any_other_known_limitations_and_management_strategies: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "AnyOtherKnownLimitationsAndManagementStrategies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnApplicationOfProduct:
    class Meta:
        global_type = False

    method_of_application: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnApplicationOfProductMethodOfApplication
    ] = field(
        default_factory=list,
        metadata={
            "name": "MethodOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    details_on_application: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnIntendedUseAndApplication:
    class Meta:
        global_type = False

    function_addressed: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnIntendedUseAndApplicationFunctionAddressed
    ] = field(
        default_factory=list,
        metadata={
            "name": "FunctionAddressed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    product_type: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnIntendedUseAndApplicationProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    field_of_use_envisaged_user: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "FieldOfUseEnvisagedUser",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    scientific_name: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryScientificName
    ] = field(
        default=None,
        metadata={
            "name": "ScientificName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    common_name: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryCommonName
    ] = field(
        default=None,
        metadata={
            "name": "CommonName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    developmental_stage: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryDevelopmentalStage
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    developmental_stage_of_target_plant: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntryDevelopmentalStageOfTargetPlant
    ] = field(
        default_factory=list,
        metadata={
            "name": "DevelopmentalStageOfTargetPlant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganisms:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganismsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlled:
    class Meta:
        global_type = False

    target_organisms: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlledTargetOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TargetOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformation:
    class Meta:
        global_type = False

    background_information: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    pest_target_organisms_to_be_controlled: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationPestTargetOrganismsToBeControlled
    ] = field(
        default=None,
        metadata={
            "name": "PestTargetOrganismsToBeControlled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    products_organisms_or_objects_to_be_protected_under_study: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationProductsOrganismsOrObjectsToBeProtectedUnderStudy
    ] = field(
        default=None,
        metadata={
            "name": "ProductsOrganismsOrObjectsToBeProtectedUnderStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    information_on_intended_use_and_application: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnIntendedUseAndApplication
    ] = field(
        default=None,
        metadata={
            "name": "InformationOnIntendedUseAndApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    information_on_application_of_product: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationInformationOnApplicationOfProduct
    ] = field(
        default=None,
        metadata={
            "name": "InformationOnApplicationOfProduct",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    general_information_on_effectiveness: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationGeneralInformationOnEffectiveness
    ] = field(
        default=None,
        metadata={
            "name": "GeneralInformationOnEffectiveness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformationModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussion:
    class Meta:
        global_type = False

    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0",
        },
    )


@dataclass
class EndpointStudyRecordEffectivenessAgainstTargetOrganisms:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EffectivenessAgainstTargetOrganisms"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EffectivenessAgainstTargetOrganisms/9.0"

    administrative_data: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    general_information: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsGeneralInformation
    ] = field(
        default=None,
        metadata={
            "name": "GeneralInformation",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordEffectivenessAgainstTargetOrganismsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
