\
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${ROOT_DIR}/docs/index.adoc"
OUT_DIR="${ROOT_DIR}/build"
THEME="${ROOT_DIR}/docs/pdf-theme/theme.yml"
NOTO_FONT_DIR="/usr/share/fonts/opentype/noto"

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
  -o "${OUT_DIR}/index.pdf" \
  "${SRC}"

echo "PDF written to: ${OUT_DIR}/index.pdf"
