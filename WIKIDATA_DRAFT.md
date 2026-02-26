<!-- 
  Wikidata QuickStatements Draft for VibeTags
  Submit via: https://quickstatements.toolforge.org/
  
  WICHTIG: Manuell einreichen, nicht automatisiert!
  Wikidata-Richtlinien erfordern manuelle Prüfung.
-->

# Wikidata Entwurf: VibeTags

## Neues Item erstellen

**Label (en):** VibeTags  
**Label (de):** VibeTags  
**Description (en):** Open-source semantic extension for Schema.org that adds emotional positioning and AI recommendation context to structured data  
**Description (de):** Open-Source semantische Erweiterung für Schema.org, die emotionale Positionierung und AI-Empfehlungskontext zu strukturierten Daten hinzufügt  
**Also known as (en):** VibeTags Spec, VibeTags and AgenticContext

---

## Properties (QuickStatements V2 Format)

```
CREATE
LAST	Len	"VibeTags"
LAST	Den	"open-source semantic extension for Schema.org that adds emotional positioning and AI recommendation context to structured data"
LAST	Lde	"VibeTags"
LAST	Dde	"Open-Source semantische Erweiterung für Schema.org für emotionale Markenpositionierung in strukturierten Daten"
LAST	Aen	"VibeTags Spec"
LAST	Aen	"VibeTags and AgenticContext"

LAST	P31	Q7397		/* instance of: software */
LAST	P31	Q2188189	/* instance of: data model */
LAST	P277	Q15026		/* programming language: JSON */
LAST	P275	Q334661		/* license: MIT license */
LAST	P178	Q131765111	/* developer: Hope & Glory Studio (may need to create this entity first) */

LAST	P856	"https://vibetags.studio"		/* official website */
LAST	P1324	"https://github.com/vibetags/vibetags-spec"	/* source code repository */
LAST	P348	"2.0"		/* software version: 2.0 */
LAST	P577	+2026-02-16T00:00:00Z/11	/* publication date: Feb 2026 */

LAST	P2283	Q3512458	/* uses: Schema.org */
LAST	P2283	Q6108942	/* uses: JSON-LD */
LAST	P366	Q11660	    /* main use: artificial intelligence */
LAST	P366	Q182524		/* main use: search engine */

LAST	P170	Q131765111	/* creator: Sascha Deforth (may need to create entity first) */
```

---

## Voraussetzungen prüfen

Bevor du das Item erstellst, prüfe ob diese referenzierten Entities existieren:

| Property | Wikidata ID | Was | Status |
|:---|:---|:---|:---|
| Schema.org | Q3512458 | ✅ Existiert | OK |
| JSON-LD | Q6108942 | ✅ Existiert | OK |
| MIT License | Q334661 | ✅ Existiert | OK |
| JSON | Q15026 | ✅ Existiert | OK |
| AI | Q11660 | ✅ Existiert | OK |
| Search engine | Q182524 | ✅ Existiert | OK |
| Software | Q7397 | ✅ Existiert | OK |
| Data model | Q2188189 | ✅ Existiert | OK |
| Hope & Glory Studio | ? | ❌ Muss evtl. erst erstellt werden | Prüfen |
| Sascha Deforth | ? | ❌ Muss evtl. erst erstellt werden | Prüfen |

---

## Referenzen (für Wikidata-Quellen)

Wikidata-Einträge brauchen **Referenzen**. Mögliche Quellen:

1. GitHub Repository: https://github.com/vibetags/vibetags-spec
2. Schema.org Proposal Issue: (Link zum eingereichten Issue einfügen)
3. vibetags.studio Website
4. LinkedIn Posts über VibeTags (wenn veröffentlicht)

---

## Anleitung zum Einreichen

1. Gehe zu https://www.wikidata.org/wiki/Special:NewItem
2. Fülle Label, Description, Aliases aus (siehe oben)
3. Klicke "Create"
4. Füge die Statements einzeln hinzu über die Wikidata UI
5. ODER nutze QuickStatements: https://quickstatements.toolforge.org/

> **Hinweis:** Der Eintrag wird von Wikidata-Freiwilligen geprüft. 
> Ohne externe Sekundärquellen (Presse, Papers) könnte der Eintrag 
> als "nicht relevant" gelöscht werden. Die Schema.org Proposal 
> stärkt die Relevanz erheblich.
