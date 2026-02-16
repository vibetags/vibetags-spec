# VibeTags™ & AgenticContext™ — Formal Specification v1.0

**Status:** Draft
**Version:** 1.0
**Date:** February 2026
**Authors:** Sascha Deforth (Hope & Glory Studio)

---

## 1. Abstract
This specification defines two complementary semantic extensions for Schema.org structured data:
- **VibeTags™** — Emotional positioning descriptors for brands, products, and services
- **AgenticContext™** — Recommendation triggers for AI agents and search engines

Both use standard Schema.org `PropertyValue` objects within `additionalProperty`, ensuring full backward compatibility with existing Schema.org processors.

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
| **propertyID** | The machine-readable identifier: `vibetag` or `agentic-context` |

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

## 5. Applicable Schema.org Types
VibeTags and AgenticContext can be applied to any Schema.org type that supports `additionalProperty`: `Product`, `Service`, `Organization`, `LocalBusiness`, etc.

## 6. Discovery
Sites implementing VibeTags SHOULD include the following meta tags in `<head>`:
```html
<meta name="vibetags-version" content="1.0">
<meta name="vibetags-spec" content="https://github.com/vibetags/vibetags-spec">
```

## 7. License
This specification is published under the MIT license.
