#!/bin/bash

# SuperClaude Commands - Final Comprehensive Fixes
# Purpose: Fix all remaining validation issues
# Date: October 2, 2025

set -e

COMMANDS_DIR="SuperClaude/Commands"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}SuperClaude Commands - Final Comprehensive Fixes${NC}"
echo "=================================================="
echo ""

# Fix 1: Replace invalid category 'special' with 'utility'
echo -e "${YELLOW}Fixing invalid categories...${NC}"
for file in estimate index reflect select-tool spawn task; do
    filepath="$COMMANDS_DIR/${file}.md"
    if [ -f "$filepath" ] && grep -q "^category: special" "$filepath"; then
        echo "  → ${file}.md: special → utility"
        sed -i.bak 's/^category: special/category: utility/' "$filepath"
        rm -f "${filepath}.bak"
    fi
done
echo -e "${GREEN}✓ Categories fixed${NC}"
echo ""

# Fix 2: Fix invalid complexity 'high' → 'advanced'
echo -e "${YELLOW}Fixing invalid complexity values...${NC}"
for file in select-tool spawn; do
    filepath="$COMMANDS_DIR/${file}.md"
    if [ -f "$filepath" ] && grep -q "^complexity: high" "$filepath"; then
        echo "  → ${file}.md: high → advanced"
        sed -i.bak 's/^complexity: high/complexity: advanced/' "$filepath"
        rm -f "${filepath}.bak"
    fi
done
echo -e "${GREEN}✓ Complexity values fixed${NC}"
echo ""

# Fix 3: Fix unknown personas
echo -e "${YELLOW}Fixing unknown personas...${NC}"
# performance → performance-engineer
if grep -q "personas:.*performance[^-]" "$COMMANDS_DIR/estimate.md"; then
    echo "  → estimate.md: performance → performance-engineer"
    sed -i.bak 's/\bperformance\b/performance-engineer/g' "$COMMANDS_DIR/estimate.md"
    rm -f "$COMMANDS_DIR/estimate.md.bak"
fi

# scribe and quality → project-manager and qa-specialist
if grep -q "personas:" "$COMMANDS_DIR/index.md"; then
    echo "  → index.md: scribe → project-manager, quality → qa-specialist"
    sed -i.bak -e 's/\bscribe\b/project-manager/g' -e 's/\bquality\b/qa-specialist/g' "$COMMANDS_DIR/index.md"
    rm -f "$COMMANDS_DIR/index.md.bak"
fi
echo -e "${GREEN}✓ Persona names fixed${NC}"
echo ""

# Fix 4: Shorten spec-panel description
echo -e "${YELLOW}Fixing description length...${NC}"
if grep -q "^description:" "$COMMANDS_DIR/spec-panel.md"; then
    echo "  → spec-panel.md: Shortening description"
    sed -i.bak 's/^description: ".*"/description: "Multi-expert specification review with comprehensive analysis"/' "$COMMANDS_DIR/spec-panel.md"
    rm -f "$COMMANDS_DIR/spec-panel.md.bak"
fi
echo -e "${GREEN}✓ Description fixed${NC}"
echo ""

echo -e "${GREEN}=================================================="
echo -e "Final fixes complete!${NC}"
echo ""
echo -e "${YELLOW}Run validation:${NC} python scripts/validate_commands.py --summary"
echo ""
