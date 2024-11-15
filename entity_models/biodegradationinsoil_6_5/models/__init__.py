from biodegradationinsoil_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    A102,
    C113,
    E34,
    E149,
    F11,
    F12,
    F16,
    F17,
    F25,
    F103,
    F109,
    F110,
    F132,
    F136,
    F137,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660267,
    Pg660268,
    Pg660490,
    Pg660822,
    Pg661121,
    Pg661157,
    Pg661170,
    Pg661171,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from biodegradationinsoil_6_5.models.endpoint_study_record_biodegradation_in_soil_9_0 import (
    EndpointStudyRecordBiodegradationInSoil,
    EndpointStudyRecordBiodegradationInSoilAdministrativeData,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustification,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReference,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtection,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaiving,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataEndpoint,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataPurposeFlag,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataRationalReliability,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataReliability,
    EndpointStudyRecordBiodegradationInSoilAdministrativeDataStudyResultType,
    EndpointStudyRecordBiodegradationInSoilApplicantSummaryAndConclusion,
    EndpointStudyRecordBiodegradationInSoilDataSource,
    EndpointStudyRecordBiodegradationInSoilDataSourceDataAccess,
    EndpointStudyRecordBiodegradationInSoilDataSourceDataProtectionClaimed,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethods,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuideline,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTime,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntry,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntryDuration,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditions,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntry,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySterileConditions,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignOxygenConditions,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignParameterFollowed,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilClassification,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilProperties,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntry,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryBulkDensityGcm,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryCec,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryClay,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryMoistureContent,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryOrgC,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryPh,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySand,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySilt,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilType,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling,
    EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestType,
    EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachments,
    EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussion,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradation,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntry,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryDegr,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParameter,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParentProduct,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySamplingTime,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompound,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntry,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryParameter,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryPvalue,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryRemarksOnResults,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryTemp,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryType,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryTypeOfValue,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryValue,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionEvaporationOfParentCompound,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalance,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntry,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryCo2,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryNonExtractable,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRecovery,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingTime,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMineralizationRateInCo2,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionResidues,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProducts,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetails,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntry,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryIdno,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryParameter,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryPvalue,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntrySoilNo,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryTemp,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryTypeOfKineticsAndMethodOfCalculation,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryTypeOfValue,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryValue,
    EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionVolatileMetabolites,
)
from biodegradationinsoil_6_5.models.platform_fields import (
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
from biodegradationinsoil_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A102",
    "A36",
    "C113",
    "E149",
    "E34",
    "F103",
    "F109",
    "F11",
    "F110",
    "F12",
    "F136",
    "F137",
    "F132",
    "F16",
    "F17",
    "F25",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660267",
    "Pg660268",
    "Pg660490",
    "Pg660822",
    "Pg661121",
    "Pg661157",
    "Pg661170",
    "Pg661171",
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
    "EndpointStudyRecordBiodegradationInSoil",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeData",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustification",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReference",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtection",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaiving",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataEndpoint",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataPurposeFlag",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataRationalReliability",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataReliability",
    "EndpointStudyRecordBiodegradationInSoilAdministrativeDataStudyResultType",
    "EndpointStudyRecordBiodegradationInSoilApplicantSummaryAndConclusion",
    "EndpointStudyRecordBiodegradationInSoilDataSource",
    "EndpointStudyRecordBiodegradationInSoilDataSourceDataAccess",
    "EndpointStudyRecordBiodegradationInSoilDataSourceDataProtectionClaimed",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethods",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuideline",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTime",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntry",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntryDuration",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignDurationOfTestContactTimeEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditions",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntry",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignExperimentalConditionsEntrySterileConditions",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentration",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntry",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryBasedOn",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntryInitialConc",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignInitialTestSubstanceConcentrationEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignOxygenConditions",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignParameterFollowed",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilClassification",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilProperties",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntry",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryBulkDensityGcm",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryCec",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryClay",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryMoistureContent",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryOrgC",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntryPh",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySand",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySilt",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsStudyDesignSoilPropertiesEntrySoilType",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestMaterialsRadiolabelling",
    "EndpointStudyRecordBiodegradationInSoilMaterialsAndMethodsTestType",
    "EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachments",
    "EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordBiodegradationInSoilOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussion",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompound",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntry",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryParameter",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryRemarksOnResults",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryTemp",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryType",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryTypeOfValue",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryValue",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDtparentCompoundEntryPvalue",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradation",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntry",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryDegr",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParameter",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryParentProduct",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntryRemarksOnResults",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySamplingTime",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionDegradationEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionEvaporationOfParentCompound",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalance",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntry",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryCo2",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryNonExtractable",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryOtherVolatiles",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRecovery",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryRemarksOnResults",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySamplingTime",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMaterialMassBalanceEntryTotalExtractable",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionMineralizationRateInCo2",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionResidues",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProducts",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetails",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntry",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryIdno",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryParameter",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntrySoilNo",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryTemp",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryTypeOfKineticsAndMethodOfCalculation",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryTypeOfValue",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryValue",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionTransformationProductsDetailsEntryPvalue",
    "EndpointStudyRecordBiodegradationInSoilResultsAndDiscussionVolatileMetabolites",
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
