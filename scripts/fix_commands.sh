#!/bin/bash

# SuperClaude Commands - Systematic Validation Fix Script
# Purpose: Fix common validation issues across all command files
# Date: October 2, 2025

set -e

COMMANDS_DIR="SuperClaude/Commands"
BACKUP_DIR=".command_backups_$(date +%Y%m%d_%H%M%S)"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}SuperClaude Commands - Systematic Validation Fix${NC}"
echo "=============================================="
echo ""

# Create backup directory
echo -e "${YELLOW}Creating backup directory: $BACKUP_DIR${NC}"
mkdir -p "$BACKUP_DIR"

# Backup all command files
echo -e "${YELLOW}Backing up command files...${NC}"
cp "$COMMANDS_DIR"/*.md "$BACKUP_DIR/" 2>/dev/null || true
echo -e "${GREEN}✓ Backup complete${NC}"
echo ""

# Function to fix a single command file
fix_command() {
    local file="$1"
    local filename=$(basename "$file")
    
    echo -e "${BLUE}Processing: $filename${NC}"
    
    # Fix 1: Replace "Context Trigger Pattern" with "Usage"
    if grep -q "## Context Trigger Pattern" "$file"; then
        echo "  → Renaming 'Context Trigger Pattern' to 'Usage'"
        sed -i.bak 's/^## Context Trigger Pattern/## Usage/' "$file"
        rm -f "${file}.bak"
    fi
    
    # Fix 2: Add ByteRover integration if missing
    if ! grep -q "byterover-retrieve-knowledge\|byterover-store-knowledge" "$file"; then
        echo "  → Adding ByteRover workflow integration"
        
        # Find the MCP Integration section and add ByteRover subsection
        if grep -q "## MCP Integration" "$file"; then
            # Add after MCP Integration heading
            awk '/^## MCP Integration$/ {
                print
                print ""
                print "### Knowledge & Memory Integration"
                print "- **ByteRover MCP**: Primary memory layer for storing implementation knowledge"
                print "  - Before: `byterover-retrieve-knowledge` for relevant context"
                print "  - During: Track progress and decisions"
                print "  - After: `byterover-store-knowledge` with complete implementation details"
                print "- **Basic-Memory MCP**: Session notes and cross-session context"
                print ""
                print "### Workflow Integration (per AGENTS.md)"
                print "```"
                print "Before Command:"
                print "  → byterover-retrieve-knowledge(query=\"relevant context\")"
                print ""
                print "During Command:"
                print "  → Track decisions and progress"
                print "  → Document key findings"
                print ""
                print "After Command:"
                print "  → byterover-store-knowledge(messages=\"implementation details with code\")"
                print "  → Include timestamps and full context"
                print "```"
                print ""
                next
            }
            { print }' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
        fi
    fi
    
    echo -e "${GREEN}  ✓ Complete${NC}"
}

# Process all command files
echo -e "${YELLOW}Processing command files...${NC}"
echo ""

for file in "$COMMANDS_DIR"/*.md; do
    # Skip special files
    if [[ $(basename "$file") == "README.md" ]] || [[ $(basename "$file") == "TEMPLATE.md" ]]; then
        continue
    fi
    
    fix_command "$file"
done

echo ""
echo -e "${GREEN}=============================================="
echo -e "Fix process complete!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Run validation: python scripts/validate_commands.py --summary"
echo "2. Review changes: git diff SuperClaude/Commands/"
echo "3. Restore backup if needed: cp $BACKUP_DIR/*.md SuperClaude/Commands/"
echo ""
