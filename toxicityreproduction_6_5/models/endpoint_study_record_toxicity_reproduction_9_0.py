from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from toxicityreproduction_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    P29,
    T027,
    T24,
    T25,
    T27,
    T40,
    T102,
    T112,
    T166,
    T281,
    T284,
    T2312346,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z38,
    Z40,
    A03Rh,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660234,
    Pg660235,
    Pg660242,
    Pg660275,
    Pg660288,
    Pg660294,
    Pg660295,
    Pg660306,
    Pg660307,
    Pg660316,
    Pg660329,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td390,
)
from toxicityreproduction_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0"


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660306] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660275] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureControlAnimals(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[P29] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureRouteOfAdministration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposureIfApplicable(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Td390] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    parental_animals_observations_and_examinations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ParentalAnimalsObservationsAndExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    estrous_cyclicity_parental_animals: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "EstrousCyclicityParentalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    sperm_parameters_parental_animals: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "SpermParametersParentalAnimals",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            },
        )
    )
    litter_observations: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "LitterObservations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    postmortem_examinations_parental_animals: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "PostmortemExaminationsParentalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    postmortem_examinations_offspring: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "PostmortemExaminationsOffspring",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            },
        )
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_indices: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ReproductiveIndices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    offspring_viability_indices: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "OffspringViabilityIndices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsLimitTest(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T027] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T2312346] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelationToOtherToxicEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660294] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryReproductiveEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDetailsOnResultsF2:
    class Meta:
        global_type = False

    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1GenerationDevelopmentalImmunotoxicity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1GenerationBehaviourFunctionalFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660288] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryGeneration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660316] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2AnogenitalDistance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2DermalIrritationOffspringIfDermalStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2NippleRetentionInMalePups(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservBodyweightOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinChemOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodConsumOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodEfficiencyOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservGrpatholOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHaematolOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHistopatholOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservMaturationOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOphthalmOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOrganWeightsOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservUrinOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservViabilityOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservWaterConsumOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2OtherEffectsOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryCriticalEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryOrgan(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntrySystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDetailsOnResultsF1:
    class Meta:
        global_type = False

    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1DevelopmentalImmunotoxicity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1BehaviourFunctionalFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660288] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryGeneration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660295] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1AnogenitalDistance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1DermalIrritationOffspringIfDermalStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1NippleRetentionInMalePups(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservBodyweightOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinChemOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodConsumOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodEfficiencyOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservGrpatholOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHaematolOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHistopatholOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservMaturationOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOphthalmOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOrganWeightsOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservUrinOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservViabilityOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservWaterConsumOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1OtherEffectsOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryCriticalEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryOrgan(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntrySystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationDetailsOnResultsP0:
    class Meta:
        global_type = False

    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660329] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0EndocrineFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ImmunologicalFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservBodyweight(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinChem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinSigns(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservDermalIrritationIfDermalStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodEfficiency(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservGrpathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHaematol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopatholNeoplastic(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservMortality(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeurobehaviour(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeuropathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOphthalm(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOrganWeights(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservUrin(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservWaterConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0OtherEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservEstrousParent(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservReproPerformParent(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservSpermParent(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryCriticalEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryOrgan(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntrySystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationDetailsOnResultsP1:
    class Meta:
        global_type = False

    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660329] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1EndocrineFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ImmunologicalFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservBodyweight(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinChem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinSigns(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservDermalIrritationIfDermalStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodEfficiency(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservGrpathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHaematol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopatholNeoplastic(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservMortality(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeurobehaviour(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeuropathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOphthalm(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOrganWeights(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservUrin(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservWaterConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1OtherEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionEstrousCycle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionSpermMeasures(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductivePerformance(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryCriticalEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T281] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryOrgan(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntrySystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordToxicityReproductionDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordToxicityReproductionDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_species_strain_selection: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    organism_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryReproductiveEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    relation_to_other_toxic_effects: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelationToOtherToxicEffects
    ] = field(
        default=None,
        metadata={
            "name": "RelationToOtherToxicEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1Generation:
    class Meta:
        global_type = False

    developmental_immunotoxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1GenerationDevelopmentalImmunotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_developmental_immunotoxicity: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1Generation:
    class Meta:
        global_type = False

    behaviour_functional_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1GenerationBehaviourFunctionalFindings
    ] = field(
        default=None,
        metadata={
            "name": "BehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_behaviour_functional_findings: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityBehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryGeneration
    ] = field(
        default=None,
        metadata={
            "name": "Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2:
    class Meta:
        global_type = False

    observ_clin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dermal_irritation_offspring_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2DermalIrritationOffspringIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "DermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_dermal_irritation_offspring_if_dermal_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_viability_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservViabilityOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_viability_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_bodyweight_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservBodyweightOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_consum_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_efficiency_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservFoodEfficiencyOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_water_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservWaterConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_water_consum_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_ophthalm_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOphthalmOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalmOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalmOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_haematol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHaematolOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematolOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_haematol_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematolOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_clin_chem_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservClinChemOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_urin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservUrinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_urin_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_maturation_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservMaturationOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_maturation_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    anogenital_distance: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2AnogenitalDistance
    ] = field(
        default=None,
        metadata={
            "name": "AnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_anogenital_distance: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityAnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    nipple_retention_in_male_pups: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2NippleRetentionInMalePups
    ] = field(
        default=None,
        metadata={
            "name": "NippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_nipple_retention_in_male_pups: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityNippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_organ_weights_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservOrganWeightsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_grpathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservGrpatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_grpathol_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_histopathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2ObservHistopatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other_effects_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2OtherEffectsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffectsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_other_effects_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffectsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1:
    class Meta:
        global_type = False

    developmental_immunotoxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1DevelopmentalImmunotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_developmental_immunotoxicity: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDevelopmentalImmunotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1:
    class Meta:
        global_type = False

    behaviour_functional_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1BehaviourFunctionalFindings
    ] = field(
        default=None,
        metadata={
            "name": "BehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_behaviour_functional_findings: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityBehaviourFunctionalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryGeneration
    ] = field(
        default=None,
        metadata={
            "name": "Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1:
    class Meta:
        global_type = False

    observ_clin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dermal_irritation_offspring_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1DermalIrritationOffspringIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "DermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_dermal_irritation_offspring_if_dermal_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDermalIrritationOffspringIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_viability_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservViabilityOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_viability_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservViabilityOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_bodyweight_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservBodyweightOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweightOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_consum_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_efficiency_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservFoodEfficiencyOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiencyOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_water_consum_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservWaterConsumOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_water_consum_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsumOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_ophthalm_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOphthalmOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalmOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalmOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_haematol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHaematolOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematolOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_haematol_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematolOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_clin_chem_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservClinChemOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChemOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_urin_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservUrinOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_urin_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrinOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_maturation_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservMaturationOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_maturation_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservMaturationOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    anogenital_distance: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1AnogenitalDistance
    ] = field(
        default=None,
        metadata={
            "name": "AnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_anogenital_distance: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityAnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    nipple_retention_in_male_pups: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1NippleRetentionInMalePups
    ] = field(
        default=None,
        metadata={
            "name": "NippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_nipple_retention_in_male_pups: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityNippleRetentionInMalePups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_organ_weights_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservOrganWeightsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeightsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_grpathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservGrpatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_grpathol_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_histopathol_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1ObservHistopatholOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other_effects_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1OtherEffectsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffectsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_other_effects_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffectsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_dermal_irritation_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservDermalIrritationIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "ObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_dermal_irritation_if_dermal_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_mortality: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_water_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endocrine_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0EndocrineFindings
    ] = field(
        default=None,
        metadata={
            "name": "EndocrineFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_endocrine: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityEndocrine",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    immunological_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0ObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0OtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_other_effects: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0:
    class Meta:
        global_type = False

    observ_estrous_parent: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservEstrousParent
    ] = field(
        default=None,
        metadata={
            "name": "ObservEstrousParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_estrous_parent: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservEstrousParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_sperm_parent: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservSpermParent
    ] = field(
        default=None,
        metadata={
            "name": "ObservSpermParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_sperm_parent: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservSpermParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_repro_perform_parent: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0ObservReproPerformParent
    ] = field(
        default=None,
        metadata={
            "name": "ObservReproPerformParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_repro_perform_parent: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservReproPerformParent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_dermal_irritation_if_dermal_study: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservDermalIrritationIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "ObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_dermal_irritation_if_dermal_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_mortality: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_water_consum: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endocrine_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1EndocrineFindings
    ] = field(
        default=None,
        metadata={
            "name": "EndocrineFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_endocrine: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityEndocrine",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    immunological_findings: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1ObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1OtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_other_effects: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1:
    class Meta:
        global_type = False

    reproductive_function_estrous_cycle: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionEstrousCycle
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionEstrousCycle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_reproductive_function_estrous_cycle: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityReproductiveFunctionEstrousCycle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_function_sperm_measures: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductiveFunctionSpermMeasures
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionSpermMeasures",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_reproductive_function_sperm_measures: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityReproductiveFunctionSpermMeasures",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_performance: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1ReproductivePerformance
    ] = field(
        default=None,
        metadata={
            "name": "ReproductivePerformance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    description_incidence_and_severity_reproductive_performance: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityReproductivePerformance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    system: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    organ: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1Efflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1EfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordToxicityReproductionAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    type_of_inhalation_exposure_if_applicable: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposureIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfInhalationExposureIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    mass_median_aerodynamic_diameter: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter
    ] = field(
        default=None,
        metadata={
            "name": "MassMedianAerodynamicDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    geometric_standard_deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GeometricStandardDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    remarks_on_mmad: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnMMAD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_exposure: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_mating_procedure: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMatingProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    duration_of_treatment_exposure: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "DurationOfTreatmentExposure",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
            },
        )
    )
    frequency_of_treatment: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_study_schedule: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudySchedule",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    positive_control: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicity:
    class Meta:
        global_type = False

    reproductive_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicityReproductiveToxicity
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1Efflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1TargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    justification_for_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2Generation:
    class Meta:
        global_type = False

    general_toxicity_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationGeneralToxicityF2
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    developmental_neurotoxicity_of_f1_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalNeurotoxicityOfF1Generation
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalNeurotoxicityOfF1Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    developmental_immunotoxicity_of_f1_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDevelopmentalImmunotoxicityOfF1Generation
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicityOfF1Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_results_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationDetailsOnResultsF2
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_levels_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationEffectLevelsF2
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    target_system_organ_toxicity_f2: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2GenerationTargetSystemOrganToxicityF2
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityF2",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspring:
    class Meta:
        global_type = False

    general_toxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringGeneralToxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    developmental_neurotoxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalNeurotoxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalNeurotoxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    developmental_immunotoxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDevelopmentalImmunotoxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalImmunotoxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_results_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringDetailsOnResultsF1
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_levels_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringEffectLevelsF1
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    target_system_organ_toxicity_f1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspringTargetSystemOrganToxicityF1
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityF1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGeneration:
    class Meta:
        global_type = False

    general_toxicity_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationGeneralToxicityP0
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_function_performance_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationReproductiveFunctionPerformanceP0
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionPerformanceP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_results_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationDetailsOnResultsP0
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_levels_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationEffectLevelsP0
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    target_system_organ_toxicity_p0: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGenerationTargetSystemOrganToxicityP0
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityP0",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGeneration:
    class Meta:
        global_type = False

    general_toxicity_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationGeneralToxicityP1
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_function_performance_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationReproductiveFunctionPerformanceP1
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveFunctionPerformanceP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    details_on_results_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationDetailsOnResultsP1
    ] = field(
        default=None,
        metadata={
            "name": "DetailsOnResultsP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    effect_levels_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationEffectLevelsP1
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    target_system_organ_toxicity_p1: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGenerationTargetSystemOrganToxicityP1
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicityP1",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproductionResultsAndDiscussion:
    class Meta:
        global_type = False

    results_of_examinations_parental_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsParentalGeneration
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminationsParentalGeneration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    results_p1_second_parental_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsP1SecondParentalGeneration
    ] = field(
        default=None,
        metadata={
            "name": "ResultsP1SecondParentalGeneration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    results_of_examinations_offspring: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsOfExaminationsOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminationsOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    results_f2_generation: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionResultsF2Generation
    ] = field(
        default=None,
        metadata={
            "name": "ResultsF2Generation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    reproductive_toxicity: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionReproductiveToxicity
    ] = field(
        default=None,
        metadata={
            "name": "ReproductiveToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0",
        },
    )


@dataclass
class EndpointStudyRecordToxicityReproduction:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ToxicityReproduction"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ToxicityReproduction/9.0"

    administrative_data: Optional[
        EndpointStudyRecordToxicityReproductionAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordToxicityReproductionDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordToxicityReproductionMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordToxicityReproductionResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordToxicityReproductionOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordToxicityReproductionApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
