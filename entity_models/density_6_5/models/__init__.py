from density_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    N64,
    N78,
    P04,
    P05,
    P18,
    P34,
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
    Pg660035,
    Pg660037,
    Pg660038,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from density_6_5.models.endpoint_study_record_density_9_0 import (
    EndpointStudyRecordDensity,
    EndpointStudyRecordDensityAdministrativeData,
    EndpointStudyRecordDensityAdministrativeDataAttachedJustification,
    EndpointStudyRecordDensityAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordDensityAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordDensityAdministrativeDataCrossReference,
    EndpointStudyRecordDensityAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordDensityAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordDensityAdministrativeDataDataProtection,
    EndpointStudyRecordDensityAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordDensityAdministrativeDataDataWaiving,
    EndpointStudyRecordDensityAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordDensityAdministrativeDataEndpoint,
    EndpointStudyRecordDensityAdministrativeDataPurposeFlag,
    EndpointStudyRecordDensityAdministrativeDataRationalReliability,
    EndpointStudyRecordDensityAdministrativeDataReliability,
    EndpointStudyRecordDensityAdministrativeDataStudyResultType,
    EndpointStudyRecordDensityApplicantSummaryAndConclusion,
    EndpointStudyRecordDensityDataSource,
    EndpointStudyRecordDensityDataSourceDataAccess,
    EndpointStudyRecordDensityDataSourceDataProtectionClaimed,
    EndpointStudyRecordDensityMaterialsAndMethods,
    EndpointStudyRecordDensityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordDensityMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordDensityMaterialsAndMethodsGuideline,
    EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordDensityMaterialsAndMethodsMethodType,
    EndpointStudyRecordDensityMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordDensityMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordDensityMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordDensityOverallRemarksAttachments,
    EndpointStudyRecordDensityOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordDensityResultsAndDiscussion,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordDensityResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordDensityResultsAndDiscussionDensity,
    EndpointStudyRecordDensityResultsAndDiscussionDensityEntry,
    EndpointStudyRecordDensityResultsAndDiscussionDensityEntryDensity,
    EndpointStudyRecordDensityResultsAndDiscussionDensityEntryRemarksOnResults,
    EndpointStudyRecordDensityResultsAndDiscussionDensityEntryTemp,
    EndpointStudyRecordDensityResultsAndDiscussionDensityEntryType,
)
from density_6_5.models.platform_fields import (
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
from density_6_5.models.xml import LangValue

__all__ = [
    "A102",
    "A36",
    "N64",
    "N78",
    "P04",
    "P05",
    "P18",
    "P34",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660035",
    "Pg660037",
    "Pg660038",
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
    "EndpointStudyRecordDensity",
    "EndpointStudyRecordDensityAdministrativeData",
    "EndpointStudyRecordDensityAdministrativeDataAttachedJustification",
    "EndpointStudyRecordDensityAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordDensityAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordDensityAdministrativeDataCrossReference",
    "EndpointStudyRecordDensityAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordDensityAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordDensityAdministrativeDataDataProtection",
    "EndpointStudyRecordDensityAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordDensityAdministrativeDataDataWaiving",
    "EndpointStudyRecordDensityAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordDensityAdministrativeDataEndpoint",
    "EndpointStudyRecordDensityAdministrativeDataPurposeFlag",
    "EndpointStudyRecordDensityAdministrativeDataRationalReliability",
    "EndpointStudyRecordDensityAdministrativeDataReliability",
    "EndpointStudyRecordDensityAdministrativeDataStudyResultType",
    "EndpointStudyRecordDensityApplicantSummaryAndConclusion",
    "EndpointStudyRecordDensityDataSource",
    "EndpointStudyRecordDensityDataSourceDataAccess",
    "EndpointStudyRecordDensityDataSourceDataProtectionClaimed",
    "EndpointStudyRecordDensityMaterialsAndMethods",
    "EndpointStudyRecordDensityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordDensityMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordDensityMaterialsAndMethodsGuideline",
    "EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordDensityMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordDensityMaterialsAndMethodsMethodType",
    "EndpointStudyRecordDensityMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordDensityMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordDensityMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordDensityOverallRemarksAttachments",
    "EndpointStudyRecordDensityOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordDensityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordDensityResultsAndDiscussion",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordDensityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordDensityResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordDensityResultsAndDiscussionDensity",
    "EndpointStudyRecordDensityResultsAndDiscussionDensityEntry",
    "EndpointStudyRecordDensityResultsAndDiscussionDensityEntryDensity",
    "EndpointStudyRecordDensityResultsAndDiscussionDensityEntryRemarksOnResults",
    "EndpointStudyRecordDensityResultsAndDiscussionDensityEntryTemp",
    "EndpointStudyRecordDensityResultsAndDiscussionDensityEntryType",
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
