from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from developmentaltoxicityteratogenicity_6_5.models.common_types_oecd_v9 import (
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
    T44,
    T102,
    T112,
    T166,
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
    Pg660307,
    Pg660312,
    Pg660313,
    Pg660314,
    Pg660317,
    Pg660318,
    Pg660331,
    Pg660520,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td390,
)
from developmentaltoxicityteratogenicity_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0"


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660313] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660312] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureControlAnimals(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[P29] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureRouteOfAdministration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposureIfApplicable(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Td390] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    maternal_examinations: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MaternalExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    ovaries_and_uterine_content: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OvariesAndUterineContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    blood_sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "BloodSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    fetal_examinations: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "FetalExaminations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    indices: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Indices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    historical_control_data: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "HistoricalControlData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T44] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsLimitTest(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T027] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T2312346] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryDevelopmentalEffectsObserved(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryDoseResponseRelationship(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryLowestEffectiveDoseConc(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryRelationToMaternalToxicity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660520] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryRelevantForHumans(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03Rh] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryTreatmentRelated(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesAnogenitalDistanceOfAllRodentFetuses(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesChangesInLitterSizeAndWeights(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesChangesInPostnatalSurvival(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesChangesInSexRatio(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660318] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesExternalMalformations(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalitiesEntryAbnormalities(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalitiesEntryLocalisation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660317] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalBodyWeightChanges(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesOtherEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesReductionInNumberOfLiveOffspring(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesSkeletalMalformations(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesVisceralMalformations(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660331] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T166] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660234] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsEndocrineFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsImmunologicalFindings(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservBodyweight(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservClinChem(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservClinSigns(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservDermalIrritationIfDermalStudy(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservFoodConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservFoodEfficiency(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservGrpathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservHaematol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservHistopathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservHistopatholNeoplastic(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservMortality(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660307] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservNeurobehaviour(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservNeuropathol(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservOphthalm(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservOrganWeights(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservUrin(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservWaterConsum(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsOtherEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalitiesEntryAbnormalities(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalitiesEntryLocalisation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660314] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityChangesInNumberOfPregnant(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityChangesInPregnancyDuration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityDeadFetuses(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityEarlyOrLateResorptions(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityNumberOfAbortions(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityOtherEffects(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityPreAndPostImplantationLoss(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityTotalLitterLossesByResorption(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    organism_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    developmental_effects_observed: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryDevelopmentalEffectsObserved
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalEffectsObserved",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    lowest_effective_dose_conc: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryLowestEffectiveDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "LowestEffectiveDoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    treatment_related: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryTreatmentRelated
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentRelated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    relation_to_maternal_toxicity: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryRelationToMaternalToxicity
    ] = field(
        default=None,
        metadata={
            "name": "RelationToMaternalToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    dose_response_relationship: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryDoseResponseRelationship
    ] = field(
        default=None,
        metadata={
            "name": "DoseResponseRelationship",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    relevant_for_humans: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntryRelevantForHumans
    ] = field(
        default=None,
        metadata={
            "name": "RelevantForHumans",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalitiesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    abnormalities: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalitiesEntryAbnormalities
    ] = field(
        default=None,
        metadata={
            "name": "Abnormalities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    localisation: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalitiesEntryLocalisation
    ] = field(
        default_factory=list,
        metadata={
            "name": "Localisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverity",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    basis: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryBasis
    ] = field(
        default_factory=list,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimals:
    class Meta:
        global_type = False

    observ_clin_signs: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservClinSigns
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_signs: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_dermal_irritation_if_dermal_study: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservDermalIrritationIfDermalStudy
    ] = field(
        default=None,
        metadata={
            "name": "ObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_dermal_irritation_if_dermal_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservDermalIrritationIfDermalStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_mortality: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservMortality
    ] = field(
        default=None,
        metadata={
            "name": "ObservMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_mortality: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceMortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_bodyweight: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservBodyweight
    ] = field(
        default=None,
        metadata={
            "name": "ObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_bodyweight: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservBodyweight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_food_consum: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservFoodConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_food_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_food_efficiency: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservFoodEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "ObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_food_efficiency: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservFoodEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_water_consum: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservWaterConsum
    ] = field(
        default=None,
        metadata={
            "name": "ObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_water_consum: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservWaterConsum",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_ophthalm: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservOphthalm
    ] = field(
        default=None,
        metadata={
            "name": "ObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_ophthalm: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOphthalm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_haematol: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservHaematol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_haematol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHaematol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_clin_chem: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservClinChem
    ] = field(
        default=None,
        metadata={
            "name": "ObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_clin_chem: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservClinChem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    endocrine_findings: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsEndocrineFindings
    ] = field(
        default=None,
        metadata={
            "name": "EndocrineFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_endocrine: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityEndocrine",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_urin: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservUrin
    ] = field(
        default=None,
        metadata={
            "name": "ObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_urin: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservUrin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_neurobehaviour: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservNeurobehaviour
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_neurobehaviour: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeurobehaviour",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    immunological_findings: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsImmunologicalFindings
    ] = field(
        default=None,
        metadata={
            "name": "ImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_immunological_findings: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityImmunologicalFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_organ_weights: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservOrganWeights
    ] = field(
        default=None,
        metadata={
            "name": "ObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_organ_weights: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservOrganWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_grpathol: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservGrpathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_grpathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservGrpathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_neuropathol: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservNeuropathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_neuropathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservNeuropathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_histopathol: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservHistopathol
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopathol",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    observ_histopathol_neoplastic: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsObservHistopatholNeoplastic
    ] = field(
        default=None,
        metadata={
            "name": "ObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_observ_histopathol_neoplastic: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityObservHistopatholNeoplastic",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimalsOtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_other_effects: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalitiesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    abnormalities: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalitiesEntryAbnormalities
    ] = field(
        default=None,
        metadata={
            "name": "Abnormalities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    localisation: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalitiesEntryLocalisation
    ] = field(
        default_factory=list,
        metadata={
            "name": "Localisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverity",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            },
        )
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicity:
    class Meta:
        global_type = False

    number_of_abortions: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityNumberOfAbortions
    ] = field(
        default=None,
        metadata={
            "name": "NumberOfAbortions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_number_of_abortions: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityNumberOfAbortions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    pre_and_post_implantation_loss: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityPreAndPostImplantationLoss
    ] = field(
        default=None,
        metadata={
            "name": "PreAndPostImplantationLoss",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_pre_and_post_implantation_loss: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityPreAndPostImplantationLoss",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    total_litter_losses_by_resorption: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityTotalLitterLossesByResorption
    ] = field(
        default=None,
        metadata={
            "name": "TotalLitterLossesByResorption",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_total_litter_losses_by_resorption: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityTotalLitterLossesByResorption",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    early_or_late_resorptions: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityEarlyOrLateResorptions
    ] = field(
        default=None,
        metadata={
            "name": "EarlyOrLateResorptions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_early_or_late_resorptions: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityEarlyOrLateResorptions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    dead_fetuses: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityDeadFetuses
    ] = field(
        default=None,
        metadata={
            "name": "DeadFetuses",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_dead_fetuses: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityDeadFetuses",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    changes_in_pregnancy_duration: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityChangesInPregnancyDuration
    ] = field(
        default=None,
        metadata={
            "name": "ChangesInPregnancyDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_changes_in_pregnancy_duration: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityChangesInPregnancyDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    changes_in_number_of_pregnant: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityChangesInNumberOfPregnant
    ] = field(
        default=None,
        metadata={
            "name": "ChangesInNumberOfPregnant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_changes_in_number_of_pregnant: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityChangesInNumberOfPregnant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicityOtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_other_effects: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    results_details_maternal: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetailsMaternal",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicity:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicityEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalities:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalitiesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevel:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevelEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalities:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalitiesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    type_of_inhalation_exposure_if_applicable: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposureIfApplicable
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfInhalationExposureIfApplicable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    mass_median_aerodynamic_diameter: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter
    ] = field(
        default=None,
        metadata={
            "name": "MassMedianAerodynamicDiameter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    geometric_standard_deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GeometricStandardDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    remarks_on_mmad: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnMMAD",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    details_on_exposure: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    analytical_verification_of_doses_or_concentrations: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    details_on_analytical_verification_of_doses_or_concentrations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalVerificationOfDosesOrConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    details_on_mating_procedure: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnMatingProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    duration_of_treatment_exposure: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "DurationOfTreatmentExposure",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            },
        )
    )
    frequency_of_treatment: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    duration_of_test: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    control_animals: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicity:
    class Meta:
        global_type = False

    developmental_toxicity: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicityDevelopmentalToxicity
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetuses:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetusesEfflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalities:
    class Meta:
        global_type = False

    fetal_abnormalities: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalitiesFetalAbnormalities
    ] = field(
        default=None,
        metadata={
            "name": "FetalAbnormalities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimals:
    class Meta:
        global_type = False

    efflevel: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimalsEfflevel
    ] = field(
        default=None,
        metadata={
            "name": "Efflevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalities:
    class Meta:
        global_type = False

    maternal_abnormalities: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalitiesMaternalAbnormalities
    ] = field(
        default=None,
        metadata={
            "name": "MaternalAbnormalities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetuses:
    class Meta:
        global_type = False

    fetal_body_weight_changes: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalBodyWeightChanges
    ] = field(
        default=None,
        metadata={
            "name": "FetalBodyWeightChanges",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "DescriptionIncidenceAndSeverity",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
            },
        )
    )
    reduction_in_number_of_live_offspring: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesReductionInNumberOfLiveOffspring
    ] = field(
        default=None,
        metadata={
            "name": "ReductionInNumberOfLiveOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_reduction_in_number_of_live_offspring: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityReductionInNumberOfLiveOffspring",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    changes_in_sex_ratio: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesChangesInSexRatio
    ] = field(
        default=None,
        metadata={
            "name": "ChangesInSexRatio",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_changes_in_sex_ratio: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityChangesInSexRatio",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    changes_in_litter_size_and_weights: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesChangesInLitterSizeAndWeights
    ] = field(
        default=None,
        metadata={
            "name": "ChangesInLitterSizeAndWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_changes_in_litter_size_and_weights: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityChangesInLitterSizeAndWeights",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    anogenital_distance_of_all_rodent_fetuses: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesAnogenitalDistanceOfAllRodentFetuses
    ] = field(
        default=None,
        metadata={
            "name": "AnogenitalDistanceOfAllRodentFetuses",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_changes_in_anogenital_distance: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityChangesInAnogenitalDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    changes_in_postnatal_survival: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesChangesInPostnatalSurvival
    ] = field(
        default=None,
        metadata={
            "name": "ChangesInPostnatalSurvival",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_changes_in_postnatal_survival: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityChangesInPostnatalSurvival",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    external_malformations: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesExternalMalformations
    ] = field(
        default=None,
        metadata={
            "name": "ExternalMalformations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_external_malformations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityExternalMalformations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    skeletal_malformations: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesSkeletalMalformations
    ] = field(
        default=None,
        metadata={
            "name": "SkeletalMalformations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_skeletal_malformations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeveritySkeletalMalformations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    visceral_malformations: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesVisceralMalformations
    ] = field(
        default=None,
        metadata={
            "name": "VisceralMalformations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_visceral_malformations: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityVisceralMalformations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    other_effects: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesOtherEffects
    ] = field(
        default=None,
        metadata={
            "name": "OtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    description_incidence_and_severity_other_effects: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionIncidenceAndSeverityOtherEffects",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    results_details_develop: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetailsDevelop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    effect_levels_fetuses: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesEffectLevelsFetuses
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsFetuses",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    fetal_abnormalities: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetusesFetalAbnormalities
    ] = field(
        default=None,
        metadata={
            "name": "FetalAbnormalities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimals:
    class Meta:
        global_type = False

    general_toxicity_maternal_animals: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsGeneralToxicityMaternalAnimals
    ] = field(
        default=None,
        metadata={
            "name": "GeneralToxicityMaternalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    maternal_developmental_toxicity: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalDevelopmentalToxicity
    ] = field(
        default=None,
        metadata={
            "name": "MaternalDevelopmentalToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    effect_levels_maternal_animals: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsEffectLevelsMaternalAnimals
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevelsMaternalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    maternal_abnormalities: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimalsMaternalAbnormalities
    ] = field(
        default=None,
        metadata={
            "name": "MaternalAbnormalities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussion:
    class Meta:
        global_type = False

    results_maternal_animals: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsMaternalAnimals
    ] = field(
        default=None,
        metadata={
            "name": "ResultsMaternalAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    results_fetuses: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionResultsFetuses
    ] = field(
        default=None,
        metadata={
            "name": "ResultsFetuses",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    developmental_toxicity: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionDevelopmentalToxicity
    ] = field(
        default=None,
        metadata={
            "name": "DevelopmentalToxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0",
        },
    )


@dataclass
class EndpointStudyRecordDevelopmentalToxicityTeratogenicity:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.DevelopmentalToxicityTeratogenicity"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-DevelopmentalToxicityTeratogenicity/9.0"

    administrative_data: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordDevelopmentalToxicityTeratogenicityApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
