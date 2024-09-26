from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from genetictoxicityvitro_6_5.models.common_types_oecd_v9 import (
    A36,
    N64,
    N78,
    T30,
    T31,
    T32,
    T140,
    T141,
    T142,
    T143,
    T144,
    T146,
    T148,
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
    Pg660299,
    Pg660300,
    Pg660301,
    Pg660302,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from genetictoxicityvitro_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0"


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660300] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660299] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryNegativeControls(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryPositiveControlSubstance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T142] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryPositiveControls(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntrySolventControls(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryTrueNegativeControls(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodMetabolicActivation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T32] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrainEntryAdditionalStrainCharacteristics(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T141] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrainEntrySpeciesStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T140] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsTypeOfAssay(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660301] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryCytotoxicity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T146] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryGenotoxicity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryMetActIndicator(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T32] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryNegContrValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryOrganism(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660302] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryPosContrValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryTrueNegativeControlsValidity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryVehContrValid(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordGeneticToxicityVitroDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordGeneticToxicityVitroDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    negative_controls: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryNegativeControls
    ] = field(
        default=None,
        metadata={
            "name": "NegativeControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    solvent_controls: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntrySolventControls
    ] = field(
        default=None,
        metadata={
            "name": "SolventControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    true_negative_controls: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryTrueNegativeControls
    ] = field(
        default=None,
        metadata={
            "name": "TrueNegativeControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    positive_controls: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryPositiveControls
    ] = field(
        default=None,
        metadata={
            "name": "PositiveControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    positive_control_substance: List[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntryPositiveControlSubstance
    ] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControlSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrainEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    species_strain: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrainEntrySpeciesStrain
    ] = field(
        default=None,
        metadata={
            "name": "SpeciesStrain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    details_on_mammalian_cell_lines_if_applicable: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMammalianCellLinesIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    additional_strain_characteristics: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrainEntryAdditionalStrainCharacteristics
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalStrainCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    organism: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryOrganism
    ] = field(
        default=None,
        metadata={
            "name": "Organism",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    met_act_indicator: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryMetActIndicator
    ] = field(
        default=None,
        metadata={
            "name": "MetActIndicator",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    genotoxicity: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryGenotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "Genotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    cytotoxicity: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryCytotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "Cytotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    veh_contr_valid: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryVehContrValid
    ] = field(
        default=None,
        metadata={
            "name": "VehContrValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    neg_contr_valid: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryNegContrValid
    ] = field(
        default=None,
        metadata={
            "name": "NegContrValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    true_negative_controls_validity: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryTrueNegativeControlsValidity
    ] = field(
        default=None,
        metadata={
            "name": "TrueNegativeControlsValidity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    pos_contr_valid: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntryPosContrValid
    ] = field(
        default=None,
        metadata={
            "name": "PosContrValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControls:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControlsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrain:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrainEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRs:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethod:
    class Meta:
        global_type = False

    target_gene: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TargetGene",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    species_strain: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodSpeciesStrain
    ] = field(
        default=None,
        metadata={
            "name": "SpeciesStrain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    cytokinesis_block_if_used: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "CytokinesisBlockIfUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    metabolic_activation: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodMetabolicActivation
    ] = field(
        default=None,
        metadata={
            "name": "MetabolicActivation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    metabolic_activation_system: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MetabolicActivationSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    test_concentrations: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TestConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    vehicle: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    controls: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethodControls
    ] = field(
        default=None,
        metadata={
            "name": "Controls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    details_on_test_system_and_conditions: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DetailsOnTestSystemAndConditions",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
            },
        )
    )
    rationale_for_test_conditions: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "RationaleForTestConditions",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
            },
        )
    )
    evaluation_criteria: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "EvaluationCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    type_of_assay: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsTypeOfAssay
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfAssay",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    method: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsMethod
    ] = field(
        default=None,
        metadata={
            "name": "Method",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussion:
    class Meta:
        global_type = False

    test_rs: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionTestRs
    ] = field(
        default=None,
        metadata={
            "name": "TestRs",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    results_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVitro:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.GeneticToxicityVitro"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVitro/9.0"

    administrative_data: Optional[
        EndpointStudyRecordGeneticToxicityVitroAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordGeneticToxicityVitroDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordGeneticToxicityVitroMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordGeneticToxicityVitroResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordGeneticToxicityVitroOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordGeneticToxicityVitroApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
