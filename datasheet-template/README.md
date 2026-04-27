# ASCIIDoc Datasheet Tutorial Template

This repository is a practical ASCIIDoc tutorial project for software and embedded documentation teams. It shows how to build a structured datasheet or programming guide with reusable chapters, code examples, register descriptions, diagrams, and HTML/PDF output.

It is designed for:

- technical writers building product documentation
- firmware and software engineers documenting registers, interfaces, and examples
- teams that want a small, editable ASCIIDoc project instead of a heavy publishing stack

## What This Project Teaches

The sample document demonstrates how to:

- organize a document with `include::` and reusable chapter files
- write conventions and authoring rules for contributors
- show Python and C code examples
- document register maps and bitfields
- render formulas with AsciiMath
- add WaveDrom timing diagrams
- add PlantUML architecture diagrams
- build HTML and themed PDF output

## Start Here

If you are new to this repository, use this order:

1. Read `README.md` for the project layout and build flow.
2. Open `datasheet.adoc` to see how the tutorial is assembled.
3. Review `chapters/conventions.adoc` for writing rules.
4. Review `chapters/python_code.adoc` for code-example patterns.
5. Review `regs/_ctrl_reg.adoc` for register documentation style.

## Repository Structure

- `datasheet.adoc` - main tutorial-style sample document
- `datasheet.html` - generated HTML output; do not edit directly
- `build-zh-pdf.sh` - helper script for Chinese PDF output
- `chapters/` - reusable chapter fragments
- `examples/` - external code samples included into the document
- `regs/` - reusable register-description snippets
- `images/` - diagrams and image assets
- `themes/` - Asciidoctor PDF theme files

## Quick Preview

In VS Code:

1. Open the project folder.
2. If prompted, reopen in the Dev Container.
3. Open `datasheet.adoc`.
4. Use the AsciiDoc preview extension to inspect the rendered output.

## Build Output

Build HTML:

```bash
asciidoctor -r asciidoctor-diagram -a toc=left -a source-highlighter=rouge datasheet.adoc
```

Build PDF with the default theme:

```bash
asciidoctor-pdf -a pdf-theme=themes/theme.yml datasheet.adoc
```

Build the Chinese PDF variant:

```bash
./build-zh-pdf.sh
```

## Suggested Authoring Workflow

1. Edit `datasheet.adoc` to define the overall structure.
2. Move reusable material into `chapters/` or `regs/`.
3. Keep executable examples in `examples/` and include them into the document.
4. Store diagrams in `images/` and reference them from the document.
5. Rebuild HTML or PDF after each meaningful change.

## Source of Truth

To keep the tutorial maintainable:

- treat `datasheet.adoc` as the assembled source document
- treat files under `chapters/`, `regs/`, and `examples/` as reusable source content
- do not hand-edit `datasheet.html`
- keep sample code as close to runnable as possible

## Writing Guidance

This repository works best when contributors follow a few simple rules:

- prefer short, task-oriented sections over long narrative blocks
- keep naming consistent between prose, code, tables, and diagrams
- use includes for repeated material instead of copy-paste
- prefer SVG for schematics and line art
- prefer AsciiMath for formulas when cross-format portability matters

## Good Next Steps

If you want to evolve this project into a fuller documentation starter kit, the most useful additions are:

- a dedicated `tutorial.adoc` for step-by-step teaching
- a `.gitignore` for generated artifacts
- an author checklist for reviews and release builds
- more sample chapters for admonitions, cross-references, and conditional content

