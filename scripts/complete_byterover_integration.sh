#!/bin/bash

# Complete ByteRover Integration for All Commands
# Updates Workflow Integration section to include 3-step pattern
# Date: October 2, 2025

COMMANDS_DIR="SuperClaude/Commands"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Adding Complete ByteRover Integration${NC}"
echo "========================================="
echo ""

# Counter
count=0

for file in "$COMMANDS_DIR"/*.md; do
    # Skip special files
    if [[ $(basename "$file") == "README.md" ]] || [[ $(basename "$file") == "TEMPLATE.md" ]]; then
        continue
    fi
    
    filename=$(basename "$file")
    
    # Check if file needs update (doesn't have "During.*basic-memory" pattern)
    if ! grep -q "During.*basic-memory" "$file"; then
        echo "Updating $filename..."
        
        # Replace existing Workflow Integration section with complete 3-step pattern
        awk '
        /^### Workflow Integration \(per AGENTS\.md\)/ {
            print "### Workflow Integration (per AGENTS.md)"
            print "1. **Before Command**: Use byterover-retrieve-knowledge to gather relevant context"
            print "2. **During Command**: Use basic-memory write_note to log decisions with WikiLinks"
            print "3. **After Command**: Store verified insights in byterover with complete implementation context"
            print ""
            # Skip until next section or code block
            in_section = 1
            next
        }
        in_section && /^(###|##|```)/ {
            in_section = 0
        }
        !in_section { print }
        ' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
        
        ((count++))
    fi
done

echo ""
echo -e "${GREEN}========================================="
echo -e "Updated $count command files${NC}"
echo ""
echo -e "Run validation: python scripts/validate_commands.py --summary"
echo ""
