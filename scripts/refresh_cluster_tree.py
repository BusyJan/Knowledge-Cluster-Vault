#!/usr/bin/env python3
"""
Regenerate CLUSTER-TREE.md with a Mermaid top-down tree (root → projects → standard files).
Run from vault root: python3 scripts/refresh_cluster_tree.py
"""

from __future__ import annotations

import os
import re
import sys
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


def main() -> None:
    vault = vault_root()
    projects_dir = vault / "Projects"
    if not projects_dir.is_dir():
        raise SystemExit("No Projects/ directory")

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

    lines: list[str] = [
        "---",
        "tags: [cluster, index, tree, meta]",
        "---",
        "",
        "# Cluster tree",
        "",
        "This note is a **real tree** (top-down diagram). The **Graph** view cannot do this for the whole vault — it uses physics, not hierarchy.",
        "",
        "Regenerate after adding a project:",
        "",
        "```bash",
        "python3 scripts/refresh_cluster_tree.py",
        "```",
        "",
        "## Tree diagram",
        "",
        "```mermaid",
        "flowchart TB",
        "  D[Dashboard]",
    ]

    for slug, title in rows:
        pid = safe_mermaid_id(slug, "root")
        label = f"{slug} — {title}".replace('"', "'")[:120]
        lines.append(f'  D --> {pid}["{label}"]')
        rid = safe_mermaid_id(slug, "readme")
        lines.append(f"  {pid} --> {rid}[README]")
        for name in ("Notes", "Summary", "Decisions", "Tasks"):
            nid = safe_mermaid_id(slug, name.lower())
            lines.append(f"  {rid} --> {nid}[{name}]")

    lines.append("```")
    lines.extend(
        [
            "",
            "## Quick links (Obsidian)",
            "",
            "- [[Dashboard]]",
        ]
    )
    for slug, _title in rows:
        lines.append(f"- [[Projects/{slug}/README|{slug}]]")

    lines.extend(
        [
            "",
            "## Make the Graph less messy",
            "",
            "- In **Graph** → filters: **hide tags** (green nodes connect many notes).",
            "- Use **Local graph** from **Dashboard** with depth **2**.",
            "- This **CLUSTER-TREE** note is for hierarchy; Graph is for discovery.",
            "",
        ]
    )

    out = vault / "CLUSTER-TREE.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(out)


if __name__ == "__main__":
    main()
