from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_7.endocrinedisrupterscreeninginvitro_6_5.models.common_types_oecd_v8 import (
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
    Z36,
    Z40,
    Z52,
    IntEffAccResults,
    IntEffAddAnalysis,
    IntEffAttachmentType,
    IntEffConcSelection,
    IntEffMetabolic,
    IntEffOtherQuality,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660361,
    Pg660363,
    Pg660377,
    Pg660380,
    Pg661157,
    Pg661434,
    Pg661435,
    Pg661436,
    Pg661437,
    Pg661438,
    Pg661439,
    Pg661440,
    Pg661441,
    Pg661442,
    Pg661443,
    Pg661444,
    Pg661445,
    Pg661446,
)
from entity_models_6_7.endocrinedisrupterscreeninginvitro_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0"


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661434] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionExecutiveSummary:
    class Meta:
        global_type = False

    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservationsConcentration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660377] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservationsEffectConcentrationChoice(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661446] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservationsTypeOfResult(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660380] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsDetectionMethodDetectionMethodUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660361] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661436] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsOtherQualityFollowed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[IntEffOtherQuality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceItemsUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstancesEntryControlOrReferenceItemsUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661442] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstancesEntryTypeOfControls(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660363] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignDataAnalysis:
    class Meta:
        global_type = False

    acceptance_criteria: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "AcceptanceCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    data_calculation_and_statistics: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DataCalculationAndStatistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    evaluation_data_interpretation_criteria: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "EvaluationDataInterpretationCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignExperimentalConditionsAdditionalAnalysis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[IntEffAddAnalysis] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignTestMaterialPreparationConcSelectTestMat(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661440] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignTestMaterialPreparationVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661441] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemGeneticModOfSystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661439] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemMetabolicCompetence(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[IntEffMetabolic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemTestSystemIdentity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661438] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemTestSystemType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661437] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTypeOfStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661435] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAcceptanceOfResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[IntEffAccResults] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAttachedMaterialEntryAttachmentType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[IntEffAttachmentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryConcentrationRangeTested(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660377] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryConcentrationSelection(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[IntEffConcSelection] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservationEntryConcentration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660377] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservationEntryObservation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661444] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResultEntryParameter(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661443] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResultEntryParameterResult(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660377] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryResultsForTheTestMaterial(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661445] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    legislation: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservations:
    class Meta:
        global_type = False

    overall_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OverallResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    type_of_result: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservationsTypeOfResult
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    effect_concentration_choice: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservationsEffectConcentrationChoice
    ] = field(
        default=None,
        metadata={
            "name": "EffectConcentrationChoice",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    concentration: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservationsConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsDetectionMethod:
    class Meta:
        global_type = False

    detection_method_used: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsDetectionMethodDetectionMethodUsed
    ] = field(
        default=None,
        metadata={
            "name": "DetectionMethodUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    details_on_detection_method: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnDetectionMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstancesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_of_controls: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstancesEntryTypeOfControls
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    control_or_reference_items_used: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstancesEntryControlOrReferenceItemsUsed
    ] = field(
        default=None,
        metadata={
            "name": "ControlOrReferenceItemsUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignExperimentalConditions:
    class Meta:
        global_type = False

    additional_analysis: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignExperimentalConditionsAdditionalAnalysis
    ] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignTestMaterialPreparation:
    class Meta:
        global_type = False

    conc_select_test_mat: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignTestMaterialPreparationConcSelectTestMat
    ] = field(
        default=None,
        metadata={
            "name": "ConcSelectTestMat",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignTestMaterialPreparationVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    dilution_steps_dose_intervals: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DilutionStepsDoseIntervals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystem:
    class Meta:
        global_type = False

    test_system_type: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemTestSystemType
    ] = field(
        default=None,
        metadata={
            "name": "TestSystemType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    test_system_identity: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemTestSystemIdentity
    ] = field(
        default=None,
        metadata={
            "name": "TestSystemIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    genetic_mod_of_system: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemGeneticModOfSystem
    ] = field(
        default=None,
        metadata={
            "name": "GeneticModOfSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    test_system_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "TestSystemDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    metabolic_competence: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystemMetabolicCompetence
    ] = field(
        default=None,
        metadata={
            "name": "MetabolicCompetence",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAttachedMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attachment_type: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAttachedMaterialEntryAttachmentType
    ] = field(
        default_factory=list,
        metadata={
            "name": "AttachmentType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    attachment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    observation: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservationEntryObservation
    ] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    concentration: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservationEntryConcentration
    ] = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResultEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    parameter: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResultEntryParameter
    ] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    parameter_result: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResultEntryParameterResult
    ] = field(
        default=None,
        metadata={
            "name": "ParameterResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusion:
    class Meta:
        global_type = False

    interpretation_of_results_observations: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionInterpretationOfResultsObservations
    ] = field(
        default=None,
        metadata={
            "name": "InterpretationOfResultsObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    executive_summary: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusionExecutiveSummary
    ] = field(
        default=None,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstances:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstancesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAttachedMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAttachedMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResult:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResultEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItems:
    class Meta:
        global_type = False

    controls_reference_items_used: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceItemsUsed
    ] = field(
        default=None,
        metadata={
            "name": "ControlsReferenceItemsUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    controls_reference_substances: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItemsControlsReferenceSubstances
    ] = field(
        default=None,
        metadata={
            "name": "ControlsReferenceSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_observation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyObservation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    concentration_selection: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryConcentrationSelection
    ] = field(
        default=None,
        metadata={
            "name": "ConcentrationSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    concentration_range_tested: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryConcentrationRangeTested
    ] = field(
        default=None,
        metadata={
            "name": "ConcentrationRangeTested",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    number_of_replicates_and_outliers: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "NumberOfReplicatesAndOutliers",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
            },
        )
    )
    parameter_and_result: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryParameterAndResult
    ] = field(
        default=None,
        metadata={
            "name": "ParameterAndResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other_observation: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryOtherObservation
    ] = field(
        default=None,
        metadata={
            "name": "OtherObservation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    results_for_the_test_material: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryResultsForTheTestMaterial
    ] = field(
        default=None,
        metadata={
            "name": "ResultsForTheTestMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    acceptance_of_results: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAcceptanceOfResults
    ] = field(
        default_factory=list,
        metadata={
            "name": "AcceptanceOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    remarks_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    attached_material: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntryAttachedMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesign:
    class Meta:
        global_type = False

    test_material_preparation: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignTestMaterialPreparation
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterialPreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    control_and_reference_items: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignControlAndReferenceItems
    ] = field(
        default=None,
        metadata={
            "name": "ControlAndReferenceItems",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    experimental_conditions: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignExperimentalConditions
    ] = field(
        default=None,
        metadata={
            "name": "ExperimentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    data_analysis: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesignDataAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "DataAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethods:
    class Meta:
        global_type = False

    type_of_study: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTypeOfStudy
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    other_quality_followed: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsOtherQualityFollowed
    ] = field(
        default=None,
        metadata={
            "name": "OtherQualityFollowed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    test_system: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestSystem
    ] = field(
        default=None,
        metadata={
            "name": "TestSystem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    detection_method: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsDetectionMethod
    ] = field(
        default=None,
        metadata={
            "name": "DetectionMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    test_design: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsTestDesign
    ] = field(
        default=None,
        metadata={
            "name": "TestDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResults:
    class Meta:
        global_type = False

    test_results: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResultsTestResults
    ] = field(
        default=None,
        metadata={
            "name": "TestResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussion:
    class Meta:
        global_type = False

    test_results: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussionTestResults
    ] = field(
        default=None,
        metadata={
            "name": "TestResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0",
        },
    )


@dataclass
class EndpointStudyRecordEndocrineDisrupterScreeningInVitro:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.EndocrineDisrupterScreeningInVitro"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-EndocrineDisrupterScreeningInVitro/8.0"

    administrative_data: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_ssummary_and_conclusion: Optional[
        EndpointStudyRecordEndocrineDisrupterScreeningInVitroApplicantSsummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSSummaryAndConclusion",
            "type": "Element",
        },
    )
