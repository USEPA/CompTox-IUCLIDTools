from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from entity_models_6_4.genetictoxicityvivo_6_5.models.common_types_oecd_v5 import (
    A36,
    N64,
    N78,
    T028,
    T24,
    T25,
    T27,
    T34,
    T37,
    T143,
    T144,
    T284,
    T23123456,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660303,
    Pg660360,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0"


@dataclass
class EndpointStudyRecordGeneticToxicityVivoApplicantSummaryAndConclusion:
    class Meta:
        global_type = False

    conclusions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    executive_summary: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsExaminations:
    class Meta:
        global_type = False

    tissues_and_cell_types_examined: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TissuesAndCellTypesExamined",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    details_of_tissue_and_slide_preparation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOfTissueAndSlidePreparation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    evaluation_criteria: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EvaluationCriteria",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    statistics: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestMaterials:
    class Meta:
        global_type = False

    test_material_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMaterialInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    specific_details_on_test_material_used_for_the_study_confidential: List[
        str
    ] = field(
        default_factory=list,
        metadata={
            "name": "SpecificDetailsOnTestMaterialUsedForTheStudyConfidential",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoOverallRemarksAttachmentsAttachedBackgroundMaterialEntry:
    class Meta:
        global_type = False

    attached_document: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocument",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionAnyOtherInformationOnResultsInclTables:
    class Meta:
        global_type = False

    other_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataAttachedJustificationEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660009] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataCrossReferenceEntryReasonPurpose:
    class Meta:
        global_type = False

    value: Optional[Pg660010] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataWaiving:
    class Meta:
        global_type = False

    value: Optional[Z02] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataWaivingJustification:
    class Meta:
        global_type = False

    value: Optional[Z52] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataEndpoint:
    class Meta:
        global_type = False

    value: Optional[Pg660303] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataPurposeFlag:
    class Meta:
        global_type = False

    value: Optional[Y143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataRationalReliability:
    class Meta:
        global_type = False

    value: Optional[Pg660013] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataReliability:
    class Meta:
        global_type = False

    value: Optional[A36] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataStudyResultType:
    class Meta:
        global_type = False

    value: Optional[Z05] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoDataSourceDataAccess:
    class Meta:
        global_type = False

    value: Optional[Z03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoDataSourceDataProtectionClaimed:
    class Meta:
        global_type = False

    value: Optional[Z30] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureControlGroup:
    class Meta:
        global_type = False

    value: Optional[T27] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc:
    class Meta:
        global_type = False

    unit_code: Optional[T284] = field(
        default=None,
        metadata={
            "name": "unitCode",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    unit_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "unitOther",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureRouteOfAdministration:
    class Meta:
        global_type = False

    value: Optional[T25] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGlpcomplianceStatement:
    class Meta:
        global_type = False

    value: Optional[Z40] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntryDeviation:
    class Meta:
        global_type = False

    value: Optional[Z08] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntryGuideline:
    class Meta:
        global_type = False

    value: Optional[T37] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntryQualifier:
    class Meta:
        global_type = False

    value: Optional[Z06] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsStudytype:
    class Meta:
        global_type = False

    value: Optional[T34] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimalsSex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimalsSpecies:
    class Meta:
        global_type = False

    value: Optional[T028] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimalsStrain:
    class Meta:
        global_type = False

    value: Optional[T23123456] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoOverallRemarksAttachmentsAttachedBackgroundMaterial:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVivoOverallRemarksAttachmentsAttachedBackgroundMaterialEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryGenotoxicity:
    class Meta:
        global_type = False

    value: Optional[T143] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryNegContrValid:
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryPosContrValid:
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryRemarksOnResults:
    class Meta:
        global_type = False

    value: Optional[Pg660038] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntrySex:
    class Meta:
        global_type = False

    value: Optional[T24] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryToxicity:
    class Meta:
        global_type = False

    value: Optional[Pg660360] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryVehContrValid:
    class Meta:
        global_type = False

    value: Optional[T144] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    other: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataAttachedJustificationEntry:
    class Meta:
        global_type = False

    attached_justification: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    reason_purpose: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataAttachedJustificationEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataCrossReferenceEntry:
    class Meta:
        global_type = False

    reason_purpose: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataCrossReferenceEntryReasonPurpose
    ] = field(
        default=None,
        metadata={
            "name": "ReasonPurpose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    related_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelatedInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataProtection:
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    justification: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    legislation: List[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataProtectionLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoDataSource:
    class Meta:
        global_type = False

    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    data_access: Optional[
        EndpointStudyRecordGeneticToxicityVivoDataSourceDataAccess
    ] = field(
        default=None,
        metadata={
            "name": "DataAccess",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    data_protection_claimed: Optional[
        EndpointStudyRecordGeneticToxicityVivoDataSourceDataProtectionClaimed
    ] = field(
        default=None,
        metadata={
            "name": "DataProtectionClaimed",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry:
    class Meta:
        global_type = False

    dose_conc: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc
    ] = field(
        default=None,
        metadata={
            "name": "DoseConc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntry:
    class Meta:
        global_type = False

    qualifier: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntryQualifier
    ] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    guideline: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntryGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    version_remarks: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionRemarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    deviation: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntryDeviation
    ] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimals:
    class Meta:
        global_type = False

    species: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimalsSpecies
    ] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    strain: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimalsStrain
    ] = field(
        default=None,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    details_on_species_strain_selection: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnSpeciesStrainSelection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    sex: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimalsSex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    organism_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OrganismDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoOverallRemarksAttachments:
    class Meta:
        global_type = False

    remarks_on_results: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    attached_background_material: Optional[
        EndpointStudyRecordGeneticToxicityVivoOverallRemarksAttachmentsAttachedBackgroundMaterial
    ] = field(
        default=None,
        metadata={
            "name": "AttachedBackgroundMaterial",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    attached_study_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedStudyReport",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    illustration_pic_graph: Optional[str] = field(
        default=None,
        metadata={
            "name": "IllustrationPicGraph",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntry:
    class Meta:
        global_type = False

    key_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyResult",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
            "nillable": True,
        },
    )
    sex: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntrySex
    ] = field(
        default=None,
        metadata={
            "name": "Sex",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    genotoxicity: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryGenotoxicity
    ] = field(
        default=None,
        metadata={
            "name": "Genotoxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    toxicity: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryToxicity
    ] = field(
        default=None,
        metadata={
            "name": "Toxicity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    veh_contr_valid: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryVehContrValid
    ] = field(
        default=None,
        metadata={
            "name": "VehContrValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    neg_contr_valid: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryNegContrValid
    ] = field(
        default=None,
        metadata={
            "name": "NegContrValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    pos_contr_valid: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryPosContrValid
    ] = field(
        default=None,
        metadata={
            "name": "PosContrValid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    remarks_on_results: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntryRemarksOnResults
    ] = field(
        default=None,
        metadata={
            "name": "RemarksOnResults",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataAttachedJustification:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataAttachedJustificationEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeDataCrossReference:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataCrossReferenceEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureDosesConcentrations:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuideline:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuidelineEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRs:
    class Meta:
        global_type = False

    entry: List[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRsEntry
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoAdministrativeData:
    class Meta:
        global_type = False

    data_protection: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataProtection
    ] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    endpoint: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataEndpoint
    ] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    study_result_type: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataStudyResultType
    ] = field(
        default=None,
        metadata={
            "name": "StudyResultType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    purpose_flag: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataPurposeFlag
    ] = field(
        default=None,
        metadata={
            "name": "PurposeFlag",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    robust_study: Optional[str] = field(
        default=None,
        metadata={
            "name": "RobustStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
            "nillable": True,
        },
    )
    used_for_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForClassification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
            "nillable": True,
        },
    )
    used_for_msds: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsedForMSDS",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
            "nillable": True,
        },
    )
    study_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StudyPeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    reliability: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataReliability
    ] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    rational_reliability: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataRationalReliability
    ] = field(
        default=None,
        metadata={
            "name": "RationalReliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    data_waiving: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataWaiving
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiving",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    data_waiving_justification: List[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataDataWaivingJustification
    ] = field(
        default_factory=list,
        metadata={
            "name": "DataWaivingJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    justification_for_type_of_information: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JustificationForTypeOfInformation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    attached_justification: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataAttachedJustification
    ] = field(
        default=None,
        metadata={
            "name": "AttachedJustification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    cross_reference: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeDataCrossReference
    ] = field(
        default=None,
        metadata={
            "name": "CrossReference",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposure:
    class Meta:
        global_type = False

    route_of_administration: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureRouteOfAdministration
    ] = field(
        default=None,
        metadata={
            "name": "RouteOfAdministration",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    vehicle: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    details_on_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DetailsOnExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    duration_of_treatment_exposure: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DurationOfTreatmentExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    frequency_of_treatment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfTreatment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    post_exposure_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PostExposurePeriod",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    doses_concentrations: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureDosesConcentrations
    ] = field(
        default=None,
        metadata={
            "name": "DosesConcentrations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    no_of_animals_per_sex_per_dose: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoOfAnimalsPerSexPerDose",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    control_group: List[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposureControlGroup
    ] = field(
        default_factory=list,
        metadata={
            "name": "ControlGroup",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    positive_controls: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PositiveControls",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussion:
    class Meta:
        global_type = False

    test_rs: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionTestRs
    ] = field(
        default=None,
        metadata={
            "name": "TestRs",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    results_details: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResultsDetails",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    any_other_information_on_results_incl_tables: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussionAnyOtherInformationOnResultsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnResultsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethods:
    class Meta:
        global_type = False

    guideline: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGuideline
    ] = field(
        default=None,
        metadata={
            "name": "Guideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    method_no_guideline: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MethodNoGuideline",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    glpcompliance_statement: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsGlpcomplianceStatement
    ] = field(
        default=None,
        metadata={
            "name": "GLPComplianceStatement",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    studytype: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsStudytype
    ] = field(
        default=None,
        metadata={
            "name": "Studytype",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    test_materials: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestMaterials
    ] = field(
        default=None,
        metadata={
            "name": "TestMaterials",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    test_animals: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsTestAnimals
    ] = field(
        default=None,
        metadata={
            "name": "TestAnimals",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    administration_exposure: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAdministrationExposure
    ] = field(
        default=None,
        metadata={
            "name": "AdministrationExposure",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    examinations: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsExaminations
    ] = field(
        default=None,
        metadata={
            "name": "Examinations",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )
    any_other_information_on_materials_and_methods_incl_tables: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables
    ] = field(
        default=None,
        metadata={
            "name": "AnyOtherInformationOnMaterialsAndMethodsInclTables",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0",
        },
    )


@dataclass
class EndpointStudyRecordGeneticToxicityVivo:
    class Meta:
        name = "ENDPOINT_STUDY_RECORD.GeneticToxicityVivo"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-GeneticToxicityVivo/5.0"

    administrative_data: Optional[
        EndpointStudyRecordGeneticToxicityVivoAdministrativeData
    ] = field(
        default=None,
        metadata={
            "name": "AdministrativeData",
            "type": "Element",
        },
    )
    data_source: Optional[EndpointStudyRecordGeneticToxicityVivoDataSource] = (
        field(
            default=None,
            metadata={
                "name": "DataSource",
                "type": "Element",
            },
        )
    )
    materials_and_methods: Optional[
        EndpointStudyRecordGeneticToxicityVivoMaterialsAndMethods
    ] = field(
        default=None,
        metadata={
            "name": "MaterialsAndMethods",
            "type": "Element",
        },
    )
    results_and_discussion: Optional[
        EndpointStudyRecordGeneticToxicityVivoResultsAndDiscussion
    ] = field(
        default=None,
        metadata={
            "name": "ResultsAndDiscussion",
            "type": "Element",
        },
    )
    overall_remarks_attachments: Optional[
        EndpointStudyRecordGeneticToxicityVivoOverallRemarksAttachments
    ] = field(
        default=None,
        metadata={
            "name": "OverallRemarksAttachments",
            "type": "Element",
        },
    )
    applicant_summary_and_conclusion: Optional[
        EndpointStudyRecordGeneticToxicityVivoApplicantSummaryAndConclusion
    ] = field(
        default=None,
        metadata={
            "name": "ApplicantSummaryAndConclusion",
            "type": "Element",
        },
    )
