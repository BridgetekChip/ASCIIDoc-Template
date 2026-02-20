# Copilot / AI Agent Instructions — AsciiDoc Dev Container Sample

Purpose: quickly onboard an AI coding agent to edit, build, and extend the documentation in this repository.

- **Big picture**: This repo is a minimal AsciiDoc-based docs project.
  - Source: `docs/index.adoc` (single entry point).
  - Outputs: HTML and PDF written to `build/`.
  - Build helpers: `scripts/build.sh` (HTML) and `scripts/build_pdf.sh` (PDF).
  - Preview: VS Code AsciiDoc extension (uses `asciidoctor.js` in the editor).

- **How docs are built (explicit commands)**:
  - HTML: `./scripts/build.sh` → writes `build/index.html`.
  - PDF:  `./scripts/build_pdf.sh` → writes `build/index.pdf`.
  - VS Code Tasks: run `Docs: Build HTML` or `Docs: Build PDF` from the Command Palette.

- **Key project conventions & patterns**:
  - Language/encoding: `:lang: zh-CN` and `:encoding: utf-8` are used in `docs/index.adoc`.
  - Syntax highlighters: preview (VS Code) uses `highlightjs`; CLI builds use `rouge` (`:source-highlighter:` switched by env).
  - Diagrams: asciidoctor-diagram is used. HTML builds render SVG (`diagram-format=svg`); PDF builds render PNG (`diagram-format=png`). Diagrams live in `.diagrams` by convention (see `scripts/*`).
  - Styles: HTML CSS is `docs/styles/asciidoc-style.css`; PDF theme is `docs/pdf-theme/theme.yml`.
  - Fonts: container installs `fonts-noto-cjk`; if PDF shows missing glyphs run `./scripts/check_fonts.sh` and adjust `docs/pdf-theme/theme.yml`.

- **Integration & external dependencies**:
  - `asciidoctor`, `asciidoctor-pdf`, and `asciidoctor-diagram` are required for CLI builds.
  - PlantUML jar path is discovered in the build scripts (`DIAGRAM_PLANTUML_CLASSPATH`).
  - `pdf-fontsdir` points to `/usr/share/fonts` in `build_pdf.sh` — change if the runtime environment differs.

- **When editing content**:
  - Primary file to modify: `docs/index.adoc`.
  - Put images in `docs/images` and reference them via `:imagesdir: images`.
  - Update CSS under `docs/styles/` for HTML presentation.
  - If adding new diagrams, commit the PlantUML source (recommended) and let `asciidoctor-diagram` generate outputs in `.diagrams`.

- **Useful examples from the repo**:
  - Sequence diagram usage (see `docs/index.adoc`):

    [plantuml, "hello-seq", format={diagram-format}]
    ....
    @startuml
    Alice -> Bob: 你好, Bob!
    Bob --> Alice: 你好, Alice!
    @enduml
    ....

- **What to avoid / known limitations**:
  - The project is a docs sample — there are no unit tests or CI workflows to modify.
  - PDF font names vary across distributions; always verify fonts with `./scripts/check_fonts.sh` before changing `theme.yml`.

- **Actionable checklist for an AI agent**:
  1. Edit `docs/index.adoc` for content changes.
 2. Run `./scripts/build.sh` to validate HTML; open `build/index.html` to spot layout issues.
 3. Run `./scripts/build_pdf.sh` to validate PDF output; check for missing glyphs.
 4. If diagrams fail, confirm `DIAGRAM_PLANTUML_CLASSPATH` or render locally.

If anything here is unclear or you want the instructions to include more examples (e.g., editing conventions for large multi-file docs), say which area to expand.
