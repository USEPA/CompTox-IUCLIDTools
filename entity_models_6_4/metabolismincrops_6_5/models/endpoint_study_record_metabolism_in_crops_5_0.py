from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.metabolismincrops_6_5.models.common_types_oecd_v5 import (
    A36,
    C1112,
    F137,
    N64,
    N78,
    T148,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z49,
    Z50,
    Z51,
    Z52,
    Z56,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660289,
    Pg660473,
    Pg660474,
    Pg660475,
    Pg660480,
    Pg660481,
    Pg660490,
    Pg660516,
    Pg660517,
    Pg660518,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0"


@dataclass
class EndpointStudyRecordMetabolismInCropsApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupsEntry:
    class Meta:
        global_type = False

    test_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    phipbi: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PHIPBI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    method_of_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    rate_sof_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RateSOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    number_of_applications: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfApplications",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    timing_of_applications: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TimingOfApplications",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    matrix_racor_extract: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MatrixRACOrExtract",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    experimental_descriptor: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExperimentalDescriptor",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    reference_citation: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceCitation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    radiolabel_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    test_crop_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestCropNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    soil_type_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "SoilTypeNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsApplicationUsePatternInformationEntry:
    class Meta:
        global_type = False

    method_of_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    rate_sof_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RateSOfApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    number_of_applications: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfApplications",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    timing_of_applications: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TimingOfApplications",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    phipbi: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PHIPBI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsEnvironmentalConditions:
    class Meta:
        global_type = False

    temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    rainfall: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Rainfall",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lighting: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    potential_for_photodegradation_of_substance: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PotentialForPhotodegradationOfSubstance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysisOfSoil:
    class Meta:
        global_type = False

    details_on_sampling_of_soil: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSamplingOfSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    details_on_analytical_methodology_for_soil_residues: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnAnalyticalMethodologyForSoilResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemesEntry:
    class Meta:
        global_type = False

    description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    illustration_picture_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPictureGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiochemicalPurity:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryCecmeg100G:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryClay:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryOrganicMatter:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryPh:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntrySand:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntrySilt:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrr:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrrppm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudyEntry:
    class Meta:
        global_type = False

    identity_of_compound: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditionsEntry:
    class Meta:
        global_type = False

    matrix_racor_extract: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MatrixRACOrExtract",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    plant_back_interval_pbi: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PlantBackIntervalPBI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    storage_temperature: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StorageTemperature",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    actual_study_duration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ActualStudyDuration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    interval_limit_of_demonstrated_storage_stability: List[str] = field(
        default_factory=list,
        metadata={
            "name": "IntervalLimitOfDemonstratedStorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrr:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrrppm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrr:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrrppm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueExtractionEfficiency:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueMgKg:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryOverallExtractionEfficiency:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryRecoveredEquivalentsMgKg:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrr:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrrppm:
    class Meta:
        global_type = False

    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660289] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroups:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroupsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsApplicationUsePatternInformation:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsApplicationUsePatternInformationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[Z50] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsProductType:
    class Meta:
        global_type = False

    value: Optional[C1112] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemes:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiolabelNo:
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityAsReceived:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660474] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityOfDose:
    class Meta:
        global_type = False

    unit_code: Optional[Pg660474] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperQualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    lower_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    upper_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelling:
    class Meta:
        global_type = False

    value: Optional[T148] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryCropGroup:
    class Meta:
        global_type = False

    value: Optional[Z56] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryScientificName:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryTestCropNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryTypeOfRotationalCrop:
    class Meta:
        global_type = False

    value: Optional[Z51] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntrySoilTypeNo:
    class Meta:
        global_type = False

    value: Optional[F137] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesTestSiteType:
    class Meta:
        global_type = False

    value: Optional[Z49] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryExpertise:
    class Meta:
        global_type = False

    value: Optional[Pg660517] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryIdno:
    class Meta:
        global_type = False

    value: Optional[Pg660490] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTypeOfExpertise:
    class Meta:
        global_type = False

    value: Optional[Pg660518] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryMetaboliteFraction:
    class Meta:
        global_type = False

    value: Optional[Pg660480] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryRadiolabelNo:
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryRemarksOnResult:
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudy:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudyEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditions:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditionsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryMetaboliteFraction:
    class Meta:
        global_type = False

    value: Optional[Pg660481] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryRadiolabelNo:
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryRemarksOnResult:
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryMetaboliteFraction:
    class Meta:
        global_type = False

    value: Optional[Pg660481] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryRadiolabelNo:
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryRemarksOnResult:
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryTypeOfMethod:
    class Meta:
        global_type = False

    value: Optional[Pg660473] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryRadiolabelNo:
    class Meta:
        global_type = False

    value: Optional[Pg660475] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryRemarksOnResult:
    class Meta:
        global_type = False

    value: Optional[Pg660516] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordMetabolismInCropsDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordMetabolismInCropsDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAppendixTreatmentGroups:
    class Meta:
        global_type = False

    treatment_groups: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAppendixTreatmentGroupsTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "TreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsApplication:
    class Meta:
        global_type = False

    use_pattern_information: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsApplicationUsePatternInformation
    ] = field(
        default=None,
        metadata={
            "name": "UsePatternInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    details_on_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    further_details_on_study_design: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FurtherDetailsOnStudyDesign",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysis:
    class Meta:
        global_type = False

    details_on_sampling_and_analytical_methods: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSamplingAndAnalyticalMethods",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    details_on_extraction_and_analysis: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExtractionAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    details_on_identification_and_characterisation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnIdentificationAndCharacterisation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    flowchart_of_extraction_and_fractionation_schemes: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysisFlowchartOfExtractionAndFractionationSchemes
    ] = field(
        default=None,
        metadata={
            "name": "FlowchartOfExtractionAndFractionationSchemes",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntry:
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    smilesnotation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SMILESNotation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    radiochemical_purity: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntryRadiochemicalPurity
    ] = field(
        default=None,
        metadata={
            "name": "RadiochemicalPurity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    specific_activity_as_received: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityAsReceived
    ] = field(
        default=None,
        metadata={
            "name": "SpecificActivityAsReceived",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    specific_activity_of_dose: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntrySpecificActivityOfDose
    ] = field(
        default=None,
        metadata={
            "name": "SpecificActivityOfDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntry:
    class Meta:
        global_type = False

    test_crop_no: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryTestCropNo
    ] = field(
        default=None,
        metadata={
            "name": "TestCropNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    type_of_rotational_crop: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryTypeOfRotationalCrop
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfRotationalCrop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    crop: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Crop",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    crop_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CropCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    variety: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Variety",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    scientific_name: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryScientificName
    ] = field(
        default=None,
        metadata={
            "name": "ScientificName",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    crop_group: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntryCropGroup
    ] = field(
        default=None,
        metadata={
            "name": "CropGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    growth_stage_at_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStageAtApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    growth_stage_at_harvest: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GrowthStageAtHarvest",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    harvested_commodities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "HarvestedCommodities",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    harvested_procedure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "HarvestedProcedure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntry:
    class Meta:
        global_type = False

    soil_type_no: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntrySoilTypeNo
    ] = field(
        default=None,
        metadata={
            "name": "SoilTypeNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    soil_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SoilType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    ph: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryPh
    ] = field(
        default=None,
        metadata={
            "name": "PH",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    organic_matter: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryOrganicMatter
    ] = field(
        default=None,
        metadata={
            "name": "OrganicMatter",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    sand: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntrySand
    ] = field(
        default=None,
        metadata={
            "name": "Sand",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    silt: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntrySilt
    ] = field(
        default=None,
        metadata={
            "name": "Silt",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    clay: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryClay
    ] = field(
        default=None,
        metadata={
            "name": "Clay",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    moisture_holding_capacity: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MoistureHoldingCapacity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    cecmeg100_g: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntryCecmeg100G
    ] = field(
        default=None,
        metadata={
            "name": "CECMeg100G",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordMetabolismInCropsOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntry:
    class Meta:
        global_type = False

    idno: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryIdno
    ] = field(
        default=None,
        metadata={
            "name": "IDNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    identity_of_compound: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfCompound",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    parent_compound_s: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentCompoundS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    treatment_group_test_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TreatmentGroupTestNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    expertise: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryExpertise
    ] = field(
        default=None,
        metadata={
            "name": "Expertise",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    type_of_expertise: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntryTypeOfExpertise
    ] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfExpertise",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntry:
    class Meta:
        global_type = False

    matrix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks_on_result: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntryRemarksOnResult
    ] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionProposedMetabolicPathway:
    class Meta:
        global_type = False

    identification_of_compounds_from_metabolism_study: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionProposedMetabolicPathwayIdentificationOfCompoundsFromMetabolismStudy
    ] = field(
        default=None,
        metadata={
            "name": "IdentificationOfCompoundsFromMetabolismStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    metabolic_pathway: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MetabolicPathway",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    metabolic_map_picture_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetabolicMapPictureGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionStorageStabilityOfResidues:
    class Meta:
        global_type = False

    summary_of_storage_conditions: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionStorageStabilityOfResiduesSummaryOfStorageConditions
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfStorageConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    storage_stability: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StorageStability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntry:
    class Meta:
        global_type = False

    matrix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntry:
    class Meta:
        global_type = False

    soil_sample: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SoilSample",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntry:
    class Meta:
        global_type = False

    type_of_method: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryTypeOfMethod
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    recovered_equivalents_mg_kg: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryRecoveredEquivalentsMgKg
    ] = field(
        default=None,
        metadata={
            "name": "RecoveredEquivalentsMgKg",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    overall_extraction_efficiency: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryOverallExtractionEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "OverallExtractionEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    defined_residue_mg_kg: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueMgKg
    ] = field(
        default=None,
        metadata={
            "name": "DefinedResidueMgKg",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    defined_residue_extraction_efficiency: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntryDefinedResidueExtractionEfficiency
    ] = field(
        default=None,
        metadata={
            "name": "DefinedResidueExtractionEfficiency",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntry:
    class Meta:
        global_type = False

    matrix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Matrix",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    timing_and_application: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TimingAndApplication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    preharvest_interval_phi: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PreharvestIntervalPHI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    plant_back_interval_pbi: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PlantBackIntervalPBI",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trr: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrr
    ] = field(
        default=None,
        metadata={
            "name": "TRR",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrppm: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryTrrppm
    ] = field(
        default=None,
        metadata={
            "name": "TRRPpm",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    remarks_on_result: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntryRemarksOnResult
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCrops:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCropsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilProperties:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilPropertiesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroups:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroupsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatrices:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatricesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatrices:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatricesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamples:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamplesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethod:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethodEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatrices:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatricesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    radiolabelling: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelling
    ] = field(
        default=None,
        metadata={
            "name": "Radiolabelling",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    radiolabelled_test_material: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterialsRadiolabelledTestMaterial
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelledTestMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformation:
    class Meta:
        global_type = False

    test_crops: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformationTestCrops
    ] = field(
        default=None,
        metadata={
            "name": "TestCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    details_on_test_crops: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilProperties:
    class Meta:
        global_type = False

    test_site_type: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesTestSiteType
    ] = field(
        default=None,
        metadata={
            "name": "TestSiteType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    soil_properties: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilPropertiesSoilProperties
    ] = field(
        default=None,
        metadata={
            "name": "SoilProperties",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    details_on_test_site: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnTestSite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroups:
    class Meta:
        global_type = False

    metabolites_in_treatment_groups: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroupsMetabolitesInTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "MetabolitesInTreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntry:
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    metabolite_fraction: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryMetaboliteFraction
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    identity_of_parent_or_metabolite: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfParentOrMetabolite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrs_in_matrices: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntryTrrsInMatrices
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInMatrices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntry:
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    metabolite_fraction: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryMetaboliteFraction
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    identity_of_parent_or_metabolite: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfParentOrMetabolite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrs_in_matrices: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntryTrrsInMatrices
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInMatrices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntry:
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    metabolite_fraction: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryMetaboliteFraction
    ] = field(
        default=None,
        metadata={
            "name": "MetaboliteFraction",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    identity_of_parent_or_metabolite: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityOfParentOrMetabolite",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrs_in_soil_samples: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntryTrrsInSoilSamples
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInSoilSamples",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntry:
    class Meta:
        global_type = False

    radiolabel_no: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryRadiolabelNo
    ] = field(
        default=None,
        metadata={
            "name": "RadiolabelNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrs_in_matrices: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntryTrrsInMatrices
    ] = field(
        default=None,
        metadata={
            "name": "TRRsInMatrices",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsMaterialsAndMethods:
    class Meta:
        global_type = False

    background_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BackgroundInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    product_type: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsProductType
    ] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    test_site_and_crop_information: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndCropInformation
    ] = field(
        default=None,
        metadata={
            "name": "TestSiteAndCropInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    test_site_and_soil_properties: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsTestSiteAndSoilProperties
    ] = field(
        default=None,
        metadata={
            "name": "TestSiteAndSoilProperties",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    environmental_conditions: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsEnvironmentalConditions
    ] = field(
        default=None,
        metadata={
            "name": "EnvironmentalConditions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    application: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsApplication
    ] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    sampling_and_analysis: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysis
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysis",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    sampling_and_analysis_of_soil: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsSamplingAndAnalysisOfSoil
    ] = field(
        default=None,
        metadata={
            "name": "SamplingAndAnalysisOfSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    appendix_treatment_groups: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAppendixTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "AppendixTreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolites:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolitesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResidues:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResiduesEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoil:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoilEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresults:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresultsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResidues:
    class Meta:
        global_type = False

    distribution_of_parent_and_metabolites: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResiduesDistributionOfParentAndMetabolites
    ] = field(
        default=None,
        metadata={
            "name": "DistributionOfParentAndMetabolites",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    distribution_of_residues: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DistributionOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCrops:
    class Meta:
        global_type = False

    characterisation_and_identification_of_radioactive_residues: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCropsCharacterisationAndIdentificationOfRadioactiveResidues
    ] = field(
        default=None,
        metadata={
            "name": "CharacterisationAndIdentificationOfRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    characterisation_and_identification_of_residues: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CharacterisationAndIdentificationOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoil:
    class Meta:
        global_type = False

    radioactive_residues_in_soil: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoilRadioactiveResiduesInSoil
    ] = field(
        default=None,
        metadata={
            "name": "RadioactiveResiduesInSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResidues:
    class Meta:
        global_type = False

    extraction_efficiency_of_radioactive_residues_using_enforcement_method: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethod
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionEfficiencyOfRadioactiveResiduesUsingEnforcementMethod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    quantitation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Quantitation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    trrresults: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResiduesTrrresults
    ] = field(
        default=None,
        metadata={
            "name": "TRRResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    total_radioactive_residues: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TotalRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCropsResultsAndDiscussion:
    class Meta:
        global_type = False

    total_radioactive_residues: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionTotalRadioactiveResidues
    ] = field(
        default=None,
        metadata={
            "name": "TotalRadioactiveResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    extraction_characterisation_and_distribution_of_residues: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionExtractionCharacterisationAndDistributionOfResidues
    ] = field(
        default=None,
        metadata={
            "name": "ExtractionCharacterisationAndDistributionOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    storage_stability_of_residues: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionStorageStabilityOfResidues
    ] = field(
        default=None,
        metadata={
            "name": "StorageStabilityOfResidues",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    summary_of_radioactive_residues_in_crops: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInCrops
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfRadioactiveResiduesInCrops",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    summary_of_radioactive_residues_in_soil: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionSummaryOfRadioactiveResiduesInSoil
    ] = field(
        default=None,
        metadata={
            "name": "SummaryOfRadioactiveResiduesInSoil",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    proposed_metabolic_pathway: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionProposedMetabolicPathway
    ] = field(
        default=None,
        metadata={
            "name": "ProposedMetabolicPathway",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    appendix_metabolites_and_their_parents_in_treatment_groups: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAppendixMetabolitesAndTheirParentsInTreatmentGroups
    ] = field(
        default=None,
        metadata={
            "name": "AppendixMetabolitesAndTheirParentsInTreatmentGroups",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0",
        },
    )


@dataclass
class EndpointStudyRecordMetabolismInCrops:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.MetabolismInCrops"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-MetabolismInCrops/5.0"

    administrative_data: Optional[
        EndpointStudyRecordMetabolismInCropsAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordMetabolismInCropsDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordMetabolismInCropsMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordMetabolismInCropsResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordMetabolismInCropsOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordMetabolismInCropsApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
