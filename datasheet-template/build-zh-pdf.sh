#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="${ROOT_DIR}/datasheet.adoc"
OUT_DIR="${ROOT_DIR}/build"
THEME="${ROOT_DIR}/themes/theme-zh.yml"
NOTO_FONT_DIR="/usr/share/fonts/opentype/noto"
PDF_OUT="${OUT_DIR}/datasheet.pdf"
PDF_TEMP="${OUT_DIR}/datasheet_tmp.pdf"

export DIAGRAM_PLANTUML_CLASSPATH="$(dpkg -L plantuml | grep -i '\.jar$' | head -n 1)"

mkdir -p "${OUT_DIR}"

# PDF build (PNG diagrams)
# pdf-fontsdir points to system font directories; adjust if needed.
asciidoctor-pdf --trace\
  -r asciidoctor-diagram \
  -a lang=zh-CN \
  -a encoding=utf-8 \
  -a source-highlighter=rouge \
  -a rouge-style=thankful_eyes \
  -a pdf-theme="${THEME}" \
  -a pdf-fontsdir="${NOTO_FONT_DIR}" \
  -a diagramsdir="${ROOT_DIR}/.diagrams" \
  -a diagram-format=png \
  -a stem=asciimath \
  -o "${PDF_TEMP}" \
  "${SRC}"

# Replace the old PDF with the new one
mv "${PDF_TEMP}" "${PDF_OUT}"

echo "PDF written to: ${PDF_OUT}"