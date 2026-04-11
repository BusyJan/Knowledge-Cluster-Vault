#!/usr/bin/env python3
"""
Deterministic vault operations for MyKnowledgeVault.
No LLM calls — safe for hooks and CI.

Environment:
  KNOWLEDGE_VAULT  Override vault root (default: parent of scripts/).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

# Legacy: ## [YYYY-MM-DD]
# Current: ## YYYY-MM-DD HH:MM
SECTION_RE = re.compile(
    r"^## (?:\[(\d{4}-\d{2}-\d{2})\]|(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}))\s*$",
    re.MULTILINE,
)
FM_RE = re.compile(
    r"^---\s*$(.*?)^---\s*$",
    re.MULTILINE | re.DOTALL,
)


def vault_root(explicit: Path | None) -> Path:
    if explicit:
        return explicit.resolve()
    env = __import__("os").environ.get("KNOWLEDGE_VAULT")
    if env:
        return Path(env).resolve()
    return Path(__file__).resolve().parent.parent


def project_dir(vault: Path, slug: str) -> Path:
    safe = slug.strip().lower().replace(" ", "-")
    safe = re.sub(r"[^a-z0-9._-]", "-", safe)
    safe = re.sub(r"-+", "-", safe).strip("-")
    if not safe:
        raise SystemExit("Invalid slug after sanitization.")
    return vault / "Projects" / safe


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def now_iso() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat(sep=" ")


def parse_notes_sections(text: str) -> list[tuple[str, str, str]]:
    """
    Return list of (date_yyyy_mm_dd, body, heading_line) for each section.
    date is used for compression window; heading_line is preserved for output.
    """
    matches = list(SECTION_RE.finditer(text))
    if not matches:
        return []
    out: list[tuple[str, str, str]] = []
    for i, m in enumerate(matches):
        if m.group(1):
            d = m.group(1)
        else:
            d = m.group(2)  # YYYY-MM-DD from new format
        heading_line = m.group(0).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        out.append((d, body, heading_line))
    return out


def ensure_project(
    vault: Path,
    slug: str,
    project_title: str | None,
    status: str,
    repo: str,
) -> Path:
    pdir = project_dir(vault, slug)
    tpl = vault / "Templates"
    title = project_title or slug.replace("-", " ").title()
    iso = now_iso()

    pdir.mkdir(parents=True, exist_ok=True)
    seeds = {
        "README.md": tpl / "project-README.md",
        "Notes.md": tpl / "Notes.seed.md",
        "Decisions.md": tpl / "Decisions.seed.md",
        "Tasks.md": tpl / "Tasks.seed.md",
        "Summary.md": tpl / "Summary.seed.md",
    }
    for fname, src in seeds.items():
        dst = pdir / fname
        if dst.exists():
            continue
        if not src.exists():
            raise SystemExit(f"Missing template: {src}")
        raw = read_text(src)
        raw = raw.replace("{{PROJECT_TITLE}}", title)
        raw = raw.replace("{{PROJECT_SLUG}}", slug)
        raw = raw.replace("{{ISO_DATETIME}}", iso)
        raw = raw.replace("{{PROJECT_REPO}}", repo)
        if fname == "README.md":
            raw = raw.replace("status: active", f"status: {status}")
        if fname == "Notes.md":
            now = dt.datetime.now().replace(second=0, microsecond=0)
            raw = raw.replace(
                "{{DATETIME_HEADING}}",
                now.strftime("%Y-%m-%d %H:%M"),
            )
        if fname == "Tasks.md":
            raw = raw.replace("{{DATE_ISO}}", dt.date.today().isoformat())
        write_text(dst, raw)
    return pdir


def append_note(
    vault: Path,
    slug: str,
    insight: str,
    context: str,
    problem: str,
    decision: str,
    next_step: str,
) -> Path:
    pdir = project_dir(vault, slug)
    notes = pdir / "Notes.md"
    if not notes.exists():
        raise SystemExit(f"Notes.md missing — run ensure-project first: {notes}")
    now = dt.datetime.now().replace(second=0, microsecond=0)
    heading = f"## {now.strftime('%Y-%m-%d %H:%M')}"
    block = f"""
{heading}

- Insight: {insight or "(none)"}
- Context: {context or "(none)"}
- Problem: {problem or "(none)"}
- Decision: {decision or "(none)"}
- Next step: {next_step or "(none)"}
"""
    text = read_text(notes).rstrip() + "\n" + block.lstrip()
    write_text(notes, text + "\n")
    bump_readme_updated(pdir / "README.md")
    return notes


def bump_readme_updated(readme: Path) -> None:
    if not readme.exists():
        return
    iso = now_iso()
    t = read_text(readme)
    if re.search(r"(?m)^updated:\s*", t):
        t = re.sub(r"(?m)^updated:\s*.*$", f"updated: {iso}", t, count=1)
    elif re.search(r"(?m)^last_updated:\s*", t):
        t = re.sub(r"(?m)^last_updated:\s*.*$", f"last_updated: {iso}", t, count=1)
    write_text(readme, t)


def append_decision(vault: Path, slug: str, title: str, body: str) -> Path:
    pdir = project_dir(vault, slug)
    dec = pdir / "Decisions.md"
    if not dec.exists():
        raise SystemExit(f"Decisions.md missing: {dec}")
    today = dt.date.today().isoformat()
    block = f"""

### [{today}] {title}

{body.strip()}

"""
    write_text(dec, read_text(dec).rstrip() + block + "\n")
    bump_readme_updated(pdir / "README.md")
    return dec


def compress_notes(
    vault: Path,
    slug: str,
    keep_recent_days: int,
) -> Path:
    pdir = project_dir(vault, slug)
    notes_path = pdir / "Notes.md"
    summary_path = pdir / "Summary.md"
    if not notes_path.exists():
        raise SystemExit(f"Notes.md missing: {notes_path}")

    sections = parse_notes_sections(read_text(notes_path))
    if not sections:
        raise SystemExit("No dated sections found in Notes.md.")

    today = dt.date.today()
    cutoff = today - dt.timedelta(days=keep_recent_days)

    recent: list[tuple[str, str, str]] = []
    rolled: list[tuple[str, str, str]] = []
    for d, body, heading in sections:
        day = dt.date.fromisoformat(d)
        if day >= cutoff:
            recent.append((d, body, heading))
        else:
            rolled.append((d, body, heading))

    recent_md = []
    for _d, body, heading in recent:
        recent_md.append(f"{heading}\n\n{body}\n")

    rolled_md = []
    for d, body, _heading in rolled:
        first = next(
            (ln.strip() for ln in body.splitlines() if ln.strip().startswith("- Insight:")),
            body.splitlines()[0] if body else "",
        )
        rolled_md.append(f"- **{d}:** {first}")

    injection = (
        "<!-- VAULTCTL:COMPRESSED_START -->\n"
        "## Recent (from Notes, last "
        f"{keep_recent_days} days)\n\n"
        + ("\n".join(recent_md) if recent_md else "_No entries in window._\n")
        + "\n## Rolled up (older)\n\n"
        + ("\n".join(rolled_md) if rolled_md else "_None._\n")
        + "\n<!-- VAULTCTL:COMPRESSED_END -->\n"
    )

    if summary_path.exists():
        s = read_text(summary_path)
        if "<!-- VAULTCTL:COMPRESSED_START -->" in s:
            s = re.sub(
                r"<!-- VAULTCTL:COMPRESSED_START -->.*?<!-- VAULTCTL:COMPRESSED_END -->",
                injection.strip(),
                s,
                flags=re.DOTALL,
            )
        else:
            s = s.rstrip() + "\n\n" + injection
        write_text(summary_path, s)
    else:
        write_text(
            summary_path,
            "# Summary (compressed knowledge)\n\n" + injection,
        )

    bump_readme_updated(pdir / "README.md")
    return summary_path


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FM_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    out: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            val = v.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            out[k.strip()] = val
    return out


def refresh_dashboard(vault: Path) -> str:
    projects = vault / "Projects"
    rows: list[dict[str, str]] = []
    if projects.is_dir():
        for d in sorted(projects.iterdir()):
            if not d.is_dir():
                continue
            readme = d / "README.md"
            if not readme.exists():
                continue
            fm = parse_frontmatter(read_text(readme))
            title = fm.get("title") or fm.get("project", d.name)
            updated = fm.get("updated") or fm.get("last_updated", "")
            rows.append(
                {
                    "title": title,
                    "slug": fm.get("slug", d.name),
                    "status": fm.get("status", ""),
                    "updated": updated,
                    "repo": fm.get("repo", ""),
                }
            )

    rows.sort(key=lambda r: r.get("updated") or "", reverse=True)

    lines = [
        "| Title | Slug | Status | Updated | Repo |",
        "|-------|------|--------|---------|------|",
    ]
    for r in rows:
        lines.append(
            f"| {r['title']} | {r['slug']} | {r['status']} | {r['updated']} | {r['repo']} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="MyKnowledgeVault control (no LLM).")
    ap.add_argument(
        "--vault",
        type=Path,
        default=None,
        help="Vault root (default: KNOWLEDGE_VAULT or next to this script).",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_ens = sub.add_parser("ensure-project", help="Create project tree from Templates.")
    p_ens.add_argument("--slug", required=True)
    p_ens.add_argument("--title", default=None)
    p_ens.add_argument("--status", default="active")
    p_ens.add_argument("--repo", default="")

    p_an = sub.add_parser("append-note", help="Append a dated block to Notes.md.")
    p_an.add_argument("--slug", required=True)
    for flag, dest in (
        ("insight", "insight"),
        ("context", "context"),
        ("problem", "problem"),
        ("decision", "decision"),
        ("next-step", "next_step"),
    ):
        p_an.add_argument(f"--{flag}", default="", dest=dest)

    p_ad = sub.add_parser("append-decision", help="Append a decision block.")
    p_ad.add_argument("--slug", required=True)
    p_ad.add_argument("--title", required=True)
    p_ad.add_argument("--body", required=True)

    p_co = sub.add_parser("compress", help="Roll Notes into Summary (deterministic).")
    p_co.add_argument("--slug", required=True)
    p_co.add_argument("--keep-days", type=int, default=14)

    sub.add_parser("refresh-dashboard", help="Print Markdown table for Dashboard fallback.")

    args = ap.parse_args()
    vault = vault_root(args.vault)

    if args.cmd == "ensure-project":
        path = ensure_project(
            vault,
            args.slug,
            args.title,
            args.status,
            args.repo,
        )
        print(path)
    elif args.cmd == "append-note":
        path = append_note(
            vault,
            args.slug,
            args.insight,
            args.context,
            args.problem,
            args.decision,
            args.next_step,
        )
        print(path)
    elif args.cmd == "append-decision":
        path = append_decision(vault, args.slug, args.title, args.body)
        print(path)
    elif args.cmd == "compress":
        path = compress_notes(vault, args.slug, args.keep_days)
        print(path)
    elif args.cmd == "refresh-dashboard":
        sys.stdout.write(refresh_dashboard(vault))
    else:
        raise SystemExit("Unknown command")


if __name__ == "__main__":
    main()
