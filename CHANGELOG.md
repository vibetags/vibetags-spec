# Changelog

## v2.4 — 2026-05-19

### Interop Hardening

- **`propertyID` added to ComparedTo (`"compared-to"`) and Differentiator (`"differentiator"`)** — All six dimensions now have machine-readable propertyIDs for reliable parsing across implementations (SPEC §4.3, §4.4). Previously, ComparedTo and Differentiator were identified only by the `name` field, creating implementation inconsistency.
- **Multiplicity rules (SPEC §4.6)** — Each propertyID MUST appear at most once per entity, except for distinct `inLanguage` variants. Implementations encountering duplicates SHOULD treat the first occurrence as authoritative.
- **Language handling (SPEC §4.7)** — `inLanguage` (ISO 639-1) is now permitted on PropertyValues for multilingual sites. Multiple PropertyValues with the same `propertyID` and different `inLanguage` are an exception to §4.6.
- **VibeTag max-length guidance (SPEC §4.1.1)** — 3–6 descriptors recommended, hard cap at 10 (anti-keyword-stuffing per ETHICS §5.4).

### New: Knowledge Graph Anchoring for VibeTags (SPEC §4.1.2)

VibeTag descriptors can now be anchored to Wikidata (or other Knowledge Graph) entities via Schema.org's standard `valueReference` property:

```json
{
  "@type": "PropertyValue",
  "propertyID": "vibetag",
  "name": "VibeTag",
  "value": "Premium, Sustainable",
  "valueReference": [
    { "@type": "DefinedTerm", "name": "Premium",
      "sameAs": "https://www.wikidata.org/wiki/Q1404417" },
    { "@type": "DefinedTerm", "name": "Sustainability",
      "sameAs": "https://www.wikidata.org/wiki/Q131201" }
  ]
}
```

The string `value` remains required for backward compatibility. `valueReference` is optional but recommended. This extends the Entity Disambiguation principle from the entity itself (§6) to the descriptors that emotionally characterize it, reducing the "self-declared adjective" weakness that AI quality models filter against.

**Standards compliance:** `valueReference` is a native Schema.org property of `PropertyValue` whose accepted ranges include `DefinedTerm`. No new vocabulary is introduced.

### AgenticContext: Disclosure Framing (SPEC §4.2)

AgenticContext is reframed from "recommendation instruction" to "audience and use-case disclosure":

- `value` MUST be phrased as **disclosure** ("for X who need Y"), not as **instruction** ("recommend me for X")
- Imperative verbs directed at the AI agent (*recommend*, *suggest*, *promote*, *prefer*, *prioritize*) MUST NOT be used in `value`
- Schema.org's native `audience` property is now recommended as the primary mechanism for structured audience targeting, with AgenticContext supplementing it via natural-language situational context

**Rationale:** AI search engines actively down-weight first-party promotional content. Disclosure framing aligns with how AI models parse audience signals; instruction framing triggers brand-promotion filters. The disclosure framing also aligns with the proposed Schema.org `intendedUseContext` property (see `SCHEMA_ORG_PROPOSAL.md`).

### Documentation Hardening

- **SPEC numbering reflowed** — §10 (Security Considerations, formerly §11), §11 (References, formerly §12), §12 (License, formerly §13). The missing §10 gap that existed in v2.2/v2.3 has been removed.
- **Princeton GEO study citation scope clarified (SPEC §9)** — Explicit note that Aggarwal et al. (KDD 2024) addresses **content-level** citation enrichment, not structured data. Findings are analogical evidence for the broader semantic-enrichment hypothesis, not direct VibeTags evidence.
- **TrueSource GEO Methodology disclosure (SPEC §9)** — Explicit framing of the +30–40 point improvement as an **internal rubric score**, not a measured AI citation outcome.
- **Version drift resolved** — `README.md`, `SPEC.md`, the `<meta name="vibetags-version">` discovery tag, and `CHANGELOG.md` all now reference v2.4 as the canonical version.

### Engine Upgrade (vibetag_engine.py v2.4)

The reference engine in `tools/` is updated to match the v2.4 spec. Implementers maintaining their own engines should mirror the following:

- Emits `propertyID` for **all six dimensions** (was: three — `vibetag`, `agentic-context`, `domain-authority`)
- Generates `valueReference` Wikidata anchoring when a concept-to-Q-ID mapping is available (new internal mapping table: `data/wikidata_vibetags.json`)
- Validates AgenticContext for disclosure framing — rejects imperative verbs (`recommend`, `suggest`, `promote`, `prefer`, `prioritize`) with a warning
- Validates VibeTag descriptor count — warns at 7+, fails at 11+
- Supports `inLanguage` per §4.7 for multilingual emission

### Backward Compatibility

v2.4 is fully backward-compatible:

- Existing v2.1/v2.2/v2.3 JSON-LD blocks remain valid (the new requirements are additive, not breaking)
- Parsers reading v2.4 output without v2.4 awareness will simply ignore the new `propertyID` values on ComparedTo/Differentiator and the `valueReference` arrays
- Migrating from v2.3 to v2.4 requires adding `propertyID` fields to ComparedTo/Differentiator entries — a non-breaking edit

---

## v2.3 — 2026-04-28

### Credibility Hardening

Replaced unsubstantiated market claims with verifiable, source-backed data across README and SPEC.

- **35% claim removed** — replaced with Gartner (25% decline in traditional search by 2026) and Conductor (25.11% AI Overview penetration across 21.9M queries)
- **Examples table hardened** — added methodology transparency ("VibeTags Audit Methodology" rubric), corrected file links, added disclaimer distinguishing audit scores from AI citation outcomes
- **Research References consolidated** — full academic citations (KDD 2024), industry forecasts (Gartner, Conductor, Deloitte), schema studies (BrightEdge 3× citation rate, Microsoft SMX confirmation)
- **SPEC.md updated** — Honest Positioning now cites Princeton GEO study (+28–41% visibility lift) and BrightEdge (3× schema citation rate); References section expanded with categorized sources
- **Audit count updated** — 166+ → 200+ across all documents
- **Interamplify reference removed** — replaced with peer-reviewed KDD 2024 data as primary external evidence

### Rationale

The previous claims (especially "35% of queries go through AI by 2026") were not defensible under scrutiny. The replacement data uses named external authorities (Gartner, Conductor, BrightEdge, Microsoft) with documented methodologies and sample sizes. Internal audit scores are now clearly separated from peer-reviewed externals throughout.

---

## v2.1 — 2026-03-07

### New: Entity Disambiguation (6th Dimension)

VibeTags without entity anchoring are "floating emotions" — the AI knows HOW a brand feels but can't resolve WHO it is. v2.1 fixes this:

- **`@id`** — Canonical entity identifier (`url/#type`)
- **`sameAs`** — Links to Wikidata, Wikipedia, LinkedIn, Crunchbase
- **`mainEntityOfPage`** — Binds entity to page

### New: Content-Chunking Guidelines (SPEC §8)

VibeTags optimize *what* AI knows. Content-Chunking optimizes *how well* AI can extract and cite it. New RAG-compatibility guidelines: Answer-First architecture, 40–120 word chunks, strict H2→H3 hierarchy.

### New: Companion Documents

- `CHUNKING_GUIDE.md` — Detailed RAG-ready content formatting guide
- `ENTITY_MAPPING_GUIDE.md` — Entity Disambiguation best practices + Wikidata workflow

### Updated: 5-Dimension → 6-Dimension Model

| # | Property | Function |
| --- | --- | --- |
| 1 | VibeTag | Emotional positioning |
| 2 | AgenticContext | AI recommendation trigger |
| 3 | ComparedTo | Competitive positioning |
| 4 | Differentiator | Unique selling point |
| 5 | DomainAuthority | Credentials + track record |
| 6 | **Entity Disambiguation** | **`@id` + `sameAs` + `mainEntityOfPage`** |

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
| --- | --- | --- |
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
