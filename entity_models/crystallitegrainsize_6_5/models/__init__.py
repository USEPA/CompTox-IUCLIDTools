from crystallitegrainsize_6_5.models.common_types_oecd_v9 import (
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
    Z38,
    Z40,
    Z52,
    Nm13,
    Nm15,
    Nm20,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660334,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from crystallitegrainsize_6_5.models.endpoint_study_record_crystallite_grain_size_9_0 import (
    EndpointStudyRecordCrystalliteGrainSize,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeData,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataAttachedJustification,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataCrossReference,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataProtection,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataWaiving,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataEndpoint,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataPurposeFlag,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataRationalReliability,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataReliability,
    EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataStudyResultType,
    EndpointStudyRecordCrystalliteGrainSizeApplicantSummaryAndConclusion,
    EndpointStudyRecordCrystalliteGrainSizeDataSource,
    EndpointStudyRecordCrystalliteGrainSizeDataSourceDataAccess,
    EndpointStudyRecordCrystalliteGrainSizeDataSourceDataProtectionClaimed,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethods,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsDataGathering,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuideline,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsMethodType,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsTestMaterialsReferenceMaterial,
    EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsTestMaterialsReferenceMaterialEntry,
    EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachments,
    EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussion,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSize,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntry,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntryMean,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntryRemarksOnResults,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntryStDev,
    EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionMaterialIsotropic,
)
from crystallitegrainsize_6_5.models.platform_fields import (
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
from crystallitegrainsize_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "N64",
    "N78",
    "Nm13",
    "Nm15",
    "Nm20",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660334",
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
    "Z38",
    "Z40",
    "Z52",
    "EndpointStudyRecordCrystalliteGrainSize",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeData",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataAttachedJustification",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataCrossReference",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataProtection",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataWaiving",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataEndpoint",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataPurposeFlag",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataRationalReliability",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataReliability",
    "EndpointStudyRecordCrystalliteGrainSizeAdministrativeDataStudyResultType",
    "EndpointStudyRecordCrystalliteGrainSizeApplicantSummaryAndConclusion",
    "EndpointStudyRecordCrystalliteGrainSizeDataSource",
    "EndpointStudyRecordCrystalliteGrainSizeDataSourceDataAccess",
    "EndpointStudyRecordCrystalliteGrainSizeDataSourceDataProtectionClaimed",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethods",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsDataGathering",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuideline",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsMethodType",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsTestMaterialsReferenceMaterial",
    "EndpointStudyRecordCrystalliteGrainSizeMaterialsAndMethodsTestMaterialsReferenceMaterialEntry",
    "EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachments",
    "EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordCrystalliteGrainSizeOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussion",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSize",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntry",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntryMean",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntryRemarksOnResults",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionCrystalliteGrainSizeEntryStDev",
    "EndpointStudyRecordCrystalliteGrainSizeResultsAndDiscussionMaterialIsotropic",
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
