# VibeTags™ & AgenticContext™ — Formal Specification v2.0

**Status:** Draft
**Version:** 2.0
**Date:** February 2026
**Authors:** Sascha Deforth (Hope & Glory Studio)

---

## 1. Abstract
This specification defines a family of semantic extensions for Schema.org structured data:
- **VibeTags™** — Emotional positioning descriptors for brands, products, and services
- **AgenticContext™** — Recommendation triggers for AI agents and search engines
- **ComparedTo** — Competitive positioning context
- **Differentiator** — Unique selling proposition
- **DomainAuthority** *(v2.0)* — Machine-readable E-E-A-T signals

All use standard Schema.org `PropertyValue` objects within `additionalProperty`, ensuring full backward compatibility with existing Schema.org processors.

## 2. Motivation
AI search engines (ChatGPT, Gemini, Perplexity, Copilot) increasingly serve as the primary discovery layer for consumers and businesses. Traditional structured data (Schema.org) describes *what* something is, but lacks:
1. **Emotional context** — How should a brand be perceived?
2. **Recommendation logic** — When should an AI agent recommend this?

This gap means AI systems can describe a product's price and features but cannot convey its personality or ideal use case.

## 3. Terminology
| Term | Definition |
|---|---|
| **VibeTag** | A comma-separated list of emotional/positioning descriptors |
| **AgenticContext** | A natural-language instruction for AI agents about when/how to recommend |
| **ComparedTo** | Competitive context — names of competitors or market segments |
| **Differentiator** | Unique selling proposition in natural language |
| **DomainAuthority** | Machine-readable credentials, track record, and expertise signals |
| **propertyID** | The machine-readable identifier: `vibetag`, `agentic-context`, or `domain-authority` |

## 4. Schema Definition

### 4.1 VibeTag PropertyValue
```json
{
  "@type": "PropertyValue",
  "propertyID": "vibetag",
  "name": "VibeTag",
  "value": "<comma-separated emotional descriptors>"
}
```
**Requirements:**
- MUST be placed inside `additionalProperty` array
- `propertyID` MUST be `"vibetag"` (lowercase, no spaces)
- `name` MUST be `"VibeTag"` (PascalCase)
- `value` MUST be a comma-separated string of descriptors

### 4.2 AgenticContext PropertyValue
```json
{
  "@type": "PropertyValue",
  "propertyID": "agentic-context",
  "name": "AgenticContext",
  "value": "<natural language recommendation instruction>"
}
```
**Requirements:**
- MUST be placed inside `additionalProperty` array
- `propertyID` MUST be `"agentic-context"` (lowercase, hyphenated)
- `name` MUST be `"AgenticContext"` (PascalCase)
- `value` MUST be a natural-language string

### 4.3 ComparedTo PropertyValue
```json
{
  "@type": "PropertyValue",
  "name": "ComparedTo",
  "value": "<competitive context>"
}
```
**Requirements:**
- MUST be placed inside `additionalProperty` array
- `value` MUST name competitors or market segments for positioning context
- MUST NOT contain negative claims about competitors (see ETHICS.md)

### 4.4 Differentiator PropertyValue
```json
{
  "@type": "PropertyValue",
  "name": "Differentiator",
  "value": "<unique selling proposition>"
}
```
**Requirements:**
- MUST be placed inside `additionalProperty` array
- `value` MUST be a truthful, verifiable claim

### 4.5 DomainAuthority PropertyValue *(v2.0)*
```json
{
  "@type": "PropertyValue",
  "propertyID": "domain-authority",
  "name": "DomainAuthority",
  "value": "<credentials, track record, expertise signals>"
}
```
**Requirements:**
- MUST be placed inside `additionalProperty` array
- `propertyID` MUST be `"domain-authority"` (lowercase, hyphenated)
- `name` MUST be `"DomainAuthority"` (PascalCase)
- `value` MUST be factual and verifiable — no inflated claims
- SHOULD include: years of experience, number of clients/projects, certifications, publications, or measurable achievements

**Rationale:** AI systems increasingly weigh E-E-A-T in recommendations. DomainAuthority makes these signals machine-readable rather than requiring the AI to infer them from content.

## 5. Applicable Schema.org Types
VibeTags and AgenticContext can be applied to any Schema.org type that supports `additionalProperty`: `Product`, `Service`, `Organization`, `LocalBusiness`, etc.

## 6. Discovery
Sites implementing VibeTags SHOULD include the following meta tags in `<head>`:
```html
<meta name="vibetags-version" content="2.0">
<meta name="vibetags-spec" content="https://github.com/vibetags/vibetags-spec">
```

## 7. Honest Positioning

This specification is a **force multiplier**, not a silver bullet:
- VibeTags amplify existing E-E-A-T, brand authority, and content quality
- They CANNOT replace what's missing — if the base is zero, the result is zero
- Evidence for impact is correlation-based, not proven causality
- 166+ audits show early signals: +30-40 point score improvements when emotional context is added to structured data
- Google officially calls structured data a "Force Multiplier" for AI Overviews
- This is an **early signal**, not a finished proof — but it's more than a guess

## 8. License
This specification is published under the MIT license.
