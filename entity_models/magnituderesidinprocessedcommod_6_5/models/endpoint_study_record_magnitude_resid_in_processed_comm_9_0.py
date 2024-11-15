from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from magnituderesidinprocessedcommod_6_5.models.common_types_oecd_v9 import (
    A36,
    C1112,
    N21,
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
    Pg660493,
    Pg660495,
    Pg660497,
    Pg660560,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Pg6604962,
)
from magnituderesidinprocessedcommod_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0"


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660493] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660495] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsProductType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsSamplingAndAnalyticalMethodology:
    class Meta:
        global_type = False

    details_on_sample_collection: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    details_on_sample_handling_and_preparation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleHandlingAndPreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    details_on_analytical_methodology: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnAnalyticalMethodology",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsStudyDesignBulkRawAgriculturalCommodity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660560] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryCorrectionByRecovery(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryCorrectionByStorageStability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryResidueLevelCalculated(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryResidueLevelCalculatedAndCorrected(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryResidueLevelMeasured(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryCorrectionByRecovery(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryCorrectionByStorageStability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryResidueLevelCalculated(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryResidueLevelCalculatedAndCorrected(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryResidueLevelMeasured(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryProcessedFractionPfsample(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660497] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryCorrectionByRecovery(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryCorrectionByStorageStability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryResidueLevelCalculated(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryResidueLevelCalculatedAndCorrected(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryResidueLevelMeasured(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604962] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    bulk_raw_agricultural_commodity: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsStudyDesignBulkRawAgriculturalCommodity
    ] = field(
        default=None,
        metadata={
            "name": "BulkRawAgriculturalCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    details_on_test_commodity: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    sample_processing: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "SampleProcessing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    further_details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "FurtherDetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    storage_stability_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StorageStabilityFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    use_of_factor: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "UseOfFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    correction_by_storage_stability: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryCorrectionByStorageStability
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    correction_by_recovery: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryCorrectionByRecovery
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_measured: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryResidueLevelMeasured
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_calculated: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryResidueLevelCalculated
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_calculated_and_corrected: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntryResidueLevelCalculatedAndCorrected
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculatedAndCorrected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    storage_stability_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StorageStabilityFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    use_of_factor: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "UseOfFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    correction_by_storage_stability: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryCorrectionByStorageStability
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    correction_by_recovery: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryCorrectionByRecovery
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    reference_portion: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ReferencePortion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_measured: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryResidueLevelMeasured
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_calculated: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryResidueLevelCalculated
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_calculated_and_corrected: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntryResidueLevelCalculatedAndCorrected
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculatedAndCorrected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    storage_stability_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StorageStabilityFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    use_of_factor: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "UseOfFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    correction_by_storage_stability: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryCorrectionByStorageStability
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    correction_by_recovery: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryCorrectionByRecovery
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    reference_portion: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ReferencePortion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_measured: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryResidueLevelMeasured
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_calculated: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryResidueLevelCalculated
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residue_level_calculated_and_corrected: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntryResidueLevelCalculatedAndCorrected
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculatedAndCorrected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasured:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasuredEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasured:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasuredEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasured:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasuredEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethods:
    class Meta:
        global_type = False

    product_type: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    sampling_and_analytical_methodology: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsSamplingAndAnalyticalMethodology
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    agfanalysis_sample: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AGFAnalysisSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    date_of_agfsample: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfAGFSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    analysis_sample_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    analyte_measured: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntryAnalyteMeasured
    ] = field(
        default=None,
        metadata={
            "name": "AnalyteMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    processed_fraction_pfsample: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryProcessedFractionPfsample
    ] = field(
        default=None,
        metadata={
            "name": "ProcessedFractionPFSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    pfsample_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "PFSampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    date_of_processing: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfProcessing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    analysis_sample_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    analysis_sample_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisSampleDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    analyte_measured: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntryAnalyteMeasured
    ] = field(
        default=None,
        metadata={
            "name": "AnalyteMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    date_of_sub_sample: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfSubSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
            "nillable": True,
        },
    )
    analysis_sample_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    analysis_sample_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisSampleDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    analyte_measured: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntryAnalyteMeasured
    ] = field(
        default=None,
        metadata={
            "name": "AnalyteMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsample:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsampleEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFraction:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFractionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNo:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNoEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgf:
    class Meta:
        global_type = False

    processing_information: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ProcessingInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    processed_fraction: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfProcessedFraction
    ] = field(
        default=None,
        metadata={
            "name": "ProcessedFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    aspirated_grain_fractions_agfsample: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgfAspiratedGrainFractionsAgfsample
    ] = field(
        default=None,
        metadata={
            "name": "AspiratedGrainFractionsAGFSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    distribution_of_residues: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DistributionOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessing:
    class Meta:
        global_type = False

    bulk_racsub_sample_sample_no: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessingBulkRacsubSampleSampleNo
    ] = field(
        default=None,
        metadata={
            "name": "BulkRACSubSampleSampleNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussion:
    class Meta:
        global_type = False

    storage_stability_of_residues_sample_integrity: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "StorageStabilityOfResiduesSampleIntegrity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residues_in_racprior_to_processing: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInRacpriorToProcessing
    ] = field(
        default=None,
        metadata={
            "name": "ResiduesInRACPriorToProcessing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    residues_in_processed_fractions_pfand_aspirated_grain_fractions_agf: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionResiduesInProcessedFractionsPfandAspiratedGrainFractionsAgf
    ] = field(
        default=None,
        metadata={
            "name": "ResiduesInProcessedFractionsPFAndAspiratedGrainFractionsAGF",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMagnitudeResidInProcessedComm:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.MagnitudeResidInProcessedComm"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MagnitudeResidInProcessedComm/9.0"

    administrative_data: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordMagnitudeResidInProcessedCommApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
