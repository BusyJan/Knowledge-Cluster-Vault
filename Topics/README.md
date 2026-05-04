---
tags: [cluster/meta, index]
cluster: meta
---

# Topics — atomare Punkte

**Ein Thema → eine Datei.** Ordnernamen entsprechen dem Cluster aus `cluster-registry.json` (`hardware`, `software`, `meta`, …).

## Namensvorschlag

`Topics/<cluster>/YYYY-MM-DD-kurzbeschreibung.md`

Kein Zwang — Hauptsache **ein Gedanke pro Datei** und passendes Frontmatter (`Templates/topic.atomic.md`).

## Sammeln ohne Link-Chaos

- In Cluster-MOCs (`Clusters/`) mit **Dataview** nach `WHERE contains(file.folder, "Topics/hardware")` listen.
- Keine `[[wikilinks]]` zu allen Nachbarn — nur wenn wirklich eine **harte Abhängigkeit** besteht.

Siehe [[Vault-Leitfaden]].
