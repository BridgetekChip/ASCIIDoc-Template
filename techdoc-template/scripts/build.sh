\
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${ROOT_DIR}/docs/index.adoc"
OUT_DIR="${ROOT_DIR}/build"
CSS_DIR="${ROOT_DIR}/docs/styles"
PDF_THEME_DIR="${ROOT_DIR}/docs/pdf-theme"


export DIAGRAM_PLANTUML_CLASSPATH="$(dpkg -L plantuml | grep -i '\.jar$' | head -n 1)"


mkdir -p "${OUT_DIR}"

# Copy styles to output directory so they're available relative to HTML
cp -r "${CSS_DIR}"/* "${OUT_DIR}/" 2>/dev/null || true

# Copy images to output directory
cp -r "${ROOT_DIR}/docs/images" "${OUT_DIR}/" 2>/dev/null || true

# HTML build (SVG diagrams)
asciidoctor --trace \
  -r asciidoctor-diagram \
  -a icons=font \
  -a source-highlighter=rouge \
  -a rouge-style=github \
  -a lang=zh-CN \
  -a encoding=utf-8 \
  -a stylesheet=asciidoc-style.css \
  -a stylesdir=styles \
  -a linkcss \
  -a diagramsdir="${ROOT_DIR}/.diagrams" \
  -a diagram-format=svg \
  -o "${OUT_DIR}/index.html" \
  "${SRC}"

echo "HTML written to: ${OUT_DIR}/index.html"
