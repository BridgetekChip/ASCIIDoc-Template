# AsciiDoc + Chinese + PDF (VS Code Dev Container Sample)

This repo is a minimal starter template for writing technical docs in **AsciiDoc** in **VS Code**, with:
- HTML preview/build
- PDF export via `asciidoctor-pdf`
- **Chinese/CJK** support (fonts + PDF theme)

## Quick start (VS Code)

1. Open this folder in VS Code.
2. When prompted: **Reopen in Container** (Dev Containers).
3. Build outputs:
   - HTML: `./scripts/build.sh`
   - PDF:  `./scripts/build_pdf.sh`

Outputs will be written to `build/`.

## VS Code Tasks

Open Command Palette → **Tasks: Run Task**:
- `Docs: Build HTML`
- `Docs: Build PDF`

## Chinese fonts notes (PDF)

The container installs `fonts-noto-cjk`. The PDF theme is configured to use Noto CJK fonts.

If you ever see missing boxes (□) in PDF:
- Run: `./scripts/check_fonts.sh`
- Then update filenames in `docs/pdf-theme/theme.yml` if your distro uses different font file names.

## Folder layout

- `docs/index.adoc` – main doc entry
- `docs/styles/asciidoc-style.css` – HTML CSS
- `docs/pdf-theme/theme.yml` – PDF theme (CJK fonts)
- `scripts/` – build helpers
- `.devcontainer/` – devcontainer config

Enjoy!
