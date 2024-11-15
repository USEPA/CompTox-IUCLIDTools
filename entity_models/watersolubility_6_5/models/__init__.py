from watersolubility_6_5.models.common_types_oecd_v9 import (
    A36,
    A102,
    E04,
    E105,
    N64,
    N78,
    P08,
    P09,
    P37,
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
    Pg660044,
    Pg660045,
    Pg660047,
    Pg660055,
    Pg660058,
    Pg660059,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from watersolubility_6_5.models.endpoint_study_record_water_solubility_9_0 import (
    EndpointStudyRecordWaterSolubility,
    EndpointStudyRecordWaterSolubilityAdministrativeData,
    EndpointStudyRecordWaterSolubilityAdministrativeDataAttachedJustification,
    EndpointStudyRecordWaterSolubilityAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordWaterSolubilityAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordWaterSolubilityAdministrativeDataCrossReference,
    EndpointStudyRecordWaterSolubilityAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordWaterSolubilityAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordWaterSolubilityAdministrativeDataDataProtection,
    EndpointStudyRecordWaterSolubilityAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordWaterSolubilityAdministrativeDataDataWaiving,
    EndpointStudyRecordWaterSolubilityAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordWaterSolubilityAdministrativeDataEndpoint,
    EndpointStudyRecordWaterSolubilityAdministrativeDataPurposeFlag,
    EndpointStudyRecordWaterSolubilityAdministrativeDataRationalReliability,
    EndpointStudyRecordWaterSolubilityAdministrativeDataReliability,
    EndpointStudyRecordWaterSolubilityAdministrativeDataStudyResultType,
    EndpointStudyRecordWaterSolubilityApplicantSummaryAndConclusion,
    EndpointStudyRecordWaterSolubilityDataSource,
    EndpointStudyRecordWaterSolubilityDataSourceDataAccess,
    EndpointStudyRecordWaterSolubilityDataSourceDataProtectionClaimed,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethods,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuideline,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsMethodType,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsStudyDesignAnalyticalMethod,
    EndpointStudyRecordWaterSolubilityMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordWaterSolubilityOverallRemarksAttachments,
    EndpointStudyRecordWaterSolubilityOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordWaterSolubilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordWaterSolubilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussion,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMedia,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntry,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryIncubationDuration,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryLoadingOfAqueousPhase,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryMeanDissolvedConc,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryRemarksOnResults,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryTypeOfTest,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubility,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntry,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryConcBasedOn,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryIncubationDuration,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryLoadingOfAqueousPhase,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryPh,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryRemarksOnResults,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntrySolubility,
    EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryTemp,
)
from watersolubility_6_5.models.platform_fields import (
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
from watersolubility_6_5.models.xml import LangValue

__all__ = [
    "A102",
    "A36",
    "E04",
    "E105",
    "N64",
    "N78",
    "P08",
    "P09",
    "P37",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660044",
    "Pg660045",
    "Pg660047",
    "Pg660055",
    "Pg660058",
    "Pg660059",
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
    "EndpointStudyRecordWaterSolubility",
    "EndpointStudyRecordWaterSolubilityAdministrativeData",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataAttachedJustification",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataCrossReference",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataDataProtection",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataDataWaiving",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataEndpoint",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataPurposeFlag",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataRationalReliability",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataReliability",
    "EndpointStudyRecordWaterSolubilityAdministrativeDataStudyResultType",
    "EndpointStudyRecordWaterSolubilityApplicantSummaryAndConclusion",
    "EndpointStudyRecordWaterSolubilityDataSource",
    "EndpointStudyRecordWaterSolubilityDataSourceDataAccess",
    "EndpointStudyRecordWaterSolubilityDataSourceDataProtectionClaimed",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethods",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuideline",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsMethodType",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsStudyDesignAnalyticalMethod",
    "EndpointStudyRecordWaterSolubilityMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordWaterSolubilityOverallRemarksAttachments",
    "EndpointStudyRecordWaterSolubilityOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordWaterSolubilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordWaterSolubilityOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussion",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMedia",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntry",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryIncubationDuration",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryLoadingOfAqueousPhase",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryMeanDissolvedConc",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryRemarksOnResults",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionSolubilityOfMetalIonsInAqueousMediaEntryTypeOfTest",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubility",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntry",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryConcBasedOn",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryIncubationDuration",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryLoadingOfAqueousPhase",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryPh",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryRemarksOnResults",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntrySolubility",
    "EndpointStudyRecordWaterSolubilityResultsAndDiscussionWaterSolubilityEntryTemp",
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
