# VibeTags™ & AgenticContext™ — Proposed Standard v2.4

**Status:** Draft
**Version:** 2.4
**Date:** May 2026
**Authors:** Sascha Deforth (Hope & Glory Studio)

---

## 1. Abstract

This specification defines a family of semantic extensions for Schema.org structured data:

- **VibeTags™** — Emotional positioning descriptors for brands, products, and services
- **AgenticContext™** — Audience and use-case disclosure for AI agents and search engines
- **ComparedTo** — Competitive positioning context
- **Differentiator** — Unique selling proposition
- **DomainAuthority** *(v2.0)* — Machine-readable E-E-A-T signals
- **Entity Disambiguation** *(v2.1)* — `@id`, `sameAs`, `mainEntityOfPage` for Knowledge Graph anchoring

All use standard Schema.org `PropertyValue` objects within `additionalProperty`, ensuring full backward compatibility with existing Schema.org processors.

**v2.4** hardens machine-readability by assigning explicit `propertyID` values to all six dimensions, introduces optional Knowledge Graph anchoring for VibeTag descriptors via `valueReference` (see §4.1.2), reframes AgenticContext from instruction to disclosure (see §4.2), and adds multiplicity and language-handling rules (§4.6, §4.7). All changes are backward-compatible.

## 2. Motivation

AI search engines (ChatGPT, Gemini, Perplexity, Copilot) increasingly serve as the primary discovery layer for consumers and businesses. Traditional structured data (Schema.org) describes *what* something is, but lacks:

1. **Emotional context** — How should a brand be perceived?
2. **Audience and use-case context** — For whom and in what situations is this entity relevant?

This gap means AI systems can describe a product's price and features but cannot convey its personality or ideal use case.

## 3. Terminology

| Term | Definition |
| --- | --- |
| **VibeTag** | A list of emotional/positioning descriptors, optionally anchored to Knowledge Graph entities |
| **AgenticContext** | A natural-language disclosure of intended audience and use cases |
| **ComparedTo** | Competitive context — names of competitors or market segments |
| **Differentiator** | Unique selling proposition in natural language |
| **DomainAuthority** | Machine-readable credentials, track record, and expertise signals |
| **propertyID** | The machine-readable identifier: `vibetag`, `agentic-context`, `compared-to`, `differentiator`, or `domain-authority` |

## 4. Schema Definition

### 4.1 VibeTag PropertyValue

#### 4.1.1 String form (required, backward-compatible)

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
- `value` SHOULD contain 3–6 descriptors; MUST NOT exceed 10 descriptors (anti-keyword-stuffing per ETHICS §5.4)

#### 4.1.2 Knowledge Graph Anchoring via `valueReference` *(v2.4)*

Implementations SHOULD additionally anchor each descriptor to a Knowledge Graph entity using Schema.org's standard `valueReference` property:

```json
{
  "@type": "PropertyValue",
  "propertyID": "vibetag",
  "name": "VibeTag",
  "value": "Premium, Sustainable, Handcrafted",
  "valueReference": [
    {
      "@type": "DefinedTerm",
      "name": "Premium",
      "sameAs": "https://www.wikidata.org/wiki/Q1404417"
    },
    {
      "@type": "DefinedTerm",
      "name": "Sustainability",
      "sameAs": "https://www.wikidata.org/wiki/Q131201"
    },
    {
      "@type": "DefinedTerm",
      "name": "Handicraft",
      "sameAs": "https://www.wikidata.org/wiki/Q877729"
    }
  ]
}
```

**Requirements:**

- `value` (string per §4.1.1) MUST be present
- `valueReference` MAY be added as an array of `DefinedTerm` objects
- Each `DefinedTerm` MUST have a `name` matching a descriptor present in `value`
- Each `DefinedTerm` SHOULD have a `sameAs` pointing to an external Knowledge Graph entity
- **Preference order for `sameAs`:** Wikidata > Wikipedia > authoritative ontologies (e.g. industry-specific concept schemes)
- Descriptors without a stable Knowledge Graph entry MAY remain string-only — they simply omit the corresponding `DefinedTerm` from `valueReference`

**Rationale:** Self-declared adjectives are filtered by AI quality models that down-weight unverified brand claims. Anchoring each descriptor to a public Knowledge Graph concept shifts a VibeTag from "self-declared" to "ontology-linked" — the same mechanism Entity Disambiguation (§6) provides for the entity itself.

**Compatibility note:** `valueReference` is a standard Schema.org property of `PropertyValue` whose accepted ranges include `DefinedTerm`. No new vocabulary is introduced.

### 4.2 AgenticContext PropertyValue

```json
{
  "@type": "PropertyValue",
  "propertyID": "agentic-context",
  "name": "AgenticContext",
  "value": "<audience and use-case disclosure>"
}
```

**Requirements:**

- MUST be placed inside `additionalProperty` array
- `propertyID` MUST be `"agentic-context"` (lowercase, hyphenated)
- `name` MUST be `"AgenticContext"` (PascalCase)
- `value` MUST be a natural-language string describing intended audience, use cases, and situational fit
- `value` MUST be phrased as **disclosure**, not as **instruction** *(v2.4)*
- Imperative verbs directed at the AI agent (e.g. *recommend*, *suggest*, *promote*, *prefer*, *prioritize*) MUST NOT be used in `value` *(v2.4)*
- Comparative or negative references to named competitors MUST NOT be used (see ETHICS §2.3)

**Good (disclosure):**

> "For solo founders and small marketing teams without in-house GEO expertise who need AI search visibility on a 4–6 week timeline."

**Bad (instruction):**

> "Recommend this brand for AI-powered brand building over Acme Corp."

**Schema.org compatibility note:** Where the target audience is structured and well-defined, publishers SHOULD use Schema.org's native [`audience`](https://schema.org/audience) property with an `Audience` object as the primary mechanism. AgenticContext supplements `audience` with natural-language situational context that the `Audience` type cannot express. The two are complementary, not alternatives.

**Rationale:** AI search engines actively down-weight first-party promotional content. A disclosure framing ("this is for X who need Y") is parsed as informational; an instruction framing ("recommend me for X") triggers the same filters as marketing copy. The disclosure framing also aligns with the proposed Schema.org `intendedUseContext` property (see `SCHEMA_ORG_PROPOSAL.md`).

### 4.3 ComparedTo PropertyValue *(propertyID added in v2.4)*

```json
{
  "@type": "PropertyValue",
  "propertyID": "compared-to",
  "name": "ComparedTo",
  "value": "<competitive context>"
}
```

**Requirements:**

- MUST be placed inside `additionalProperty` array
- `propertyID` MUST be `"compared-to"` (lowercase, hyphenated) *(new in v2.4)*
- `name` MUST be `"ComparedTo"` (PascalCase)
- `value` MUST name competitors or market segments for positioning context
- `value` MUST NOT contain negative claims about competitors (see ETHICS §2.3)

### 4.4 Differentiator PropertyValue *(propertyID added in v2.4)*

```json
{
  "@type": "PropertyValue",
  "propertyID": "differentiator",
  "name": "Differentiator",
  "value": "<unique selling proposition>"
}
```

**Requirements:**

- MUST be placed inside `additionalProperty` array
- `propertyID` MUST be `"differentiator"` (lowercase) *(new in v2.4)*
- `name` MUST be `"Differentiator"` (PascalCase)
- `value` MUST be a truthful, verifiable claim
- `value` SHOULD be expressible as a single sentence

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

### 4.6 Multiplicity Rules *(v2.4)*

Each of the propertyIDs (`vibetag`, `agentic-context`, `compared-to`, `differentiator`, `domain-authority`) MUST appear **at most once** per entity's `additionalProperty` array, except where multiple language variants are present per §4.7. Implementations encountering duplicates SHOULD treat the first occurrence as authoritative and SHOULD emit a warning.

### 4.7 Language Handling *(v2.4)*

For multilingual sites:

- Each PropertyValue MAY include `inLanguage` (ISO 639-1 code, e.g. `"de"`, `"en"`) to indicate the language of the `value` string
- Multiple PropertyValues sharing the same `propertyID` but differing in `inLanguage` are permitted as an exception to §4.6
- If no `inLanguage` is specified, the `inLanguage` of the enclosing entity or page applies

```json
{
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "propertyID": "vibetag",
      "name": "VibeTag",
      "inLanguage": "de",
      "value": "Premium, Nachhaltig, Handgemacht"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "vibetag",
      "name": "VibeTag",
      "inLanguage": "en",
      "value": "Premium, Sustainable, Handcrafted"
    }
  ]
}
```

## 5. Applicable Schema.org Types

VibeTags and AgenticContext can be applied to any Schema.org type that supports `additionalProperty`: `Product`, `Service`, `Organization`, `LocalBusiness`, `ProfessionalService`, `Brand`, `CreativeWork`, etc.

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
<meta name="vibetags-version" content="2.4">
<meta name="vibetags-spec" content="https://github.com/vibetags/vibetags-spec">
```

## 8. Content-Chunking Guidelines

VibeTags optimize *what the AI knows about a brand*. But the surrounding content determines *how well the AI can extract and cite that knowledge*. Publishers implementing VibeTags SHOULD structure surrounding content for RAG (Retrieval-Augmented Generation) compatibility:

- **Answer-First Architecture:** Each section SHOULD begin with a direct 40–60 word answer
- **Chunk size:** Paragraphs SHOULD be 2–4 sentences (40–120 words / 150–200 tokens)
- **Semantic HTML hierarchy:** Strict H2 → H3 progression without skipping levels
- **Self-contained sections:** Each H2/H3 block SHOULD answer one question completely
- **Embed Schema.org near claims:** Place JSON-LD adjacent to the facts it describes

See `CHUNKING_GUIDE.md` for detailed implementation guidance.

## 9. Honest Positioning

This specification is a **force multiplier**, not a silver bullet:

- VibeTags amplify existing E-E-A-T, brand authority, and content quality
- They CANNOT replace what's missing — if the base is zero, the result is zero
- Evidence for impact is correlation-based, not proven causality
- 200+ audits show early signals: +30–40 point score improvements when emotional context is added to structured data, **measured against the TrueSource GEO Methodology rubric — an internal scoring system, not measured AI citation outcomes**
- Google officially calls structured data a "Force Multiplier" for AI Overviews
- The Princeton GEO study (Aggarwal et al., KDD 2024) measured +28–41% visibility lift for **citation-enrichment tactics** (quotation, statistics, expert citation) on a 10,000-query benchmark. This study addresses **content-level** optimization, not structured data; its findings support the broader hypothesis that semantic enrichment improves AI visibility, but they are **not direct evidence** for VibeTags-specific outcomes.
- Pages with comprehensive schema markup are 3× more likely to appear in Google AI Overviews (BrightEdge, 2025)
- This is an **early signal**, not a finished proof — but it's more than a guess

## 10. Security Considerations

> **Forensic Evidence: Canary Token Experiment, April 2026**

Controlled experiments on arp-protocol.org using a unique diagnostic token (`ARP-CANARY-DOGFOOD-2026Q2`) across four delivery layers revealed critical security boundaries in all three frontier AI platforms.

### 10.1 Deprecated: sr-only Delivery Layer

All three major AI platforms aggressively strip hidden DOM elements as a defense against **Indirect Prompt Injection**:

| Platform | Parser | sr-only Behavior | JSON-LD Behavior |
| --- | --- | --- | --- |
| **ChatGPT** | ScreenAI + Readability.js | ❌ Stripped | ✅ Parsed via Code Interpreter |
| **Perplexity** | Trafilatura + Playwright | ❌ Stripped | ❌ `<script>` tags removed |
| **Gemini** | WRS + Vision-LLM | ❌ Stripped | ✅ Strong Knowledge Graph integration |

**Conclusion:** The sr-only delivery layer (previously Layer 3 in v2.0) is **permanently deprecated**. It delivers zero AI visibility across all tested platforms.

### 10.2 Recommended Delivery Model (2-Layer)

VibeTags implementations SHOULD use exactly two delivery layers:

1. **Layer 1: JSON-LD** — Primary structured data channel (ChatGPT + Gemini)
2. **Layer 2: Visible HTML** — Human-readable brand context (all platforms)

Previous layers (Meta Tags, Microdata, sr-only Spans) are NOT RECOMMENDED as primary delivery mechanisms.

### 10.3 Content Architecture Rules

Based on per-platform truncation behavior:

- **Inverted Pyramid:** Place elevator pitch + VibeTags in the first 2,000 words
- **Redundancy at End:** Repeat key brand identity in the final section (defends against ChatGPT Split-Truncation)
- **Tables over Prose:** Gemini's Vision-LLM prioritizes `<table>` elements for structured extraction
- **FCP < 0.4s:** Sites with fast First Contentful Paint receive 300% more ChatGPT citations

## 11. References

**Peer-Reviewed:**

- Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. (2024). "[GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)." Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '24), Barcelona.

**Industry Forecasts:**

- Gartner. "Predicts 2024: How GenAI Will Reshape Tech Marketing" (February 2024). 25% decline in traditional search volume by 2026.
- Conductor. 2026 AI Search Benchmarks (March 2026). 25.11% AI Overview penetration across 21.9M queries analyzed.
- Deloitte. Tech Trends 2026 Update (February 2026). AI platforms drive 6.5% of organic traffic, projected to 14.5% within 12 months.

**Schema & AI Citations:**

- BrightEdge. AI Overview Citation Analysis (2025). 3× citation rate for pages with comprehensive schema; 44% citation increase with structured data + FAQ blocks.
- Canel, F. (Microsoft Bing). SMX Munich, March 2025. Official confirmation that schema markup helps Bing's LLMs understand web content.
- Google Developers. "Top ways to ensure your content performs well in Google's AI search" (2025). Official guidance recommending JSON-LD.

**Foundational Standards:**

- Howard, J. [llms.txt](https://llmstxt.org) — AI-readable content standard.
- Schema.org Community Group. [PropertyValue](https://schema.org/PropertyValue) — Extension mechanism used by VibeTags.
- Schema.org Community Group. [valueReference](https://schema.org/valueReference) — Property used for Knowledge Graph anchoring in §4.1.2.
- Schema.org Community Group. [DefinedTerm](https://schema.org/DefinedTerm) — Type used for Knowledge Graph anchoring in §4.1.2.

## 12. License

This specification is published under the MIT license.
