#!/bin/bash

# Batch update script for SuperClaude Commands MCP integration
# Updates all command files to include comprehensive MCP server integration per AGENTS.md

COMMAND_DIR="SuperClaude/Commands"
COMPLETE_MCP_LIST="zen, byterover, basic-memory, sequential-thinking, context7, ref, firecrawl, octocode, serena, playwright, tavily"

echo "Updating SuperClaude Commands with comprehensive MCP integration..."

# Define MCP integration template
MCP_INTEGRATION_TEMPLATE='
## MCP Integration

### Core Tools
- **Zen**: Deep reasoning (zen_thinkdeep), systematic analysis (zen_codereview), consensus building (zen_consensus)
- **Sequential-thinking**: Multi-step workflows and structured problem-solving
- **Serena**: Semantic code understanding, project memory, and symbol operations
- **Playwright**: Browser automation and E2E testing validation

### Knowledge & Memory Integration
- **ByteRover**: Retrieve relevant patterns and store verified insights with timestamps
- **Basic-Memory**: Document decisions and patterns with WikiLinks in Obsidian graph

### Research & Documentation
- **Context7**: Official framework documentation and best practices
- **Ref**: Search documentation across web/github repositories
- **Firecrawl**: Advanced web scraping and content extraction (preferred for all web tasks)
- **Octocode**: GitHub code exploration and repository analysis
- **Tavily**: Web search with real-time information retrieval

### Workflow Integration (per AGENTS.md)
1. **Before Task**: Use byterover-retrieve-knowledge to gather relevant context
2. **During Task**: Use basic-memory write_note to log observations with WikiLinks
3. **Analysis**: Use zen tools for deep reasoning and systematic analysis
4. **Research**: Use firecrawl/ref/context7 for documentation and examples
5. **After Task**: Store verified patterns in byterover with complete details
'

# Update files with empty MCP servers
echo "Updating commands with empty MCP server lists..."
for file in $(grep -l "mcp-servers: \[\]" $COMMAND_DIR/*.md); do
    echo "Updating $(basename $file)..."
    sed -i.bak "s/mcp-servers: \[\]/mcp-servers: [$COMPLETE_MCP_LIST]/" "$file"
    
    # Add MCP Integration section if Tool Coordination exists
    if grep -q "## Tool Coordination" "$file"; then
        # Insert MCP integration section before Tool Coordination
        sed -i.bak "/## Tool Coordination/i\\
$MCP_INTEGRATION_TEMPLATE" "$file"
    fi
done

echo "Command MCP integration update complete!"
echo "Updated files can be found with .bak backups for safety"