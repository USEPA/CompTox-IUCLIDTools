from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from category_6_5.models.common_types_domain_v9 import (
    N64,
    N78,
)
from category_6_5.models.platform_fields import (
    BaseDataProtectionField,
    BasePicklistField,
    DocumentReferenceMultipleField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldMultiLine,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
    SectionTypesField,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0"


@dataclass
class CategoryCategoryDocuments:
    class Meta:
        global_type = False

    category_sections: Optional[SectionTypesField] = field(
        default=None,
        metadata={
            "name": "CategorySections",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class CategoryJustificationsAndDiscussionsReportsEntryFlagsLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class CategoryRegulatoryPurposes(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class CategoryJustificationsAndDiscussionsReportsEntryFlags(
    BaseDataProtectionField
):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    legislation: List[
        CategoryJustificationsAndDiscussionsReportsEntryFlagsLegislation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class CategoryJustificationsAndDiscussionsReportsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    flags: Optional[CategoryJustificationsAndDiscussionsReportsEntryFlags] = (
        field(
            default=None,
            metadata={
                "name": "Flags",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
            },
        )
    )
    report: Optional[str] = field(
        default=None,
        metadata={
            "name": "Report",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class CategoryJustificationsAndDiscussionsReports:
    class Meta:
        global_type = False

    entry: List[CategoryJustificationsAndDiscussionsReportsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class CategoryJustificationsAndDiscussions:
    class Meta:
        global_type = False

    category_definition: List[MultilingualTextFieldMultiLine] = field(
        default_factory=list,
        metadata={
            "name": "CategoryDefinition",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    category_order_description: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CategoryOrderDescription",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    category_rationale: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "CategoryRationale",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )
    reports: Optional[CategoryJustificationsAndDiscussionsReports] = field(
        default=None,
        metadata={
            "name": "Reports",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0",
        },
    )


@dataclass
class Category:
    class Meta:
        name = "CATEGORY"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/CATEGORY/9.0"

    category_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryName",
            "type": "Element",
            "required": True,
        },
    )
    public_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicName",
            "type": "Element",
        },
    )
    owner_legal_entity: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnerLegalEntity",
            "type": "Element",
        },
    )
    regulatory_purposes: List[CategoryRegulatoryPurposes] = field(
        default_factory=list,
        metadata={
            "name": "RegulatoryPurposes",
            "type": "Element",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
        },
    )
    members: Optional[DocumentReferenceMultipleField] = field(
        default=None,
        metadata={
            "name": "Members",
            "type": "Element",
        },
    )
    category_documents: Optional[CategoryCategoryDocuments] = field(
        default=None,
        metadata={
            "name": "CategoryDocuments",
            "type": "Element",
        },
    )
    justifications_and_discussions: Optional[
        CategoryJustificationsAndDiscussions
    ] = field(
        default=None,
        metadata={
            "name": "JustificationsAndDiscussions",
            "type": "Element",
        },
    )
