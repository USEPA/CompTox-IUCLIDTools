from toxicitytosoilmicroorganisms_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    E04,
    E15,
    E35,
    E105,
    E122,
    E127,
    E128,
    E129,
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
    Z40,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660250,
    Pg660252,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td3602,
)
from toxicitytosoilmicroorganisms_6_5.models.endpoint_study_record_toxicity_to_soil_microorganisms_9_0 import (
    EndpointStudyRecordToxicityToSoilMicroorganisms,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeData,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataAttachedJustification,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataCrossReference,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataProtection,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataWaiving,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataEndpoint,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataPurposeFlag,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataRationalReliability,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataReliability,
    EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataStudyResultType,
    EndpointStudyRecordToxicityToSoilMicroorganismsApplicantSummaryAndConclusion,
    EndpointStudyRecordToxicityToSoilMicroorganismsApplicantSummaryAndConclusionValidityCriteriaFulfilled,
    EndpointStudyRecordToxicityToSoilMicroorganismsDataSource,
    EndpointStudyRecordToxicityToSoilMicroorganismsDataSourceDataAccess,
    EndpointStudyRecordToxicityToSoilMicroorganismsDataSourceDataProtectionClaimed,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethods,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuideline,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsSamplingAndAnalysis,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsStudyDesignTotalExposureDuration,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestConditions,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestOrganisms,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestOrganismsTestOrganismsInoculum,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestSubstrate,
    EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestSubstrateVehicle,
    EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachments,
    EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussion,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrations,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntry,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryConfInterval,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryDuration,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryEffectConc,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryEndpoint,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured,
    EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults,
)
from toxicitytosoilmicroorganisms_6_5.models.platform_fields import (
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
from toxicitytosoilmicroorganisms_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A36",
    "E04",
    "E105",
    "E127",
    "E128",
    "E129",
    "E122",
    "E15",
    "E35",
    "F102",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660250",
    "Pg660252",
    "Pg661157",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "Td3602",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z36",
    "Z40",
    "EndpointStudyRecordToxicityToSoilMicroorganisms",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeData",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataAttachedJustification",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataCrossReference",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataProtection",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataWaiving",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataEndpoint",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataPurposeFlag",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataRationalReliability",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataReliability",
    "EndpointStudyRecordToxicityToSoilMicroorganismsAdministrativeDataStudyResultType",
    "EndpointStudyRecordToxicityToSoilMicroorganismsApplicantSummaryAndConclusion",
    "EndpointStudyRecordToxicityToSoilMicroorganismsApplicantSummaryAndConclusionValidityCriteriaFulfilled",
    "EndpointStudyRecordToxicityToSoilMicroorganismsDataSource",
    "EndpointStudyRecordToxicityToSoilMicroorganismsDataSourceDataAccess",
    "EndpointStudyRecordToxicityToSoilMicroorganismsDataSourceDataProtectionClaimed",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethods",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuideline",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsSamplingAndAnalysis",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsSamplingAndAnalysisAnalyticalMonitoring",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsStudyDesignTotalExposureDuration",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestConditions",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestConditionsReferenceSubstancePositiveControl",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestOrganisms",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestOrganismsTestOrganismsInoculum",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestSubstrate",
    "EndpointStudyRecordToxicityToSoilMicroorganismsMaterialsAndMethodsTestSubstrateVehicle",
    "EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachments",
    "EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordToxicityToSoilMicroorganismsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussion",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrations",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntry",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryBasisForEffect",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryConcBasedOn",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryConfInterval",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryDuration",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryEffectConc",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryEndpoint",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryNominalMeasured",
    "EndpointStudyRecordToxicityToSoilMicroorganismsResultsAndDiscussionEffectConcentrationsEntryRemarksOnResults",
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
