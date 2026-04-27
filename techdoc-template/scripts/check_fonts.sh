#!/usr/bin/env bash
set -euo pipefail

echo "Looking for Simplified Chinese PDF fonts..."
fc-list | grep -iE "noto.*cjk" | head -n 50 || true
fc-list | grep -iE "NotoSans(CJKsc|MonoCJKsc).*VF|Noto Sans CJK SC|Noto Sans Mono CJK SC" | head -n 20 || true

echo ""
echo "If PDF shows missing boxes or wrong CJK glyph variants, verify:"
echo "  docs/pdf-theme/theme.yml"
echo "with the actual font filenames shown above."
