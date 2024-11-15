from phototoxicityvitro_6_5.models.common_types_oecd_v9 import (
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
    ControlsPhototox,
    ControlSubPhototox,
    Pg6Phototox,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg661157,
    Pg661253,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    ResultRemarksPhototox,
    SpeciesPhototox,
    VehiclePhototox,
    Z18Phototox,
    Z52Phototox,
)
from phototoxicityvitro_6_5.models.endpoint_study_record_phototoxicity_vitro_9_0 import (
    EndpointStudyRecordPhototoxicityVitro,
    EndpointStudyRecordPhototoxicityVitroAdministrativeData,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataAttachedJustification,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataCrossReference,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataProtection,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataWaiving,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataEndpoint,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataPurposeFlag,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataRationalReliability,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataReliability,
    EndpointStudyRecordPhototoxicityVitroAdministrativeDataStudyResultType,
    EndpointStudyRecordPhototoxicityVitroApplicantSummaryAndConclusion,
    EndpointStudyRecordPhototoxicityVitroApplicantSummaryAndConclusionValidityCriteriaFulfilled,
    EndpointStudyRecordPhototoxicityVitroDataSource,
    EndpointStudyRecordPhototoxicityVitroDataSourceDataAccess,
    EndpointStudyRecordPhototoxicityVitroDataSourceDataProtectionClaimed,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethods,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuideline,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystem,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControls,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntry,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntryNegativeControls,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntryPositiveControls,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntryPositiveControlSubstance,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemSpeciesStrain,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemSpeciesStrainEntry,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemSpeciesStrainEntrySpeciesStrainCell,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemVehicle,
    EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTypeOfStudy,
    EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachments,
    EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussion,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionRemarksOnResult,
)
from phototoxicityvitro_6_5.models.platform_fields import (
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
from phototoxicityvitro_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "ControlSubPhototox",
    "ControlsPhototox",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg661157",
    "Pg661253",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "Pg6Phototox",
    "ResultRemarksPhototox",
    "SpeciesPhototox",
    "VehiclePhototox",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z18Phototox",
    "Z30",
    "Z40",
    "Z52",
    "Z52Phototox",
    "EndpointStudyRecordPhototoxicityVitro",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeData",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataAttachedJustification",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataCrossReference",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataProtection",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataWaiving",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataEndpoint",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataPurposeFlag",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataRationalReliability",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataReliability",
    "EndpointStudyRecordPhototoxicityVitroAdministrativeDataStudyResultType",
    "EndpointStudyRecordPhototoxicityVitroApplicantSummaryAndConclusion",
    "EndpointStudyRecordPhototoxicityVitroApplicantSummaryAndConclusionValidityCriteriaFulfilled",
    "EndpointStudyRecordPhototoxicityVitroDataSource",
    "EndpointStudyRecordPhototoxicityVitroDataSourceDataAccess",
    "EndpointStudyRecordPhototoxicityVitroDataSourceDataProtectionClaimed",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethods",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuideline",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystem",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControls",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntry",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntryNegativeControls",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntryPositiveControlSubstance",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemControlsEntryPositiveControls",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemSpeciesStrain",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemSpeciesStrainEntry",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemSpeciesStrainEntrySpeciesStrainCell",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTestSystemVehicle",
    "EndpointStudyRecordPhototoxicityVitroMaterialsAndMethodsTypeOfStudy",
    "EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachments",
    "EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordPhototoxicityVitroOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussion",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordPhototoxicityVitroResultsAndDiscussionRemarksOnResult",
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