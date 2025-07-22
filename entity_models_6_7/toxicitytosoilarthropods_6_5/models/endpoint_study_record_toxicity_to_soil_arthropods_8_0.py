from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_7.toxicitytosoilarthropods_6_5.models.common_types_oecd_v8 import (
    A03,
    A36,
    E04,
    E15,
    E35,
    E105,
    F102,
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
    Z38,
    Z40,
    Agsoil61208,
    ApplSoil61206,
    EndpointSoilArthro61204,
    Ls61213,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660240,
    Pg661157,
    SoilArthroSpec61207,
    SoilBe61214,
    SoilDd61210,
    SoilEc61211,
    Stsoil61209,
    Tgsoil61205,
)
from entity_models_6_7.toxicitytosoilarthropods_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0"


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660240] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[EndpointSoilArthro61204] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsApplicantSummaryAndConclusionValidityCriteriaFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Tgsoil61205] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesignLimitTest(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesignStudyType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Stsoil61209] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesignTotalExposureDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E15] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestOrganismsAnimalGroup(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Agsoil61208] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SoilArthroSpec61207] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestSubstrateApplicationMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[ApplSoil61206] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestSubstrateVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SoilBe61214] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryConfInterval(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryDuration(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryEffectConc(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[SoilEc61211] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[SoilDd61210] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryLifeStage(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Ls61213] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E35] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    analytical_monitoring: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMonitoring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    details_on_sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    study_type: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesignStudyType
    ] = field(
        default=None,
        metadata={
            "name": "StudyType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesignLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    total_exposure_duration: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesignTotalExposureDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    post_exposure_observation_period: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "PostExposureObservationPeriod",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
            },
        )
    )
    extraction_method: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExtractionMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    test_temperature: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    humidity: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Humidity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    photoperiod_and_lighting: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PhotoperiodAndLighting",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    details_on_test_conditions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    nominal_and_measured_concentrations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    identity_of_the_reference_substance_positive_control: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "IdentityOfTheReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    animal_group: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestOrganismsAnimalGroup
    ] = field(
        default=None,
        metadata={
            "name": "AnimalGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    details_on_test_organisms: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestSubstrate:
    class Meta:
        global_type = False

    application_method: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestSubstrateApplicationMethod
    ] = field(
        default=None,
        metadata={
            "name": "ApplicationMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestSubstrateVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    details_on_preparation_and_application_of_test_substrate: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnPreparationAndApplicationOfTestSubstrate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    duration: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryDuration
    ] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    effect_conc: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryEffectConc
    ] = field(
        default=None,
        metadata={
            "name": "EffectConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    conf_interval: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryConfInterval
    ] = field(
        default=None,
        metadata={
            "name": "ConfInterval",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    nominal_measured: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured
    ] = field(
        default=None,
        metadata={
            "name": "NominalMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    conc_based_on: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "ConcBasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    life_stage: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryLifeStage
    ] = field(
        default=None,
        metadata={
            "name": "LifeStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    basis_for_effect: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect
    ] = field(
        default=None,
        metadata={
            "name": "BasisForEffect",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    test_substrate: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestSubstrate
    ] = field(
        default=None,
        metadata={
            "name": "TestSubstrate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_concentrations: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionEffectConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    results_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    results_ref_substance: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ResultsRefSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityToSoilArthropods:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ToxicityToSoilArthropods"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityToSoilArthropods/8.0"

    administrative_data: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordToxicityToSoilArthropodsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
