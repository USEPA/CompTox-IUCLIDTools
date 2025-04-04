from specificinvestigations_6_5.models.common_types_oecd_v9 import (
    A03,
    A36,
    C08,
    N64,
    N78,
    T0210,
    T24,
    T25,
    T27,
    T167,
    T168,
    T284,
    T23123456,
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
    Pg660321,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
    Td390,
)
from specificinvestigations_6_5.models.endpoint_study_record_specific_investigations_9_0 import (
    EndpointStudyRecordSpecificInvestigations,
    EndpointStudyRecordSpecificInvestigationsAdministrativeData,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataAttachedJustification,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataCrossReference,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataProtection,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataWaiving,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataEndpoint,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataPurposeFlag,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataRationalReliability,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataReliability,
    EndpointStudyRecordSpecificInvestigationsAdministrativeDataStudyResultType,
    EndpointStudyRecordSpecificInvestigationsApplicantSummaryAndConclusion,
    EndpointStudyRecordSpecificInvestigationsDataSource,
    EndpointStudyRecordSpecificInvestigationsDataSourceDataAccess,
    EndpointStudyRecordSpecificInvestigationsDataSourceDataProtectionClaimed,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethods,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposure,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureControlAnimals,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureDosesConcentrations,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureRouteOfAdministration,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureVehicle,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsEndpointAddressed,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsExaminations,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuideline,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsMethodType,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimals,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimalsSex,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimalsSpecies,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimalsStrain,
    EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachments,
    EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussion,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
)
from specificinvestigations_6_5.models.platform_fields import (
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
from specificinvestigations_6_5.models.xml import LangValue

__all__ = [
    "A03",
    "A36",
    "C08",
    "N64",
    "N78",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660321",
    "Pg661157",
    "Pg661574",
    "Pg661576",
    "Pg661577",
    "Pg661579",
    "T0210",
    "T167",
    "T168",
    "T23123456",
    "T24",
    "T25",
    "T27",
    "T284",
    "Td390",
    "Y143",
    "Z02",
    "Z03",
    "Z05",
    "Z06",
    "Z08",
    "Z30",
    "Z40",
    "Z52",
    "EndpointStudyRecordSpecificInvestigations",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeData",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataAttachedJustification",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataCrossReference",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataProtection",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataWaiving",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataEndpoint",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataPurposeFlag",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataRationalReliability",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataReliability",
    "EndpointStudyRecordSpecificInvestigationsAdministrativeDataStudyResultType",
    "EndpointStudyRecordSpecificInvestigationsApplicantSummaryAndConclusion",
    "EndpointStudyRecordSpecificInvestigationsDataSource",
    "EndpointStudyRecordSpecificInvestigationsDataSourceDataAccess",
    "EndpointStudyRecordSpecificInvestigationsDataSourceDataProtectionClaimed",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethods",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposure",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureAnalyticalVerificationOfDosesOrConcentrations",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureControlAnimals",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureDosesConcentrations",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntry",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureDosesConcentrationsEntryDoseConc",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureRouteOfAdministration",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAdministrationExposureVehicle",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsEndpointAddressed",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsExaminations",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuideline",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsMethodType",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimals",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimalsSex",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimalsSpecies",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestAnimalsStrain",
    "EndpointStudyRecordSpecificInvestigationsMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachments",
    "EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordSpecificInvestigationsOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussion",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordSpecificInvestigationsResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
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
