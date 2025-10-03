# ORCHESTRATOR.md - SuperClaude Framework Intelligent Routing System

## 🎯 Overview

Intelligent routing system providing comprehensive orchestration capabilities for analyzing codebases, selecting tools, and optimizing workflows with wave-based execution.

**Core Capabilities**:
- Pattern-based tool selection with confidence scoring
- Wave orchestration for complex multi-step operations
- Resource management with dynamic thresholds
- Auto-activation based on context and keywords
- MCP coordination and optimization

---

## 🧠 Detection Engine

### Pre-Operation Validation

**Resource Validation**:
- Token usage prediction (operation complexity + scope)
- Memory and processing requirements estimation
- MCP server availability and response checks
- File system permissions verification

**Compatibility Validation**:
- Tool combination conflict detection
- Persona + command compatibility verification
- MCP availability for requested operations
- Project structure requirements validation

**Risk Assessment**:
- Operation complexity scoring (0.0-1.0 scale)
- Failure probability based on patterns
- Resource exhaustion likelihood
- Cascading failure potential analysis

### Pattern Recognition Rules

#### Complexity Detection

```yaml
simple:
  indicators:
    - single file operations
    - basic queries
    - < 3 step workflows
  token_budget: 5K
  time_estimate: < 5 min
  routing: direct tool selection

moderate:
  indicators:
    - multi-file operations
    - analysis tasks
    - 3-10 step workflows
  token_budget: 15K
  time_estimate: 5-30 min
  routing: coordinated tool sequence

complex:
  indicators:
    - system-wide changes
    - architectural decisions
    - > 10 step workflows
  token_budget: 30K+
  time_estimate: > 30 min
  routing: wave orchestration
```

#### Domain Identification

```yaml
frontend:
  keywords: [UI, component, React, Vue, CSS, responsive, accessibility]
  file_patterns: ["*.jsx", "*.tsx", "*.vue", "*.css", "*.scss"]
  primary_tools: [Magic MCP, playwright, morphllm-fast-apply]
  operations: [create, implement, style, optimize, test]

backend:
  keywords: [API, database, server, endpoint, authentication, performance]
  file_patterns: ["*.js", "*.ts", "*.py", "*.go", "controllers/*", "models/*"]
  primary_tools: [context7, serena, morphllm-fast-apply]
  operations: [implement, optimize, secure, scale]

infrastructure:
  keywords: [deploy, Docker, CI/CD, monitoring, scaling, configuration]
  file_patterns: ["Dockerfile", "*.yml", "*.yaml", ".github/*"]
  primary_tools: [github, serena, context7]
  operations: [setup, configure, automate, monitor]

research:
  keywords: [investigate, research, examples, documentation, patterns]
  file_patterns: ["*.md", "docs/*"]
  primary_tools: [firecrawl, context7, exa, ref, octocode, tavily]
  operations: [search, analyze, document, synthesize]

analysis:
  keywords: [analyze, debug, trace, investigate, review]
  file_patterns: ["*.*"]
  primary_tools: [zen, serena, repomix, sequential-thinking]
  operations: [analyze, debug, trace, review]
```

---

## 🚦 Wave Orchestration Engine

Multi-stage command execution with compound intelligence for complex operations.

### Wave Activation

```yaml
automatic_triggers:
  complexity_threshold: 0.7
  multi_domain: true
  cross_file_operations: > 5
  estimated_time: > 30min
  
explicit_flags:
  - --wave-mode
  - --force-waves
  
override_flags:
  - --single-wave
  - --no-waves
```

### Wave Strategies

**Progressive Enhancement**:
1. **Discovery Wave**: Map codebase, identify patterns
2. **Analysis Wave**: Deep dive into specific areas
3. **Planning Wave**: Create execution strategy
4. **Implementation Wave**: Execute changes
5. **Validation Wave**: Test and verify

**Systematic Analysis**:
1. **Context Gathering**: Collect all relevant information
2. **Pattern Recognition**: Identify recurring themes
3. **Hypothesis Formation**: Develop theories
4. **Testing**: Validate hypotheses
5. **Synthesis**: Combine findings

**Adaptive Configuration**:
- Dynamic wave sizing based on complexity
- Resource-aware wave distribution
- Failure recovery and retry logic
- Progress tracking and reporting

### Wave Configuration

```yaml
wave_settings:
  enable_auto_detection: true
  wave_score_threshold: 0.7
  max_waves_per_operation: 5
  adaptive_wave_sizing: true
  wave_validation_required: true
  parallel_wave_execution: false
  
resource_management:
  token_reserve_per_wave: 10%
  emergency_threshold: 90%
  compression_threshold: 75%
```

---

## 📋 Master Routing Table

| Pattern | Complexity | Primary Tools | Auto-Activates | Confidence |
|---------|------------|---------------|----------------|------------|
| "analyze architecture" | complex | zen (thinkdeep), serena, repomix | architect persona, sequential-thinking | 95% |
| "create component" | simple | Magic MCP, morphllm-fast-apply | frontend persona | 90% |
| "implement feature" | moderate | morphllm-fast-apply, serena, context7 | domain persona, sequential-thinking | 88% |
| "implement API" | moderate | morphllm-fast-apply, context7, serena | backend persona | 92% |
| "implement UI" | simple | Magic MCP, morphllm-fast-apply, playwright | frontend persona | 94% |
| "fix bug" | moderate | zen (debug), serena, sequential-thinking | analyzer persona | 85% |
| "optimize performance" | complex | zen (thinkdeep), playwright, serena | performance persona | 90% |
| "security audit" | complex | zen (thinkdeep), serena | security persona | 95% |
| "write documentation" | moderate | context7, serena, byterover | scribe persona | 95% |
| "research topic" | moderate | firecrawl, exa, ref, tavily, context7 | research persona | 90% |
| "trace execution" | moderate | zen (tracer), serena, repomix | analyzer persona | 88% |
| "code review" | moderate | zen (codereview), serena | qa persona | 92% |

---

## 🔧 Tool Selection Intelligence

### Primary Tool Categories

**Code Generation & Editing**:
- **morphllm-fast-apply**: Fast surgical edits, line-based changes
- **Magic MCP**: UI component generation, design systems
- **serena**: Symbol-based refactoring, code navigation

**Analysis & Investigation**:
- **zen**: Deep reasoning (thinkdeep, debug, codereview, planner)
- **sequential-thinking**: Structured step-by-step reasoning
- **repomix**: Codebase packing and context preparation
- **serena**: Symbol analysis, pattern search

**Research & Documentation**:
- **context7**: Official library/API documentation
- **firecrawl**: Web scraping, site crawling
- **exa**: Deep research, code examples (to be configured)
- **ref**: Documentation search (to be configured)
- **tavily**: Web search
- **octocode**: GitHub code exploration

**Memory & Knowledge**:
- **byterover**: Durable knowledge storage with timestamps
- **basic-memory**: Graph-based Obsidian integration
- **serena**: Project-specific memory

**Testing & Validation**:
- **playwright**: Browser automation, E2E testing, visual testing
- **github**: Repository operations, PR workflows

**Utilities**:
- **time**: Time operations, timezone conversions
- **github**: Version control, deployment coordination

### Tool Coordination Patterns

**Research Workflow**:
```
context7 (official docs) → firecrawl (web) → exa (deep research) → 
ref (specific docs) → octocode (GitHub examples) → 
byterover (store findings)
```

**Code Implementation**:
```
serena (navigation) → context7 (patterns) → 
morphllm-fast-apply (edits) → playwright (test) → 
byterover (store learnings)
```

**Deep Analysis**:
```
repomix (pack) → zen:thinkdeep (analyze) → 
sequential-thinking (plan) → serena (investigate) → 
byterover (document insights)
```

**Complex Feature**:
```
Wave 1: serena + repomix (discovery)
Wave 2: zen:planner + sequential-thinking (planning)
Wave 3: context7 + firecrawl (research)
Wave 4: morphllm-fast-apply + Magic MCP (implementation)
Wave 5: playwright + zen:codereview (validation)
Wave 6: byterover + basic-memory (documentation)
```

---

## 🚨 Resource Management

### Unified Resource Thresholds

- **Green Zone** (0-60%): Full operations, all tools available
- **Yellow Zone** (60-75%): Resource optimization, reduce verbosity
- **Orange Zone** (75-85%): Warning alerts, disable optional features
- **Red Zone** (85-95%): Force efficiency modes, critical only
- **Critical Zone** (95%+): Emergency protocols, essential only

### Graceful Degradation Levels

**Level 1** (Yellow Zone):
- Reduce verbosity and optional enhancements
- Skip non-critical validations
- Use token-efficient symbols

**Level 2** (Orange Zone):
- Disable advanced features
- Simplify operations
- Batch tool calls
- Aggressive compression

**Level 3** (Red Zone):
- Essential operations only
- Maximum compression
- Single tool per operation
- Minimal output

---

## 🎯 MCP Coordination

### Server Optimization

**Context7**:
- Cache documentation lookups (2-5K tokens/query saved)
- Batch similar library queries
- Prefer version-specific searches

**Zen**:
- Reuse reasoning analysis results
- Share context across tool calls
- Use appropriate thinking modes

**Sequential-Thinking**:
- Track thought chains for reuse
- Branch exploration when needed
- Collapse similar reasoning paths

**Magic MCP & Playwright**:
- Store UI component patterns
- Batch operations where possible
- Reuse test scenarios

**Memory Tools (Byterover + Basic Memory)**:
- Parallel retrieval from both systems
- Cross-reference findings
- Deduplicate before storage

---

## 📊 Performance Metrics

### Target Metrics

- **Wave Efficiency**: 30-50% token reduction through batching
- **Tool Selection Accuracy**: >90% confidence in routing
- **Resource Utilization**: <85% average token usage
- **Completion Time**: Within estimated timeframe ±20%
- **Quality Preservation**: ≥95% information retention

### Monitoring

- Real-time token usage tracking
- Wave completion and success rates
- Tool effectiveness per domain
- Resource threshold crossings
- User satisfaction indicators

---

## 🔍 Troubleshooting

### Common Issues

**High Token Usage**:
- Check wave sizing (may be too large)
- Enable compression (--uc flag)
- Review tool selection (redundant calls?)
- Consider splitting into smaller operations

**Slow Performance**:
- Check MCP server availability
- Review tool coordination (sequential vs parallel?)
- Verify wave configuration
- Consider caching opportunities

**Poor Tool Selection**:
- Review pattern matching rules
- Check keyword detection
- Verify persona activation
- Update routing table confidence scores

**Wave Execution Failures**:
- Check resource thresholds
- Review wave dependencies
- Verify tool availability
- Check for cascading failures

---

**Version**: 5.0 (SuperClaude Framework Full Transformation)
**Last Updated**: 2025-10-02
**Status**: Production Ready
