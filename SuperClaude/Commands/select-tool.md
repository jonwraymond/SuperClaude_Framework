---
name: select-tool
description: "Intelligent MCP tool selection based on complexity scoring and operation analysis"
category: utility
complexity: advanced
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena, serena]
personas: []
---

# /sc:select-tool - Intelligent MCP Tool Selection

> **Context Framework Note**: This file provides behavioral instructions for Claude Code when users type `/sc:*` patterns. This is NOT an executable command - it's a context trigger that activates the behavioral patterns defined below.

## Triggers
- Operations requiring optimal MCP tool selection between Serena and Morphllm
- Meta-system decisions needing complexity analysis and capability matching
- Tool routing decisions requiring performance vs accuracy trade-offs
- Operations benefiting from intelligent tool capability assessment

## Usage
```
/sc:select-tool [operation] [--analyze] [--explain]
```

## Behavioral Flow
1. **Parse**: Analyze operation type, scope, file count, and complexity indicators
2. **Score**: Apply multi-dimensional complexity scoring across various operation factors
3. **Match**: Compare operation requirements against Serena and Morphllm capabilities
4. **Select**: Choose optimal tool based on scoring matrix and performance requirements
5. **Validate**: Verify selection accuracy and provide confidence metrics

Key behaviors:
- Complexity scoring based on file count, operation type, language, and framework requirements
- Performance assessment evaluating speed vs accuracy trade-offs for optimal selection
- Decision logic matrix with direct mappings and threshold-based routing rules
- Tool capability matching for Serena (semantic operations) vs Morphllm (pattern operations)

## MCP Integration

### Knowledge & Memory Integration
- **ByteRover MCP**: Primary memory layer for storing implementation knowledge
  - Before: `byterover-retrieve-knowledge` for relevant context
  - During: Track progress and decisions
  - After: `byterover-store-knowledge` with complete implementation details
- **Basic-Memory MCP**: Session notes and cross-session context

### Workflow Integration (per AGENTS.md)
1. **Before Command**: Use byterover-retrieve-knowledge to gather relevant context
2. **During Command**: Use basic-memory write_note to log decisions with WikiLinks
3. **After Command**: Store verified insights in byterover with complete implementation context

```
Before Command:
  → byterover-retrieve-knowledge(query="relevant context")

During Command:
  → Track decisions and progress
  → Document key findings

After Command:
  → byterover-store-knowledge(messages="implementation details with code")
  → Include timestamps and full context
```

- **Serena MCP**: Optimal for semantic operations, LSP functionality, symbol navigation, and project context
- **Morphllm MCP**: Optimal for pattern-based edits, bulk transformations, and speed-critical operations
- **Decision Matrix**: Intelligent routing based on complexity scoring and operation characteristics

## Tool Coordination
- **get_current_config**: System configuration analysis for tool capability assessment
- **execute_sketched_edit**: Operation testing and validation for selection accuracy
- **Read/Grep**: Operation context analysis and complexity factor identification
- **Integration**: Automatic selection logic used by refactor, edit, implement, and improve commands

## Key Patterns
- **Direct Mapping**: Symbol operations → Serena, Pattern edits → Morphllm, Memory operations → Serena
- **Complexity Thresholds**: Score >0.6 → Serena, Score <0.4 → Morphllm, 0.4-0.6 → Feature-based
- **Performance Trade-offs**: Speed requirements → Morphllm, Accuracy requirements → Serena
- **Fallback Strategy**: Serena → Morphllm → Native tools degradation chain

## Examples

### Complex Refactoring Operation
```
/sc:select-tool "rename function across 10 files" --analyze
# Analysis: High complexity (multi-file, symbol operations)
# Selection: Serena MCP (LSP capabilities, semantic understanding)
```

### Pattern-Based Bulk Edit
```
/sc:select-tool "update console.log to logger.info across project" --explain
# Analysis: Pattern-based transformation, speed priority
# Selection: Morphllm MCP (pattern matching, bulk operations)
```

### Memory Management Operation
```
/sc:select-tool "save project context and discoveries"
# Direct mapping: Memory operations → Serena MCP
# Rationale: Project context and cross-session persistence
```

## Boundaries

**Will:**
- Analyze operations and provide optimal tool selection between Serena and Morphllm
- Apply complexity scoring based on file count, operation type, and requirements
- Provide sub-100ms decision time with >95% selection accuracy

**Will Not:**
- Override explicit tool specifications when user has clear preference
- Select tools without proper complexity analysis and capability matching
- Compromise performance requirements for convenience or speed

