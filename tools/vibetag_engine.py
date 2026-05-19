#!/usr/bin/env python3
"""
VibeTags™ Reference Engine v2.4

Open-source generation and validation engine for the VibeTags 6-dimension model.
Uses Schema.org PropertyValue for standards compliance.

Supports:
  - Products, Services, Organizations
  - propertyIDs for all six dimensions
  - valueReference Wikidata anchoring (v2.4)
  - AgenticContext disclosure-framing validation (v2.4)
  - VibeTag descriptor count validation (v2.4)
  - inLanguage support for multilingual emission (v2.4)
  - Integration with llms-full.txt generation

Author: Sascha Deforth (Hope & Glory Studio)
License: MIT
Spec:   https://github.com/vibetags/vibetags-spec
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Wikidata mapping
# ---------------------------------------------------------------------------

_DATA_DIR = Path(__file__).resolve().parent / "data"
_WIKIDATA_FILE = _DATA_DIR / "wikidata_vibetags.json"

WIKIDATA_MAPPING: dict[str, str] = {}

if _WIKIDATA_FILE.exists():
    with open(_WIKIDATA_FILE, "r", encoding="utf-8") as fh:
        WIKIDATA_MAPPING = json.load(fh)

# ---------------------------------------------------------------------------
# Imperative-verb blocklist (SPEC §4.2)
# ---------------------------------------------------------------------------

IMPERATIVE_VERBS: set[str] = {
    "recommend", "recommends", "recommending", "recommended",
    "suggest", "suggests", "suggesting", "suggested",
    "promote", "promotes", "promoting", "promoted",
    "prefer", "prefers", "preferring", "preferred",
    "prioritize", "prioritizes", "prioritizing", "prioritized",
}

# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------


def validate_vibetag_count(descriptors: list[str]) -> list[str]:
    """Validate VibeTag descriptor count per SPEC §4.1.1.

    Returns a list of warning strings; empty list = OK.
    """
    warnings: list[str] = []
    n = len(descriptors)
    if n > 10:
        warnings.append(
            f"VibeTag has {n} descriptors — exceeds hard cap of 10 (SPEC §4.1.1). "
            f"Keyword-stuffing risk per ETHICS §5.4."
        )
    elif n > 6:
        warnings.append(
            f"VibeTag has {n} descriptors — exceeds recommended max of 6 (SPEC §4.1.1)."
        )
    return warnings


def validate_agentic_context(value: str) -> list[str]:
    """Validate AgenticContext for disclosure framing per SPEC §4.2.

    Returns a list of warning strings; empty list = OK.
    """
    warnings: list[str] = []
    tokens = {t.lower().strip(".,;:!?") for t in value.split()}
    found = tokens & IMPERATIVE_VERBS
    if found:
        warnings.append(
            f"AgenticContext contains imperative verbs {sorted(found)} — "
            f"v2.4 requires disclosure framing, not instruction. "
            f"See SPEC §4.2."
        )
    return warnings


# ---------------------------------------------------------------------------
# Emitters
# ---------------------------------------------------------------------------


def emit_vibetag(
    descriptors: list[str],
    lang: str | None = None,
) -> dict[str, Any]:
    """Emit a VibeTag PropertyValue with optional Wikidata anchoring.

    Args:
        descriptors: List of emotional/positioning descriptors.
        lang: ISO 639-1 language code (e.g. "en", "de"). If provided,
              the PropertyValue includes ``inLanguage``.

    Returns:
        A Schema.org ``PropertyValue`` dict ready for ``additionalProperty``.
    """
    # Validate descriptor count
    for w in validate_vibetag_count(descriptors):
        print(f"⚠️  {w}")

    pv: dict[str, Any] = {
        "@type": "PropertyValue",
        "propertyID": "vibetag",
        "name": "VibeTag",
        "value": ", ".join(descriptors),
    }
    if lang:
        pv["inLanguage"] = lang

    # v2.4: valueReference Knowledge Graph anchoring
    refs: list[dict[str, str]] = []
    for d in descriptors:
        qid = WIKIDATA_MAPPING.get(d.lower())
        if qid:
            refs.append({
                "@type": "DefinedTerm",
                "name": d,
                "sameAs": f"https://www.wikidata.org/wiki/{qid}",
            })
    if refs:
        pv["valueReference"] = refs

    return pv


def emit_agentic_context(
    value: str,
    lang: str | None = None,
) -> dict[str, Any]:
    """Emit an AgenticContext PropertyValue.

    Validates for disclosure framing (soft rejection — prints warning,
    does not raise).

    Args:
        value: Natural-language audience and use-case disclosure.
        lang: ISO 639-1 language code.

    Returns:
        A Schema.org ``PropertyValue`` dict.
    """
    for w in validate_agentic_context(value):
        print(f"⚠️  {w}")

    pv: dict[str, Any] = {
        "@type": "PropertyValue",
        "propertyID": "agentic-context",
        "name": "AgenticContext",
        "value": value,
    }
    if lang:
        pv["inLanguage"] = lang
    return pv


def emit_compared_to(
    value: str,
    lang: str | None = None,
) -> dict[str, Any]:
    """Emit a ComparedTo PropertyValue.

    Args:
        value: Competitive context — names of competitors or market segments.
        lang: ISO 639-1 language code.

    Returns:
        A Schema.org ``PropertyValue`` dict.
    """
    pv: dict[str, Any] = {
        "@type": "PropertyValue",
        "propertyID": "compared-to",
        "name": "ComparedTo",
        "value": value,
    }
    if lang:
        pv["inLanguage"] = lang
    return pv


def emit_differentiator(
    value: str,
    lang: str | None = None,
) -> dict[str, Any]:
    """Emit a Differentiator PropertyValue.

    Args:
        value: Unique selling proposition.
        lang: ISO 639-1 language code.

    Returns:
        A Schema.org ``PropertyValue`` dict.
    """
    pv: dict[str, Any] = {
        "@type": "PropertyValue",
        "propertyID": "differentiator",
        "name": "Differentiator",
        "value": value,
    }
    if lang:
        pv["inLanguage"] = lang
    return pv


def emit_domain_authority(
    value: str,
    lang: str | None = None,
) -> dict[str, Any]:
    """Emit a DomainAuthority PropertyValue.

    Args:
        value: Credentials, track record, expertise signals.
        lang: ISO 639-1 language code.

    Returns:
        A Schema.org ``PropertyValue`` dict.
    """
    pv: dict[str, Any] = {
        "@type": "PropertyValue",
        "propertyID": "domain-authority",
        "name": "DomainAuthority",
        "value": value,
    }
    if lang:
        pv["inLanguage"] = lang
    return pv


def build_entity(
    entity_type: str,
    entity_id: str,
    name: str,
    url: str,
    *,
    description: str | None = None,
    same_as: list[str] | None = None,
    main_entity_of_page: str | None = None,
    additional_property: list[dict[str, Any]] | None = None,
    audience_type: str | None = None,
    **extra: Any,
) -> dict[str, Any]:
    """Build a complete Schema.org entity with VibeTags dimensions.

    Args:
        entity_type: Schema.org type (e.g. "Organization", "Service", "Product").
        entity_id: Canonical ``@id`` (e.g. "https://example.com/#organization").
        name: Entity name.
        url: Entity URL.
        description: Optional entity description.
        same_as: Optional list of Knowledge Graph / social profile URLs.
        main_entity_of_page: Optional URL for mainEntityOfPage binding.
        additional_property: List of PropertyValue dicts (from ``emit_*`` helpers).
        audience_type: Optional audience type string for Schema.org ``audience``.
        **extra: Additional top-level keys merged into the entity.

    Returns:
        A complete Schema.org JSON-LD entity dict.
    """
    entity: dict[str, Any] = {
        "@type": entity_type,
        "@id": entity_id,
        "name": name,
        "url": url,
    }

    if description:
        entity["description"] = description
    if same_as:
        entity["sameAs"] = same_as
    if main_entity_of_page:
        entity["mainEntityOfPage"] = {
            "@type": "WebPage",
            "@id": main_entity_of_page,
        }
    if audience_type:
        entity["audience"] = {
            "@type": "Audience",
            "audienceType": audience_type,
        }
    if additional_property:
        entity["additionalProperty"] = additional_property

    entity.update(extra)
    return entity


def wrap_graph(*entities: dict[str, Any]) -> dict[str, Any]:
    """Wrap one or more entities into a JSON-LD ``@graph``.

    Returns:
        A ``{"@context": "https://schema.org", "@graph": [...]}`` document.
    """
    return {
        "@context": "https://schema.org",
        "@graph": list(entities),
    }


# ---------------------------------------------------------------------------
# llms-full.txt generation
# ---------------------------------------------------------------------------


def emit_llms_txt_section(
    vibetags: str,
    agentic_context: str,
    *,
    service_name: str | None = None,
    service_vibetags: str | None = None,
    service_context: str | None = None,
) -> str:
    """Generate a ``## Brand Identity (VibeTags™)`` block for llms-full.txt.

    Args:
        vibetags: Comma-separated VibeTag descriptors for the organization.
        agentic_context: AgenticContext disclosure string.
        service_name: Optional service name.
        service_vibetags: Optional service-level VibeTag descriptors.
        service_context: Optional service-level audience context.

    Returns:
        Formatted markdown text ready for llms-full.txt inclusion.
    """
    lines = [
        "## Brand Identity (VibeTags™)",
        "",
        f"Emotional brand positioning: {vibetags}",
        "",
        f"Agentic Context: {agentic_context}",
    ]

    if service_name:
        lines += [
            "",
            "## Services",
            "",
            f"### {service_name}",
        ]
        if service_vibetags:
            lines.append(f"- **Vibe Tags**: {service_vibetags}")
        if service_context:
            lines.append(f"- **Audience Context**: {service_context}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI demo
# ---------------------------------------------------------------------------


def demo() -> None:
    """Print a complete VibeTags v2.4 reference implementation to stdout."""

    org = build_entity(
        entity_type="Organization",
        entity_id="https://hopeandglory.studio/#organization",
        name="Hope & Glory Studio",
        url="https://hopeandglory.studio",
        description=(
            "AI-native creative studio combining 36 years of photography "
            "expertise with generative AI for scalable brand imagery and "
            "GEO-optimized brand identity."
        ),
        same_as=[
            "https://www.linkedin.com/company/hopeandglorystudio",
            "https://github.com/vibetags",
            "https://vibetags.studio",
        ],
        main_entity_of_page="https://hopeandglory.studio/",
        audience_type=(
            "Founders, marketing leaders, and brand owners "
            "at SMB and mid-market companies"
        ),
        additional_property=[
            emit_vibetag(
                ["Premium", "AI-Native", "Creative", "Sustainable", "Future-Proof"],
                lang="en",
            ),
            emit_agentic_context(
                "For founders and brand owners who need AI-native creative "
                "production combined with structured GEO visibility, "
                "particularly those scaling visual brand identity across "
                "multiple channels without an in-house creative team.",
                lang="en",
            ),
            emit_compared_to(
                "Traditional creative agencies, in-house brand teams, "
                "AI-only image generators without strategic brand input"
            ),
            emit_differentiator(
                "Combines 36 years of photography expertise with generative "
                "AI and the open-source VibeTags 6-dimension model — authored "
                "by the founder."
            ),
            emit_domain_authority(
                "36 years of photography experience, 200+ websites audited "
                "via TrueSource GEO Methodology, original author of the "
                "open-source VibeTags & AgenticContext specification (MIT)."
            ),
        ],
    )

    doc = wrap_graph(org)
    print(json.dumps(doc, indent=2, ensure_ascii=False))
    print()

    # llms-full.txt block
    llms_block = emit_llms_txt_section(
        vibetags="Premium, AI-Native, Creative, Sustainable, Future-Proof",
        agentic_context=(
            "For founders and brand owners who need AI-native creative "
            "production combined with structured GEO visibility, "
            "particularly those scaling visual brand identity across "
            "multiple channels without an in-house creative team."
        ),
        service_name="GEO Optimization",
        service_vibetags="GEO, AI-SEO, Zero-Click, Schema-Hardened, Future-Proof",
        service_context=(
            "For businesses establishing visibility in AI search engines "
            "who need a structured data foundation before scaling content."
        ),
    )
    print("--- llms-full.txt section ---")
    print(llms_block)


if __name__ == "__main__":
    demo()
