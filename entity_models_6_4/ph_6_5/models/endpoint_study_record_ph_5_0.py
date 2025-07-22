from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.ph_6_5.models.common_types_oecd_v5 import (
    A36,
    A102,
    N64,
    N78,
    P08,
    P114,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660098,
    Pg660107,
    Pg660115,
)

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0"
)


@dataclass
class EndpointStudyRecordPhApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsTitrationOfAcidityAndAlkalinity:
    class Meta:
        global_type = False

    details_on_titrant_used: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTitrantUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryValue:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionPhValueEntryValue:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660098] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[P114] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsOtherQualityAssurance:
    class Meta:
        global_type = False

    value: Optional[Pg660008] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsReagentsReagent:
    class Meta:
        global_type = False

    value: Optional[Pg660115] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryAcidityOrAlkalinity:
    class Meta:
        global_type = False

    value: Optional[Pg660107] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionPhValueEntryConcentration:
    class Meta:
        global_type = False

    unit_code: Optional[P08] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionPhValueEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionPhValueEntryTemp:
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordPhAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordPhAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    data_access: Optional[EndpointStudyRecordPhDataSourceDataAccess] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordPhDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsReagents:
    class Meta:
        global_type = False

    reagent: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsReagentsReagent
    ] = field(
        default=None,
        metadata={
            "name": "Reagent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            "nillable": True,
        },
    )
    acidity_or_alkalinity: Optional[
        EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryAcidityOrAlkalinity
    ] = field(
        default=None,
        metadata={
            "name": "AcidityOrAlkalinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    value: Optional[
        EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionPhValueEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            "nillable": True,
        },
    )
    value: Optional[
        EndpointStudyRecordPhResultsAndDiscussionPhValueEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordPhResultsAndDiscussionPhValueEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    concentration: Optional[
        EndpointStudyRecordPhResultsAndDiscussionPhValueEntryConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordPhResultsAndDiscussionPhValueEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[EndpointStudyRecordPhAdministrativeDataCrossReferenceEntry] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntry] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussionPhValue:
    class Meta:
        global_type = False

    entry: List[EndpointStudyRecordPhResultsAndDiscussionPhValueEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordPhAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    endpoint: Optional[EndpointStudyRecordPhAdministrativeDataEndpoint] = (
        field(
            default=None,
            metadata={
                "name": "Endpoint",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            },
        )
    )
    study_result_type: Optional[
        EndpointStudyRecordPhAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordPhAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordPhAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordPhAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordPhAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordPhAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordPhAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordPhAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[EndpointStudyRecordPhMaterialsAndMethodsGuideline] = (
        field(
            default=None,
            metadata={
                "name": "Guideline",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            },
        )
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    other_quality_assurance: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsOtherQualityAssurance
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityAssurance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    reagents: Optional[EndpointStudyRecordPhMaterialsAndMethodsReagents] = (
        field(
            default=None,
            metadata={
                "name": "Reagents",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            },
        )
    )
    titration_of_acidity_and_alkalinity: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsTitrationOfAcidityAndAlkalinity
    ] = field(
        default=None,
        metadata={
            "name": "TitrationOfAcidityAndAlkalinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordPhMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPhResultsAndDiscussion:
    class Meta:
        global_type = False

    ph_value: Optional[EndpointStudyRecordPhResultsAndDiscussionPhValue] = (
        field(
            default=None,
            metadata={
                "name": "phValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
            },
        )
    )
    acidity_or_alkalinity: Optional[
        EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinity
    ] = field(
        default=None,
        metadata={
            "name": "AcidityOrAlkalinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordPhResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0",
        },
    )


@dataclass
class EndpointStudyRecordPh:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.Ph"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-Ph/5.0"

    administrative_data: Optional[EndpointStudyRecordPhAdministrativeData] = (
        field(
            default=None,
            metadata={
                "name": "AdministrativeData",
                "type": "Element",
            },
        )
    )
    data_source: Optional[EndpointStudyRecordPhDataSource] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordPhMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordPhResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordPhOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordPhApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
