# VibeTags™ & AgenticContext™ — Proposed Standard v2.1

**Status:** Draft
**Version:** 2.1
**Date:** March 2026
**Authors:** Sascha Deforth (Hope & Glory Studio)

---

## 1. Abstract
This specification defines a family of semantic extensions for Schema.org structured data:
- **VibeTags™** — Emotional positioning descriptors for brands, products, and services
- **AgenticContext™** — Recommendation triggers for AI agents and search engines
- **ComparedTo** — Competitive positioning context
- **Differentiator** — Unique selling proposition
- **DomainAuthority** *(v2.0)* — Machine-readable E-E-A-T signals
- **Entity Disambiguation** *(v2.1)* — `@id`, `sameAs`, `mainEntityOfPage` for Knowledge Graph anchoring

All use standard Schema.org `PropertyValue` objects within `additionalProperty`, ensuring full backward compatibility with existing Schema.org processors. v2.1 adds mandatory entity anchoring to ensure VibeTags are bound to disambiguated entities.

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

## 6. Entity Disambiguation *(v2.1)*

VibeTags are emotional signals — but without a disambiguated entity anchor, AI systems cannot determine *whose* emotions they describe. Entity Disambiguation resolves this by binding VibeTags to a uniquely identifiable Knowledge Graph entity.

### 6.1 Required: `@id`
Every JSON-LD block containing VibeTags MUST include an `@id` that uniquely identifies the entity:
```json
{
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Example Corp"
}
```
**Convention:** Use `{url}/#{type}` format (e.g., `https://example.com/#organization`).

### 6.2 Recommended: `sameAs`
Entities SHOULD include `sameAs` links to external Knowledge Graph references:
```json
"sameAs": [
  "https://www.wikidata.org/wiki/Q12345",
  "https://www.linkedin.com/company/example",
  "https://en.wikipedia.org/wiki/Example_Corp"
]
```
**Priority order:** Wikidata > Wikipedia > LinkedIn > Crunchbase > Social profiles.

Without `sameAs`, the entity exists only within the website's own context. With `sameAs`, it is linked to the global semantic web, enabling cross-reference disambiguation.

### 6.3 Recommended: `mainEntityOfPage`
The page-entity binding SHOULD be made explicit:
```json
"mainEntityOfPage": {
  "@type": "WebPage",
  "@id": "https://example.com/"
}
```
This tells AI: "This page is *about* this entity" — not merely mentioning it.

### 6.4 Rationale
Generative AI engines are vulnerable to **Entity Ambiguity** (semantic drift). Without structured disambiguation signals, an AI cannot determine with certainty whether "Apple" refers to the fruit or the technology company. When confidence drops, the engine skips the entity entirely and cites safer, established alternatives. `@id` + `sameAs` provide the mathematical certainty needed for reliable citation.

## 7. Discovery
Sites implementing VibeTags SHOULD include the following meta tags in `<head>`:
```html
<meta name="vibetags-version" content="2.1">
<meta name="vibetags-spec" content="https://github.com/vibetags/vibetags-spec">
```

## 8. Content-Chunking Guidelines

VibeTags optimize *what the AI knows about a brand*. But the surrounding content determines *how well the AI can extract and cite that knowledge*. Publishers implementing VibeTags SHOULD structure surrounding content for RAG (Retrieval-Augmented Generation) compatibility:

- **Answer-First Architecture:** Each section SHOULD begin with a direct 40-60 word answer
- **Chunk size:** Paragraphs SHOULD be 2-4 sentences (40-120 words / 150-200 tokens)
- **Semantic HTML hierarchy:** Strict H2 → H3 progression without skipping levels
- **Self-contained sections:** Each H2/H3 block SHOULD answer one question completely
- **Embed Schema.org near claims:** Place JSON-LD adjacent to the facts it describes

See `CHUNKING_GUIDE.md` for detailed implementation guidance.

## 9. Honest Positioning

This specification is a **force multiplier**, not a silver bullet:
- VibeTags amplify existing E-E-A-T, brand authority, and content quality
- They CANNOT replace what's missing — if the base is zero, the result is zero
- Evidence for impact is correlation-based, not proven causality
- 166+ audits show early signals: +30-40 point score improvements when emotional context is added to structured data
- Google officially calls structured data a "Force Multiplier" for AI Overviews
- The Interamplify Hybrid GEO Framework demonstrated +40% citation prominence through Technical Justification, Statistics Addition, and Expert Citations across 3,500+ queries
- This is an **early signal**, not a finished proof — but it's more than a guess

## 10. References

- Aggarwal, P. et al. (2023). "GEO: Generative Engine Optimization." [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) — Original GEO research (Georgia Tech, Princeton, IIT Delhi)
- Interamplify Data & AI Research Lab. "Hybrid GEO Framework." — 3,500+ query analysis, +40% citation prominence
- Schema.org Community Group. [PropertyValue](https://schema.org/PropertyValue) — Extension mechanism used by VibeTags
- Howard, J. "llms.txt." [llmstxt.org](https://llmstxt.org) — LLM-readable site summaries

## 11. License
This specification is published under the MIT license.
