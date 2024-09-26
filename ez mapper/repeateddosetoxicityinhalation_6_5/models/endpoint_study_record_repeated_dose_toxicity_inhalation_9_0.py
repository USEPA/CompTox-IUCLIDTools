from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from repeateddosetoxicityinhalation_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    P29,
    T023,
    T24,
    T27,
    T102,
    T112,
    T166,
    T252,
    T262,
    T282,
    T23123456,
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
    Pg660233,
    Pg660234,
    Pg660235,
    Pg660242,
    Pg660245,
    Pg660307,
    Pg660422,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td380,
)
from repeateddosetoxicityinhalation_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0"


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660422] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660245] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureControlAnimals(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T282] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[P29] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureRouteOfAdministration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T252] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposure(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Td380] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    observations_and_examinations_performed_and_frequency: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ObservationsAndExaminationsPerformedAndFrequency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    sacrifice_and_pathology: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "SacrificeAndPathology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other_examinations: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OtherExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T262] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsLimitTest(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimalsSex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T023] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660233] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T282] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsEndocrineFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsImmunologicalFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservBodyweight(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservClinChem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservClinSigns(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservFoodConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservFoodEfficiency(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservGrpathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservHaematol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservHistopathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservHistopatholNeoplastic(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservMortality(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservNeurobehaviour(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservNeuropathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservOphthalm(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservOrganWeights(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservUrin(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservWaterConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsOtherEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryCriticalEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T282] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryOrgan(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660242] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntrySystem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660235] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    details_on_species_strain_selection: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    organism_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminations:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_mortality: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_water_consum: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    endocrine_findings: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsEndocrineFindings
    ] = field(
        default=None,
        metadata={
            "name": "EndocrineFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_endocrine: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityEndocrine",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    immunological_findings: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminationsOtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    description_incidence_and_severity_other_effects: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    critical_effects_observed: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryCriticalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "CriticalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    system: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntrySystem
    ] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    organ: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryOrgan
    ] = field(
        default_factory=list,
        metadata={
            "name": "Organ",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    type_of_inhalation_exposure: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposure
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfInhalationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    mass_median_aerodynamic_diameter: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter
    ] = field(
        default=None,
        metadata={
            "name": "MassMedianAerodynamicDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    geometric_standard_deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GeometricStandardDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    remarks_on_mmad: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnMMAD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    details_on_inhalation_exposure: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnInhalationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    duration_of_treatment_exposure: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "DurationOfTreatmentExposure",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
            },
        )
    )
    frequency_of_treatment: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    positive_control: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevels:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevelsEfflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicity:
    class Meta:
        global_type = False

    target_system_organ_toxicity: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicityTargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussion:
    class Meta:
        global_type = False

    results_of_examinations: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionResultsOfExaminations
    ] = field(
        default=None,
        metadata={
            "name": "ResultsOfExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    effect_levels: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionEffectLevels
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    target_system_organ_toxicity: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionTargetSystemOrganToxicity
    ] = field(
        default=None,
        metadata={
            "name": "TargetSystemOrganToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0",
        },
    )


@dataclass
class EndpointStudyRecordRepeatedDoseToxicityInhalation:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.RepeatedDoseToxicityInhalation"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-RepeatedDoseToxicityInhalation/9.0"

    administrative_data: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordRepeatedDoseToxicityInhalationApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
