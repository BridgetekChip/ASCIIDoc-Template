# ASCIIDoc Template Datasheet

A lightweight ASCIIDoc project for creating product datasheets and documentation with automatic HTML/PDF output.

## Overview

- The main source document is `datasheet.adoc`.
- Generated output files include `datasheet.html` and PDF artifacts produced by the build script.
- The repository supports Chinese styling with separate theme settings.

## Repository Structure

- `datasheet.adoc` — main ASCIIDoc source.
- `datasheet.html` — generated HTML output (do not edit directly).
- `build-zh-pdf.sh` — script to build the Chinese PDF version.
- `chapters/` — reusable chapter fragments.
- `images/` — embedded image assets.
- `regs/` — control/register documentation snippets.
- `themes/` — styling theme files for Asciidoctor output.

## Usage

1. Open the project folder in VS Code.
2. Allow the Dev Container extension and container environment to load if prompted.
3. Open `datasheet.adoc` and use the AsciiDoc preview pane.

## Build

Example HTML build with Asciidoctor:

```bash
asciidoctor -r asciidoctor-diagram -a toc=left -a source-highlighter=rouge datasheet.adoc
```

Example PDF build if your toolchain supports it:

```bash
asciidoctor-pdf -a pdf-theme=themes/theme.yml datasheet.adoc
```

To build the Chinese PDF version:

```bash
./build-zh-pdf.sh
```

## Notes

- Do not edit `datasheet.html`; it is generated from `datasheet.adoc`.
- Keep reusable content in `chapters/` and `regs/` to reduce duplication.
- Theme files in `themes/` control layout and styling.

## Tips

- Ask ChatGPT for ASCIIDoc formatting examples when needed.
- Keep the source document concise and reuse included fragments for structured content.


