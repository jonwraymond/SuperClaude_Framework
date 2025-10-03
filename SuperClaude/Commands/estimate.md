---
name: estimate
description: "Provide development estimates for tasks, features, or projects with intelligent analysis"
category: utility
complexity: standard
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena]
personas: [architect, performance, project-manager]
---

# /sc:estimate - Development Estimation

> **Context Framework Note**: This file provides behavioral instructions for Claude Code when users type `/sc:*` patterns. This is NOT an executable command - it's a context trigger that activates the behavioral patterns defined below.

## Triggers
- Development planning requiring time, effort, or complexity estimates
- Project scoping and resource allocation decisions
- Feature breakdown needing systematic estimation methodology
- Risk assessment and confidence interval analysis requirements

## Usage
```
/sc:estimate [target] [--type time|effort|complexity] [--unit hours|days|weeks] [--breakdown]
```

## Behavioral Flow
1. **Analyze**: Examine scope, complexity factors, dependencies, and framework patterns
2. **Calculate**: Apply estimation methodology with historical benchmarks and complexity scoring
3. **Validate**: Cross-reference estimates with project patterns and domain expertise
4. **Present**: Provide detailed breakdown with confidence intervals and risk assessment
5. **Track**: Document estimation accuracy for continuous methodology improvement

Key behaviors:
- Multi-persona coordination (architect, performance, project-manager) based on estimation scope
- Sequential MCP integration for systematic analysis and complexity assessment
- Context7 MCP integration for framework-specific patterns and historical benchmarks
- Intelligent breakdown analysis with confidence intervals and risk factors

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

- **Sequential MCP**: Complex multi-step estimation analysis and systematic complexity assessment
- **Context7 MCP**: Framework-specific estimation patterns and historical benchmark data
- **Persona Coordination**: Architect (design complexity), Performance (optimization effort), Project Manager (timeline)

## Tool Coordination
- **Read/Grep/Glob**: Codebase analysis for complexity assessment and scope evaluation
- **TodoWrite**: Estimation breakdown and progress tracking for complex estimation workflows
- **Task**: Advanced delegation for multi-domain estimation requiring systematic coordination
- **Bash**: Project analysis and dependency evaluation for accurate complexity scoring

## Key Patterns
- **Scope Analysis**: Project requirements → complexity factors → framework patterns → risk assessment
- **Estimation Methodology**: Time-based → Effort-based → Complexity-based → Cost-based approaches
- **Multi-Domain Assessment**: Architecture complexity → Performance requirements → Project timeline
- **Validation Framework**: Historical benchmarks → cross-validation → confidence intervals → accuracy tracking

## Examples

### Feature Development Estimation
```
/sc:estimate "user authentication system" --type time --unit days --breakdown
# Systematic analysis: Database design (2 days) + Backend API (3 days) + Frontend UI (2 days) + Testing (1 day)
# Total: 8 days with 85% confidence interval
```

### Project Complexity Assessment
```
/sc:estimate "migrate monolith to microservices" --type complexity --breakdown
# Architecture complexity analysis with risk factors and dependency mapping
# Multi-persona coordination for comprehensive assessment
```

### Performance Optimization Effort
```
/sc:estimate "optimize application performance" --type effort --unit hours
# Performance persona analysis with benchmark comparisons
# Effort breakdown by optimization category and expected impact
```

## Boundaries

**Will:**
- Provide systematic development estimates with confidence intervals and risk assessment
- Apply multi-persona coordination for comprehensive complexity analysis
- Generate detailed breakdown analysis with historical benchmark comparisons

**Will Not:**
- Guarantee estimate accuracy without proper scope analysis and validation
- Provide estimates without appropriate domain expertise and complexity assessment
- Override historical benchmarks without clear justification and analysis

