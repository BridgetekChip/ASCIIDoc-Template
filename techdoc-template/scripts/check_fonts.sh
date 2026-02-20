\
#!/usr/bin/env bash
set -euo pipefail

echo "Looking for Noto CJK fonts..."
fc-list | grep -iE "noto.*cjk" | head -n 50 || true

echo ""
echo "If PDF shows □ boxes or build fails, update:"
echo "  docs/pdf-theme/theme.yml"
echo "with the actual font filenames shown above."
