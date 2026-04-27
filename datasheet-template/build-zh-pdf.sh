#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="${ROOT_DIR}/datasheet.adoc"
OUT_DIR="${ROOT_DIR}/build"
THEME="${ROOT_DIR}/themes/theme-zh.yml"
PDF_FONTS_DIR="/usr/local/share/fonts/noto-cjk-sc;/usr/share/fonts/opentype/noto;GEM_FONTS_DIR"
PDF_OUT="${OUT_DIR}/datasheet.pdf"
PDF_TEMP="${OUT_DIR}/datasheet_tmp.pdf"

export PATH="/usr/local/bundle/bin:${PATH}"

if [[ -z "${DIAGRAM_PLANTUML_CLASSPATH:-}" ]]; then
  DIAGRAM_PLANTUML_CLASSPATH="$(find /usr/local/share/plantuml /usr/share/plantuml -maxdepth 1 -type f -name '*.jar' 2>/dev/null | head -n 1 || true)"
fi

if [[ -z "${DIAGRAM_PLANTUML_CLASSPATH:-}" ]]; then
  echo "PlantUML JAR not found. Set DIAGRAM_PLANTUML_CLASSPATH or install PlantUML in the devcontainer." >&2
  exit 1
fi

if ! command -v phantomjs >/dev/null 2>&1; then
  echo "WaveDrom renderer shim not found. Rebuild the devcontainer image to restore the Chromium-backed renderer." >&2
  exit 1
fi

export DIAGRAM_PLANTUML_CLASSPATH

mkdir -p "${OUT_DIR}"

# PDF build (PNG diagrams)
asciidoctor-pdf --trace\
  -r asciidoctor-diagram \
  -a lang=zh-CN \
  -a scripts=cjk \
  -a encoding=utf-8 \
  -a source-highlighter=rouge \
  -a rouge-style=thankful_eyes \
  -a pdf-theme="${THEME}" \
  -a pdf-fontsdir="${PDF_FONTS_DIR}" \
  -a diagramsdir="${ROOT_DIR}/.diagrams" \
  -a diagram-format=png \
  -a stem=asciimath \
  -o "${PDF_TEMP}" \
  "${SRC}"

# Replace the old PDF with the new one
mv "${PDF_TEMP}" "${PDF_OUT}"

echo "PDF written to: ${PDF_OUT}"
