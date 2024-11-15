from oxidisingproperties_6_5.models.common_types_oecd_v9 import (
    A36,
    C113,
    N64,
    N78,
    P17,
    P109,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660080,
    Pg660082,
    Pg660085,
    Pg660095,
    Pg660096,
    Pg660097,
    Pg660099,
    Pg660101,
    Pg660102,
    Pg660103,
    Pg660104,
    Pg660106,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from oxidisingproperties_6_5.models.endpoint_study_record_oxidising_properties_9_0 import (
    EndpointStudyRecordOxidisingProperties,
    EndpointStudyRecordOxidisingPropertiesAdministrativeData,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataAttachedJustification,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataCrossReference,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataProtection,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataWaiving,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataEndpoint,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataPurposeFlag,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataRationalReliability,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataReliability,
    EndpointStudyRecordOxidisingPropertiesAdministrativeDataStudyResultType,
    EndpointStudyRecordOxidisingPropertiesApplicantSummaryAndConclusion,
    EndpointStudyRecordOxidisingPropertiesApplicantSummaryAndConclusionInterpretationOfResults,
    EndpointStudyRecordOxidisingPropertiesDataSource,
    EndpointStudyRecordOxidisingPropertiesDataSourceDataAccess,
    EndpointStudyRecordOxidisingPropertiesDataSourceDataProtectionClaimed,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethods,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuideline,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsStudyDesignContactWith,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsStudyDesignDurationOfTest,
    EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachments,
    EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussion,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGases,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntry,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntryParameter,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntryRemarksOnResults,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntryResults,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquids,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntry,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntryParameter,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntryRemarksOnResults,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntryResults,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntrySampleTested,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolids,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntry,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntryParameter,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntryRemarksOnResults,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntryResults,
    EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntrySampleTested,
)
from oxidisingproperties_6_5.models.platform_fields import (
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
from oxidisingproperties_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "C113",
    "N64",
    "N78",
    "P109",
    "P17",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660080",
    "Pg660082",
    "Pg660085",
    "Pg660095",
    "Pg660096",
    "Pg660097",
    "Pg660099",
    "Pg660101",
    "Pg660102",
    "Pg660103",
    "Pg660104",
    "Pg660106",
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
    "EndpointStudyRecordOxidisingProperties",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeData",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataAttachedJustification",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataCrossReference",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataProtection",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataWaiving",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataEndpoint",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataPurposeFlag",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataRationalReliability",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataReliability",
    "EndpointStudyRecordOxidisingPropertiesAdministrativeDataStudyResultType",
    "EndpointStudyRecordOxidisingPropertiesApplicantSummaryAndConclusion",
    "EndpointStudyRecordOxidisingPropertiesApplicantSummaryAndConclusionInterpretationOfResults",
    "EndpointStudyRecordOxidisingPropertiesDataSource",
    "EndpointStudyRecordOxidisingPropertiesDataSourceDataAccess",
    "EndpointStudyRecordOxidisingPropertiesDataSourceDataProtectionClaimed",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethods",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuideline",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsStudyDesignContactWith",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsStudyDesignDurationOfTest",
    "EndpointStudyRecordOxidisingPropertiesMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachments",
    "EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordOxidisingPropertiesOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussion",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGases",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntry",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntryParameter",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntryRemarksOnResults",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultOxidisingGasesEntryResults",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquids",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntry",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntryParameter",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntryRemarksOnResults",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntryResults",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingLiquidsEntrySampleTested",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolids",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntry",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntryParameter",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntryRemarksOnResults",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntryResults",
    "EndpointStudyRecordOxidisingPropertiesResultsAndDiscussionTestResultsOxidisingSolidsEntrySampleTested",
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
