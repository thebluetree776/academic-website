# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Preview

```bash
quarto render        # build site to _site/
quarto preview       # live-reload local dev server
```

Deployment is automatic: pushing to `main` triggers the GitHub Actions workflow (`.github/workflows/deploy.yml`), which renders the site and pushes `_site/` to the `gh-pages` branch, served by GitHub Pages at `ichio-aoki.com`.

`_site/` is build output and is gitignored — never commit it. Only `*.qmd` files are rendered (`project.render` in `_quarto.yml`), so Markdown files like this one are not published.

## Architecture

This is a [Quarto](https://quarto.org) static website — an academic personal/CV site. Configuration is in `_quarto.yml` (theme: cosmo/Bootstrap, sidebar nav).

**Content files:**
- `index.qmd` — English CV page (primary)
- `index-jp.qmd` — Japanese CV page (must be kept in sync with `index.qmd`)
- `blog.qmd` — "Notes" page (under construction)

**When updating CV content** (publications, presentations, affiliations, etc.), both `index.qmd` and `index-jp.qmd` must be updated together.

**CV conventions** (inside the `::: {.cv-list}` div):
- Entry: `* **Title** [Download](assets/file.pdf){.dl} [Mon YYYY]{.float-end}` then `  <br> detail line`. Lists are newest first.
- Mark future items with `*(Upcoming)*` / `*(予定)*` before the title; remove it once the event has passed.
- On the Japanese page, paper/talk titles stay in English, and foreign conference names/places stay in English; Japanese institutions are written in Japanese.
- Update the "Last updated" footer on both pages.

**Download badges:** links with the `.dl` class get `download`/`target="_blank"` from `filters/download-links.lua` and badge styling from `styles.css`.

## Syncing Research Data

`scripts/sync_researchmap.py` fetches presentations and papers from the researchmap.jp API (`https://api.researchmap.jp/ichio`) and prints them to stdout for manual review. It does **not** auto-update the `.qmd` files — the output is used as a reference to manually update `index.qmd` and `index-jp.qmd`.

```bash
python scripts/sync_researchmap.py
```

## Assets

PDF files (theses, presentations, working papers) live in `assets/`, named like `pres_YYYYMMDD_topic.pdf`, `poster_YYYYMMDD_event.pdf`, `paper_YYYYMM_topic.pdf`, `thesis_degree_school.pdf`, and are linked directly from the `.qmd` files via relative paths. New PDFs should be added to `assets/` and referenced in both language versions (there are no separate Japanese PDFs).
