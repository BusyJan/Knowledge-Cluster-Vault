#!/usr/bin/env python3
"""
Regenerate CLUSTER-TREE.md — Mermaid tree with colored subgraph clusters (cluster-registry.json).

Run from vault root: python3 scripts/refresh_cluster_tree.py
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

FM_RE = re.compile(r"^---\s*$(.*?)^---\s*$", re.MULTILINE | re.DOTALL)


def vault_root() -> Path:
    env = os.environ.get("KNOWLEDGE_VAULT")
    if env:
        return Path(env).resolve()
    return Path(__file__).resolve().parent.parent


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FM_RE.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            val = v.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            out[k.strip()] = val
    return out


def safe_mermaid_id(slug: str, suffix: str) -> str:
    base = re.sub(r"[^a-zA-Z0-9_]", "_", f"{slug}_{suffix}")
    if base[0].isdigit():
        base = "n_" + base
    return base


def load_registry(vault: Path) -> dict:
    p = vault / "cluster-registry.json"
    if not p.is_file():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def sync_obsidian_graph(vault: Path, registry: dict, rows: list[tuple[str, str]]) -> None:
    """Write .obsidian/graph.json color groups from cluster-registry + unassigned projects."""
    graph_path = vault / ".obsidian/graph.json"
    base: dict = {}
    if graph_path.exists():
        base = json.loads(graph_path.read_text(encoding="utf-8"))

    clusters = registry.get("clusters", {})
    all_assigned: set[str] = set()
    for cdata in clusters.values():
        all_assigned.update(cdata.get("projects", []))

    groups: list[dict] = []
    for key, cdata in clusters.items():
        if key == "uncategorized":
            continue
        projects = sorted(cdata.get("projects", []))
        if not projects:
            continue
        q = " OR ".join(f"path:Projects/{p}" for p in projects)
        rgb = int(cdata["graph_rgb"])
        groups.append({"query": q, "color": {"a": 1, "rgb": rgb}})

    loose = sorted(s for s, _ in rows if s not in all_assigned)
    if loose:
        u = clusters.get("uncategorized", {})
        rgb = int(u.get("graph_rgb", 7901340))
        q = " OR ".join(f"path:Projects/{p}" for p in loose)
        groups.append({"query": q, "color": {"a": 1, "rgb": rgb}})

    for _k, vp in registry.get("vault_paths", {}).items():
        groups.append({"query": vp["query"], "color": {"a": 1, "rgb": int(vp["graph_rgb"])}})

    base["showTags"] = False
    base["showAttachments"] = False
    base["colorGroups"] = groups
    base["collapse-color-groups"] = False
    base.setdefault("centerStrength", 0.55)
    base.setdefault("repelStrength", 8.5)
    base.setdefault("linkStrength", 0.55)
    base.setdefault("linkDistance", 28)
    graph_path.parent.mkdir(parents=True, exist_ok=True)
    graph_path.write_text(json.dumps(base, indent=2) + "\n", encoding="utf-8")
    print(graph_path)


def main() -> None:
    vault = vault_root()
    projects_dir = vault / "Projects"
    if not projects_dir.is_dir():
        raise SystemExit("No Projects/ directory")

    raw = load_registry(vault)
    cluster_cfg = raw.get("clusters", {})

    slug_to_cluster: dict[str, str] = {}
    cluster_order: list[str] = []
    for key, data in cluster_cfg.items():
        if key == "uncategorized":
            continue
        cluster_order.append(key)
        for slug in data.get("projects", []):
            slug_to_cluster[slug] = key

    rows: list[tuple[str, str]] = []
    for d in sorted(projects_dir.iterdir()):
        if not d.is_dir():
            continue
        readme = d / "README.md"
        if not readme.exists():
            continue
        fm = parse_frontmatter(readme.read_text(encoding="utf-8"))
        title = fm.get("title", d.name)
        rows.append((d.name, title))

    uncategorized_key = "uncategorized"
    cluster_rows: dict[str, list[tuple[str, str]]] = {k: [] for k in cluster_order}
    cluster_rows[uncategorized_key] = []

    for slug, title in rows:
        ck = slug_to_cluster.get(slug, uncategorized_key)
        if ck not in cluster_rows:
            cluster_rows[uncategorized_key].append((slug, title))
        else:
            cluster_rows[ck].append((slug, title))

    lines: list[str] = [
        "---",
        "tags: [cluster, index, tree, meta]",
        "---",
        "",
        "# Cluster tree",
        "",
        "Hierarchie **oben → unten** (Projektordner). **Graph-Ansicht** bleibt physikalisch (Keulen) — Farb-Cluster kommen aus **Einstellungen → Graph view → Gruppen** (`cluster-registry.json` + `.obsidian/graph.json`).",
        "",
        "**Weniger unnötige Kanten:** möglichst **keine** `[[Wiki-Links]]` zwischen beliebigen Notizen; Themen atomic unter `Topics/<cluster-slug>/` mit Tag `topic` / `cluster/...` — Verknüpfung über Ordner und Dataview oder einzelne Cluster-MOCs in `Clusters/`.",
        "",
        "Nach neuem Projekt oder Registry-Änderung:",
        "",
        "```bash",
        "python3 scripts/refresh_cluster_tree.py",
        "```",
        "",
        "Details: [[Vault-Leitfaden]].",
        "",
        "## Tree diagram",
        "",
        "```mermaid",
        "flowchart TB",
    ]

    # classDef lines
    for key, data in cluster_cfg.items():
        style = data.get("mermaid_style", "fill:#ECEFF1,stroke:#546E7A")
        cid = safe_mermaid_id(key, "style")
        lines.append(f"  classDef {cid} {style}")

    lines.append('  D["Dashboard"]')

    roots_by_cluster: dict[str, list[str]] = {}

    for ck in cluster_order + [uncategorized_key]:
        projects = cluster_rows.get(ck, [])
        if not projects:
            continue
        data = cluster_cfg.get(ck, {})
        emoji = data.get("emoji", "")
        label = data.get("label", ck)
        subgraph_title = f"{emoji + ' ' if emoji else ''}{label}".strip()
        subgraph_id = safe_mermaid_id(ck, "cluster")
        lines.append(f'  subgraph {subgraph_id} ["{subgraph_title}"]')
        root_ids: list[str] = []
        for slug, title in sorted(projects, key=lambda x: x[0]):
            pid = safe_mermaid_id(slug, "root")
            root_ids.append(pid)
            label_esc = f"{slug} — {title}".replace('"', "'")[:120]
            lines.append(f'    {pid}["{label_esc}"]')
            rid = safe_mermaid_id(slug, "readme")
            lines.append(f"    {pid} --> {rid}[README]")
            nid_notes = safe_mermaid_id(slug, "notes")
            nid_summary = safe_mermaid_id(slug, "summary")
            nid_dec = safe_mermaid_id(slug, "decisions")
            nid_tasks = safe_mermaid_id(slug, "tasks")
            lines.append(f"    {rid} --> {nid_notes}[Notes]")
            lines.append(f"    {nid_notes} --> {nid_summary}[Summary]")
            lines.append(f"    {nid_summary} --> {nid_dec}[Decisions]")
            lines.append(f"    {nid_dec} --> {nid_tasks}[Tasks]")
        lines.append("  end")
        roots_by_cluster[ck] = root_ids

    # Edges Dashboard → each project root
    for ck in cluster_order + [uncategorized_key]:
        for pid in roots_by_cluster.get(ck, []):
            lines.append(f"  D --> {pid}")

    # Color project root nodes per cluster classDef
    for ck in cluster_order + [uncategorized_key]:
        pids = roots_by_cluster.get(ck, [])
        if not pids:
            continue
        cid = safe_mermaid_id(ck, "style")
        joined = ",".join(pids)
        lines.append(f"  class {joined} {cid}")

    lines.append("```")
    lines.extend(
        [
            "",
            "## Quick links (minimal)",
            "",
            "- [[Dashboard]]",
            "- [[Vault-Leitfaden]]",
            "- [[Clusters/README|Clusters]]",
            "- [[Topics/README|Topics (atomare Punkte)]]",
        ]
    )
    for slug, _title in sorted(rows, key=lambda x: x[0]):
        lines.append(f"- [[Projects/{slug}/README|{slug}]]")

    lines.extend(
        [
            "",
            "## Graph weniger unübersichtlich",
            "",
            "- **Globale Graph-Ansicht:** Tags ausblenden (`showTags: false` ist voreingestellt), damit keine grünen Pseudo-Kanten zu Tag-Knoten entstehen.",
            "- **Farben:** Projekt-Knoten nach Cluster (Pfad-Groups); `Topics/` und `Clusters/` eigene Farben.",
            "- **Links sparsam:** neue Themen als **eigene Datei** unter `Topics/…`; nur wo nötig `[[wikilinks]]` oder Überschrift in einem Cluster-MOC.",
            "",
        ]
    )

    out = vault / "CLUSTER-TREE.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(out)

    reg = load_registry(vault)
    if reg.get("clusters"):
        sync_obsidian_graph(vault, reg, rows)


if __name__ == "__main__":
    main()
