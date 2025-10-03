#!/bin/bash

# SuperClaude Commands - Phase 2 Validation Fixes
# Purpose: Fix metadata and structural issues
# Date: October 2, 2025

set -e

COMMANDS_DIR="SuperClaude/Commands"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}SuperClaude Commands - Phase 2 Fixes${NC}"
echo "======================================"
echo ""

# Fix 1: Replace invalid complexity values
echo -e "${YELLOW}Fixing complexity values...${NC}"
for file in "$COMMANDS_DIR"/*.md; do
    if grep -q "^complexity: enhanced" "$file"; then
        filename=$(basename "$file")
        echo "  → $filename: enhanced → advanced"
        sed -i.bak 's/^complexity: enhanced/complexity: advanced/' "$file"
        rm -f "${file}.bak"
    fi
done
echo -e "${GREEN}✓ Complexity values fixed${NC}"
echo ""

# Fix 2: Add serena to mcp-servers if missing
echo -e "${YELLOW}Adding missing core MCP servers...${NC}"
for file in "$COMMANDS_DIR"/*.md; do
    if ! grep -q "serena" "$file" | grep -q "mcp-servers"; then
        filename=$(basename "$file")
        # Add serena to mcp-servers list
        sed -i.bak '/^mcp-servers:/ s/\]/, serena]/' "$file"
        echo "  → $filename: Added serena to mcp-servers"
        rm -f "${file}.bak"
    fi
done
echo -e "${GREEN}✓ Core servers added${NC}"
echo ""

# Fix 3: Fix known invalid personas
echo -e "${YELLOW}Fixing persona names...${NC}"
for file in "$COMMANDS_DIR"/*.md; do
    if grep -q "devops-engineer" "$file"; then
        filename=$(basename "$file")
        echo "  → $filename: devops-engineer → devops"
        sed -i.bak 's/devops-engineer/devops/g' "$file"
        rm -f "${file}.bak"
    fi
    if grep -q "qa-engineer" "$file"; then
        filename=$(basename "$file")
        echo "  → $filename: qa-engineer → qa-specialist"
        sed -i.bak 's/qa-engineer/qa-specialist/g' "$file"
        rm -f "${file}.bak"
    fi
done
echo -e "${GREEN}✓ Persona names fixed${NC}"
echo ""

# Fix 4: Add Context Framework Note if missing
echo -e "${YELLOW}Adding Context Framework Notes...${NC}"
for file in "$COMMANDS_DIR"/*.md; do
    if ! grep -q "> \*\*Context Framework Note\*\*:" "$file"; then
        filename=$(basename "$file")
        # Find the command header line and add note after it
        awk '/^# \/sc:/ {
            print
            print ""
            print "> **Context Framework Note**: This file provides behavioral instructions for Claude Code when users type `/sc:*` patterns. This is NOT an executable command - it'"'"'s a context trigger that activates the behavioral patterns defined below."
            next
        }
        { print }' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
        echo "  → $filename: Added Context Framework Note"
    fi
done
echo -e "${GREEN}✓ Context Framework Notes added${NC}"
echo ""

echo -e "${GREEN}======================================"
echo -e "Phase 2 fixes complete!${NC}"
echo ""
echo -e "${YELLOW}Run validation:${NC} python scripts/validate_commands.py --summary"
echo ""
