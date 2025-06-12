from dataclasses import field
from typing import Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDateTime

from platform_container_6_5.models.xlink import TypeType

__NAMESPACE__ = (
    "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1"
)


@dataclass
class AttachmentRef:
    """
    Specifies the unique identifier of an attachment that is directly linked to a
    IUCLID6 document.
    """

    class Meta:
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AttachmentContent:
    class Meta:
        global_type = False

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
class Attachment:
    """
    Defines the attachment metadata information.

    :ivar document_key: The unique identifier of the attachment
    :ivar name: The name of the uploaded attachment
    :ivar creation_date: The date that the attachment was created
    :ivar last_modification_date: The last modification date of the
        attachment
    :ivar remarks: The remarks provided by the user during the
        attachment uploading
    :ivar md5: The MD5 hash of the uploaded attachment content
    :ivar mimetype: The media type of the attachment content
    :ivar symbolic: Indicates that the actual attachment file is not
        included in the i6z file
    :ivar content: The name/location of the attachment binary under the
        "attachments" directory inside the i6z archive file
    """

    class Meta:
        namespace = (
            "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1"
        )

    document_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "documentKey",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Element",
            "required": True,
        },
    )
    last_modification_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModificationDate",
            "type": "Element",
            "required": True,
        },
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    md5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    symbolic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    content: Optional[AttachmentContent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
