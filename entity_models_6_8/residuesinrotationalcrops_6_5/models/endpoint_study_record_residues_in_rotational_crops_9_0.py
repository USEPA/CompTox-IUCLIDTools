from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from residuesinrotationalcrops_6_5.models.common_types_oecd_v9 import (
    A31,
    A36,
    B04,
    N64,
    N78,
    Y143,
    Z02,
    Z03,
    Z06,
    Z08,
    Z38,
    Z40,
    Z49,
    Z51,
    Z52,
    Z53,
    Z55,
    Z56,
    C1112Crops,
    KgrainWeight,
    Pg660009Crops,
    Pg660010Crops,
    Pg660013Crops,
    Pg660353,
    Pg660497,
    Pg660504,
    Pg660505,
    Pg660506,
    Pg660508,
    Pg660509,
    Pg660510,
    Pg660511,
    Pg660512,
    Pg660513,
    Pg660519,
    Pg660542,
    Pg661157,
    Pg661254,
    Pg661255,
    Pg661259,
    Pg6604961,
    Z05Crops,
    Z30Crops,
)
from residuesinrotationalcrops_6_5.models.platform_fields import (
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

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0"


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660009Crops] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntryReasonPurpose(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660010Crops] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaiving(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaivingJustification(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataEndpoint(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660353] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataPurposeFlag(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataRationalReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660013Crops] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataReliability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataStudyResultType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z05Crops] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsApplicantSummaryAndConclusionInterpretationOfResults(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z55] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsDataSourceDataAccess(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsDataSourceDataProtectionClaimed(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z30Crops] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntryFortificationEntryFortificationLevel(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGlpcomplianceStatement(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryDeviation(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryGuideline(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z53] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryQualifier(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsProductType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[C1112Crops] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCountry(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroup(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z56] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroupingPrimary(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660504] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsGeographicRegion(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660513] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsStateProvince(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660542] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTestSiteType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z49] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfCrop(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z51] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfTrial(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660519] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryBareSoil(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryCrownHeightDuringApplication(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661254] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryLeafWallArea(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661255] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryMethodOfApplication(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660505] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryPlantRowDistance(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661254] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntrySeedingRate(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660506] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountAiseedActual(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660510] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountOfWaterUsedInSpray(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660509] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountAiactual(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg661259] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountActual(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660509] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountCumulative(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660511] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryNominalAicontent(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg660508] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryFormulationType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[B04] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryThousandGrainWeight(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[KgrainWeight] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryControlPlot(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalysisOfSoil:
    class Meta:
        global_type = False

    details_on_sampling_of_soil: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSamplingOfSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    details_on_analytical_methodology_for_soil_residues: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethodologyForSoilResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalyticalMethodology:
    class Meta:
        global_type = False

    details_on_sample_collection: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    details_on_sample_handling_and_preparation: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleHandlingAndPreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    additional_test_material_information: Optional[
        DocumentReferenceMultipleField
    ] = field(
        default=None,
        metadata={
            "name": "AdditionalTestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        MultilingualTextFieldLarge
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByRecovery(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByStorageStability(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCalculated(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCorrected(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelMeasured(
    BasePhysicalQuantityRangeField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    lower_qualifier: Optional[LowerQualifier] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    upper_qualifier: Optional[UpperQualifier] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySampledMaterialCommodity(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660497] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySamplingTiming(
    BasePicklistField
):
    class Meta:
        global_type = False

    value: Optional[Pg660512] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryTotalMean(
    BasePhysicalQuantityField
):
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    unit_other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataProtection(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    legislation: List[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    interpretation_of_results: Optional[
        EndpointStudyRecordResiduesInRotationalCropsApplicantSummaryAndConclusionInterpretationOfResults
    ] = field(
        default=None,
        metadata={
            "name": "InterpretationOfResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsDataSource:
    class Meta:
        global_type = False

    reference: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordResiduesInRotationalCropsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordResiduesInRotationalCropsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntryFortificationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    fortification_level: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntryFortificationEntryFortificationLevel
    ] = field(
        default=None,
        metadata={
            "name": "FortificationLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    version_remarks: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristics:
    class Meta:
        global_type = False

    test_site_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTestSiteType
    ] = field(
        default=None,
        metadata={
            "name": "TestSiteType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    geographic_location: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "GeographicLocation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    trial_deviation: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TrialDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    country: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCountry
    ] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    geographic_region: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsGeographicRegion
    ] = field(
        default=None,
        metadata={
            "name": "GeographicRegion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    state_province: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsStateProvince
    ] = field(
        default=None,
        metadata={
            "name": "StateProvince",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    county: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    city: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    gpscoordinates: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "GPSCoordinates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    type_of_crop: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfCrop
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfCrop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    type_of_trial: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfTrial
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfTrial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crop_grouping_primary: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroupingPrimary
    ] = field(
        default=None,
        metadata={
            "name": "CropGroupingPrimary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crop_group: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroup
    ] = field(
        default=None,
        metadata={
            "name": "CropGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crop: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Crop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crop_code: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CropCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crop_variety: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CropVariety",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    replant_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReplantNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    date_of_planting: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfPlanting",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    date_of_seeding: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfSeeding",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    date_of_flowering_beginning: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfFloweringBeginning",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    date_of_flowering_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfFloweringEnd",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    date_of_harvest_begin: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfHarvestBegin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    date_of_harvest_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfHarvestEnd",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    crop_plant_back_interval: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CropPlantBackInterval",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crop_information: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "CropInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    soil_characterization: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SoilCharacterization",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other_details_on_test_crops: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "OtherDetailsOnTestCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    related_substance_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedSubstanceInfo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    name_of_ai: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOfAI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    nominal_aicontent: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryNominalAicontent
    ] = field(
        default=None,
        metadata={
            "name": "NominalAIContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    applied_amount_actual: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountActual
    ] = field(
        default=None,
        metadata={
            "name": "AppliedAmountActual",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    applied_amount_aiactual: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountAiactual
    ] = field(
        default=None,
        metadata={
            "name": "AppliedAmountAIActual",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    amount_aiseed_actual: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountAiseedActual
    ] = field(
        default=None,
        metadata={
            "name": "AmountAISeedActual",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    applied_amount_cumulative: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountCumulative
    ] = field(
        default=None,
        metadata={
            "name": "AppliedAmountCumulative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    adjuvant_added: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "AdjuvantAdded",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    amount_of_water_used_in_spray: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountOfWaterUsedInSpray
    ] = field(
        default=None,
        metadata={
            "name": "AmountOfWaterUsedInSpray",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    type_value: Optional[
        EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType
    ] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    analysis_sample_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisSampleDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    storage_stability_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StorageStabilityFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    use_of_factor: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "UseOfFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    correction_by_storage_stability: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByStorageStability
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    recovery: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    correction_by_recovery: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByRecovery
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    reference_portion: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "ReferencePortion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    residue_level_measured: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelMeasured
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    calculated_analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "CalculatedAnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    residue_level_calculated: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCalculated
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    residue_level_corrected: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCorrected
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCorrected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntryFortification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntryFortificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredients:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevels:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    study_period_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodStartDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    study_period_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StudyPeriodEndDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    study_period: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    justification_for_type_of_information: List[MultilingualTextFieldLarge] = (
        field(
            default_factory=list,
            metadata={
                "name": "JustificationForTypeOfInformation",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            },
        )
    )
    attached_justification: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    analysed_sample_portion_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "AnalysedSamplePortionID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    analysed_sample_portion_description: List[MultilingualTextFieldSmall] = (
        field(
            default_factory=list,
            metadata={
                "name": "AnalysedSamplePortionDescription",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            },
        )
    )
    fortification: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntryFortification
    ] = field(
        default=None,
        metadata={
            "name": "Fortification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    description_of_test_item: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionOfTestItem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    formulation_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryFormulationType
    ] = field(
        default=None,
        metadata={
            "name": "FormulationType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    trade_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradeName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    active_ingredients: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredients
    ] = field(
        default=None,
        metadata={
            "name": "ActiveIngredients",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    trial_idno: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TrialIDNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    plot_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "PlotID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    sampling_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "SamplingID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    sampling_timing: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySamplingTiming
    ] = field(
        default=None,
        metadata={
            "name": "SamplingTiming",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    growth_stage_code: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStageCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    growth_stage: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    date_of_sampling: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    sampling_information: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "SamplingInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    sampled_material_commodity: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySampledMaterialCommodity
    ] = field(
        default=None,
        metadata={
            "name": "SampledMaterialCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    sampled_material_commodity_description: List[
        MultilingualTextFieldSmall
    ] = field(
        default_factory=list,
        metadata={
            "name": "SampledMaterialCommodityDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    residue_levels: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevels
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    total_mean: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryTotalMean
    ] = field(
        default=None,
        metadata={
            "name": "TotalMean",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortion:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortionEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItem:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResidues:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    details_on_analytical_methods: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    combinations_of_substance_and_sample_portion: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntryCombinationsOfSubstanceAndSamplePortion
    ] = field(
        default=None,
        metadata={
            "name": "CombinationsOfSubstanceAndSamplePortion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    application_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "ApplicationNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    bare_soil: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryBareSoil
    ] = field(
        default=None,
        metadata={
            "name": "BareSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    growth_stage_code: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStageCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    growth_stage: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    plant_row_distance: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryPlantRowDistance
    ] = field(
        default=None,
        metadata={
            "name": "PlantRowDistance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    crown_height_during_application: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryCrownHeightDuringApplication
    ] = field(
        default=None,
        metadata={
            "name": "CrownHeightDuringApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    leaf_wall_area: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryLeafWallArea
    ] = field(
        default=None,
        metadata={
            "name": "LeafWallArea",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    date_of_application: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
            "nillable": True,
        },
    )
    method_of_application: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryMethodOfApplication
    ] = field(
        default=None,
        metadata={
            "name": "MethodOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    seeding_rate: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntrySeedingRate
    ] = field(
        default=None,
        metadata={
            "name": "SeedingRate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    thousand_grain_weight: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryThousandGrainWeight
    ] = field(
        default=None,
        metadata={
            "name": "ThousandGrainWeight",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    test_item: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItem
    ] = field(
        default=None,
        metadata={
            "name": "TestItem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCrops:
    class Meta:
        global_type = False

    sampling_and_residues: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResidues
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplication:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussion:
    class Meta:
        global_type = False

    storage_stability: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    summary_of_radioactive_residues_in_crops: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCrops
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfRadioactiveResiduesInCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethods:
    class Meta:
        global_type = False

    analytical_method: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethodsAnalyticalMethod
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplication:
    class Meta:
        global_type = False

    application: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplication
    ] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    other_details_on_application: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "OtherDetailsOnApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    plot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlotID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    control_plot: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryControlPlot
    ] = field(
        default=None,
        metadata={
            "name": "ControlPlot",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    corresponding_control_plot_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CorrespondingControlPlotID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    plot_description: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "PlotDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    environmental_conditions: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    details_on_test_site: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    application: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplication
    ] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    sampling_and_analytical_methodology: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalyticalMethodology
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    sampling_and_analysis_of_soil: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalysisOfSoil
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysisOfSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlot:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescription:
    class Meta:
        global_type = False

    plot: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlot
    ] = field(
        default=None,
        metadata={
            "name": "Plot",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntry(
    RepeatableEntryType
):
    class Meta:
        global_type = False

    trial_id_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrialIdNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    geographic_location_and_soil_characteristics: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristics
    ] = field(
        default=None,
        metadata={
            "name": "GeographicLocationAndSoilCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    plot_description: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescription
    ] = field(
        default=None,
        metadata={
            "name": "PlotDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePattern:
    class Meta:
        global_type = False

    trial_information: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformation
    ] = field(
        default=None,
        metadata={
            "name": "TrialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethods:
    class Meta:
        global_type = False

    product_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    method_no_guideline: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    analytical_methods: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnalyticalMethods
    ] = field(
        default=None,
        metadata={
            "name": "AnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    study_use_pattern: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePattern
    ] = field(
        default=None,
        metadata={
            "name": "StudyUsePattern",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCrops:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ResiduesInRotationalCrops"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/9.0"

    administrative_data: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[
        EndpointStudyRecordResiduesInRotationalCropsDataSource
    ] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        },
    )
    materials_and_methods: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordResiduesInRotationalCropsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
