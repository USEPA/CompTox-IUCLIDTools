from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from metabolisminlivestock_6_5.models.common_types_oecd_v9 import (
    A36,
    C1112,
    F137,
    N21,
    N64,
    N78,
    T24,
    T25,
    T148,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z28,
    Z30,
    Z40,
    Z41,
    Z46,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660286,
    Pg660473,
    Pg660474,
    Pg660475,
    Pg660476,
    Pg660480,
    Pg660481,
    Pg660483,
    Pg660484,
    Pg660490,
    Pg660514,
    Pg660515,
    Pg660516,
    Pg660517,
    Pg660518,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from metabolisminlivestock_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0"


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660286] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegimeEntryDosingRegimeNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegimeEntryRouteOfAdministration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryDoseMeasured(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660514] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryDoseNominal(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660514] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryDoseType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660515] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryMatrix(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660476] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryRouteOfAdministration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z46] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsProductType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    illustration_picture_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPictureGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollectionEntrySampleInformationNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollectionEntryTypeOfSamplesCollected(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660483] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntryAnimalInformationNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntryScientificName(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntrySpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z28] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegimeEntryDietaryRegimeNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegimeEntryPredosing(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[N21] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiochemicalPurity(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiolabelNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityAsReceived(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660474] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityOfDose(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660474] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTypeOfStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z41] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryExpertise(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660517] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryIdno(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTreatmentGroupsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    treatment_group_test_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TreatmentGroupTestNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTypeOfExpertise(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660518] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryMetaboliteFraction(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660480] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryRadiolabelNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryMatrix(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660476] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryRemarksOnResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrr(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrrppm(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudyEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    identity_of_compound: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditionsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    matrix_racor_extract: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "MatrixRACOrExtract",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    storage_temperature: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StorageTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    actual_study_duration: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ActualStudyDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    interval_limit_of_demonstrated_storage_stability: List[
        MultilingualTextFieldSmall
    ] = field(
        default_factory=list,
        metadata={
            "name": "IntervalLimitOfDemonstratedStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryMetaboliteFraction(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660481] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryRadiolabelNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryMatrix(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660476] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryRemarksOnResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrr(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrrppm(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueExtractionEfficiency(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueMgKg(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryOverallExtractionEfficiency(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryRecoveredEquivalentsMgKg(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryTypeOfMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660473] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesGraphicalPlotOfTrrsAsAfunctionOfTimeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    illustration_picture_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPictureGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryRadiolabelNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryMatrix(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660476] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryRemarksOnResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrr(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrrppm(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryRadiolabelNo(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntryRemarksOnResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntryTrrofDose(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntryTrrppm(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTypeOfSamples(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660483] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsReachedPlateauAtEndOfDosing(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660484] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordMetabolismInLivestockDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordMetabolismInLivestockDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegimeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    dosing_regime_no: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegimeEntryDosingRegimeNo
    ] = field(
        default=None,
        metadata={
            "name": "DosingRegimeNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    route_of_administration: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegimeEntryRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    treatment_level: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TreatmentLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    vehicle: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    parameters: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Parameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    dosing: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Dosing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    timing_duration: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TimingDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    timing_from_final_dose_to_sacrifice: List[MultilingualTextFieldSmall] = (
        field(
            default_factory=list,
            metadata={
                "name": "TimingFromFinalDoseToSacrifice",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    treatment_group: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TreatmentGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    route_of_administration: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    dose_nominal: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryDoseNominal
    ] = field(
        default=None,
        metadata={
            "name": "DoseNominal",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    dose_measured: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryDoseMeasured
    ] = field(
        default=None,
        metadata={
            "name": "DoseMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    matrix: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryMatrix
    ] = field(
        default=None,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    test_duration: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TestDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    experimental_descriptor: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalDescriptor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    dose_type: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntryDoseType
    ] = field(
        default=None,
        metadata={
            "name": "DoseType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    frequency_on_every: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOnEvery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    duration_of_treatment: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    reference_citation: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "ReferenceCitation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    radiolabel_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    animal_information_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnimalInformationNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    dietary_regime_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "DietaryRegimeNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    dosing_regime_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "DosingRegimeNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    sample_information_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleInformationNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemes:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollectionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    sample_information_no: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollectionEntrySampleInformationNo
    ] = field(
        default=None,
        metadata={
            "name": "SampleInformationNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    type_of_samples_collected: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollectionEntryTypeOfSamplesCollected
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfSamplesCollected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    frequency_of_sample_collection: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfSampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    amount_number_produced_during_normal_production: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmountNumberProducedDuringNormalProduction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    excreta_and_cage_wash_collected: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "ExcretaAndCageWashCollected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    interval_from_last_dose_to_sacrifice: List[MultilingualTextFieldSmall] = (
        field(
            default_factory=list,
            metadata={
                "name": "IntervalFromLastDoseToSacrifice",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            },
        )
    )
    corresponding_dose_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrespondingDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    tissues_harvested_and_analyzed: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TissuesHarvestedAndAnalyzed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    animal_information_no: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntryAnimalInformationNo
    ] = field(
        default=None,
        metadata={
            "name": "AnimalInformationNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    species: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntrySpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    scientific_name: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntryScientificName
    ] = field(
        default=None,
        metadata={
            "name": "ScientificName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    age: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    weight_at_study_initiation_kg: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "WeightAtStudyInitiationKg",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    health_status_condition_of_animals: List[MultilingualTextFieldSmall] = (
        field(
            default_factory=list,
            metadata={
                "name": "HealthStatusConditionOfAnimals",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            },
        )
    )
    health_status: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "HealthStatus",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    description_of_housing_holding_area: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionOfHousingHoldingArea",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegimeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    dietary_regime_no: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegimeEntryDietaryRegimeNo
    ] = field(
        default=None,
        metadata={
            "name": "DietaryRegimeNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    composition_of_diet: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CompositionOfDiet",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    feed_consumption: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "FeedConsumption",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    water: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Water",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    acclimation_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AcclimationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    predosing: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegimeEntryPredosing
    ] = field(
        default=None,
        metadata={
            "name": "Predosing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    smilesnotation: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SMILESNotation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    radiochemical_purity: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiochemicalPurity
    ] = field(
        default=None,
        metadata={
            "name": "RadiochemicalPurity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    specific_activity_as_received: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityAsReceived
    ] = field(
        default=None,
        metadata={
            "name": "SpecificActivityAsReceived",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    specific_activity_of_dose: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityOfDose
    ] = field(
        default=None,
        metadata={
            "name": "SpecificActivityOfDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTreatmentGroups:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTreatmentGroupsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    matrix: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryMatrix
    ] = field(
        default=None,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks_on_result: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryRemarksOnResult
    ] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudy:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudyEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditions:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditionsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    matrix: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryMatrix
    ] = field(
        default=None,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_of_method: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryTypeOfMethod
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    recovered_equivalents_mg_kg: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryRecoveredEquivalentsMgKg
    ] = field(
        default=None,
        metadata={
            "name": "RecoveredEquivalentsMgKg",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    overall_extraction_efficiency: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryOverallExtractionEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "OverallExtractionEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    defined_residue_mg_kg: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueMgKg
    ] = field(
        default=None,
        metadata={
            "name": "DefinedResidueMgKg",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    defined_residue_extraction_efficiency: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueExtractionEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "DefinedResidueExtractionEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesGraphicalPlotOfTrrsAsAfunctionOfTime:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesGraphicalPlotOfTrrsAsAfunctionOfTimeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    matrix: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryMatrix
    ] = field(
        default=None,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    interval: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Interval",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrof_dose: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntryTrrofDose
    ] = field(
        default=None,
        metadata={
            "name": "TRROfDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegime:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegimeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroup:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollection:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollectionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegime:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegimeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    idno: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryIdno
    ] = field(
        default=None,
        metadata={
            "name": "IDNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    identity_of_compound: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    parent_compound_s: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "ParentCompoundS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    treatment_groups: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    expertise: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryExpertise
    ] = field(
        default=None,
        metadata={
            "name": "Expertise",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    type_of_expertise: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTypeOfExpertise
    ] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfExpertise",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatrices:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionProposedMetabolicPathway:
    class Meta:
        global_type = False

    identification_of_compounds_from_metabolism_study: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudy
    ] = field(
        default=None,
        metadata={
            "name": "IdentificationOfCompoundsFromMetabolismStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    metabolic_pathway: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "MetabolicPathway",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    metabolic_map_picture_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetabolicMapPictureGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionStorageStabilityOfResidues:
    class Meta:
        global_type = False

    summary_of_storage_conditions: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditions
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfStorageConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    storage_stability: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatrices:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatrices:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervals:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervalsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    test_animal_dosing_regime: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposureTestAnimalDosingRegime
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimalDosingRegime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    details_on_dosing: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDosing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    no_of_animals_per_dose_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerDoseGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    rationale_for_selection_of_dose_group: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "RationaleForSelectionOfDoseGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    analysis_of_feed_and_water: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisOfFeedAndWater",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    further_details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "FurtherDetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroups:
    class Meta:
        global_type = False

    treatment_group: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroup
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    sample_collection: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisSampleCollection
    ] = field(
        default=None,
        metadata={
            "name": "SampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    details_on_sampling_and_analytical_methods: List[MultilingualTextField] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnSamplingAndAnalyticalMethods",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
            },
        )
    )
    details_on_extraction_and_analysis: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExtractionAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    details_on_identification_and_characterisation: List[
        MultilingualTextField
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnIdentificationAndCharacterisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    flowchart_of_extraction_and_fractionation_schemes: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemes
    ] = field(
        default=None,
        metadata={
            "name": "FlowchartOfExtractionAndFractionationSchemes",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    general_test_animal_information: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsGeneralTestAnimalInformation
    ] = field(
        default=None,
        metadata={
            "name": "GeneralTestAnimalInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    details_on_housing_conditions_and_test_animals: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnHousingConditionsAndTestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    test_animal_dietary_regime: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimalsTestAnimalDietaryRegime
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimalDietaryRegime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    details_on_dietary_regime: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDietaryRegime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    radiolabelled_test_material: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterial
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelledTestMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroups:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    metabolite_fraction: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryMetaboliteFraction
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    identity_of_parent_or_metabolite: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfParentOrMetabolite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrs_in_matrices: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatrices
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInMatrices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    metabolite_fraction: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryMetaboliteFraction
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    identity_of_parent_or_metabolite: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfParentOrMetabolite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrs_in_matrices: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatrices
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInMatrices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrs_in_matrices: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatrices
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInMatrices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_of_samples: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTypeOfSamples
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfSamples",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrs_at_time_intervals: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntryTrrsAtTimeIntervals
    ] = field(
        default=None,
        metadata={
            "name": "TRRsAtTimeIntervals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockMaterialsAndMethods:
    class Meta:
        global_type = False

    background_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    product_type: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    type_of_study: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTypeOfStudy
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    appendix_treatment_groups: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAppendixTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "AppendixTreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroups:
    class Meta:
        global_type = False

    metabolites_in_treatment_groups: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "MetabolitesInTreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolites:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResidues:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResiduesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTime:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTimeEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResidues:
    class Meta:
        global_type = False

    distribution_of_parent_and_metabolites: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "DistributionOfParentAndMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    distribution_of_residues: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DistributionOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResidues:
    class Meta:
        global_type = False

    characterisation_and_identification_of_radioactive_residues: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResiduesCharacterisationAndIdentificationOfRadioactiveResidues
    ] = field(
        default=None,
        metadata={
            "name": "CharacterisationAndIdentificationOfRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    characterisation_and_identification_of_residues: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "CharacterisationAndIdentificationOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    general_health_of_animals: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "GeneralHealthOfAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResidues:
    class Meta:
        global_type = False

    extraction_efficiency_of_radioactive_residues_using_enforcement_method: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethod
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    quantitation: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Quantitation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrresults: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrresults
    ] = field(
        default=None,
        metadata={
            "name": "TRRResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrs_reached_plateau_at_end_of_dosing: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsReachedPlateauAtEndOfDosing
    ] = field(
        default=None,
        metadata={
            "name": "TRRsReachedPlateauAtEndOfDosing",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    trrs_as_afunction_of_time: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesTrrsAsAfunctionOfTime
    ] = field(
        default=None,
        metadata={
            "name": "TRRsAsAFunctionOfTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    graphical_plot_of_trrs_as_afunction_of_time: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResiduesGraphicalPlotOfTrrsAsAfunctionOfTime
    ] = field(
        default=None,
        metadata={
            "name": "GraphicalPlotOfTRRsAsAFunctionOfTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    total_radioactive_residues: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "TotalRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestockResultsAndDiscussion:
    class Meta:
        global_type = False

    total_radioactive_residues: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionTotalRadioactiveResidues
    ] = field(
        default=None,
        metadata={
            "name": "TotalRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    extraction_characterisation_and_distribution_of_residues: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionExtractionCharacterisationAndDistributionOfResidues
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionCharacterisationAndDistributionOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    storage_stability_of_residues: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionStorageStabilityOfResidues
    ] = field(
        default=None,
        metadata={
            "name": "StorageStabilityOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    summary_of_characterisation_and_identification_of_radioactive_residues: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionSummaryOfCharacterisationAndIdentificationOfRadioactiveResidues
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfCharacterisationAndIdentificationOfRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    proposed_metabolic_pathway: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionProposedMetabolicPathway
    ] = field(
        default=None,
        metadata={
            "name": "ProposedMetabolicPathway",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    appendix_metabolites_and_their_parents_in_treatment_groups: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "AppendixMetabolitesAndTheirParentsInTreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInLivestock:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.MetabolismInLivestock"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInLivestock/9.0"

    administrative_data: Optional[
        EndpointStudyRecordMetabolismInLivestockAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordMetabolismInLivestockDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordMetabolismInLivestockMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordMetabolismInLivestockResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordMetabolismInLivestockOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordMetabolismInLivestockApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
