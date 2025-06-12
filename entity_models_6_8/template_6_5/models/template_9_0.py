from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from template_6_5.models.common_types_domain_v9 import (
    N64,
    N78,
)
from template_6_5.models.platform_fields import (
    BaseDataProtectionField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0"


@dataclass
class TemplateOwnerLegalEntityProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0",
        },
    )


@dataclass
class TemplateOwnerLegalEntityProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0",
        },
    )
    legislation: List[TemplateOwnerLegalEntityProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0",
        },
    )


@dataclass
class Template:
    class Meta:
        name = "TEMPLATE"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/TEMPLATE/9.0"

    template_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TemplateName",
            "type": "Element",
            "required": True,
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
        },
    )
    owner_legal_entity_protection: Optional[
        TemplateOwnerLegalEntityProtection
    ] = field(
        default=None,
        metadata={
            "name": "OwnerLegalEntityProtection",
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
