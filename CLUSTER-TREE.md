---
tags: [cluster, index, tree, meta]
---

# Cluster tree

This note is a **real tree** (top-down diagram). The **Graph** view cannot do this for the whole vault — it uses physics, not hierarchy.

Regenerate after adding a project:

```bash
python3 scripts/refresh_cluster_tree.py
```

## Tree diagram

```mermaid
flowchart TB
  D[Dashboard]
  D --> esp_projects_root["esp-projects — ESP Projects workspace"]
  esp_projects_root --> esp_projects_readme[README]
  esp_projects_readme --> esp_projects_notes[Notes]
  esp_projects_readme --> esp_projects_summary[Summary]
  esp_projects_readme --> esp_projects_decisions[Decisions]
  esp_projects_readme --> esp_projects_tasks[Tasks]
  D --> nocturn_root["nocturn — nocturn"]
  nocturn_root --> nocturn_readme[README]
  nocturn_readme --> nocturn_notes[Notes]
  nocturn_readme --> nocturn_summary[Summary]
  nocturn_readme --> nocturn_decisions[Decisions]
  nocturn_readme --> nocturn_tasks[Tasks]
  D --> project_apex_root["project-apex — project-apex (SubZero KiCad)"]
  project_apex_root --> project_apex_readme[README]
  project_apex_readme --> project_apex_notes[Notes]
  project_apex_readme --> project_apex_summary[Summary]
  project_apex_readme --> project_apex_decisions[Decisions]
  project_apex_readme --> project_apex_tasks[Tasks]
  D --> subzero_pcb_engine_root["subzero-pcb-engine — subzero-pcb-engine"]
  subzero_pcb_engine_root --> subzero_pcb_engine_readme[README]
  subzero_pcb_engine_readme --> subzero_pcb_engine_notes[Notes]
  subzero_pcb_engine_readme --> subzero_pcb_engine_summary[Summary]
  subzero_pcb_engine_readme --> subzero_pcb_engine_decisions[Decisions]
  subzero_pcb_engine_readme --> subzero_pcb_engine_tasks[Tasks]
```

## Quick links (Obsidian)

- [[Dashboard]]
- [[Projects/esp-projects/README|esp-projects]]
- [[Projects/nocturn/README|nocturn]]
- [[Projects/project-apex/README|project-apex]]
- [[Projects/subzero-pcb-engine/README|subzero-pcb-engine]]

## Make the Graph less messy

- In **Graph** → filters: **hide tags** (green nodes connect many notes).
- Use **Local graph** from **Dashboard** with depth **2**.
- This **CLUSTER-TREE** note is for hierarchy; Graph is for discovery.

