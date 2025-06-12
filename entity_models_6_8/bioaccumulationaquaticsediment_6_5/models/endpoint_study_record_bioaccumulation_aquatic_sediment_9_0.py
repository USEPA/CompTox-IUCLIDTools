from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from bioaccumulationaquaticsediment_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    A102,
    E04,
    E34,
    E147,
    F34,
    F102,
    F119,
    F120,
    F121,
    F122,
    F123,
    F138,
    F141,
    F142,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660150,
    Pg660151,
    Pg660161,
    Pg660171,
    Pg660177,
    Pg660180,
    Pg660490,
    Pg661157,
    Pg661166,
    Pg661567,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td330,
)
from bioaccumulationaquaticsediment_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0"


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660151] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660150] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusionValidityCriteriaFulfilled(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsModelAndSoftware:
    class Meta:
        global_type = False

    model_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ModelNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    software_name_and_version: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoftwareNameAndVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    details_on_sampling: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignJustificationForMethod(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660180] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignRouteOfExposure(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F142] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTestType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F122] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalDepurationDuration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignWaterMediaType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660161] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterialsRadiolabelling(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganismsTestOrganismsSpecies(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E147] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutionsVehicle(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661574] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661576] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661577] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661579] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F120] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F121] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryConcInEnvironmentDose(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660171] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661567] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTemp(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[A102] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F141] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryValue(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Td330] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryDepurationTime(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[E04] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryElimination(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F123] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolitesEntryIdno(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolitesEntryMaximumOccurrence(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661166] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryLipidContent(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[F119] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryTimePoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[F138] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionMetabolitesDetails(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[E34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRateConstant(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660177] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRemarksOnResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    validity_criteria_fulfilled: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusionValidityCriteriaFulfilled
    ] = field(
        default=None,
        metadata={
            "name": "ValidityCriteriaFulfilled",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesign:
    class Meta:
        global_type = False

    route_of_exposure: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignRouteOfExposure
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    justification_for_method: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignJustificationForMethod
    ] = field(
        default=None,
        metadata={
            "name": "JustificationForMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    test_type: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTestType
    ] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    water_media_type: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignWaterMediaType
    ] = field(
        default=None,
        metadata={
            "name": "WaterMediaType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    total_exposure_uptake_duration: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalExposureUptakeDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    total_depuration_duration: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesignTotalDepurationDuration
    ] = field(
        default=None,
        metadata={
            "name": "TotalDepurationDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditions:
    class Meta:
        global_type = False

    hardness: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    test_temperature: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    ph: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    dissolved_oxygen: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "DissolvedOxygen",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    toc: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "TOC",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    salinity: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    conductivity: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    details: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    nominal_and_measured_concentrations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "NominalAndMeasuredConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    reference_substance_positive_control: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl
    ] = field(
        default=None,
        metadata={
            "name": "ReferenceSubstancePositiveControl",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    details_on_estimation_of_bioconcentration: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnEstimationOfBioconcentration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganisms:
    class Meta:
        global_type = False

    test_organisms_species: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganismsTestOrganismsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganismsSpecies",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    details_on_test_organisms: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutions:
    class Meta:
        global_type = False

    vehicle: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutionsVehicle
    ] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    details_on_preparation_of_test_solutions_spiked_fish_food_or_sediment: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnPreparationOfTestSolutionsSpikedFishFoodOrSediment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    conc_in_environment_dose: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryConcInEnvironmentDose
    ] = field(
        default=None,
        metadata={
            "name": "ConcInEnvironmentDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    temp: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTemp
    ] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    ph: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Ph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    type_value: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    value: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryValue
    ] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    basis: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryBasis
    ] = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    time_of_plateau: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau
    ] = field(
        default=None,
        metadata={
            "name": "TimeOfPlateau",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    calculation_basis: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis
    ] = field(
        default=None,
        metadata={
            "name": "CalculationBasis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    elimination: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryElimination
    ] = field(
        default=None,
        metadata={
            "name": "Elimination",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    depuration_time: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryDepurationTime
    ] = field(
        default=None,
        metadata={
            "name": "DepurationTime",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolitesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    idno: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolitesEntryIdno
    ] = field(
        default=None,
        metadata={
            "name": "IDNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    identity_of_compound: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    parent_compound_s: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "ParentCompoundS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    maximum_occurrence: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolitesEntryMaximumOccurrence
    ] = field(
        default=None,
        metadata={
            "name": "MaximumOccurrence",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    lipid_content: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryLipidContent
    ] = field(
        default=None,
        metadata={
            "name": "LipidContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    time_point: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryTimePoint
    ] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    key_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    rate_constant: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRateConstant
    ] = field(
        default=None,
        metadata={
            "name": "RateConstant",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    field5295: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    identifiers: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Identifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    source: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource
    ] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    experimental_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    reference_for_experimental_value: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ReferenceForExperimentalValue",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
            },
        )
    )
    predicted_value: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PredictedValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    accuracy_of_the_prediction: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AccuracyOfThePrediction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactor:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactorEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepuration:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepurationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolites:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolitesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContent:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContentEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstants:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstantsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    robust_study: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    used_for_classification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    used_for_msds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    test_solutions: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestSolutions
    ] = field(
        default=None,
        metadata={
            "name": "TestSolutions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    test_organisms: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestOrganisms
    ] = field(
        default=None,
        metadata={
            "name": "TestOrganisms",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    study_design: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsStudyDesign
    ] = field(
        default=None,
        metadata={
            "name": "StudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    test_conditions: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsTestConditions
    ] = field(
        default=None,
        metadata={
            "name": "TestConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    model_and_software: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsModelAndSoftware
    ] = field(
        default=None,
        metadata={
            "name": "ModelAndSoftware",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions:
    class Meta:
        global_type = False

    fit_with_the_applicability_domain: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    justification_for_the_fit_with_the_applicability_domain: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTheFitWithTheApplicabilityDomain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    fit_with_the_space_defined_by_the_training_set_of_the_model: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel
    ] = field(
        default=None,
        metadata={
            "name": "FitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    mechanistic_and_metabolic_considerations: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "MechanisticAndMetabolicConsiderations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    similar_substances_with_experimental_data: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData
    ] = field(
        default=None,
        metadata={
            "name": "SimilarSubstancesWithExperimentalData",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    performance_of_the_model_for_similar_substances: List[
        MultilingualTextFieldMultiLine
    ] = field(
        default_factory=list,
        metadata={
            "name": "PerformanceOfTheModelForSimilarSubstances",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    conclusions_on_applicability_domain_and_reliability: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "ConclusionsOnApplicabilityDomainAndReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    uncertainty: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty
    ] = field(
        default=None,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussion:
    class Meta:
        global_type = False

    lipid_content: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionLipidContent
    ] = field(
        default=None,
        metadata={
            "name": "LipidContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    bioaccumulation_factor: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionBioaccumulationFactor
    ] = field(
        default=None,
        metadata={
            "name": "BioaccumulationFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    depuration: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionDepuration
    ] = field(
        default=None,
        metadata={
            "name": "Depuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    rate_constants: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionRateConstants
    ] = field(
        default=None,
        metadata={
            "name": "RateConstants",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    kinetic_parameters: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "KineticParameters",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    metabolites: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Metabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    metabolites_details: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionMetabolitesDetails
    ] = field(
        default=None,
        metadata={
            "name": "MetabolitesDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    identity_of_metabolites: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionIdentityOfMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "IdentityOfMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    results_with_reference_substance: List[MultilingualTextFieldMultiLine] = (
        field(
            default_factory=list,
            metadata={
                "name": "ResultsWithReferenceSubstance",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
            },
        )
    )
    details_on_results: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    reported_statistics: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ReportedStatistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    additional_information_about_applicability_domain_and_reliability_of_qsarpredictions: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationAboutApplicabilityDomainAndReliabilityOfQSARPredictions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0",
        },
    )


@dataclass
class EndpointStudyRecordBioaccumulationAquaticSediment:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.BioaccumulationAquaticSediment"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-BioaccumulationAquaticSediment/9.0"

    administrative_data: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordBioaccumulationAquaticSedimentApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
