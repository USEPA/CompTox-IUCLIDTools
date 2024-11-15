from autoflammability_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    N64,
    N78,
    P02,
    P13,
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
    Pg660064,
    Pg660065,
    Pg660071,
    Pg660077,
    Pg660081,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from autoflammability_6_5.models.endpoint_study_record_auto_flammability_9_0 import (
    EndpointStudyRecordAutoFlammability,
    EndpointStudyRecordAutoFlammabilityAdministrativeData,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataAttachedJustification,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataCrossReference,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataDataProtection,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataDataWaiving,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataEndpoint,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataPurposeFlag,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataRationalReliability,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataReliability,
    EndpointStudyRecordAutoFlammabilityAdministrativeDataStudyResultType,
    EndpointStudyRecordAutoFlammabilityApplicantSummaryAndConclusion,
    EndpointStudyRecordAutoFlammabilityDataSource,
    EndpointStudyRecordAutoFlammabilityDataSourceDataAccess,
    EndpointStudyRecordAutoFlammabilityDataSourceDataProtectionClaimed,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethods,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuideline,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordAutoFlammabilityOverallRemarksAttachments,
    EndpointStudyRecordAutoFlammabilityOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordAutoFlammabilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordAutoFlammabilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussion,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammability,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntry,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntryAtmPressure,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntryFlammability,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntryRemarksOnResults,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolids,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolidsEntry,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolidsEntryRelativeSelfIgnitionTemperature,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolidsEntryRemarksOnResults,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulation,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulationEntry,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulationEntryRemarksOnResults,
    EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulationEntrySelfIgnitionTemperature,
)
from autoflammability_6_5.models.platform_fields import (
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
from autoflammability_6_5.models.xml import LangValue

__all__ = [
    "A102",
    "A36",
    "N64",
    "N78",
    "P02",
    "P13",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660064",
    "Pg660065",
    "Pg660071",
    "Pg660077",
    "Pg660081",
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
    "EndpointStudyRecordAutoFlammability",
    "EndpointStudyRecordAutoFlammabilityAdministrativeData",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataAttachedJustification",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataCrossReference",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataDataProtection",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataDataWaiving",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataEndpoint",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataPurposeFlag",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataRationalReliability",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataReliability",
    "EndpointStudyRecordAutoFlammabilityAdministrativeDataStudyResultType",
    "EndpointStudyRecordAutoFlammabilityApplicantSummaryAndConclusion",
    "EndpointStudyRecordAutoFlammabilityDataSource",
    "EndpointStudyRecordAutoFlammabilityDataSourceDataAccess",
    "EndpointStudyRecordAutoFlammabilityDataSourceDataProtectionClaimed",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethods",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuideline",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordAutoFlammabilityMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordAutoFlammabilityOverallRemarksAttachments",
    "EndpointStudyRecordAutoFlammabilityOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordAutoFlammabilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordAutoFlammabilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussion",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammability",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntry",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntryAtmPressure",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntryFlammability",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionAutoFlammabilityEntryRemarksOnResults",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolids",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolidsEntry",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolidsEntryRelativeSelfIgnitionTemperature",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionRelativeSelfIgnitionTemperatureSolidsEntryRemarksOnResults",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulation",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulationEntry",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulationEntryRemarksOnResults",
    "EndpointStudyRecordAutoFlammabilityResultsAndDiscussionSelfIgnitionTemperatureOfDustAccumulationEntrySelfIgnitionTemperature",
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