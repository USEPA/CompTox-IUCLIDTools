from pourdensity_6_5.models.common_types_oecd_v9 import (
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
    Nm24,
    Nm29,
    Nm43,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660345,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from pourdensity_6_5.models.endpoint_study_record_pour_density_9_0 import (
    EndpointStudyRecordPourDensity,
    EndpointStudyRecordPourDensityAdministrativeData,
    EndpointStudyRecordPourDensityAdministrativeDataAttachedJustification,
    EndpointStudyRecordPourDensityAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordPourDensityAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordPourDensityAdministrativeDataCrossReference,
    EndpointStudyRecordPourDensityAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordPourDensityAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordPourDensityAdministrativeDataDataProtection,
    EndpointStudyRecordPourDensityAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordPourDensityAdministrativeDataDataWaiving,
    EndpointStudyRecordPourDensityAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordPourDensityAdministrativeDataEndpoint,
    EndpointStudyRecordPourDensityAdministrativeDataPurposeFlag,
    EndpointStudyRecordPourDensityAdministrativeDataRationalReliability,
    EndpointStudyRecordPourDensityAdministrativeDataReliability,
    EndpointStudyRecordPourDensityAdministrativeDataStudyResultType,
    EndpointStudyRecordPourDensityApplicantSummaryAndConclusion,
    EndpointStudyRecordPourDensityDataSource,
    EndpointStudyRecordPourDensityDataSourceDataAccess,
    EndpointStudyRecordPourDensityDataSourceDataProtectionClaimed,
    EndpointStudyRecordPourDensityMaterialsAndMethods,
    EndpointStudyRecordPourDensityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordPourDensityMaterialsAndMethodsDataGathering,
    EndpointStudyRecordPourDensityMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordPourDensityMaterialsAndMethodsGuideline,
    EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordPourDensityMaterialsAndMethodsMethodType,
    EndpointStudyRecordPourDensityMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordPourDensityMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordPourDensityMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordPourDensityMaterialsAndMethodsTestMaterialsReferenceMaterial,
    EndpointStudyRecordPourDensityMaterialsAndMethodsTestMaterialsReferenceMaterialEntry,
    EndpointStudyRecordPourDensityOverallRemarksAttachments,
    EndpointStudyRecordPourDensityOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordPourDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordPourDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordPourDensityResultsAndDiscussion,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordPourDensityResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordPourDensityResultsAndDiscussionPourDensity,
    EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntry,
    EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntryMean,
    EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntryRemarksOnResults,
    EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntryStDev,
)
from pourdensity_6_5.models.platform_fields import (
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
from pourdensity_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "N64",
    "N78",
    "Nm24",
    "Nm29",
    "Nm43",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660345",
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
    "EndpointStudyRecordPourDensity",
    "EndpointStudyRecordPourDensityAdministrativeData",
    "EndpointStudyRecordPourDensityAdministrativeDataAttachedJustification",
    "EndpointStudyRecordPourDensityAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordPourDensityAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordPourDensityAdministrativeDataCrossReference",
    "EndpointStudyRecordPourDensityAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordPourDensityAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordPourDensityAdministrativeDataDataProtection",
    "EndpointStudyRecordPourDensityAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordPourDensityAdministrativeDataDataWaiving",
    "EndpointStudyRecordPourDensityAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordPourDensityAdministrativeDataEndpoint",
    "EndpointStudyRecordPourDensityAdministrativeDataPurposeFlag",
    "EndpointStudyRecordPourDensityAdministrativeDataRationalReliability",
    "EndpointStudyRecordPourDensityAdministrativeDataReliability",
    "EndpointStudyRecordPourDensityAdministrativeDataStudyResultType",
    "EndpointStudyRecordPourDensityApplicantSummaryAndConclusion",
    "EndpointStudyRecordPourDensityDataSource",
    "EndpointStudyRecordPourDensityDataSourceDataAccess",
    "EndpointStudyRecordPourDensityDataSourceDataProtectionClaimed",
    "EndpointStudyRecordPourDensityMaterialsAndMethods",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsDataGathering",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsGuideline",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsMethodType",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsTestMaterialsReferenceMaterial",
    "EndpointStudyRecordPourDensityMaterialsAndMethodsTestMaterialsReferenceMaterialEntry",
    "EndpointStudyRecordPourDensityOverallRemarksAttachments",
    "EndpointStudyRecordPourDensityOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordPourDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordPourDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordPourDensityResultsAndDiscussion",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordPourDensityResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordPourDensityResultsAndDiscussionPourDensity",
    "EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntry",
    "EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntryMean",
    "EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntryRemarksOnResults",
    "EndpointStudyRecordPourDensityResultsAndDiscussionPourDensityEntryStDev",
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
