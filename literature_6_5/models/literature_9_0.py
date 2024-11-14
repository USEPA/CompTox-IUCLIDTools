from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDate

from literature_6_5.models.common_types_domain_v9 import (
    Z31,
    Pg661156,
    Pg661157,
)
from literature_6_5.models.platform_fields import (
    BasePicklistField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
    RepeatableEntryType,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0"


@dataclass
class LiteratureGeneralInfoAttachmentsEntryAttachmentType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg661157] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfoLiteratureType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Z31] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfoStudyIdentifiersEntryStudyIdtype(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg661156] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfoAttachmentsEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    attachment_type: Optional[
        LiteratureGeneralInfoAttachmentsEntryAttachmentType
    ] = field(
        default=None,
        metadata={
            "name": "AttachmentType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    attached_documents: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedDocuments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    attached_sanitised_docs_for_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttachedSanitisedDocsForPublication",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfoStudyIdentifiersEntry(RepeatableEntryType):
    class Meta:
        global_type = False

    study_idtype: Optional[
        LiteratureGeneralInfoStudyIdentifiersEntryStudyIdtype
    ] = field(
        default=None,
        metadata={
            "name": "StudyIDType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    study_id: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "StudyID",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfoAttachments:
    class Meta:
        global_type = False

    entry: List[LiteratureGeneralInfoAttachmentsEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfoStudyIdentifiers:
    class Meta:
        global_type = False

    entry: List[LiteratureGeneralInfoStudyIdentifiersEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class LiteratureGeneralInfo:
    class Meta:
        global_type = False

    literature_type: Optional[LiteratureGeneralInfoLiteratureType] = field(
        default=None,
        metadata={
            "name": "LiteratureType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
            "required": True,
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    reference_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceYear",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
            "min_inclusive": 1000,
            "max_inclusive": 9999,
            "nillable": True,
        },
    )
    source: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    test_lab: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "TestLab",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    report_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReportDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
            "nillable": True,
        },
    )
    report_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReportNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    company_owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyOwner",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    company_owner_study_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyOwnerStudyNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    study_identifiers: Optional[LiteratureGeneralInfoStudyIdentifiers] = field(
        default=None,
        metadata={
            "name": "StudyIdentifiers",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    attachments: Optional[LiteratureGeneralInfoAttachments] = field(
        default=None,
        metadata={
            "name": "Attachments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0",
        },
    )


@dataclass
class Literature:
    class Meta:
        name = "LITERATURE"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/LITERATURE/9.0"

    general_info: Optional[LiteratureGeneralInfo] = field(
        default=None,
        metadata={
            "name": "GeneralInfo",
            "type": "Element",
            "required": True,
        },
    )
