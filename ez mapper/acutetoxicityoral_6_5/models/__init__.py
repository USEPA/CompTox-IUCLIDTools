from acutetoxicityoral_6_5.models.common_types_oecd_v9 import (
    A36,
    E105,
    N64,
    N78,
    T01,
    T021,
    T03,
    T042,
    T24,
    T48,
    T123,
    T124,
    T148,
    T251,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660281,
    Pg660282,
    Pg660287,
    Pg661103,
    Pg661104,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from acutetoxicityoral_6_5.models.endpoint_study_record_acute_toxicity_oral_9_0 import (
    EndpointStudyRecordAcuteToxicityOral,
    EndpointStudyRecordAcuteToxicityOralAdministrativeData,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataAttachedJustification,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataCrossReference,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataProtection,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataWaiving,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataEndpoint,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataPurposeFlag,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataRationalReliability,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataReliability,
    EndpointStudyRecordAcuteToxicityOralAdministrativeDataStudyResultType,
    EndpointStudyRecordAcuteToxicityOralApplicantSummaryAndConclusion,
    EndpointStudyRecordAcuteToxicityOralApplicantSummaryAndConclusionInterpretationOfResults,
    EndpointStudyRecordAcuteToxicityOralDataSource,
    EndpointStudyRecordAcuteToxicityOralDataSourceDataAccess,
    EndpointStudyRecordAcuteToxicityOralDataSourceDataProtectionClaimed,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethods,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposure,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureControlAnimals,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureRouteOfAdministration,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureVehicle,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuideline,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsLimitTest,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimals,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimalsSex,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimalsSpecies,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimalsStrain,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestType,
    EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachments,
    EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussion,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionBodyWeight,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionClinicalSigns,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevels,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntry,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryBasedOn,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryCl,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryEffectLevel,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryEndpoint,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryRemarksOnResults,
    EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntrySex,
)
from acutetoxicityoral_6_5.models.platform_fields import (
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
from acutetoxicityoral_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "E105",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660281",
    "Pg660282",
    "Pg660287",
    "Pg661104",
    "Pg661121",
    "Pg661157",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "Pg661103",
    "T01",
    "T021",
    "T03",
    "T042",
    "T123",
    "T124",
    "T148",
    "T23123456",
    "T24",
    "T251",
    "T48",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z38",
    "Z40",
    "EndpointStudyRecordAcuteToxicityOral",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeData",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataAttachedJustification",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataCrossReference",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataProtection",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataWaiving",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataEndpoint",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataPurposeFlag",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataRationalReliability",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataReliability",
    "EndpointStudyRecordAcuteToxicityOralAdministrativeDataStudyResultType",
    "EndpointStudyRecordAcuteToxicityOralApplicantSummaryAndConclusion",
    "EndpointStudyRecordAcuteToxicityOralApplicantSummaryAndConclusionInterpretationOfResults",
    "EndpointStudyRecordAcuteToxicityOralDataSource",
    "EndpointStudyRecordAcuteToxicityOralDataSourceDataAccess",
    "EndpointStudyRecordAcuteToxicityOralDataSourceDataProtectionClaimed",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethods",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposure",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureControlAnimals",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureRouteOfAdministration",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAdministrationExposureVehicle",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuideline",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsLimitTest",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimals",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimalsSex",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimalsSpecies",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestAnimalsStrain",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordAcuteToxicityOralMaterialsAndMethodsTestType",
    "EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachments",
    "EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordAcuteToxicityOralOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussion",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionBodyWeight",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionClinicalSigns",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevels",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntry",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryBasedOn",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryEffectLevel",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryEndpoint",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryRemarksOnResults",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntrySex",
    "EndpointStudyRecordAcuteToxicityOralResultsAndDiscussionEffectLevelsEntryCl",
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
