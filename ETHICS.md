# VibeTags Ethics Policy v1.0

**Status:** Active
**Version:** 1.0
**Date:** February 2026
**Authors:** Sascha Deforth (Hope & Glory Studio)

---

## 1. Purpose

VibeTags and AgenticContext are semantic extensions that influence how AI systems perceive and recommend brands, products, and services. This power comes with responsibility.

This Ethics Policy defines clear guidelines for the responsible use of VibeTags to ensure they serve users, not manipulate them.

---

## 2. Core Principles

### 2.1 Truthfulness
VibeTags MUST accurately reflect the actual brand identity, product characteristics, or service quality.

### 2.2 Self-Description Only
VibeTags MUST only describe the entity that publishes them. You cannot set VibeTags about competitors, third parties, or entities you do not own or represent.

### 2.3 No Negative Targeting
AgenticContext MUST NOT contain negative references to competitors or attempt to divert users away from other brands.

### 2.4 Transparency
Sites implementing VibeTags SHOULD make their use transparent and consistent with visible website content.

### 2.5 User Benefit
AgenticContext recommendations MUST prioritize user benefit over brand promotion.

---

## 3. Differentiation from Dark Patterns

VibeTags are NOT dark patterns because they ADD structured, machine-readable information rather than hiding it. They use open, standardized Schema.org vocabulary under MIT license and are publicly auditable.

Key distinction: VibeTags make brand positioning explicit and machine-readable rather than implicit and hidden. This increases transparency, not deception.

---

## 4. Trust and Integrity

### 4.1 ECDSA Trust Signing (Optional)
Publishers MAY use ECDSA digital signatures to prove VibeTags were set by the domain owner and have not been tampered with.

Trust Signing provides: Integrity, Authenticity, Timestamp proof.
Trust Signing does NOT provide: Content verification, Quality assurance, Endorsement.

### 4.2 IPTC Transparency (Recommended)
Following IPTC 2025.1 standards, VibeTags implementations SHOULD include clear attribution of AI-generated content and provenance metadata.

---

## 5. Prohibited Uses

1. Impersonation - Setting VibeTags that imply affiliation with organizations you do not represent
2. False Claims - Using tags like Certified, Award-Winning, Official without verification
3. Competitor Sabotage - Any attempt to negatively influence AI perception of competitors
4. Spam Tags - Stuffing irrelevant keywords to game AI recommendations
5. Discriminatory Content - Tags that promote discrimination
6. Cloaking - Showing different VibeTags to AI crawlers than what appears on the website

---

## 6. Compliance

### Self-Assessment Checklist
Before publishing VibeTags, ask:
- Do my VibeTags truthfully represent my brand/product/service?
- Would I be comfortable if a journalist published these tags?
- Do my AgenticContext instructions prioritize user benefit?
- Am I only describing my own entity, not competitors?
- Are my VibeTags consistent with my visible website content?

### Reporting Misuse
Report violations via GitHub Issue: github.com/vibetags/vibetags-spec/issues

---

## 7. License

This Ethics Policy is published under the MIT License alongside the VibeTags specification.
