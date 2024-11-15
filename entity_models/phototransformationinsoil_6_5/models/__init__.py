from phototransformationinsoil_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    F023,
    F03,
    F13,
    F102,
    F112,
    F136,
    F137,
    N64,
    N78,
    P116,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z36,
    Z40,
    Z52,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660044,
    Pg660159,
    Pg661157,
    Pg661166,
    Pg661170,
    Pg661171,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Pg661593,
)
from phototransformationinsoil_6_5.models.endpoint_study_record_photo_transformation_in_soil_9_0 import (
    EndpointStudyRecordPhotoTransformationInSoil,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeData,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustification,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReference,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtection,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaiving,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataEndpoint,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataPurposeFlag,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataRationalReliability,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataReliability,
    EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataStudyResultType,
    EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusion,
    EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusionValidityCriteriaFulfilled,
    EndpointStudyRecordPhotoTransformationInSoilDataSource,
    EndpointStudyRecordPhotoTransformationInSoilDataSourceDataAccess,
    EndpointStudyRecordPhotoTransformationInSoilDataSourceDataProtectionClaimed,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethods,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuideline,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMethod,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMonitoring,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDarkControls,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestCondition,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntry,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryDuration,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryInitialConcMeasured,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryTemp,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSource,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSpectrumWavelengthInNm,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignReferenceSubstance,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignRelativeLightIntensity,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling,
    EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachments,
    EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussion,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradation,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntry,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryDegradationPercent,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryTimePoint,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompound,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntry,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryParameter,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryPvalue,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryRemarksOnResults,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntrySoilNo,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryTemp,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryType,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryTypeOfValue,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryValue,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformation,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntry,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntryMaximumOccurrence,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntryNo,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalance,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntry,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryCo2,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryNonExtractable,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryRecovery,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingConditions,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingTime,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrum,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntry,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryParameter,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryValue,
    EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionTransformationProducts,
)
from phototransformationinsoil_6_5.models.platform_fields import (
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
from phototransformationinsoil_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A102",
    "A36",
    "C113",
    "E34",
    "F023",
    "F03",
    "F102",
    "F112",
    "F13",
    "F136",
    "F137",
    "N64",
    "N78",
    "P116",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660044",
    "Pg660159",
    "Pg661157",
    "Pg661166",
    "Pg661170",
    "Pg661171",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "Pg661593",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z36",
    "Z40",
    "Z52",
    "EndpointStudyRecordPhotoTransformationInSoil",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeData",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustification",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReference",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtection",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaiving",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataEndpoint",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataPurposeFlag",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataRationalReliability",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataReliability",
    "EndpointStudyRecordPhotoTransformationInSoilAdministrativeDataStudyResultType",
    "EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusion",
    "EndpointStudyRecordPhotoTransformationInSoilApplicantSummaryAndConclusionValidityCriteriaFulfilled",
    "EndpointStudyRecordPhotoTransformationInSoilDataSource",
    "EndpointStudyRecordPhotoTransformationInSoilDataSourceDataAccess",
    "EndpointStudyRecordPhotoTransformationInSoilDataSourceDataProtectionClaimed",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethods",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuideline",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMethod",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignAnalyticalMonitoring",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDarkControls",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestCondition",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntry",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryDuration",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryInitialConcMeasured",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignDurationOfTestAtGivenTestConditionEntryTemp",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSource",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignLightSpectrumWavelengthInNm",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignReferenceSubstance",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsStudyDesignRelativeLightIntensity",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordPhotoTransformationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling",
    "EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachments",
    "EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordPhotoTransformationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussion",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompound",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntry",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryParameter",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryRemarksOnResults",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntrySoilNo",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryTemp",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryType",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryTypeOfValue",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryValue",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDtparentCompoundEntryPvalue",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradation",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntry",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryDegradationPercent",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionDegradationEntryTimePoint",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformation",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntry",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntryMaximumOccurrence",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionIdentityTransformationEntryNo",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalance",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntry",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryCo2",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryNonExtractable",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryRecovery",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingConditions",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingTime",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrum",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntry",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryParameter",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionSpectrumEntryValue",
    "EndpointStudyRecordPhotoTransformationInSoilResultsAndDiscussionTransformationProducts",
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
