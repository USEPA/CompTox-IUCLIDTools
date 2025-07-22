from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from entity_models_6_4.residuesinrotationalcrops_6_5.models.common_types_oecd_v5 import (
    A31,
    A36,
    C1112,
    N64,
    N78,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z38,
    Z40,
    Z49,
    Z51,
    Z52,
    Z53,
    Z55,
    Z56,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660353,
    Pg660475,
    Pg660481,
    Pg660490,
    Pg660497,
    Pg660504,
    Pg660505,
    Pg660506,
    Pg660507,
    Pg660508,
    Pg660509,
    Pg660510,
    Pg660511,
    Pg660512,
    Pg660513,
    Pg660516,
    Pg660519,
    Pg660542,
    Pg6604961,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0"


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalysisOfSoil:
    class Meta:
        global_type = False

    details_on_sampling_of_soil: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSamplingOfSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    details_on_analytical_methodology_for_soil_residues: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethodologyForSoilResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrr:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrrppm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660353] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsApplicantSummaryAndConclusionInterpretationOfResults:
    class Meta:
        global_type = False

    value: Optional[Z55] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Z53] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsProductType:
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCountry:
    class Meta:
        global_type = False

    value: Optional[A31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroup:
    class Meta:
        global_type = False

    value: Optional[Z56] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroupingPrimary:
    class Meta:
        global_type = False

    value: Optional[Pg660504] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsGeographicRegion:
    class Meta:
        global_type = False

    value: Optional[Pg660513] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsStateProvince:
    class Meta:
        global_type = False

    value: Optional[Pg660542] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTestSiteType:
    class Meta:
        global_type = False

    value: Optional[Z49] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfCrop:
    class Meta:
        global_type = False

    value: Optional[Z51] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfTrial:
    class Meta:
        global_type = False

    value: Optional[Pg660519] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryBareSoil:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryMethodOfApplication:
    class Meta:
        global_type = False

    value: Optional[Pg660505] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntrySeedingRate:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660506] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountAiseedActual:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660510] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountOfWaterUsedInSpray:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660509] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountActual:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660509] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountCumulative:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660511] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryNominalAicontent:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660508] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryFormulationType:
    class Meta:
        global_type = False

    value: Optional[Pg660507] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryControlPlot:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalyticalMethodologyFortificationLevel:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryTrialNo:
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByRecovery:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByStorageStability:
    class Meta:
        global_type = False

    value: Optional[Z38] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCalculated:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCorrected:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelMeasured:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySampledMaterialCommodity:
    class Meta:
        global_type = False

    value: Optional[Pg660497] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySamplingNo:
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySamplingTiming:
    class Meta:
        global_type = False

    value: Optional[Pg660512] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryTotalMean:
    class Meta:
        global_type = False

    unit_code: Optional[Pg6604961] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryTrialNo:
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryMetaboliteFraction:
    class Meta:
        global_type = False

    value: Optional[Pg660481] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryRadiolabelNo:
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryRemarksOnResult:
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordResiduesInRotationalCropsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordResiduesInRotationalCropsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    geographic_location: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GeographicLocation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    trial_id_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrialIdNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    trial_deviation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TrialDeviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    geographic_region: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsGeographicRegion
    ] = field(
        default=None,
        metadata={
            "name": "GeographicRegion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    state_province: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsStateProvince
    ] = field(
        default=None,
        metadata={
            "name": "StateProvince",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    county: List[str] = field(
        default_factory=list,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    city: List[str] = field(
        default_factory=list,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    gpscoordinates: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GPSCoordinates",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    gap: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GAP",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    type_of_crop: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfCrop
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfCrop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    type_of_trial: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsTypeOfTrial
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfTrial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    crop_grouping_primary: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroupingPrimary
    ] = field(
        default=None,
        metadata={
            "name": "CropGroupingPrimary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    crop_group: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristicsCropGroup
    ] = field(
        default=None,
        metadata={
            "name": "CropGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    crop: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Crop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    crop_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CropCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    crop_variety: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CropVariety",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    replant_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReplantNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    date_of_planting: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfPlanting",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    crop_plant_back_interval: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CropPlantBackInterval",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    crop_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CropInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    soil_characterization: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SoilCharacterization",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other_details_on_test_crops: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherDetailsOnTestCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntry:
    class Meta:
        global_type = False

    name_of_ai: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOfAI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    nominal_aicontent: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryNominalAicontent
    ] = field(
        default=None,
        metadata={
            "name": "NominalAIContent",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    applied_amount_actual: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountActual
    ] = field(
        default=None,
        metadata={
            "name": "AppliedAmountActual",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    amount_aiseed_actual: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountAiseedActual
    ] = field(
        default=None,
        metadata={
            "name": "AmountAISeedActual",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    applied_amount_cumulative: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAppliedAmountCumulative
    ] = field(
        default=None,
        metadata={
            "name": "AppliedAmountCumulative",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    adjuvant_added: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AdjuvantAdded",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    amount_of_water_used_in_spray: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredientsEntryAmountOfWaterUsedInSpray
    ] = field(
        default=None,
        metadata={
            "name": "AmountOfWaterUsedInSpray",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    other_details_on_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherDetailsOnApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalyticalMethodology:
    class Meta:
        global_type = False

    details_on_sample_collection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleCollection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    details_on_sample_handling_and_preparation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSampleHandlingAndPreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    details_on_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    fortification_level: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalyticalMethodologyFortificationLevel
    ] = field(
        default=None,
        metadata={
            "name": "FortificationLevel",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    recovery: Optional[str] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordResiduesInRotationalCropsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntry:
    class Meta:
        global_type = False

    analyte_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalyteIdentity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    analysis_sample_description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisSampleDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    extraction_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExtractionDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    analysis_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AnalysisDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    storage_stability_factor: Optional[str] = field(
        default=None,
        metadata={
            "name": "StorageStabilityFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    use_of_factor: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UseOfFactor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    correction_by_storage_stability: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByStorageStability
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    recovery: Optional[str] = field(
        default=None,
        metadata={
            "name": "Recovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    correction_by_recovery: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryCorrectionByRecovery
    ] = field(
        default=None,
        metadata={
            "name": "CorrectionByRecovery",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    reference_portion: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReferencePortion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    residue_level_measured: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelMeasured
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelMeasured",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    residue_level_calculated: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCalculated
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCalculated",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    residue_level_corrected: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevelsEntryResidueLevelCorrected
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevelCorrected",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntry:
    class Meta:
        global_type = False

    soil_sample: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SoilSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamples:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordResiduesInRotationalCropsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntry:
    class Meta:
        global_type = False

    description_of_test_item: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionOfTestItem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    formulation_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryFormulationType
    ] = field(
        default=None,
        metadata={
            "name": "FormulationType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    trade_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradeName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    active_ingredients: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItemEntryActiveIngredients
    ] = field(
        default=None,
        metadata={
            "name": "ActiveIngredients",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntry:
    class Meta:
        global_type = False

    trial_no: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryTrialNo
    ] = field(
        default=None,
        metadata={
            "name": "TrialNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    sampling_no: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySamplingNo
    ] = field(
        default=None,
        metadata={
            "name": "SamplingNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    sampling_timing: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySamplingTiming
    ] = field(
        default=None,
        metadata={
            "name": "SamplingTiming",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    growth_stage: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    date_of_sampling: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfSampling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
            "nillable": True,
        },
    )
    sampling_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SamplingInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    sampled_material_commodity: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntrySampledMaterialCommodity
    ] = field(
        default=None,
        metadata={
            "name": "SampledMaterialCommodity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    residue_levels: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryResidueLevels
    ] = field(
        default=None,
        metadata={
            "name": "ResidueLevels",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    total_mean: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsSamplingAndResiduesEntryTotalMean
    ] = field(
        default=None,
        metadata={
            "name": "TotalMean",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntry:
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    metabolite_fraction: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryMetaboliteFraction
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    identity_of_parent_or_metabolite: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfParentOrMetabolite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    trrs_in_soil_samples: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamples
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInSoilSamples",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoil:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntry:
    class Meta:
        global_type = False

    application_no: Optional[int] = field(
        default=None,
        metadata={
            "name": "ApplicationNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    growth_stage: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStage",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    date_of_application: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    seeding_rate: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntrySeedingRate
    ] = field(
        default=None,
        metadata={
            "name": "SeedingRate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    test_item: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplicationApplicationEntryTestItem
    ] = field(
        default=None,
        metadata={
            "name": "TestItem",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoil:
    class Meta:
        global_type = False

    radioactive_residues_in_soil: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoil
    ] = field(
        default=None,
        metadata={
            "name": "RadioactiveResiduesInSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussion:
    class Meta:
        global_type = False

    storage_stability: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    summary_of_radioactive_residues_in_crops: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCrops
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfRadioactiveResiduesInCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    summary_of_radioactive_residues_in_soil: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoil
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfRadioactiveResiduesInSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordResiduesInRotationalCropsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntry:
    class Meta:
        global_type = False

    plot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlotID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    control_plot: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryControlPlot
    ] = field(
        default=None,
        metadata={
            "name": "ControlPlot",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    plot_description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PlotDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    environmental_conditions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    details_on_test_site: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    application: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntryApplication
    ] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    sampling_and_analytical_methodology: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalyticalMethodology
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalyticalMethodology",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    sampling_and_analysis_of_soil: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescriptionPlotEntrySamplingAndAnalysisOfSoil
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysisOfSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntry:
    class Meta:
        global_type = False

    trial_no: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryTrialNo
    ] = field(
        default=None,
        metadata={
            "name": "TrialNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    geographic_location_and_soil_characteristics: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryGeographicLocationAndSoilCharacteristics
    ] = field(
        default=None,
        metadata={
            "name": "GeographicLocationAndSoilCharacteristics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    plot_description: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePatternTrialInformationEntryPlotDescription
    ] = field(
        default=None,
        metadata={
            "name": "PlotDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
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
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethods:
    class Meta:
        global_type = False

    background_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    product_type: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    study_use_pattern: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsStudyUsePattern
    ] = field(
        default=None,
        metadata={
            "name": "StudyUsePattern",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordResiduesInRotationalCropsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordResiduesInRotationalCrops:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.ResiduesInRotationalCrops"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-ResiduesInRotationalCrops/5.0"

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
