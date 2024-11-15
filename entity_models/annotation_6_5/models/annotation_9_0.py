from dataclasses import field
from typing import List, Optional

from pydantic.dataclasses import dataclass

from annotation_6_5.models.common_types_domain_v9 import (
    A03,
    N16,
    N17,
    N19,
    N64,
    N78,
    Pg661006,
)
from annotation_6_5.models.platform_fields import (
    AttachmentListField,
    BaseDataProtectionField,
    BasePicklistField,
    MultilingualTextField,
    MultilingualTextFieldLarge,
    MultilingualTextFieldSmall,
)

__NAMESPACE__ = "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0"


@dataclass
class AnnotationAnnotatedDocumentsAnnotatedDocument:
    class Meta:
        global_type = False

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
            "required": True,
        },
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
            "required": True,
        },
    )


@dataclass
class AnnotationAdminInfoAnnotationStatus(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N16] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationAdminInfoAnnotationType(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[Pg661006] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationAdminInfoDataProtectionLegislation:
    class Meta:
        global_type = False

    value: Optional[N78] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationAnnotatedDocuments:
    class Meta:
        global_type = False

    annotated_document: List[AnnotationAnnotatedDocumentsAnnotatedDocument] = (
        field(
            default_factory=list,
            metadata={
                "name": "AnnotatedDocument",
                "type": "Element",
                "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
            },
        )
    )


@dataclass
class AnnotationAttachedRegulatoryAuthoritiesEvaluation:
    class Meta:
        global_type = False

    evaluation: Optional[AttachmentListField] = field(
        default=None,
        metadata={
            "name": "Evaluation",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationEvalInfoAgreementWithApplicantsSummary(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[A03] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationEvalInfoDataWaiverAcceptable(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N19] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationEvalInfoReliability(BasePicklistField):
    class Meta:
        global_type = False

    value: Optional[N17] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    other: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationAdminInfoDataProtection(BaseDataProtectionField):
    class Meta:
        global_type = False

    confidentiality: Optional[N64] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    justification: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    legislation: List[AnnotationAdminInfoDataProtectionLegislation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationEvalInfo:
    class Meta:
        global_type = False

    agreement_with_applicants_summary: Optional[
        AnnotationEvalInfoAgreementWithApplicantsSummary
    ] = field(
        default=None,
        metadata={
            "name": "AgreementWithApplicantsSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    data_waiver_acceptable: Optional[
        AnnotationEvalInfoDataWaiverAcceptable
    ] = field(
        default=None,
        metadata={
            "name": "DataWaiverAcceptable",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    reliability: Optional[AnnotationEvalInfoReliability] = field(
        default=None,
        metadata={
            "name": "Reliability",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    remarks: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    cross_reference_to_other_study: List[MultilingualTextFieldSmall] = field(
        default_factory=list,
        metadata={
            "name": "CrossReferenceToOtherStudy",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    conclusions: List[MultilingualTextFieldLarge] = field(
        default_factory=list,
        metadata={
            "name": "Conclusions",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    executive_summary: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "ExecutiveSummary",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class AnnotationAdminInfo:
    class Meta:
        global_type = False

    data_protection: Optional[AnnotationAdminInfoDataProtection] = field(
        default=None,
        metadata={
            "name": "DataProtection",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
            "required": True,
        },
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    annotation_status: Optional[AnnotationAdminInfoAnnotationStatus] = field(
        default=None,
        metadata={
            "name": "AnnotationStatus",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    annotation_type: Optional[AnnotationAdminInfoAnnotationType] = field(
        default=None,
        metadata={
            "name": "AnnotationType",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )
    remarks: List[MultilingualTextField] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0",
        },
    )


@dataclass
class Annotation:
    class Meta:
        name = "ANNOTATION"
        namespace = "http://iuclid6.echa.europa.eu/namespaces/ANNOTATION/9.0"

    annotated_documents: Optional[AnnotationAnnotatedDocuments] = field(
        default=None,
        metadata={
            "name": "AnnotatedDocuments",
            "type": "Element",
            "required": True,
        },
    )
    admin_info: Optional[AnnotationAdminInfo] = field(
        default=None,
        metadata={
            "name": "AdminInfo",
            "type": "Element",
            "required": True,
        },
    )
    attached_regulatory_authorities_evaluation: Optional[
        AnnotationAttachedRegulatoryAuthoritiesEvaluation
    ] = field(
        default=None,
        metadata={
            "name": "AttachedRegulatoryAuthoritiesEvaluation",
            "type": "Element",
        },
    )
    eval_info: Optional[AnnotationEvalInfo] = field(
        default=None,
        metadata={
            "name": "EvalInfo",
            "type": "Element",
        },
    )
