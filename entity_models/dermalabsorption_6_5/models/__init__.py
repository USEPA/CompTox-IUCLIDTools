from dermalabsorption_6_5.models.common_types_oecd_v9 import (
    A36,
    E18,
    E34,
    N64,
    N78,
    T0210,
    T24,
    T48,
    T50,
    T132,
    T148,
    T23123456,
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
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660269,
    Pg660272,
    Pg660273,
    Pg660360,
    Pg660490,
    Pg661107,
    Pg661157,
    Pg661166,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from dermalabsorption_6_5.models.endpoint_study_record_dermal_absorption_9_0 import (
    EndpointStudyRecordDermalAbsorption,
    EndpointStudyRecordDermalAbsorptionAdministrativeData,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataAttachedJustification,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataCrossReference,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataDataProtection,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataDataWaiving,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataEndpoint,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataPurposeFlag,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataRationalReliability,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataReliability,
    EndpointStudyRecordDermalAbsorptionAdministrativeDataStudyResultType,
    EndpointStudyRecordDermalAbsorptionApplicantSummaryAndConclusion,
    EndpointStudyRecordDermalAbsorptionDataSource,
    EndpointStudyRecordDermalAbsorptionDataSourceDataAccess,
    EndpointStudyRecordDermalAbsorptionDataSourceDataProtectionClaimed,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethods,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposure,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposureControlAnimals,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposureTypeOfCoverage,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposureVehicle,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuideline,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimals,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimalsSex,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimalsSpecies,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimalsStrain,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestMaterialsRadiolabelling,
    EndpointStudyRecordDermalAbsorptionOverallRemarksAttachments,
    EndpointStudyRecordDermalAbsorptionOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordDermalAbsorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordDermalAbsorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussion,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorption,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntry,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryAbsorption,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryConcentrateDilution,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryParameter,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryRemarksOnResults,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryTimePoint,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionDermalIrritation,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolites,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolitesEntry,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolitesEntryIdno,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolitesEntryMaximumOccurrence,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionMetabolites,
    EndpointStudyRecordDermalAbsorptionResultsAndDiscussionSignsSymptomsToxicity,
)
from dermalabsorption_6_5.models.platform_fields import (
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
from dermalabsorption_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "E18",
    "E34",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660269",
    "Pg660272",
    "Pg660273",
    "Pg660360",
    "Pg660490",
    "Pg661107",
    "Pg661157",
    "Pg661166",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "T0210",
    "T132",
    "T148",
    "T23123456",
    "T24",
    "T48",
    "T50",
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
    "EndpointStudyRecordDermalAbsorption",
    "EndpointStudyRecordDermalAbsorptionAdministrativeData",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataAttachedJustification",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataCrossReference",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataDataProtection",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataDataWaiving",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataEndpoint",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataPurposeFlag",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataRationalReliability",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataReliability",
    "EndpointStudyRecordDermalAbsorptionAdministrativeDataStudyResultType",
    "EndpointStudyRecordDermalAbsorptionApplicantSummaryAndConclusion",
    "EndpointStudyRecordDermalAbsorptionDataSource",
    "EndpointStudyRecordDermalAbsorptionDataSourceDataAccess",
    "EndpointStudyRecordDermalAbsorptionDataSourceDataProtectionClaimed",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethods",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposure",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposureControlAnimals",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposureTypeOfCoverage",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAdministrationExposureVehicle",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuideline",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimals",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimalsSex",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimalsSpecies",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestAnimalsStrain",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordDermalAbsorptionMaterialsAndMethodsTestMaterialsRadiolabelling",
    "EndpointStudyRecordDermalAbsorptionOverallRemarksAttachments",
    "EndpointStudyRecordDermalAbsorptionOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordDermalAbsorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordDermalAbsorptionOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussion",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorption",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntry",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryAbsorption",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryConcentrateDilution",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryParameter",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryRemarksOnResults",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAbsorptionEntryTimePoint",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionDermalIrritation",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolites",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolitesEntry",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolitesEntryIdno",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionIdentityOfMetabolitesEntryMaximumOccurrence",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionMetabolites",
    "EndpointStudyRecordDermalAbsorptionResultsAndDiscussionSignsSymptomsToxicity",
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
