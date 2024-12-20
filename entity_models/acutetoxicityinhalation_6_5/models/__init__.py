from acutetoxicityinhalation_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    E105,
    N64,
    N78,
    P29,
    T021,
    T05,
    T06,
    T07,
    T08,
    T24,
    T112,
    T124,
    T125,
    T148,
    T252,
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
    Pg660277,
    Pg660278,
    Pg660287,
    Pg660634,
    Pg661121,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td380,
)
from acutetoxicityinhalation_6_5.models.endpoint_study_record_acute_toxicity_inhalation_9_0 import (
    EndpointStudyRecordAcuteToxicityInhalation,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeData,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataAttachedJustification,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataCrossReference,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataProtection,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataWaiving,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataEndpoint,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataPurposeFlag,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataRationalReliability,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataReliability,
    EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataStudyResultType,
    EndpointStudyRecordAcuteToxicityInhalationApplicantSummaryAndConclusion,
    EndpointStudyRecordAcuteToxicityInhalationApplicantSummaryAndConclusionInterpretationOfResults,
    EndpointStudyRecordAcuteToxicityInhalationDataSource,
    EndpointStudyRecordAcuteToxicityInhalationDataSourceDataAccess,
    EndpointStudyRecordAcuteToxicityInhalationDataSourceDataProtectionClaimed,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethods,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposure,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfTestAtmosphereConcentrations,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureControlAnimals,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureDurationOfExposure,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureGeometricStandardDeviation,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureRouteOfAdministration,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposure,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureVehicle,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuideline,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsLimitTest,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimals,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimalsSex,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimalsSpecies,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimalsStrain,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestType,
    EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachments,
    EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussion,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionClinicalSigns,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevels,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntry,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryBasedOn,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryCl,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryEffectLevel,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryEndpoint,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryExposureDuration,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryRemarksOnResults,
    EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntrySex,
)
from acutetoxicityinhalation_6_5.models.platform_fields import (
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
from acutetoxicityinhalation_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A36",
    "E105",
    "N64",
    "N78",
    "P29",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660277",
    "Pg660278",
    "Pg660287",
    "Pg660634",
    "Pg661121",
    "Pg661157",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "T021",
    "T05",
    "T06",
    "T07",
    "T08",
    "T112",
    "T124",
    "T125",
    "T148",
    "T23123456",
    "T24",
    "T252",
    "Td380",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z38",
    "Z40",
    "EndpointStudyRecordAcuteToxicityInhalation",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeData",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataAttachedJustification",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataCrossReference",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataProtection",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataWaiving",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataEndpoint",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataPurposeFlag",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataRationalReliability",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataReliability",
    "EndpointStudyRecordAcuteToxicityInhalationAdministrativeDataStudyResultType",
    "EndpointStudyRecordAcuteToxicityInhalationApplicantSummaryAndConclusion",
    "EndpointStudyRecordAcuteToxicityInhalationApplicantSummaryAndConclusionInterpretationOfResults",
    "EndpointStudyRecordAcuteToxicityInhalationDataSource",
    "EndpointStudyRecordAcuteToxicityInhalationDataSourceDataAccess",
    "EndpointStudyRecordAcuteToxicityInhalationDataSourceDataProtectionClaimed",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethods",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposure",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfTestAtmosphereConcentrations",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureControlAnimals",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureDurationOfExposure",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureGeometricStandardDeviation",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureHighDoseLevelUsed",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureMassMedianAerodynamicDiameter",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureRouteOfAdministration",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureTypeOfInhalationExposure",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAdministrationExposureVehicle",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuideline",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsLimitTest",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimals",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimalsSex",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimalsSpecies",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestAnimalsStrain",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordAcuteToxicityInhalationMaterialsAndMethodsTestType",
    "EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachments",
    "EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordAcuteToxicityInhalationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussion",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionClinicalSigns",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevels",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntry",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryBasedOn",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryEffectLevel",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryEndpoint",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryExposureDuration",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryRemarksOnResults",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntrySex",
    "EndpointStudyRecordAcuteToxicityInhalationResultsAndDiscussionEffectLevelsEntryCl",
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
