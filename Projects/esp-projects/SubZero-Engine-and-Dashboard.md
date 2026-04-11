---
title: SubZero PCB Engine + LAN Dashboard
tags: [subzero, pcb-engine, dashboard, kicad]
updated: 2026-04-11
---

# SubZero PCB Engine + LAN Dashboard

Repo folder: `subzero-pcb-engine/` (sibling workspace). Hardware lives in **`project-apex/`**; this repo parses `.kicad_pcb`, runs Shapely courtyard checks, dual-board B2B rules, optional `kicad-cli` DRC merge, **append-only** `SUBZERO_OPTIMIZATION_LOG.md`.

## Setup (engine)

```bash
cd subzero-pcb-engine
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

Copy `.env.example` → `.env` (gitignored). Variables: `SUBZERO_PROJECT_ROOT`, `SUBZERO_MAIN_PCB`, `SUBZERO_TOP_PCB`, `KICAD_CLI`, dashboard secrets, etc.

## Parse / review modes

| Mode | Meaning |
| --- | --- |
| `parse-only` | Python rules only; no KiCad copper DRC ground truth |
| `full` | + `kicad-cli pcb drc` JSON when CLI available |

```bash
.venv/bin/python -m pcb_parser --stack config/subzero_stack.yaml --mode parse-only
.venv/bin/python -m pcb_parser --stack config/subzero_stack.yaml --mode full
```

Paths in `config/subzero_stack.yaml` are relative to that YAML file.

## Dashboard (LAN)

```bash
cd subzero-pcb-engine
.venv/bin/pip install -e ".[dashboard]"
# export SUBZERO_PROJECT_ROOT="/path/to/project-apex"
.venv/bin/python -m dashboard.scripts.export_boards   # optional; needs kicad-cli
.venv/bin/subzero-dashboard
```

Same as: `.venv/bin/python -m dashboard`.

- **Port:** `SUBZERO_DASHBOARD_PORT` (default **80**; often `8080` without root)
- **Bind:** `SUBZERO_DASHBOARD_HOST` (default `0.0.0.0`)
- **DNS:** `subzero-dev.local` — see `dashboard/DNS.md`

## KiCad CLI (SVG + GLB)

- **Major version must match boards** (KiCad 10 boards vs KiCad 9 CLI fails).
- Set **`KICAD_CLI`** in `.env` to AppImage-extracted `kicad-cli` if system `PATH` still points to 9.x.

| Asset | Command idea |
| --- | --- |
| 2D SVG | `kicad-cli pcb export svg --output <file.svg> --mode-single <board.kicad_pcb>` |
| 3D GLB | `kicad-cli pcb export glb --output <file.glb> <board.kicad_pcb>` |

## Dashboard APIs (high level)

- Manifest, SSE stream, component focus overlays, **agent** start/stop/status, **rating** `POST /api/rating`, stats, logs under `dashboard/logs/`.
- See `subzero-pcb-engine/dashboard/README.md` for full detail.

## Related

- [[Workspace-Repo-Map]]
- [[SubZero-PCB-Prototypes]]
