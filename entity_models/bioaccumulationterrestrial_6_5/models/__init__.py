from bioaccumulationterrestrial_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    E04,
    E34,
    E148,
    F102,
    F119,
    F120,
    F121,
    F123,
    F133,
    F138,
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
    Pg660038,
    Pg660185,
    Pg660186,
    Pg660490,
    Pg661157,
    Pg661166,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td330,
)
from bioaccumulationterrestrial_6_5.models.endpoint_study_record_bioaccumulation_terrestrial_9_0 import (
    EndpointStudyRecordBioaccumulationTerrestrial,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeData,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustification,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReference,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtection,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaiving,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataEndpoint,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataPurposeFlag,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataRationalReliability,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataReliability,
    EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataStudyResultType,
    EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusion,
    EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusionValidityCriteriaFulfilled,
    EndpointStudyRecordBioaccumulationTerrestrialDataSource,
    EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataAccess,
    EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataProtectionClaimed,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethods,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuideline,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsSamplingAndAnalysis,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesign,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalDepurationDuration,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestConditions,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterialsRadiolabelling,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganisms,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganismsTestOrganismsSpecies,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrate,
    EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrateVehicle,
    EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachments,
    EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussion,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactor,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntry,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryBasis,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryType,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryValue,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepuration,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntry,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryDepurationTime,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryElimination,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryEndpoint,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryRemarksOnResults,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolites,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolitesEntry,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolitesEntryIdno,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolitesEntryMaximumOccurrence,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContent,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntry,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryLipidContent,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryRemarksOnResults,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryTimePoint,
    EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionMetabolitesDetails,
)
from bioaccumulationterrestrial_6_5.models.platform_fields import (
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
from bioaccumulationterrestrial_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A36",
    "E04",
    "E148",
    "E34",
    "F102",
    "F119",
    "F120",
    "F121",
    "F123",
    "F133",
    "F138",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660185",
    "Pg660186",
    "Pg660490",
    "Pg661157",
    "Pg661166",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "Td330",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z40",
    "Z52",
    "EndpointStudyRecordBioaccumulationTerrestrial",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeData",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustification",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReference",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtection",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaiving",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataEndpoint",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataPurposeFlag",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataRationalReliability",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataReliability",
    "EndpointStudyRecordBioaccumulationTerrestrialAdministrativeDataStudyResultType",
    "EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusion",
    "EndpointStudyRecordBioaccumulationTerrestrialApplicantSummaryAndConclusionValidityCriteriaFulfilled",
    "EndpointStudyRecordBioaccumulationTerrestrialDataSource",
    "EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataAccess",
    "EndpointStudyRecordBioaccumulationTerrestrialDataSourceDataProtectionClaimed",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethods",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuideline",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsSamplingAndAnalysis",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesign",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalDepurationDuration",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsStudyDesignTotalExposureUptakeDuration",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestConditions",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestMaterialsRadiolabelling",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganisms",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestOrganismsTestOrganismsSpecies",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrate",
    "EndpointStudyRecordBioaccumulationTerrestrialMaterialsAndMethodsTestSubstrateVehicle",
    "EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachments",
    "EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussion",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactor",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryBasis",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryCalculationBasis",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryRemarksOnResults",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryTimeOfPlateau",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryType",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionBioaccumulationFactorEntryValue",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepuration",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryDepurationTime",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryElimination",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryEndpoint",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionDepurationEntryRemarksOnResults",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolites",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolitesEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolitesEntryIdno",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionIdentityOfMetabolitesEntryMaximumOccurrence",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContent",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntry",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryLipidContent",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryRemarksOnResults",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionLipidContentEntryTimePoint",
    "EndpointStudyRecordBioaccumulationTerrestrialResultsAndDiscussionMetabolitesDetails",
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
