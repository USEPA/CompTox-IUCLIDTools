from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_5.henryslawconstant_6_5.models.common_types_oecd_v6 import (
    A36,
    A102,
    N64,
    N78,
    P02,
    P100,
    P101,
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
    Pg660182,
)
from entity_models_6_5.henryslawconstant_6_5.models.platform_fields import (
    AttachmentListField,
    BaseDataProtectionField,
    BasePhysicalQuantityField,
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0"


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660182] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[P100] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    details_on_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryAtmPressure(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[P02] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryH(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[P101] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryTemp(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    legislation: List[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordHenrysLawConstantDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordHenrysLawConstantDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordHenrysLawConstantOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    h: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryH
    ] = field(
        default=None,
        metadata={
            "name": "H",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    atm_pressure: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryAtmPressure
    ] = field(
        default=None,
        metadata={
            "name": "AtmPressure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordHenrysLawConstantOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    attached_study_report: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[AttachmentListField] = (
        field(
            default=None,
            metadata={
                "name": "AttachedSanitisedDocsForPublication",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantH:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantHEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstantResultsAndDiscussion:
    class Meta:
        global_type = False

    henrys_law_constant_h: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionHenrysLawConstantH
    ] = field(
        default=None,
        metadata={
            "name": "HenrysLawConstantH",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0",
        },
    )


@dataclass
class EndpointStudyRecordHenrysLawConstant:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.HenrysLawConstant"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-HenrysLawConstant/6.0"

    administrative_data: Optional[
        EndpointStudyRecordHenrysLawConstantAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordHenrysLawConstantDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordHenrysLawConstantMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordHenrysLawConstantResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordHenrysLawConstantOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordHenrysLawConstantApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
