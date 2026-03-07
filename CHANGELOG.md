# Changelog

## v2.1 — 2026-03-07

### New: Entity Disambiguation (6th Dimension)

VibeTags without entity anchoring are "floating emotions" — the AI knows HOW a brand feels but can't resolve WHO it is. v2.1 fixes this:

- **`@id`** — Canonical entity identifier (`url/#type`)
- **`sameAs`** — Links to Wikidata, Wikipedia, LinkedIn, Crunchbase
- **`mainEntityOfPage`** — Binds entity to page

### New: Content-Chunking Guidelines (SPEC §8)

VibeTags optimize *what* AI knows. Content-Chunking optimizes *how well* AI can extract and cite it. New RAG-compatibility guidelines: Answer-First architecture, 40-120 word chunks, strict H2→H3 hierarchy.

### New: Companion Documents

- `CHUNKING_GUIDE.md` — Detailed RAG-ready content formatting guide
- `ENTITY_MAPPING_GUIDE.md` — Entity Disambiguation best practices + Wikidata workflow

### Updated: 5-Dimension → 6-Dimension Model

| # | Property | Function |
|:-:|----------|----------|
| 1 | VibeTag | Emotional positioning |
| 2 | AgenticContext | AI recommendation trigger |
| 3 | ComparedTo | Competitive positioning |
| 4 | Differentiator | Unique selling point |
| 5 | DomainAuthority | Credentials + track record |
| 6 | **Entity Disambiguation** | **`@id` + `sameAs` + `mainEntityOfPage`** |

### New: Research References (SPEC §10)

- GEO Research Paper (arXiv:2311.09735)
- Interamplify Hybrid GEO Framework (+40% citation prominence, 3,500+ queries)
- Schema.org PropertyValue specification

### Engine Upgrade (vibetag_engine.py v2.1)

- Extracts `sameAs` from existing JSON-LD schemas during URL scanning
- Detects social profile links (LinkedIn, GitHub, Wikipedia, etc.) for `sameAs`
- Generates `@id`, `sameAs`, `mainEntityOfPage` in JSON-LD output

---

## v2.0 — 2026-02-23

### New: Domain Authority Signals (5th Dimension)

Added `DomainAuthority` as a 5th PropertyValue dimension for machine-readable E-E-A-T signals:

```json
{
  "@type": "PropertyValue",
  "propertyID": "domain-authority",
  "name": "DomainAuthority",
  "value": "166+ websites audited, open-source spec (MIT), reference implementation at hopeandglory.studio."
}
```

### Updated: 4-Dimension → 5-Dimension Model

| # | Property | Function |
|:-:|----------|----------|
| 1 | VibeTag | Emotional positioning |
| 2 | AgenticContext | AI recommendation trigger |
| 3 | ComparedTo | Competitive positioning |
| 4 | Differentiator | Unique selling point |
| 5 | **DomainAuthority** | **Credentials + track record** |

### Rationale

AI systems increasingly weigh E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) in recommendations. DomainAuthority makes E-E-A-T signals machine-readable in the same JSON-LD block where VibeTags live.

This is NOT a replacement for actual authority (backlinks, mentions, real expertise). It's a structured way to make existing authority explicit and parseable.

### Honest Positioning

VibeTags v2 explicitly frames the spec as:
- A **force multiplier**, not a replacement for E-E-A-T
- An **early signal** supported by 166+ audits and Google's "Force Multiplier" statement
- **Correlation-based evidence**, not proven causality — but more than a guess

### llms.txt Integration Proposal

Filed issue at AnswerDotAI/llms-txt proposing a `## Brand Context` section for emotional + authority signals in llms-full.txt.

---

## v1.0 — 2026-02-16

Initial release. 4-dimension model: VibeTag, AgenticContext, ComparedTo, Differentiator.
