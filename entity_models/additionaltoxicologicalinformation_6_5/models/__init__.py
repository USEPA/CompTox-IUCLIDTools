from additionaltoxicologicalinformation_6_5.models.common_types_oecd_v9 import (
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660327,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from additionaltoxicologicalinformation_6_5.models.endpoint_study_record_additional_toxicological_information_9_0 import (
    EndpointStudyRecordAdditionalToxicologicalInformation,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeData,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustification,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReference,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtection,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaiving,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataEndpoint,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataPurposeFlag,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataRationalReliability,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataReliability,
    EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataStudyResultType,
    EndpointStudyRecordAdditionalToxicologicalInformationApplicantSummaryAndConclusion,
    EndpointStudyRecordAdditionalToxicologicalInformationDataSource,
    EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataAccess,
    EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataProtectionClaimed,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethods,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuideline,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachments,
    EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussion,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
)
from additionaltoxicologicalinformation_6_5.models.platform_fields import (
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
from additionaltoxicologicalinformation_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660327",
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
    "EndpointStudyRecordAdditionalToxicologicalInformation",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeData",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustification",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReference",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtection",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaiving",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataEndpoint",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataPurposeFlag",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataRationalReliability",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataReliability",
    "EndpointStudyRecordAdditionalToxicologicalInformationAdministrativeDataStudyResultType",
    "EndpointStudyRecordAdditionalToxicologicalInformationApplicantSummaryAndConclusion",
    "EndpointStudyRecordAdditionalToxicologicalInformationDataSource",
    "EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataAccess",
    "EndpointStudyRecordAdditionalToxicologicalInformationDataSourceDataProtectionClaimed",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethods",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuideline",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordAdditionalToxicologicalInformationMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachments",
    "EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordAdditionalToxicologicalInformationOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussion",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordAdditionalToxicologicalInformationResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
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
