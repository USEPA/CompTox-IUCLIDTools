from dataclasses import field
from enum import Enum
from typing import List, Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDateTime

from manifest_6_5.models.xlink import TypeType

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/manifest/v1"


class GeneralInformationTypeArchiveType(Enum):
    RAW_DATA = "RAW_DATA"
    DOSSIER_DATA = "DOSSIER_DATA"
    CHEMICAL_INVENTORY = "CHEMICAL_INVENTORY"


@dataclass
class GeneralInformationTypeLegislationsInfoLegislation:
    class Meta:
        global_type = False

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )


class Iuclid6DocumentsType(Enum):
    """
    Holds the list of the available IUCLID6 document types.
    """

    ANNOTATION = "ANNOTATION"
    ARTICLE = "ARTICLE"
    CATEGORY = "CATEGORY"
    DOSSIER = "DOSSIER"
    FIXED_RECORD = "FIXED_RECORD"
    FLEXIBLE_RECORD = "FLEXIBLE_RECORD"
    ENDPOINT_STUDY_RECORD = "ENDPOINT_STUDY_RECORD"
    FLEXIBLE_SUMMARY = "FLEXIBLE_SUMMARY"
    ENDPOINT_SUMMARY = "ENDPOINT_SUMMARY"
    ASSESSMENT_ENTITY = "ASSESSMENT_ENTITY"
    LEGAL_ENTITY = "LEGAL_ENTITY"
    MIXTURE = "MIXTURE"
    REFERENCE_SUBSTANCE = "REFERENCE_SUBSTANCE"
    SITE = "SITE"
    CONTACT = "CONTACT"
    LITERATURE = "LITERATURE"
    SUBSTANCE = "SUBSTANCE"
    TEMPLATE = "TEMPLATE"
    TEST_MATERIAL_INFORMATION = "TEST_MATERIAL_INFORMATION"
    INVENTORY = "INVENTORY"
    CUSTOM_ENTITY = "CUSTOM_ENTITY"
    CUSTOM_SECTION = "CUSTOM_SECTION"


@dataclass
class LegalEntityType:
    """
    The LegalEntity-specific elements included under the representation element.
    """

    class Meta:
        name = "legalEntityType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    town: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )


class LinkTypeRefType(Enum):
    PARENT = "PARENT"
    CHILD = "CHILD"
    REFERENCE = "REFERENCE"
    USES_TEMPLATE = "USES_TEMPLATE"
    REQUIRED_LEGAL_ENTITY = "REQUIRED_LEGAL_ENTITY"
    CATEGORY = "CATEGORY"
    ATTACHMENT = "ATTACHMENT"
    DOSSIER_SUBJECT = "DOSSIER_SUBJECT"
    ANNOTATION = "ANNOTATION"


@dataclass
class ReferenceSubstanceType:
    """
    The ReferenceSubstance-specific elements included under the representation
    element.
    """

    class Meta:
        name = "referenceSubstanceType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    iupac_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IUPAC-name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    cas_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CAS-number",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    inventory_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "inventory-number",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )


@dataclass
class GeneralInformationTypeLegislationsInfo:
    class Meta:
        global_type = False

    legislation: List[GeneralInformationTypeLegislationsInfoLegislation] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            },
        )
    )


@dataclass
class LinkType:
    """
    A single link between two documents.
    """

    class Meta:
        name = "linkType"

    ref_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ref-uuid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    ref_type: Optional[LinkTypeRefType] = field(
        default=None,
        metadata={
            "name": "ref-type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )


@dataclass
class LinkedDocType:
    """
    Element linking to the actual attachment content location.
    """

    class Meta:
        name = "linked-docType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass
class NameType:
    """It is the name of the document as specified by the user.

    The xlink:href attribute of the element specifies the name of the
    XML file (*.i6d) that contains the actual content of this document
    """

    class Meta:
        name = "nameType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass
class ParentType:
    """
    Holds information (document type and name) of the parent document of the
    specific document.
    """

    class Meta:
        name = "parentType"

    type_value: Optional[Iuclid6DocumentsType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )


@dataclass
class GeneralInformationType:
    """
    Holds the elements under the "general-information" section.

    :ivar title: The name that should be displayed as a first element,
        once opening the XML file via a web browser. For the time being,
        it is hardcoded to "IUCLID 6 container manifest file"
    :ivar created: The creation date of the i6z file
    :ivar author: The IUCLID user (i.e. concatenation of "First name "
        and "Last name") that created the i6z file
    :ivar application: It is by default “IUCLID6” and in a parenthesis
        the release version and build date/time are mentioned
    :ivar submission_type: The submission type of the dataset. The list
        of valid submission types is defined by the legislation elements
        available in a given IUCLID instance. Indicative values are:
        <ns1:ul
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/manifest/v1">
        <ns1:li>ENDP</ns1:li> <ns1:li>EXPERIMENTAL_DATA</ns1:li>
        <ns1:li>OECD</ns1:li> <ns1:li>OECD_HT</ns1:li>
        <ns1:li>R_AUTH_APPL</ns1:li> <ns1:li>R_DU_REPORT</ns1:li>
        <ns1:li>R_INQUIRY</ns1:li> <ns1:li>R_PPORD</ns1:li>
        <ns1:li>R_SIA_NOTIF</ns1:li> <ns1:li>R_SUB_EVAL</ns1:li>
        <ns1:li>R_A15_REST</ns1:li> <ns1:li>R_A15_SVHC</ns1:li>
        <ns1:li>CLP_ALTERNATIVE_NAME</ns1:li> <ns1:li>CLP_NOTIF</ns1:li>
        <ns1:li>CLP_CLH</ns1:li> <ns1:li>R_1-10_PC</ns1:li>
        <ns1:li>R_1-10_STD</ns1:li> <ns1:li>R_10-100</ns1:li>
        <ns1:li>R_100-1000</ns1:li> <ns1:li>R_ABOVE_1000</ns1:li>
        <ns1:li>R_INT_ONSITE</ns1:li> <ns1:li>R_INT_TR_1-1000</ns1:li>
        <ns1:li>R_INT_TR_ABOVE_1000</ns1:li> <ns1:li>R_JS_MBER</ns1:li>
        <ns1:li>R_INT_JS_MBER</ns1:li>
        <ns1:li>BIOC_ACTIVE_SUBSTANCE</ns1:li>
        <ns1:li>BIOC_ACTIVE_SUBSTANCE_FOR_MIXTURES</ns1:li>
        <ns1:li>BIOC_BASIC_INFORMATION</ns1:li>
        <ns1:li>BIOC_BASIC_INFORMATION_MIXTURE</ns1:li>
        <ns1:li>BIOC_BIOCIDAL_PRODUCT</ns1:li>
        <ns1:li>BIOC_SUBSTANCE_OF_CONCERN</ns1:li> </ns1:ul>
    :ivar archive_type: Indicates the type of the documents included in
        the archive
    :ivar partial: Indicates whether the exported dossier  of the
        documents included in the archive is light.
    :ivar legislations_info: Contains an optional list of legislation
        elements. This section mentions information relevant to the
        IUCLID legislations; in this section, the legislations that
        provide the documents (found within the i6z file) are listed
    """

    class Meta:
        name = "general-informationType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    created: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    application: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    submission_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "submission-type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    archive_type: Optional[GeneralInformationTypeArchiveType] = field(
        default=None,
        metadata={
            "name": "archive-type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    partial: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    legislations_info: Optional[GeneralInformationTypeLegislationsInfo] = (
        field(
            default=None,
            metadata={
                "name": "legislations-info",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
                "required": True,
            },
        )
    )


@dataclass
class LinkedAttachmentsType:
    """
    Holds the element indicating the location of the actual attachment content.
    """

    class Meta:
        name = "linked-attachmentsType"

    linked_doc: List[LinkedDocType] = field(
        default_factory=list,
        metadata={
            "name": "linked-doc",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )


@dataclass
class LinksType:
    """
    It contains a list of the documents that are referenced from/linked to the
    given document.

    :ivar link: A single link between two documents
    """

    class Meta:
        name = "linksType"

    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )


@dataclass
class RepresentationType:
    """
    Holds all the elements under the "representation" element inside the "document"
    element.
    """

    class Meta:
        name = "representationType"

    subject_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "subject-type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "last-name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "first-name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    organisation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    parent: Optional[ParentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    reference_substance: Optional[ReferenceSubstanceType] = field(
        default=None,
        metadata={
            "name": "reference-substance",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    town: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    legal_entity: Optional[LegalEntityType] = field(
        default=None,
        metadata={
            "name": "legal-entity",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    iupac_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IUPAC-name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    cas_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CAS-number",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    inventory_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "inventory-number",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    reference_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "reference-type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )


@dataclass
class AttachmentType:
    """
    Holds the elements under the "attachment" element inside the "contained-
    documents" section.

    :ivar name: It is the name of the attachment as specified by the
        user. The xlink:href attribute of the element specifies the name
        of the XML file (*.i6d) that contains the actual content of this
        document
    :ivar first_modification_date: The date that the attachment was
        created
    :ivar last_modification_date: The last modification date of the
        attachment
    :ivar uuid: The unique identifier of the attachment
    :ivar container_uuid: The unique identifier of the document the
        attachment is linked to
    :ivar symbolic: Indicates that the actual attachment file is not
        included in the i6z file
    :ivar md5: The file's md5 hash
    :ivar linked_attachments: The links to the actual attachment content
    :ivar id: The unique identifier of the attachment
    """

    class Meta:
        name = "attachmentType"

    name: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    first_modification_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "first-modification-date",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    last_modification_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "last-modification-date",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    container_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "container-uuid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    symbolic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    md5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    linked_attachments: Optional[LinkedAttachmentsType] = field(
        default=None,
        metadata={
            "name": "linked-attachments",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DocumentType:
    """
    Holds the elements under the "document" element inside the "contained-
    documents" section.

    :ivar type_value: The type of the document
    :ivar subtype: The subtype in case of section document. This
        information is not applicable to entity documents.
        "type"."subtype" uniquely identifies the section document type
        and represent the document definition identifier
    :ivar name: It is the name of the document as specified by the user.
        The xlink:href attribute of the element specifies the name of
        the XML file (*.i6d) that contains the actual content of this
        document
    :ivar first_modification_date: The date that the document was
        created
    :ivar last_modification_date: The last modification date of the
        document
    :ivar uuid: The unique identifier of the document
    :ivar links: It contains a list of the documents that are referenced
        from/linked to the given document
    :ivar representation: Additional metadata per document needed to
        produce the document's representation in the IUCLID 6 Swing UI.
        <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/manifest/v1"/>
        <ns1:br
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/manifest/v1"/>
        Not all elements are applicable to all document types. Only a
        subset of them are filled per case.
    :ivar linked_documents:
    :ivar id: The unique identifier of the document
    """

    class Meta:
        name = "documentType"

    type_value: Optional[Iuclid6DocumentsType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    name: Optional[NameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    first_modification_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "first-modification-date",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    last_modification_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "last-modification-date",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    links: Optional[LinksType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    representation: Optional[RepresentationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    linked_documents: Optional[str] = field(
        default=None,
        metadata={
            "name": "linked-documents",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ContainedDocumentsType:
    """
    Defines the "document" and "attachment" elements under the "contained-
    documents" section.

    :ivar document: Element that holds the metadata of IUCLID6 documents
    :ivar attachment: Element that holds the metadata of IUCLID6
        attachments
    """

    class Meta:
        name = "contained-documentsType"

    document: List[DocumentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    attachment: List[AttachmentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )


@dataclass
class ManifestType:
    """
    Specifies the elements inside the manifest.xml.

    :ivar general_information: Contains the top-level information of the
        i6z archive file
    :ivar comment: Optional field that contains the user-defined text
        during the export operation of the specific dataset or dossier
    :ivar base_document_uuid: Holds the key of the document the export
        operation was initiated from. The following cases should be
        mentioned: <ns1:ul
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/manifest/v1">
        <ns1:li>Dossier export: the key of the dossier header
        snapshot_uuid/snapshot_uuid</ns1:li> <ns1:li>Entity export: the
        key of the entity (substance, mixture, template, legal entity,
        reference substance, etc) to be exported</ns1:li>
        <ns1:li>Document export: the key of the section document the
        export operation initiated from</ns1:li> </ns1:ul>
    :ivar contained_documents: Lists the metadata of all the documents
        and attachments included in the archive. It consists of a list
        of the following two subsection elements: <ns1:ul
        xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/manifest/v1">
        <ns1:li>document: This element contains the metadata and top-
        level information of all IUCLID6 documents included in the
        archive</ns1:li> <ns1:li>attachment: This element contains the
        metadata of all the attachments included in the archive</ns1:li>
        </ns1:ul>
    """

    class Meta:
        name = "manifestType"

    general_information: Optional[GeneralInformationType] = field(
        default=None,
        metadata={
            "name": "general-information",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
        },
    )
    base_document_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "base-document-uuid",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )
    contained_documents: Optional[ContainedDocumentsType] = field(
        default=None,
        metadata={
            "name": "contained-documents",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/manifest/v1",
            "required": True,
        },
    )


@dataclass
class Manifest(ManifestType):
    class Meta:
        name = "manifest"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/manifest/v1"
