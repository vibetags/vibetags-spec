<!-- 
  GitHub Issue Title: Proposal: intendedUseContext and brandPersonality properties
  Repository: github.com/schemaorg/schemaorg
-->

## Problem

Schema.org describes *what* entities are but lacks properties for two dimensions AI recommendation systems need: **intended use context** (for whom?) and **brand personality** (how does it feel?). Publishers work around this with `additionalProperty` / `PropertyValue`, but without standardization.

## Proposal

### `intendedUseContext`

- **Type:** `Text`
- **On:** `Organization`, `Brand`, `Product`, `Service`, `LocalBusiness`, `CreativeWork`
- **Definition:** Descriptive statement of the intended audience, use case, or situation for which this entity is most relevant.

Complements `audience` (which expects a structured `Audience` object) with a lightweight natural-language alternative — similar to how `speakable` complements `description`.

```json
{
  "@type": "Product",
  "name": "Organic Pepper Mix",
  "intendedUseContext": "Intended for home cooks seeking premium organic spices for Mediterranean cooking. Best suited when ingredient quality matters more than price."
}
```

### `brandPersonality`

- **Type:** `Text` or `DefinedTerm`
- **On:** `Organization`, `Brand`, `Product`, `Service`, `LocalBusiness`
- **Definition:** Descriptors characterizing the emotional identity of a brand or product, as defined by the publisher.

Accepting `DefinedTerm` allows linking to Wikidata concepts for verifiability — mitigating the "meta-keywords" spam risk.

```json
{
  "@type": "Organization",
  "name": "Example Spice Company",
  "brandPersonality": [
    { "@type": "DefinedTerm", "name": "Family business", "sameAs": "https://www.wikidata.org/wiki/Q955824" },
    { "@type": "DefinedTerm", "name": "Organic food", "sameAs": "https://www.wikidata.org/wiki/Q191067" }
  ]
}
```

## Compatibility

Non-breaking extension. Both properties are optional.

## Reference

- Open-source spec + implementation: [vibetags/vibetags-spec](https://github.com/vibetags/vibetags-spec) (MIT)
- Related: [#2490](https://github.com/schemaorg/schemaorg/issues/2490) (`speakable`), [#3423](https://github.com/schemaorg/schemaorg/issues/3423) (`colorSwatch`)
