from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_7.skinirritationcorrosion_6_5.models.common_types_oecd_v8 import (
    A36,
    N64,
    N78,
    T025,
    T14,
    T50,
    T59,
    T104,
    T107,
    T144,
    T164,
    T169,
    T462,
    T23123456,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660202,
    Pg660203,
    Pg660204,
    Pg660205,
    Pg660206,
    Pg660349,
    Pg660455,
    Pg660456,
    Pg660458,
    Pg660459,
    Pg660461,
    Pg660467,
    Pg661121,
    Pg661157,
)
from entity_models_6_7.skinirritationcorrosion_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0"


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660203] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660202] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionApplicantSummaryAndConclusionInterpretationOfResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T462] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T14] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemCellSource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660461] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemCellType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemControlSamples(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660458] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemSourceSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660467] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemSourceStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemTestSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660455] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T59] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T025] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemControls(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660459] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemPreparationOfTestSite(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemTypeOfCoverage(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T50] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T59] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryIrritationCorrosionParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660204] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryNegativeControlsValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryPositiveControlsValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660349] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryVehicleControlsValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T169] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T164] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660206] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryReversibility(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T107] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryScore(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryTimePoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660205] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    legislation: List[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    interpretation_of_results: Optional[
        EndpointStudyRecordSkinIrritationCorrosionApplicantSummaryAndConclusionInterpretationOfResults
    ] = field(
        default=None,
        metadata={
            "name": "InterpretationOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordSkinIrritationCorrosionDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordSkinIrritationCorrosionDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystem:
    class Meta:
        global_type = False

    test_system: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "TestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    source_species: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemSourceSpecies
    ] = field(
        default=None,
        metadata={
            "name": "SourceSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    cell_type: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemCellType
    ] = field(
        default=None,
        metadata={
            "name": "CellType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    cell_source: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemCellSource
    ] = field(
        default=None,
        metadata={
            "name": "CellSource",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    source_strain: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemSourceStrain
    ] = field(
        default=None,
        metadata={
            "name": "SourceStrain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    details_on_animal_used_as_source_of_test_system: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnimalUsedAsSourceOfTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    justification_for_test_system_used: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTestSystemUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    details_on_test_system: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    control_samples: List[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystemControlSamples
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlSamples",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    amount_concentration_applied: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "AmountConcentrationApplied",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    duration_of_treatment_exposure: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "DurationOfTreatmentExposure",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            },
        )
    )
    duration_of_post_treatment_incubation_if_applicable: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfPostTreatmentIncubationIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    number_of_replicates: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfReplicates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    organism_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystem:
    class Meta:
        global_type = False

    type_of_coverage: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemTypeOfCoverage
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfCoverage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    preparation_of_test_site: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemPreparationOfTestSite
    ] = field(
        default=None,
        metadata={
            "name": "PreparationOfTestSite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    controls: List[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemControls
    ] = field(
        default_factory=list,
        metadata={
            "name": "Controls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    amount_concentration_applied: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "AmountConcentrationApplied",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    duration_of_treatment_exposure: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "DurationOfTreatmentExposure",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            },
        )
    )
    observation_period: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ObservationPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    number_of_animals: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystemHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    irritation_corrosion_parameter: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryIrritationCorrosionParameter
    ] = field(
        default=None,
        metadata={
            "name": "IrritationCorrosionParameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    run_experiment: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "RunExperiment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    value: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    vehicle_controls_valid: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryVehicleControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "VehicleControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    negative_controls_valid: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryNegativeControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "NegativeControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    positive_controls_valid: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryPositiveControlsValid
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControlsValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    parameter: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    basis: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryBasis
    ] = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    time_point: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryTimePoint
    ] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    score: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryScore
    ] = field(
        default=None,
        metadata={
            "name": "Score",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    scale: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    reversibility: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryReversibility
    ] = field(
        default=None,
        metadata={
            "name": "Reversibility",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    in_vitro_test_system: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsInVitroTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "InVitroTestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    test_system: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "TestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitro:
    class Meta:
        global_type = False

    results: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitroResults
    ] = field(
        default=None,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    other_effects_acceptance_of_results: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "OtherEffectsAcceptanceOfResults",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivo:
    class Meta:
        global_type = False

    results: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivoResults
    ] = field(
        default=None,
        metadata={
            "name": "Results",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    irritation_corrosion_response_data: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "IrritationCorrosionResponseData",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
            },
        )
    )
    other_effects: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussion:
    class Meta:
        global_type = False

    in_vitro: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVitro
    ] = field(
        default=None,
        metadata={
            "name": "InVitro",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    in_vivo: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionInVivo
    ] = field(
        default=None,
        metadata={
            "name": "InVivo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0",
        },
    )


@dataclass
class EndpointStudyRecordSkinIrritationCorrosion:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.SkinIrritationCorrosion"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-SkinIrritationCorrosion/8.0"

    administrative_data: Optional[
        EndpointStudyRecordSkinIrritationCorrosionAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordSkinIrritationCorrosionDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordSkinIrritationCorrosionMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordSkinIrritationCorrosionResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordSkinIrritationCorrosionOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordSkinIrritationCorrosionApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
