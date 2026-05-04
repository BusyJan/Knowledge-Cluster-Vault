# Obsidian-Assets (geteilt über Git)

Der Ordner **`.obsidian/`** liegt in `.gitignore` (Plugins, fensterbezogener Workspace). Hier liegen nur **übernehmbare** Teile:

| Datei | Ziel nach Kopie |
|--------|------------------|
| `snippets/cluster-tag-colors.css` | `.obsidian/snippets/cluster-tag-colors.css` |

**Einrichtung:** `bash scripts/install_obsidian_assets.sh` im Vault-Root — kopiert das Snippet und führt `refresh_cluster_tree.py` aus (Graph-Farben). In Obsidian: **Einstellungen → Darstellung → CSS-Snippets** → Snippet aktivieren.
