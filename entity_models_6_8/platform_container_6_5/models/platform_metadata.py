from dataclasses import field
from typing import Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"


@dataclass
class CreationDate:
    """
    The date that the document was created.
    """

    class Meta:
        name = "creationDate"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class CreationTool:
    """Element that specifies the application this document was first created with.

    Default value "IUC6" should be provided for IUCLID6-documents
    """

    class Meta:
        name = "creationTool"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DefinitionVersion:
    """The definition version of the exported document.

    This value is used:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1">
    <ns1:li>indicates that the content section follows the document format of the specified version</ns1:li>
    <ns1:li>during import operation, this value drives the resolution of the proper document's .xsd to run the validation with</ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "definitionVersion"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DocumentKey:
    """
    The unique identifier of the document.
    """

    class Meta:
        name = "documentKey"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DocumentSubType:
    """The subtype in case of section document.

    This information is not applicable to entity documents.
    "type"."subtype" uniquely identify the section document type and
    represent the document definition identifier
    """

    class Meta:
        name = "documentSubType"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DocumentType:
    """The type of the document.

    Eligible values are:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1">
    <ns1:li>ANNOTATION</ns1:li>
    <ns1:li>ARTICLE</ns1:li>
    <ns1:li>CATEGORY</ns1:li>
    <ns1:li>DOSSIER</ns1:li>
    <ns1:li>FIXED_RECORD</ns1:li>
    <ns1:li>FLEXIBLE_RECORD</ns1:li>
    <ns1:li>ENDPOINT_STUDY_RECORD</ns1:li>
    <ns1:li>FLEXIBLE_SUMMARY</ns1:li>
    <ns1:li>ENDPOINT_SUMMARY</ns1:li>
    <ns1:li>ASSESSMENT_ENTITY</ns1:li>
    <ns1:li>LEGAL_ENTITY</ns1:li>
    <ns1:li>MIXTURE</ns1:li>
    <ns1:li>REFERENCE_SUBSTANCE</ns1:li>
    <ns1:li>SITE</ns1:li>
    <ns1:li>CONTACT</ns1:li>
    <ns1:li>LITERATURE</ns1:li>
    <ns1:li>SUBSTANCE</ns1:li>
    <ns1:li>TEMPLATE</ns1:li>
    <ns1:li>TEST_MATERIAL_INFORMATION</ns1:li>
    <ns1:li>INVENTORY</ns1:li>
    <ns1:li>CUSTOM_ENTITY</ns1:li>
    <ns1:li>CUSTOM_SECTION</ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "documentType"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DossierSubject:
    """
    In case this is the dossier document, it contains the document key (unique
    identifier) of the dossier subject document (SUBSTANCE, MIXTURE, CATEGORY,
    ARTICLE) which is the document the dossier was created from.
    """

    class Meta:
        name = "dossierSubject"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class I5Origin:
    """
    Flag indicating whether this document originated from a IUCLID5 instance and
    migrated to the current IUCLID6 format or not.
    """

    class Meta:
        name = "i5Origin"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class IuclidVersion:
    """
    The current iuclid version used for exporting the .i6z archive.
    """

    class Meta:
        name = "iuclidVersion"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class LastModificationDate:
    """
    The last modification date of the document.
    """

    class Meta:
        name = "lastModificationDate"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Name:
    """
    It is the name of the document as specified by the user.
    """

    class Meta:
        name = "name"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class OrderInSectionNo:
    """
    In case this is a section document, the order of the document with the specific
    definition identifier (type, subtype) under the provided parent entity.
    """

    class Meta:
        name = "orderInSectionNo"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(default="")


@dataclass
class ParentDocumentKey:
    """
    In case this document is a section document, this element keeps the unique
    identifier of its parent document.
    """

    class Meta:
        name = "parentDocumentKey"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SnapshotCreationTool:
    """In case of dossier archive, element that specifies the application this
    dossier was created from.

    Upon dossier creation this is filled in with "IUC6"
    """

    class Meta:
        name = "snapshotCreationTool"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SubmissionType:
    """Applicable only to dossier archives.

    Indicates the submission type used during dossier generation. The value is specified in case the XML concerns:
    <ns1:ul xmlns:ns1="http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1">
    <ns1:li>the dossier document</ns1:li>
    <ns1:li>the composite documents (SUBSTANCE/MIXTURE) under the dossier with a submission type different than the one of the dossier document</ns1:li>
    </ns1:ul>
    """

    class Meta:
        name = "submissionType"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SubmissionTypeVersion:
    """
    The version of the submission type used to generate the dossier for.
    """

    class Meta:
        name = "submissionTypeVersion"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SubmittingLegalEntity:
    """
    The legal entity document identifier that originated toe dossier creation.
    """

    class Meta:
        name = "submittingLegalEntity"
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
