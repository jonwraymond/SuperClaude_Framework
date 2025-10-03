---
name: research
description: Deep web research with adaptive planning and intelligent search
category: command
complexity: advanced
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena, playwright, serena]
personas: [deep-research-agent]
---

# /sc:research - Deep Research Command

> **Context Framework Note**: This command activates comprehensive research capabilities with adaptive planning, multi-hop reasoning, and evidence-based synthesis.

## Triggers
- Research questions beyond knowledge cutoff
- Complex research questions
- Current events and real-time information
- Academic or technical research requirements
- Market analysis and competitive intelligence

## Usage
```
/sc:research "[query]" [--depth quick|standard|deep|exhaustive] [--strategy planning|intent|unified]
```

## Behavioral Flow

### 1. Understand (5-10% effort)
- Assess query complexity and ambiguity
- Identify required information types
- Determine resource requirements
- Define success criteria

### 2. Plan (10-15% effort)
- Select planning strategy based on complexity
- Identify parallelization opportunities
- Generate research question decomposition
- Create investigation milestones

### 3. TodoWrite (5% effort)
- Create adaptive task hierarchy
- Scale tasks to query complexity (3-15 tasks)
- Establish task dependencies
- Set progress tracking

### 4. Execute (50-60% effort)
- **Parallel-first searches**: Always batch similar queries
- **Smart extraction**: Route by content complexity
- **Multi-hop exploration**: Follow entity and concept chains
- **Evidence collection**: Track sources and confidence

### 5. Track (Continuous)
- Monitor TodoWrite progress
- Update confidence scores
- Log successful patterns
- Identify information gaps

### 6. Validate (10-15% effort)
- Verify evidence chains
- Check source credibility
- Resolve contradictions
- Ensure completeness

## Key Patterns

### Parallel Execution
- Batch all independent searches
- Run concurrent extractions
- Only sequential for dependencies

### Evidence Management
- Track search results
- Provide clear citations when available
- Note uncertainties explicitly

### Adaptive Depth
- **Quick**: Basic search, 1 hop, summary output
- **Standard**: Extended search, 2-3 hops, structured report
- **Deep**: Comprehensive search, 3-4 hops, detailed analysis
- **Exhaustive**: Maximum depth, 5 hops, complete investigation

## MCP Integration

### Primary Research Tools
- **Firecrawl**: Advanced web scraping and content extraction (preferred for all web tasks)
- **Tavily**: Web search with real-time information retrieval
- **Zen**: Deep reasoning, consensus building, and systematic analysis (zen_thinkdeep, zen_consensus)
- **Sequential-thinking**: Multi-step reasoning and structured analysis workflows

### Knowledge & Memory
- **ByteRover**: Retrieve prior research patterns and store new insights with timestamps
- **Basic-Memory**: Create research notes with WikiLinks and tags in Obsidian graph
- **Context7**: Official library/API documentation and code examples

### Code & Documentation
- **Ref**: Search documentation across web/github repositories
- **Octocode**: GitHub code exploration and repository analysis
- **Playwright**: Browser automation for JavaScript-heavy content extraction
- **Serena**: Research session persistence and project memory

### Workflow Integration
1. **Before Research**: Use byterover-retrieve-knowledge to gather prior context
2. **During Research**: Use basic-memory write_note to log observations with WikiLinks
3. **Web Content**: Prefer firecrawl over curl for all web scraping needs
4. **Deep Analysis**: Use zen_thinkdeep for complex reasoning and synthesis
5. **After Research**: Store insights in byterover with timestamps and complete findings

## Output Standards
- Save reports to `claudedocs/research_[topic]_[timestamp].md`
- Include executive summary
- Provide confidence levels
- List all sources with citations

## Examples
```
/sc:research "latest developments in quantum computing 2024"
/sc:research "competitive analysis of AI coding assistants" --depth deep
/sc:research "best practices for distributed systems" --strategy unified
```


## Tool Coordination
- **Read/Write/Edit**: File operations and content management
- **TodoWrite**: Progress tracking for multi-step operations  
- **Task**: Parallel execution and delegation
- **WebSearch**: Research and external information gathering


## Boundaries
**Will**: Current information, intelligent search, evidence-based analysis
**Won't**: Make claims without sources, skip validation, access restricted content