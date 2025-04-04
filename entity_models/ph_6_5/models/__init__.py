from ph_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    N64,
    N78,
    P08,
    P114,
    Y143,
    Z02,
    Z03,
    Z05,
    Z06,
    Z08,
    Z30,
    Z40,
    Z52,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660098,
    Pg660107,
    Pg660115,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from ph_6_5.models.endpoint_study_record_ph_9_0 import (
    EndpointStudyRecordPh,
    EndpointStudyRecordPhAdministrativeData,
    EndpointStudyRecordPhAdministrativeDataAttachedJustification,
    EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordPhAdministrativeDataCrossReference,
    EndpointStudyRecordPhAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordPhAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordPhAdministrativeDataDataProtection,
    EndpointStudyRecordPhAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordPhAdministrativeDataDataWaiving,
    EndpointStudyRecordPhAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordPhAdministrativeDataEndpoint,
    EndpointStudyRecordPhAdministrativeDataPurposeFlag,
    EndpointStudyRecordPhAdministrativeDataRationalReliability,
    EndpointStudyRecordPhAdministrativeDataReliability,
    EndpointStudyRecordPhAdministrativeDataStudyResultType,
    EndpointStudyRecordPhApplicantSummaryAndConclusion,
    EndpointStudyRecordPhDataSource,
    EndpointStudyRecordPhDataSourceDataAccess,
    EndpointStudyRecordPhDataSourceDataProtectionClaimed,
    EndpointStudyRecordPhMaterialsAndMethods,
    EndpointStudyRecordPhMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordPhMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordPhMaterialsAndMethodsGuideline,
    EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordPhMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordPhMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordPhMaterialsAndMethodsReagents,
    EndpointStudyRecordPhMaterialsAndMethodsReagentsReagent,
    EndpointStudyRecordPhMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordPhMaterialsAndMethodsTitrationOfAcidityAndAlkalinity,
    EndpointStudyRecordPhOverallRemarksAttachments,
    EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordPhResultsAndDiscussion,
    EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinity,
    EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntry,
    EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryAcidityOrAlkalinity,
    EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryRemarksOnResults,
    EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryValue,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordPhResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordPhResultsAndDiscussionPhValue,
    EndpointStudyRecordPhResultsAndDiscussionPhValueEntry,
    EndpointStudyRecordPhResultsAndDiscussionPhValueEntryConcentration,
    EndpointStudyRecordPhResultsAndDiscussionPhValueEntryRemarksOnResults,
    EndpointStudyRecordPhResultsAndDiscussionPhValueEntryTemp,
    EndpointStudyRecordPhResultsAndDiscussionPhValueEntryValue,
)
from ph_6_5.models.platform_fields import (
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
from ph_6_5.models.xml import LangValue

__all__ = [
    "A102",
    "A36",
    "N64",
    "N78",
    "P08",
    "P114",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660098",
    "Pg660107",
    "Pg660115",
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
    "EndpointStudyRecordPh",
    "EndpointStudyRecordPhAdministrativeData",
    "EndpointStudyRecordPhAdministrativeDataAttachedJustification",
    "EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordPhAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordPhAdministrativeDataCrossReference",
    "EndpointStudyRecordPhAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordPhAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordPhAdministrativeDataDataProtection",
    "EndpointStudyRecordPhAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordPhAdministrativeDataDataWaiving",
    "EndpointStudyRecordPhAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordPhAdministrativeDataEndpoint",
    "EndpointStudyRecordPhAdministrativeDataPurposeFlag",
    "EndpointStudyRecordPhAdministrativeDataRationalReliability",
    "EndpointStudyRecordPhAdministrativeDataReliability",
    "EndpointStudyRecordPhAdministrativeDataStudyResultType",
    "EndpointStudyRecordPhApplicantSummaryAndConclusion",
    "EndpointStudyRecordPhDataSource",
    "EndpointStudyRecordPhDataSourceDataAccess",
    "EndpointStudyRecordPhDataSourceDataProtectionClaimed",
    "EndpointStudyRecordPhMaterialsAndMethods",
    "EndpointStudyRecordPhMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordPhMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordPhMaterialsAndMethodsGuideline",
    "EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordPhMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordPhMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordPhMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordPhMaterialsAndMethodsReagents",
    "EndpointStudyRecordPhMaterialsAndMethodsReagentsReagent",
    "EndpointStudyRecordPhMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordPhMaterialsAndMethodsTitrationOfAcidityAndAlkalinity",
    "EndpointStudyRecordPhOverallRemarksAttachments",
    "EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordPhOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordPhResultsAndDiscussion",
    "EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinity",
    "EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntry",
    "EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryAcidityOrAlkalinity",
    "EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryRemarksOnResults",
    "EndpointStudyRecordPhResultsAndDiscussionAcidityOrAlkalinityEntryValue",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordPhResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordPhResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordPhResultsAndDiscussionPhValue",
    "EndpointStudyRecordPhResultsAndDiscussionPhValueEntry",
    "EndpointStudyRecordPhResultsAndDiscussionPhValueEntryConcentration",
    "EndpointStudyRecordPhResultsAndDiscussionPhValueEntryRemarksOnResults",
    "EndpointStudyRecordPhResultsAndDiscussionPhValueEntryTemp",
    "EndpointStudyRecordPhResultsAndDiscussionPhValueEntryValue",
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
