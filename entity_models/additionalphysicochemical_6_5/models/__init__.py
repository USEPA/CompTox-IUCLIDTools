from additionalphysicochemical_6_5.models.common_types_oecd_v9 import (
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
    Z40,
    Z52,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660117,
    Pg660862,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from additionalphysicochemical_6_5.models.endpoint_study_record_additional_physico_chemical_9_0 import (
    EndpointStudyRecordAdditionalPhysicoChemical,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeData,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataAttachedJustification,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataCrossReference,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataProtection,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataWaiving,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataEndpoint,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataPurposeFlag,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataRationalReliability,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataReliability,
    EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataStudyResultType,
    EndpointStudyRecordAdditionalPhysicoChemicalApplicantSummaryAndConclusion,
    EndpointStudyRecordAdditionalPhysicoChemicalDataSource,
    EndpointStudyRecordAdditionalPhysicoChemicalDataSourceDataAccess,
    EndpointStudyRecordAdditionalPhysicoChemicalDataSourceDataProtectionClaimed,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethods,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuideline,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachments,
    EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussion,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
)
from additionalphysicochemical_6_5.models.platform_fields import (
    AddressField,
    AttachmentListField,
    BaseDataProtectionField,
    BasePhysicalQuantityField,
    BasePhysicalQuantityRangeField,
    BasePicklistField,
    DataProtectionField,
    DocumentReferenceMultipleField,
    HalfBoundedQualifier,
    InventoryEntry,
    Legislation,
    LowerQualifier,
    MultilingualDataProtectionField,
    MultilingualLegislation,
    MultilingualPhysicalQuantityHalfBoundedField,
    MultilingualPhysicalQuantityIntegerHalfBoundedField,
    MultilingualPhysicalQuantityIntegerRangeField,
    MultilingualPhysicalQuantityRangeField,
    MultilingualPicklistField,
    MultilingualPicklistFieldWithLargeTextRemarks,
    MultilingualPicklistFieldWithMultiLineTextRemarks,
    MultilingualPicklistFieldWithSmallTextRemarks,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    PhysicalQuantityField,
    PhysicalQuantityHalfBoundedField,
    PhysicalQuantityIntegerHalfBoundedField,
    PhysicalQuantityIntegerRangeField,
    PhysicalQuantityRangeField,
    PicklistField,
    PicklistFieldWithLargeTextRemarks,
    PicklistFieldWithMultiLineTextRemarks,
    PicklistFieldWithSmallTextRemarks,
    RepeatableEntryType,
    SectionTypesField,
    SectionTypesFieldDocumentDefinitionIdentifier,
    UpperQualifier,
)
from additionalphysicochemical_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "N64",
    "N78",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660117",
    "Pg660862",
    "Pg661157",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z40",
    "Z52",
    "EndpointStudyRecordAdditionalPhysicoChemical",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeData",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataAttachedJustification",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataCrossReference",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataProtection",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataWaiving",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataEndpoint",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataPurposeFlag",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataRationalReliability",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataReliability",
    "EndpointStudyRecordAdditionalPhysicoChemicalAdministrativeDataStudyResultType",
    "EndpointStudyRecordAdditionalPhysicoChemicalApplicantSummaryAndConclusion",
    "EndpointStudyRecordAdditionalPhysicoChemicalDataSource",
    "EndpointStudyRecordAdditionalPhysicoChemicalDataSourceDataAccess",
    "EndpointStudyRecordAdditionalPhysicoChemicalDataSourceDataProtectionClaimed",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethods",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuideline",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordAdditionalPhysicoChemicalMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachments",
    "EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordAdditionalPhysicoChemicalOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussion",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordAdditionalPhysicoChemicalResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "AddressField",
    "AttachmentListField",
    "BaseDataProtectionField",
    "BasePhysicalQuantityField",
    "BasePhysicalQuantityRangeField",
    "BasePicklistField",
    "DataProtectionField",
    "DocumentReferenceMultipleField",
    "HalfBoundedQualifier",
    "InventoryEntry",
    "Legislation",
    "LowerQualifier",
    "MultilingualDataProtectionField",
    "MultilingualLegislation",
    "MultilingualPhysicalQuantityHalfBoundedField",
    "MultilingualPhysicalQuantityIntegerHalfBoundedField",
    "MultilingualPhysicalQuantityIntegerRangeField",
    "MultilingualPhysicalQuantityRangeField",
    "MultilingualPicklistField",
    "MultilingualPicklistFieldWithLargeTextRemarks",
    "MultilingualPicklistFieldWithMultiLineTextRemarks",
    "MultilingualPicklistFieldWithSmallTextRemarks",
    "MultilingualTextField",
    "MultilingualTextFieldLarge",
    "MultilingualTextFieldMultiLine",
    "MultilingualTextFieldSmall",
    "PhysicalQuantityField",
    "PhysicalQuantityHalfBoundedField",
    "PhysicalQuantityIntegerHalfBoundedField",
    "PhysicalQuantityIntegerRangeField",
    "PhysicalQuantityRangeField",
    "PicklistField",
    "PicklistFieldWithLargeTextRemarks",
    "PicklistFieldWithMultiLineTextRemarks",
    "PicklistFieldWithSmallTextRemarks",
    "RepeatableEntryType",
    "SectionTypesField",
    "SectionTypesFieldDocumentDefinitionIdentifier",
    "UpperQualifier",
    "LangValue",
]
