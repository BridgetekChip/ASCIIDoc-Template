---
name: asciidoc-datasheet-authoring
description: Create, edit, review, and reorganize modular AsciiDoc datasheet or programming-guide repositories that use `datasheet.adoc` style assembly, reusable chapter and register snippets, embedded code examples, and generated HTML/PDF output. Use when Codex is asked to work on `.adoc` files, register-map sections, document conventions, include structure, Asciidoctor build commands, or documentation repos that should avoid hand-editing generated output.
---

# Asciidoc Datasheet Authoring

## Overview

Use this skill to keep AsciiDoc documentation changes consistent, modular, and build-friendly. Prefer small source edits in `.adoc` files, preserve the repository's include-based structure, and treat generated output as a build artifact unless the user explicitly asks otherwise.

## Quick Start

When working in a repo like this one:

1. Read `README.md` and the top-level document such as `datasheet.adoc` to understand the assembly order.
2. Inspect the included source files before editing, especially under `chapters/`, `regs/`, `examples/`, and `images/`.
3. Edit the source fragments, not generated deliverables such as `datasheet.html`, unless the user explicitly requests otherwise.
4. Preserve the current authoring conventions, build flow, and naming style.
5. Rebuild HTML or PDF after meaningful changes when the required tools are available.

## Source Of Truth

Treat these as editable source content:

- `datasheet.adoc` or the repo's main `.adoc` entrypoint
- `chapters/*.adoc` for reusable prose sections and conventions
- `regs/*.adoc` for reusable register descriptions
- `examples/*` for external code samples included into the document
- `images/*` and `themes/*` for assets and output styling

Treat generated files as derived output:

- `datasheet.html`
- generated PDFs
- any generated diagram output unless the repo clearly stores generated diagrams as source

## Editing Rules

Follow these conventions unless the user asks to change them:

- Prefer `include::`-based reuse over duplicating repeated content.
- Keep chapter and register snippets focused and modular.
- Preserve heading depth and `leveloffset` behavior when moving content between files.
- Keep code examples close to runnable and consistent with surrounding prose.
- Match the repository's language and terminology in each file; do not rewrite Chinese sections into English or vice versa unless asked.
- For formulas, prefer AsciiMath and avoid introducing `latexmath` blocks unless the user explicitly wants LaTeX syntax.
- For schematics and line art, prefer SVG references when the repo already follows that pattern.
- Keep register descriptions precise about offsets, reset values, access type, reserved bits, and read-modify-write expectations.

## Register Documentation Pattern

When adding or revising register material, prefer this flow:

1. State base address, offset, access type, and reset value when known.
2. Show the bit layout in a readable table or diagram.
3. Define fields with reset values and behavior.
4. Call out reserved-bit handling explicitly.
5. Include a minimal C example when it helps tie the register description to usage.

Prefer preserving established field naming, bit ranges, and formatting rather than normalizing them to a different house style.

## Build And Verify

Use the repo's documented build commands when available. For this project, the expected commands are:

```bash
asciidoctor -r asciidoctor-diagram -a toc=left -a source-highlighter=rouge datasheet.adoc
asciidoctor-pdf -a pdf-theme=themes/theme.yml datasheet.adoc
./build-zh-pdf.sh
```

After editing:

- Rebuild the relevant output when toolchain support is available.
- Report clearly if a build could not be run because dependencies are missing.
- Mention whether the change affected only source `.adoc` files or also regenerated output.

## Review Checklist

Before finishing, check for:

- broken `include::` paths
- inconsistent heading levels
- accidental edits to generated files
- formulas using LaTeX where the repo expects AsciiMath
- tables or diagrams that no longer match the prose
- register field descriptions that contradict code examples or reset values

## Example Requests

These requests should trigger this skill:

- "Update the conventions chapter to prefer SVG schematics."
- "Add a new register description under `regs/` and include it in the guide."
- "Refactor this long AsciiDoc chapter into reusable includes."
- "Fix the datasheet build after changing headings and code blocks."
- "Review the `.adoc` structure and tell me whether anything violates the writing conventions."
