from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from platform_container_6_5.models.platform_attachment import (
    Attachment,
    AttachmentRef,
)
from platform_container_6_5.models.platform_metadata import (
    CreationDate,
    CreationTool,
    DefinitionVersion,
    DocumentKey,
    DocumentSubType,
    DocumentType,
    DossierSubject,
    I5Origin,
    IuclidVersion,
    LastModificationDate,
    Name,
    OrderInSectionNo,
    ParentDocumentKey,
    SnapshotCreationTool,
    SubmissionType,
    SubmissionTypeVersion,
    SubmittingLegalEntity,
)
from platform_container_6_5.models.platform_modification_history import (
    Modification,
)

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/platform-container/v1"
)


@dataclass
class DocumentContent:
    class Meta:
        global_type = False

    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class DocumentAttachments:
    class Meta:
        global_type = False

    attachment: List[Attachment] = field(
        default_factory=list,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1",
            "sequence": 1,
        },
    )
    attachment_ref: List[AttachmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AttachmentRef",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1",
            "sequence": 1,
        },
    )


@dataclass
class DocumentModificationHistory:
    class Meta:
        global_type = False

    modification: List[Modification] = field(
        default_factory=list,
        metadata={
            "name": "Modification",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-modification-history/v1",
        },
    )


@dataclass
class DocumentPlatformMetadata:
    class Meta:
        global_type = False

    iuclid_version: List[IuclidVersion] = field(
        default_factory=list,
        metadata={
            "name": "iuclidVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    document_key: List[DocumentKey] = field(
        default_factory=list,
        metadata={
            "name": "documentKey",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    document_type: List[DocumentType] = field(
        default_factory=list,
        metadata={
            "name": "documentType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    definition_version: List[DefinitionVersion] = field(
        default_factory=list,
        metadata={
            "name": "definitionVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    creation_date: List[CreationDate] = field(
        default_factory=list,
        metadata={
            "name": "creationDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    last_modification_date: List[LastModificationDate] = field(
        default_factory=list,
        metadata={
            "name": "lastModificationDate",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    document_sub_type: List[DocumentSubType] = field(
        default_factory=list,
        metadata={
            "name": "documentSubType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    parent_document_key: List[ParentDocumentKey] = field(
        default_factory=list,
        metadata={
            "name": "parentDocumentKey",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    order_in_section_no: List[OrderInSectionNo] = field(
        default_factory=list,
        metadata={
            "name": "orderInSectionNo",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    submission_type: List[SubmissionType] = field(
        default_factory=list,
        metadata={
            "name": "submissionType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    submission_type_version: List[SubmissionTypeVersion] = field(
        default_factory=list,
        metadata={
            "name": "submissionTypeVersion",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    submitting_legal_entity: List[SubmittingLegalEntity] = field(
        default_factory=list,
        metadata={
            "name": "submittingLegalEntity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    dossier_subject: List[DossierSubject] = field(
        default_factory=list,
        metadata={
            "name": "dossierSubject",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    i5_origin: List[I5Origin] = field(
        default_factory=list,
        metadata={
            "name": "i5Origin",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    creation_tool: List[CreationTool] = field(
        default_factory=list,
        metadata={
            "name": "creationTool",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )
    snapshot_creation_tool: List[SnapshotCreationTool] = field(
        default_factory=list,
        metadata={
            "name": "snapshotCreationTool",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1",
            "sequence": 1,
        },
    )


@dataclass
class Document:
    """
    Contains top-level information concerning the IUCLID6 document along with the
    document's actual chemical information content.

    :ivar platform_metadata: Contains the top-level information of a
        IUCLID6 document such as document identifier, name, type and
        subtype, etc. <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> The elements are included in the platform-
        metadata.xsd
    :ivar content: Contains the chemical information of the specific
        IUCLID6 document. <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> The content is dynamic and is defined in the
        corresponding .xsd per document definition identifier. in the
        form of "document_type"-"document_subtype"-"version".xsd.
        Example: ENDPOINT_STUDY_RECORD-Density-4.0.xsd
    :ivar attachments: Lists the attachments that are directly linked to
        the document. The content of this section is an unbounded list
        of references to attachment identifiers that this document is
        linked to. <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> The elements are included in the platform-
        attachment.xsd
    :ivar modification_history: Lists the entries of the document's
        modification history. Every entry is a single operation that
        took place on the specific document and specifies the date of
        the action, the user that run the action, the submitting legal
        entity of the user and the modification remarks if any. <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-
        container/v1"/> The elements are included in the platform-
        modification-history.xsd
    """

    class Meta:
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-container/v1"
        )

    platform_metadata: Optional[DocumentPlatformMetadata] = field(
        default=None,
        metadata={
            "name": "PlatformMetadata",
            "type": "Element",
            "required": True,
        },
    )
    content: Optional[DocumentContent] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "required": True,
        },
    )
    attachments: Optional[DocumentAttachments] = field(
        default=None,
        metadata={
            "name": "Attachments",
            "type": "Element",
            "nillable": True,
        },
    )
    modification_history: Optional[DocumentModificationHistory] = field(
        default=None,
        metadata={
            "name": "ModificationHistory",
            "type": "Element",
            "nillable": True,
        },
    )
