from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from stabilityofresiduesinstoredcommod_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    C1112,
    E34,
    F05,
    F137,
    N64,
    N78,
    T148,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    EuPpp61075,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660492,
    Pg660494,
    Pg660561,
    Pg661153,
    Pg661157,
    Pg661166,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Pg6604961,
)
from stabilityofresiduesinstoredcommod_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePhysicalQuantityField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0"


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660492] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660494] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsProductType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsSamplingAndAnalyticalMethodology:
    class Meta:
        global_type = False

    details_on_sample_collection: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    details_on_sample_handling_and_preparation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleHandlingAndPreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    details_on_analytical_methodology: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnAnalyticalMethodology",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignCommodity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660561] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignDurationOfStorage(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[F05] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignOtherStorageConditions(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661153] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignStorageTemperature(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformationEntryMaximumOccurrence(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661166] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformationEntryNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryMeanResidueLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryProceduralRecoveryEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    control_sample_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ControlSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    procedural_recovery_control: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ProceduralRecoveryControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevelEntryResidueLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryFortifRateStoredSample(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryStoragePeriod(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[EuPpp61075] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryTestCommodity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660561] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionTransformationProducts(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    commodity: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignCommodity
    ] = field(
        default_factory=list,
        metadata={
            "name": "Commodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    details_on_stored_commodities: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStoredCommodities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    storage_temperature: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignStorageTemperature
    ] = field(
        default=None,
        metadata={
            "name": "StorageTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    duration_of_storage: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignDurationOfStorage
    ] = field(
        default=None,
        metadata={
            "name": "DurationOfStorage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other_storage_conditions: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesignOtherStorageConditions
    ] = field(
        default_factory=list,
        metadata={
            "name": "OtherStorageConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    no: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformationEntryNo
    ] = field(
        default=None,
        metadata={
            "name": "No",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    reference_substance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    parent_compound_s: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "ParentCompoundS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    maximum_occurrence: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformationEntryMaximumOccurrence
    ] = field(
        default=None,
        metadata={
            "name": "MaximumOccurrence",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryProceduralRecovery:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryProceduralRecoveryEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    analysed_sample_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AnalysedSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    residue_level: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevelEntryResidueLevel
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    residue_level_of_nominal_spiking_level: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ResidueLevelOfNominalSpikingLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethods:
    class Meta:
        global_type = False

    product_type: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    sampling_and_analytical_methodology: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsSamplingAndAnalyticalMethodology
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            "nillable": True,
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    residue_level: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryResidueLevel
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    mean_residue_level: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryMeanResidueLevel
    ] = field(
        default=None,
        metadata={
            "name": "MeanResidueLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    mean_residue_level_of_nominal_spiking_level: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MeanResidueLevelOfNominalSpikingLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    procedural_recovery: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntryProceduralRecovery
    ] = field(
        default=None,
        metadata={
            "name": "ProceduralRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    mean_procedural_recovery_control: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MeanProceduralRecoveryControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasured:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasuredEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    test_commodity: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryTestCommodity
    ] = field(
        default=None,
        metadata={
            "name": "TestCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    other_details_on_test_commodity: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "OtherDetailsOnTestCommodity",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            },
        )
    )
    fortification_date_day0: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FortificationDateDay0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            "nillable": True,
        },
    )
    storage_removal_date_day_x: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StorageRemovalDateDayX",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
            "nillable": True,
        },
    )
    analysis_sample_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisSampleID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    analysis_sample_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisSampleDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    storage_period: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryStoragePeriod
    ] = field(
        default=None,
        metadata={
            "name": "StoragePeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    fortif_rate_stored_sample: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryFortifRateStoredSample
    ] = field(
        default=None,
        metadata={
            "name": "FortifRateStoredSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    analyte_measured: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntryAnalyteMeasured
    ] = field(
        default=None,
        metadata={
            "name": "AnalyteMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevels:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevelsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussion:
    class Meta:
        global_type = False

    residue_levels: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionResidueLevels
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    storage_stability: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    transformation_products: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionTransformationProducts
    ] = field(
        default=None,
        metadata={
            "name": "TransformationProducts",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    identity_transformation: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionIdentityTransformation
    ] = field(
        default=None,
        metadata={
            "name": "IdentityTransformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0",
        },
    )


@dataclass
class EndpointStudyRecordStabilityOfResiduesInStoredCommod:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.StabilityOfResiduesInStoredCommod"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-StabilityOfResiduesInStoredCommod/9.0"

    administrative_data: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordStabilityOfResiduesInStoredCommodApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
