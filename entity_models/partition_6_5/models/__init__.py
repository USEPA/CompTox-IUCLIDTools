from partition_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    C15,
    N64,
    N78,
    P07,
    P19,
    P36,
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
    Pg660040,
    Pg660041,
    Pg660044,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from partition_6_5.models.endpoint_study_record_partition_9_0 import (
    EndpointStudyRecordPartition,
    EndpointStudyRecordPartitionAdministrativeData,
    EndpointStudyRecordPartitionAdministrativeDataAttachedJustification,
    EndpointStudyRecordPartitionAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordPartitionAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordPartitionAdministrativeDataCrossReference,
    EndpointStudyRecordPartitionAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordPartitionAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordPartitionAdministrativeDataDataProtection,
    EndpointStudyRecordPartitionAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordPartitionAdministrativeDataDataWaiving,
    EndpointStudyRecordPartitionAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordPartitionAdministrativeDataEndpoint,
    EndpointStudyRecordPartitionAdministrativeDataPurposeFlag,
    EndpointStudyRecordPartitionAdministrativeDataRationalReliability,
    EndpointStudyRecordPartitionAdministrativeDataReliability,
    EndpointStudyRecordPartitionAdministrativeDataStudyResultType,
    EndpointStudyRecordPartitionApplicantSummaryAndConclusion,
    EndpointStudyRecordPartitionDataSource,
    EndpointStudyRecordPartitionDataSourceDataAccess,
    EndpointStudyRecordPartitionDataSourceDataProtectionClaimed,
    EndpointStudyRecordPartitionMaterialsAndMethods,
    EndpointStudyRecordPartitionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordPartitionMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordPartitionMaterialsAndMethodsGuideline,
    EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordPartitionMaterialsAndMethodsMethodType,
    EndpointStudyRecordPartitionMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordPartitionMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordPartitionMaterialsAndMethodsPartitionCoefficientType,
    EndpointStudyRecordPartitionMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordPartitionMaterialsAndMethodsStudyDesignAnalyticalMethod,
    EndpointStudyRecordPartitionMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordPartitionOverallRemarksAttachments,
    EndpointStudyRecordPartitionOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordPartitionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordPartitionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordPartitionResultsAndDiscussion,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordPartitionResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeff,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntry,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryPartition,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryPh,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryRemarksOnResults,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryTemp,
    EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryType,
)
from partition_6_5.models.platform_fields import (
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
from partition_6_5.models.xml import LangValue

__all__ = [
    "A102",
    "A36",
    "C15",
    "N64",
    "N78",
    "P07",
    "P19",
    "P36",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660040",
    "Pg660041",
    "Pg660044",
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
    "EndpointStudyRecordPartition",
    "EndpointStudyRecordPartitionAdministrativeData",
    "EndpointStudyRecordPartitionAdministrativeDataAttachedJustification",
    "EndpointStudyRecordPartitionAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordPartitionAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordPartitionAdministrativeDataCrossReference",
    "EndpointStudyRecordPartitionAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordPartitionAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordPartitionAdministrativeDataDataProtection",
    "EndpointStudyRecordPartitionAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordPartitionAdministrativeDataDataWaiving",
    "EndpointStudyRecordPartitionAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordPartitionAdministrativeDataEndpoint",
    "EndpointStudyRecordPartitionAdministrativeDataPurposeFlag",
    "EndpointStudyRecordPartitionAdministrativeDataRationalReliability",
    "EndpointStudyRecordPartitionAdministrativeDataReliability",
    "EndpointStudyRecordPartitionAdministrativeDataStudyResultType",
    "EndpointStudyRecordPartitionApplicantSummaryAndConclusion",
    "EndpointStudyRecordPartitionDataSource",
    "EndpointStudyRecordPartitionDataSourceDataAccess",
    "EndpointStudyRecordPartitionDataSourceDataProtectionClaimed",
    "EndpointStudyRecordPartitionMaterialsAndMethods",
    "EndpointStudyRecordPartitionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordPartitionMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordPartitionMaterialsAndMethodsGuideline",
    "EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordPartitionMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordPartitionMaterialsAndMethodsMethodType",
    "EndpointStudyRecordPartitionMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordPartitionMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordPartitionMaterialsAndMethodsPartitionCoefficientType",
    "EndpointStudyRecordPartitionMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordPartitionMaterialsAndMethodsStudyDesignAnalyticalMethod",
    "EndpointStudyRecordPartitionMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordPartitionOverallRemarksAttachments",
    "EndpointStudyRecordPartitionOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordPartitionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordPartitionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordPartitionResultsAndDiscussion",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordPartitionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordPartitionResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeff",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntry",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryPartition",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryPh",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryRemarksOnResults",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryTemp",
    "EndpointStudyRecordPartitionResultsAndDiscussionPartcoeffEntryType",
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