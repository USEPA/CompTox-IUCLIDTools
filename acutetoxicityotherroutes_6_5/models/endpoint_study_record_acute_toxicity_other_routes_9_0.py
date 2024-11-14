from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from acutetoxicityotherroutes_6_5.models.common_types_oecd_v9 import (
    A36,
    E105,
    N64,
    N78,
    T02,
    T10,
    T12,
    T24,
    T48,
    T148,
    T254,
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
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660287,
    Pg660304,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from acutetoxicityotherroutes_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0"


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660304] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureControlAnimals(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureRouteOfAdministration(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T254] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T48] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsLimitTest(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimalsSex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimalsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimalsStrain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryBasedOn(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryEffectLevel(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[T12] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T10] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660287] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntrySex(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryCl(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    vehicle: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    details_on_exposure: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    doses: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Doses",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    control_animals: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureControlAnimals
    ] = field(
        default=None,
        metadata={
            "name": "ControlAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    details_on_study_design: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    high_dose_level_used: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed
    ] = field(
        default=None,
        metadata={
            "name": "HighDoseLevelUsed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    justification_for_deviation_from_the_high_dose_level: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForDeviationFromTheHighDoseLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    organism_details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    effect_level: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryEffectLevel
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    based_on: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryBasedOn
    ] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    cl: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryCl
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevels:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevelsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    limit_test: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsLimitTest
    ] = field(
        default=None,
        metadata={
            "name": "LimitTest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussion:
    class Meta:
        global_type = False

    effect_levels: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionEffectLevels
    ] = field(
        default=None,
        metadata={
            "name": "EffectLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    mortality: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Mortality",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    clinical_signs: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ClinicalSigns",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    body_weight: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "BodyWeight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    gross_pathology: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "GrossPathology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    other_findings: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OtherFindings",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0",
        },
    )


@dataclass
class EndpointStudyRecordAcuteToxicityOtherRoutes:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.AcuteToxicityOtherRoutes"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-AcuteToxicityOtherRoutes/9.0"

    administrative_data: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordAcuteToxicityOtherRoutesApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
