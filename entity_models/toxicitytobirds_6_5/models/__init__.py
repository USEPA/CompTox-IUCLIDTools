from toxicitytobirds_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    E30,
    E105,
    E136,
    E137,
    E138,
    E139,
    E261,
    E271,
    E282,
    F102,
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
    Z38,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660256,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from toxicitytobirds_6_5.models.endpoint_study_record_toxicity_to_birds_9_0 import (
    EndpointStudyRecordToxicityToBirds,
    EndpointStudyRecordToxicityToBirdsAdministrativeData,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustification,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReference,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtection,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaiving,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataEndpoint,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataPurposeFlag,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataRationalReliability,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataReliability,
    EndpointStudyRecordToxicityToBirdsAdministrativeDataStudyResultType,
    EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusion,
    EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusionValidityCriteriaFulfilled,
    EndpointStudyRecordToxicityToBirdsDataSource,
    EndpointStudyRecordToxicityToBirdsDataSourceDataAccess,
    EndpointStudyRecordToxicityToBirdsDataSourceDataProtectionClaimed,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethods,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminations,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminationsReferenceSubstancePositiveControl,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuideline,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignControlAnimals,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignHighDoseLevelUsed,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignLimitTest,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignTotalExposureDuration,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsAnalyticalMonitoring,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsDoseMethod,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsVehicle,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganisms,
    EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies,
    EndpointStudyRecordToxicityToBirdsOverallRemarksAttachments,
    EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussion,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevels,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntry,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryBasisForEffect,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryConcDoseBasedOn,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryConfInterval,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryDuration,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEffectLevel,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEndpoint,
    EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryRemarksOnResults,
)
from toxicitytobirds_6_5.models.platform_fields import (
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
from toxicitytobirds_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A36",
    "E105",
    "E136",
    "E137",
    "E138",
    "E139",
    "E261",
    "E271",
    "E282",
    "E30",
    "F102",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660256",
    "Pg661121",
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
    "Z36",
    "Z38",
    "Z40",
    "Z52",
    "EndpointStudyRecordToxicityToBirds",
    "EndpointStudyRecordToxicityToBirdsAdministrativeData",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustification",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReference",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtection",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaiving",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataEndpoint",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataPurposeFlag",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataRationalReliability",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataReliability",
    "EndpointStudyRecordToxicityToBirdsAdministrativeDataStudyResultType",
    "EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusion",
    "EndpointStudyRecordToxicityToBirdsApplicantSummaryAndConclusionValidityCriteriaFulfilled",
    "EndpointStudyRecordToxicityToBirdsDataSource",
    "EndpointStudyRecordToxicityToBirdsDataSourceDataAccess",
    "EndpointStudyRecordToxicityToBirdsDataSourceDataProtectionClaimed",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethods",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminations",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsExaminationsReferenceSubstancePositiveControl",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuideline",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignControlAnimals",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignHighDoseLevelUsed",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignLimitTest",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsStudyDesignTotalExposureDuration",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsAnalyticalMonitoring",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsDoseMethod",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestMaterialsVehicle",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganisms",
    "EndpointStudyRecordToxicityToBirdsMaterialsAndMethodsTestOrganismsTestOrganismsSpecies",
    "EndpointStudyRecordToxicityToBirdsOverallRemarksAttachments",
    "EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordToxicityToBirdsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussion",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevels",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntry",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryBasisForEffect",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryConcDoseBasedOn",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryConfInterval",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryDuration",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEffectLevel",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryEndpoint",
    "EndpointStudyRecordToxicityToBirdsResultsAndDiscussionEffectLevelsEntryRemarksOnResults",
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
