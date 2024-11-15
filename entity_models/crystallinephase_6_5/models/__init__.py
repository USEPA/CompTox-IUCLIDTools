from crystallinephase_6_5.models.common_types_oecd_v9 import (
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
    Nm21,
    Nm35,
    Nm38,
    Pg660008,
    Pg660009,
    Pg660010,
    Pg660013,
    Pg660038,
    Pg660333,
    Pg661157,
    Pg661574,
    Pg661576,
    Pg661577,
    Pg661579,
)
from crystallinephase_6_5.models.endpoint_study_record_crystalline_phase_9_0 import (
    EndpointStudyRecordCrystallinePhase,
    EndpointStudyRecordCrystallinePhaseAdministrativeData,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataAttachedJustification,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataAttachedJustificationEntry,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataAttachedJustificationEntryReasonPurpose,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataCrossReference,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataCrossReferenceEntry,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataCrossReferenceEntryReasonPurpose,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataDataProtection,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataDataProtectionLegislation,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataDataWaiving,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataDataWaivingJustification,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataEndpoint,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataPurposeFlag,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataRationalReliability,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataReliability,
    EndpointStudyRecordCrystallinePhaseAdministrativeDataStudyResultType,
    EndpointStudyRecordCrystallinePhaseApplicantSummaryAndConclusion,
    EndpointStudyRecordCrystallinePhaseDataSource,
    EndpointStudyRecordCrystallinePhaseDataSourceDataAccess,
    EndpointStudyRecordCrystallinePhaseDataSourceDataProtectionClaimed,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethods,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsDataGathering,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGlpcomplianceStatement,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuideline,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntry,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntryDeviation,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntryGuideline,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntryQualifier,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsMethodType,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsModelAndSoftware,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsOtherQualityAssurance,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsTestMaterials,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsTestMaterialsReferenceMaterial,
    EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsTestMaterialsReferenceMaterialEntry,
    EndpointStudyRecordCrystallinePhaseOverallRemarksAttachments,
    EndpointStudyRecordCrystallinePhaseOverallRemarksAttachmentsAttachedBackgroundMaterial,
    EndpointStudyRecordCrystallinePhaseOverallRemarksAttachmentsAttachedBackgroundMaterialEntry,
    EndpointStudyRecordCrystallinePhaseOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussion,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAnyOtherInformationOnResultsInclTables,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhase,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntry,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntryBravaisLattice,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntryCrystalSystem,
    EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntryRemarksOnResults,
)
from crystallinephase_6_5.models.platform_fields import (
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
from crystallinephase_6_5.models.xml import LangValue

__all__ = [
    "A36",
    "N64",
    "N78",
    "Nm21",
    "Nm35",
    "Nm38",
    "Pg660008",
    "Pg660009",
    "Pg660010",
    "Pg660013",
    "Pg660038",
    "Pg660333",
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
    "EndpointStudyRecordCrystallinePhase",
    "EndpointStudyRecordCrystallinePhaseAdministrativeData",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataAttachedJustification",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataAttachedJustificationEntry",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataAttachedJustificationEntryReasonPurpose",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataCrossReference",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataCrossReferenceEntry",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataCrossReferenceEntryReasonPurpose",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataDataProtection",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataDataProtectionLegislation",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataDataWaiving",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataDataWaivingJustification",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataEndpoint",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataPurposeFlag",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataRationalReliability",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataReliability",
    "EndpointStudyRecordCrystallinePhaseAdministrativeDataStudyResultType",
    "EndpointStudyRecordCrystallinePhaseApplicantSummaryAndConclusion",
    "EndpointStudyRecordCrystallinePhaseDataSource",
    "EndpointStudyRecordCrystallinePhaseDataSourceDataAccess",
    "EndpointStudyRecordCrystallinePhaseDataSourceDataProtectionClaimed",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethods",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsAnyOtherInformationOnMaterialsAndMethodsInclTables",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsDataGathering",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGlpcomplianceStatement",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuideline",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntry",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntryDeviation",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntryGuideline",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsGuidelineEntryQualifier",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsMethodType",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsModelAndSoftware",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsOtherQualityAssurance",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsTestMaterials",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsTestMaterialsReferenceMaterial",
    "EndpointStudyRecordCrystallinePhaseMaterialsAndMethodsTestMaterialsReferenceMaterialEntry",
    "EndpointStudyRecordCrystallinePhaseOverallRemarksAttachments",
    "EndpointStudyRecordCrystallinePhaseOverallRemarksAttachmentsAttachedBackgroundMaterial",
    "EndpointStudyRecordCrystallinePhaseOverallRemarksAttachmentsAttachedBackgroundMaterialEntry",
    "EndpointStudyRecordCrystallinePhaseOverallRemarksAttachmentsAttachedBackgroundMaterialEntryType",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussion",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictions",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheApplicabilityDomain",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsFitWithTheSpaceDefinedByTheTrainingSetOfTheModel",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalData",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntry",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntrySource",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsSimilarSubstancesWithExperimentalDataEntryField5295Legislation",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAdditionalInformationAboutApplicabilityDomainAndReliabilityOfQsarpredictionsUncertainty",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionAnyOtherInformationOnResultsInclTables",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhase",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntry",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntryBravaisLattice",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntryCrystalSystem",
    "EndpointStudyRecordCrystallinePhaseResultsAndDiscussionCrystallinePhaseEntryRemarksOnResults",
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
