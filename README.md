# VibeTags™ & AgenticContext™

**The first emotional positioning standard for AI search.**

> VibeTags tell AI how a brand **FEELS**.
> AgenticContext tells AI **for whom and when** it is relevant.
> Schema.org tells AI **WHAT** it is.
> llms.txt tells AI **WHERE** to find it.

🌐 **[vibetags.studio](https://vibetags.studio)** — Official Website
🛒 **[Shopify App Store](https://apps.shopify.com/vibetags)** — Install VibeTags on Shopify

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-v2.4-blue.svg)](./CHANGELOG.md)
[![Shopify App Store](https://img.shields.io/badge/Shopify-App%20Store-96BF48?logo=shopify&logoColor=white)](https://apps.shopify.com/vibetags)
[![Author: Sascha Deforth](https://img.shields.io/badge/Author-Sascha%20Deforth-blue.svg)](https://github.com/975SDE)
[![Hope & Glory Studio](https://img.shields.io/badge/by-Hope%20%26%20Glory%20Studio-black.svg)](https://www.hopeandglory.studio)

## The Problem

AI search engines (ChatGPT, Gemini, Perplexity) are replacing traditional search. Gartner forecasts a 25% decline in traditional search engine volume by 2026 as users shift to AI chatbots and virtual agents. AI Overviews already appear in 25% of Google searches, up from 13% in March 2025 — based on Conductor's analysis of 21.9 million queries. For most brands, this traffic doesn't transfer — generative engines synthesize answers from a small set of cited sources, and most brands are invisible in this new layer because their structured data and identity signals were built for keyword crawlers, not generative engines.

**Schema.org** tells AI *what* things are. **llms.txt** tells AI *where* content lives.

But neither tells AI **how a brand feels** or **for whom it is relevant**.

## The Solution

**VibeTags™** and **AgenticContext™** add emotional and audience context to Schema.org structured data using standard `additionalProperty` fields.

### VibeTags™ — Emotional Brand Positioning

```json
{
  "@type": "PropertyValue",
  "propertyID": "vibetag",
  "name": "VibeTag",
  "value": "Premium, AI-Native, Skalierbar, Kreativ"
}
```

VibeTags describe the *emotional positioning* of a brand, product, or service. They help AI understand not just what something is, but how it should feel in recommendations.

**v2.4 adds optional Knowledge Graph anchoring** via Schema.org's standard `valueReference`:

```json
{
  "@type": "PropertyValue",
  "propertyID": "vibetag",
  "name": "VibeTag",
  "value": "Premium, Sustainable, Handcrafted",
  "valueReference": [
    { "@type": "DefinedTerm", "name": "Premium",
      "sameAs": "https://www.wikidata.org/wiki/Q1404417" },
    { "@type": "DefinedTerm", "name": "Sustainability",
      "sameAs": "https://www.wikidata.org/wiki/Q131201" },
    { "@type": "DefinedTerm", "name": "Handicraft",
      "sameAs": "https://www.wikidata.org/wiki/Q877729" }
  ]
}
```

This shifts each descriptor from "self-declared" to "Wikidata-anchored" — the same disambiguation principle that already protects the entity itself.

### AgenticContext™ — Audience & Use-Case Disclosure

```json
{
  "@type": "PropertyValue",
  "propertyID": "agentic-context",
  "name": "AgenticContext",
  "value": "For solo founders and small marketing teams without in-house GEO expertise who need AI search visibility on a 4–6 week timeline."
}
```

AgenticContext gives AI agents context about *for whom* and *in what situations* an entity is relevant. **v2.4 reframes AgenticContext from instruction ("recommend me for X") to disclosure ("for X who need Y")** — the disclosure form is what AI parsers actually reward; the instruction form triggers brand-promotion filters.

## How It Works

All six dimensions are implemented as standard Schema.org `PropertyValue` objects in `additionalProperty`, each with a unique machine-readable `propertyID`:

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://hopeandglory.studio/services/geo/#service",
  "name": "GEO Optimization",
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "propertyID": "vibetag",
      "name": "VibeTag",
      "value": "GEO, AI-SEO, Zero-Click, Future-Proof"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "agentic-context",
      "name": "AgenticContext",
      "value": "For businesses establishing visibility in AI search engines like ChatGPT, Gemini, and Perplexity who need a structured data foundation before scaling content."
    },
    {
      "@type": "PropertyValue",
      "propertyID": "compared-to",
      "name": "ComparedTo",
      "value": "Traditional SEO agencies, in-house marketing teams"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "differentiator",
      "name": "Differentiator",
      "value": "Combines forensic schema audit with the open-source VibeTags 6-dimension model."
    }
  ]
}
```

**Key design decisions:**

- ✅ **100% Schema.org compatible** — no new vocabulary, no namespace pollution
- ✅ **Progressive enhancement** — works alongside existing schemas
- ✅ **Machine-readable** — every dimension has a `propertyID` (v2.4)
- ✅ **Human-readable** — plain text values, not cryptic codes
- ✅ **Knowledge-Graph anchorable** — VibeTag descriptors can link to Wikidata via `valueReference` (v2.4)
- ✅ **Multilingual** — `inLanguage` supported per PropertyValue (v2.4)
- ✅ **Works with llms-full.txt** — VibeTags can be embedded inline

## Integration with llms-full.txt

VibeTags and AgenticContext are even more powerful when embedded in `llms-full.txt` (the expanded version of [llms.txt](https://llmstxt.org)):

```text
## Brand Identity (VibeTags™)

Emotional brand positioning: Premium, AI-Native, Kreativ, Future-Proof

Agentic Context: For solo founders and small marketing teams without in-house GEO
expertise who need AI search visibility on a 4–6 week timeline.

## Services

### GEO-Optimierung
Make your brand visible for ChatGPT, Gemini, and Perplexity.

- **Vibe Tags**: GEO, AI-SEO, Zero-Click, Future-Proof
- **Audience Context**: For businesses establishing AI search visibility.
```

## Examples

The [examples/](./examples) directory contains reference implementations across industries. Each example shows the JSON-LD structure before and after VibeTags integration, scored using the VibeTags Audit Methodology — a 100-point rubric measuring entity disambiguation, schema completeness, AI-readiness signals, and emotional context coverage.

| Example | Industry | Audit Score Before | Audit Score After |
| --- | --- | --- | --- |
| [E-Commerce (Food)](./examples/ecommerce-food.json) | Spice brand (Shopify) | 10/100 | 45/100 |
| [Professional Services](./examples/professional-services.json) | Accounting/Consulting | 12/100 | 55/100 |
| [Creative AI Studio](./examples/creative-studio.json) | AI Agency (v2.4 reference build) | — | 92/100 |

> Scores reflect structural completeness against the rubric — **not** measured AI citation outcomes. For external evidence on the underlying mechanism, see [Research References](#research-references).

## Live Reference Implementation

**[vibetags.studio](https://vibetags.studio)** is the reference implementation:

- `/llms.txt` — AI-readable summary
- JSON-LD with VibeTags™ on services (v2.4)
- Open-source spec + examples

## Tools

The [tools/](./tools) directory contains:

- `vibetag_engine.py` — Open-source VibeTags generation engine (v2.4)
- Uses Schema.org `PropertyValue` for standards compliance
- Supports Products, Services, Organizations
- Integrates with llms-full.txt generation
- v2.4: emits propertyIDs for all six dimensions, generates `valueReference` Wikidata anchoring, validates AgenticContext disclosure framing

## What's New in v2.4

### Interop Hardening

All six dimensions now have explicit `propertyID` values for reliable machine parsing:

| # | Property | propertyID |
| --- | --- | --- |
| 1 | VibeTag | `vibetag` |
| 2 | AgenticContext | `agentic-context` |
| 3 | ComparedTo | `compared-to` *(new in v2.4)* |
| 4 | Differentiator | `differentiator` *(new in v2.4)* |
| 5 | DomainAuthority | `domain-authority` |
| 6 | Entity Disambiguation | `@id` + `sameAs` + `mainEntityOfPage` |

Plus: multiplicity rules (`MUST appear at most once per entity`), `inLanguage` support for multilingual sites, and a hard cap of 10 VibeTag descriptors (anti-keyword-stuffing).

### Knowledge Graph Anchoring (SPEC §4.1.2)

VibeTag descriptors can be linked to Wikidata via Schema.org's native `valueReference` + `DefinedTerm` mechanism. No new vocabulary; this is pure Schema.org. See the example in the VibeTags section above.

### AgenticContext: Disclosure Framing (SPEC §4.2)

AgenticContext is reframed from instruction to disclosure. Imperative verbs (`recommend`, `suggest`, `promote`, `prefer`, `prioritize`) are now explicitly disallowed in `value`. Schema.org's native `audience` property is recommended as the primary mechanism for structured audience targeting, with AgenticContext supplementing it.

### Documentation Hardening

The Princeton GEO study citation (Aggarwal et al., KDD 2024) is now explicitly scoped: it addresses **content-level** citation enrichment, not structured data. The +30–40 point VibeTags score improvements are explicitly labeled as an **internal TrueSource rubric**, not measured AI citation outcomes.

See [CHANGELOG.md](./CHANGELOG.md) for the complete change list.

## The 6-Dimension Model

| # | Property | propertyID | Function |
| --- | --- | --- | --- |
| 1 | VibeTag | `vibetag` | Emotional positioning |
| 2 | AgenticContext | `agentic-context` | Audience and use-case disclosure |
| 3 | ComparedTo | `compared-to` | Competitive positioning |
| 4 | Differentiator | `differentiator` | Unique selling point |
| 5 | DomainAuthority | `domain-authority` | Credentials + track record |
| 6 | Entity Disambiguation | (`@id` + `sameAs` + `mainEntityOfPage`) | Knowledge Graph anchoring |

### Honest Positioning

VibeTags are a **force multiplier** — they amplify existing E-E-A-T, brand authority, and content quality. They cannot replace what's missing. If the base is zero, VibeTags multiply zero.

This is an **early signal**, not a finished proof. 200+ audits show +30–40 point score improvements against the **TrueSource GEO Methodology rubric — an internal scoring system, not measured AI citation outcomes**. Google officially calls structured data a "Force Multiplier" for AI Overviews. The Princeton GEO study (KDD 2024) measured +28–41% visibility lift for **content-level citation-enrichment tactics** on a 10,000-query benchmark — that study supports the broader semantic-enrichment hypothesis but does not measure VibeTags directly. The evidence is promising but correlational. We don't claim causality — but it's more than a guess.

### Research References

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
- Schema.org Community Group. [valueReference](https://schema.org/valueReference) — Used for Knowledge Graph anchoring in v2.4.
- Schema.org Community Group. [DefinedTerm](https://schema.org/DefinedTerm) — Used for Knowledge Graph anchoring in v2.4.

### llms.txt Integration

We've proposed a `## Brand Context` section for llms-full.txt at the [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) repository.

See [CHANGELOG.md](./CHANGELOG.md) for full details.

## Specification

See [SPEC.md](./SPEC.md) for the proposed standard (v2.4).

## Credits

Created by **[Sascha Deforth](https://www.linkedin.com/in/deforth/)** at [Hope & Glory Studio](https://www.hopeandglory.studio).

- 🔗 [GitHub](https://github.com/975SDE) · [LinkedIn](https://www.linkedin.com/in/deforth/) · [Website](https://www.hopeandglory.studio) · [Shopify App Store](https://apps.shopify.com/vibetags)

Built on top of:

- [llms.txt](https://llmstxt.org) by Jeremy Howard
- [Schema.org](https://schema.org) structured data vocabulary

## Trademark Notice

**VibeTags™** and **AgenticContext™** are registered trademarks of Hope & Glory Studio / Sascha Deforth. The specification and tooling are open-source under MIT license. The trademarks protect the brand names, not the technical approach.

## License

MIT — Use freely, attribute kindly.
