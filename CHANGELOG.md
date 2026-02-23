# Changelog

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
