# Memory Integration Blocks

**Purpose**: Reusable memory integration code blocks for consistent implementation across agents and commands

**Sources**: Extracted from backend-architect.md and research.md (Gold Standard files)

**Usage**: Copy-paste these blocks into agent/command files, then customize variables

---

## Block 1: Agent Memory-First Pattern Header

**Location**: Insert after "## MCP Integration Workflow" heading in agents

**Variables to Replace**:
- `[agent-type]` → e.g., "backend architecture", "security audit", "performance analysis"
- `[workflow]` → e.g., "backend architecture", "security audit", "frontend design"
- `[Agent Type]` → e.g., "Architecture", "Security", "Performance"
- `[Step 1]`, `[Step 2]`, `[Step 3]` → Pipeline steps

```markdown
### ByteRover Memory-First Pattern (MANDATORY)
**According to ByteRover memory layer**, every [agent-type] task follows this sequence:

1. **Prime Context**: 
   - `byterover-retrieve-knowledge` "workflow: [workflow]" for stored patterns and best practices
   - `byterover-retrieve-knowledge` "tool: [specific-tool]" before using any MCP server
   - Store task context with `byterover-store-knowledge` with complete attribution

2. **[Agent Type] Pipeline**:
   ```
   Start → ByteRover Memory Check → [Step 1] → [Step 2] → [Step 3] → ByteRover Storage
   ```
```

**Example** (Backend Architect):
```markdown
### ByteRover Memory-First Pattern (MANDATORY)
**According to ByteRover memory layer**, every backend architecture task follows this sequence:

1. **Prime Context**: 
   - `byterover-retrieve-knowledge` "workflow: backend architecture" for stored patterns and best practices
   - `byterover-retrieve-knowledge` "tool: [specific-tool]" before using any MCP server
   - Store task context with `byterover-store-knowledge` with complete attribution

2. **Architecture Pipeline**:
   ```
   Start → ByteRover Memory Check → Requirements Analysis → Design → Implementation → ByteRover Storage
   ```
```

---

## Block 2: Agent Memory Management Protocol

**Location**: Insert after "Integrated Tool Orchestration" section in agents

**Variables to Replace**:
- `[Domain]` → e.g., "Architecture", "Security", "Testing", "Performance"
- `[domain]` → e.g., "architecture", "security", "testing"
- `[domain-specific records]` → e.g., "architectural decision records (ADRs)", "security audit reports"

```markdown
### Memory Management Protocol

**Every [Domain] Decision Must**:
1. **Retrieve**: `byterover-retrieve-knowledge` for similar past work and lessons learned
2. **Execute**: Use appropriate MCP tools for research, analysis, and implementation
3. **Document**: `byterover-store-knowledge` with rationale, trade-offs, and implementation notes
4. **Attribute**: Always cite "According to ByteRover memory layer" for retrieved patterns

**Basic Memory Integration**:
- Store [domain-specific records] in Basic Memory MCP
- Cross-reference [domain] patterns between ByteRover and Basic Memory systems
- Maintain [domain] evolution history across projects
```

**Example** (Backend Architect):
```markdown
### Memory Management Protocol

**Every Architecture Decision Must**:
1. **Retrieve**: `byterover-retrieve-knowledge` for similar past designs and lessons learned
2. **Design**: Use appropriate MCP tools for research, analysis, and implementation
3. **Document**: `byterover-store-knowledge` with design rationale, trade-offs, and implementation notes
4. **Attribute**: Always cite "According to ByteRover memory layer" for retrieved architectural patterns

**Basic Memory Integration**:
- Store architectural decision records (ADRs) in Basic Memory MCP
- Cross-reference design patterns between ByteRover and Basic Memory systems
- Maintain architecture evolution history across projects
```

---

## Block 3: Agent Domain-Specific Workflows Template

**Location**: Insert after "Memory Management Protocol" section in agents

**Variables to Replace**:
- `[Domain]` → e.g., "Backend", "Frontend", "Security"
- `[Workflow 1-5 Name]` → Specific workflow names
- `[Stage 1-5]` → Workflow stages
- `[MCP tools]` → Specific MCP servers used
- `[purpose]` → What each stage accomplishes
- `[artifacts]` → What gets documented

```markdown
### [Domain]-Specific MCP Workflows

**[Workflow 1 Name]**:
1. **Research**: [MCP tools] for [purpose]
2. **Analysis**: [MCP tools] for [purpose]
3. **Implementation**: [MCP tools] for [purpose]
4. **Validation**: [MCP tools] for [purpose]
5. **Documentation**: Store complete [artifacts] via ByteRover

**[Workflow 2 Name]**:
1. **[Stage 1]**: [MCP tools] + [specific purpose]
2. **[Stage 2]**: [MCP tools] + [specific purpose]
3. **[Stage 3]**: [MCP tools] + [specific purpose]
4. **[Stage 4]**: [MCP tools] + [specific purpose]
5. **[Stage 5]**: Store [findings] via ByteRover

**[Workflow 3 Name]**:
1. **[Stage 1]**: [MCP tools] for [purpose]
2. **[Stage 2]**: [MCP tools] for [purpose]
3. **[Stage 3]**: [MCP tools] for [purpose]
4. **[Stage 4]**: [MCP tools] for [purpose]
5. **[Stage 5]**: Complete [activity] stored via ByteRover
```

**Example** (Backend Architect - API Design):
```markdown
### Backend-Specific MCP Workflows

**API Design Pipeline**:
1. **Research**: Context7 + REF for API standards and documentation patterns
2. **Analysis**: Sequential Thinking for endpoint design and error handling strategy
3. **Implementation**: Cerebras for code generation + Octocode for existing code analysis
4. **Validation**: Zen for stakeholder consensus on API contracts
5. **Documentation**: Store complete API specifications via ByteRover
```

---

## Block 4: Command Workflow Integration

**Location**: Insert as subsection under "## MCP Integration" in commands

**Variables to Replace**:
- `[Command]` → e.g., "Research", "Analyze", "Build"
- `[context-type]` → e.g., "prior research", "design patterns", "project history"
- `[decision-type]` → e.g., "observations", "findings", "architectural decisions"
- `[Key MCPs]` → Specific MCP servers used in execution
- `[specific purpose]` → What the MCPs are used for
- `[findings-type]` → e.g., "insights", "analysis results", "recommendations"
- `[command-activity]` → e.g., "research", "analysis", "implementation"

```markdown
### Workflow Integration
1. **Before [Command]**: Use byterover-retrieve-knowledge to gather [context-type]
2. **During [Command]**: Use basic-memory write_note to log [decision-type] with WikiLinks
3. **[Execution Phase]**: Use [Key MCPs] for [specific purpose]
4. **After [Command]**: Store [findings-type] in byterover with timestamps and complete details

**Memory Attribution**: **According to ByteRover memory layer**, all [command-activity] follows this pattern.
```

**Example** (Research Command):
```markdown
### Workflow Integration
1. **Before Research**: Use byterover-retrieve-knowledge to gather prior context
2. **During Research**: Use basic-memory write_note to log observations with WikiLinks
3. **Web Content**: Prefer firecrawl over curl for all web scraping needs
4. **Deep Analysis**: Use zen_thinkdeep for complex reasoning and synthesis
5. **After Research**: Store insights in byterover with timestamps and complete findings

**Memory Attribution**: **According to ByteRover memory layer**, all research follows this pattern.
```

---

## Block 5: Integrated Tool Orchestration Template

**Location**: Insert after "ByteRover Memory-First Pattern" in agents

**Variables to Replace**:
- `[Domain]` → e.g., "Backend", "Security", "Frontend"
- `[Activity]` → e.g., "Design", "Analysis", "Implementation"
- `[domain-specific]` → e.g., "API design", "threat modeling"
- `[domain activity]` → e.g., "schema design", "security assessment"
- `[domain challenge]` → e.g., "architecture planning", "vulnerability analysis"
- `[domain-specific docs]` → e.g., "database documentation", "security frameworks"
- `[domain topics]` → e.g., "scaling patterns", "threat vectors"
- `[domain benchmarks]` → e.g., "performance benchmarks", "security metrics"
- `[domain implementations]` → e.g., "API implementations", "security controls"
- `[domain code artifacts]` → e.g., "endpoints", "security policies"
- `[domain]` → e.g., "backend", "security"
- `[domain decisions]` → e.g., "architecture decisions", "security controls"
- `[domain activities]` → e.g., "deployment windows", "audit schedules"

```markdown
### Integrated Tool Orchestration

**Sequential Thinking for [Domain] [Activity]**:
- Use `sequential-thinking` MCP for systematic [domain-specific] decisions
- Structure [domain activity] analysis through methodical reasoning
- Apply for complex [domain challenge] planning

**Research & Documentation**:
- **Context7 MCP**: Official framework documentation, API specifications, [domain-specific docs]
- **REF MCP**: [Domain] pattern references, industry standards, [domain-specific] documentation
- **Exa MCP**: Research on [domain topics], [domain benchmarks], [domain] case studies
- **Firecrawl MCP**: Extract specific technical documentation, [domain-specific] examples

**Code Operations & Analysis** (if applicable):
- **Octocode MCP**: Analyze existing [domain] codebases, [domain implementations], [domain queries]
- **Cerebras MCP**: Generate [domain code artifacts], [domain models], configuration files
- **MorphLLM MCP**: Apply code changes, refactor existing implementations

**Consensus & Complex Decisions**:
- **Zen MCP**: Multi-stakeholder [domain] decisions, technology selection consensus
- **Tavily MCP**: Current technology trends, [domain] comparisons, industry best practices

**Infrastructure & Operations** (if applicable):
- **Time MCP**: Timestamp [domain decisions], schedule [domain activities]
```

---

## Quick Reference Guide

### For Agents - Required Blocks (in order):

1. **Block 1**: Memory-First Pattern Header
2. **Block 5**: Integrated Tool Orchestration
3. **Block 2**: Memory Management Protocol
4. **Block 3**: Domain-Specific Workflows (3-5 workflows)

### For Commands - Required Block:

- **Block 4**: Workflow Integration (under MCP Integration section)

---

## Variable Substitution Quick Reference

### Agent Variables

| Variable | Category | Example Values |
|----------|----------|----------------|
| `[agent-type]` | Type | "backend architecture", "security audit" |
| `[Domain]` | Capitalized | "Architecture", "Security", "Testing" |
| `[domain]` | Lowercase | "architecture", "security", "testing" |
| `[workflow]` | Process | "backend architecture", "security audit" |
| `[Stage 1-5]` | Steps | "Research", "Analysis", "Implementation" |

### Command Variables

| Variable | Category | Example Values |
|----------|----------|----------------|
| `[Command]` | Capitalized | "Research", "Analyze", "Build" |
| `[context-type]` | Input | "prior research", "design patterns" |
| `[decision-type]` | Logging | "observations", "findings" |
| `[findings-type]` | Output | "insights", "analysis results" |
| `[command-activity]` | Activity | "research", "analysis" |

---

## Quality Validation

### Agent Block Checklist

- [ ] Block 1 (Memory-First Pattern) present with attribution
- [ ] Block 5 (Tool Orchestration) present with domain customization
- [ ] Block 2 (Memory Protocol) present with domain records specified
- [ ] Block 3 (Domain Workflows) present with 3-5 workflows
- [ ] All blocks use "According to ByteRover memory layer"
- [ ] All workflow arrows use → symbol
- [ ] All variables replaced (no `[placeholder]` remaining)

### Command Block Checklist

- [ ] Block 4 (Workflow Integration) present
- [ ] Before/During/Execution/After pattern complete
- [ ] Attribution phrase "According to ByteRover memory layer" present
- [ ] ByteRover and Basic-Memory operations specified
- [ ] All variables replaced (no `[placeholder]` remaining)

---

## Usage Example - Complete Agent Enhancement

**Starting Point**: Agent with no memory integration

**Step 1**: Add Block 1 after "## MCP Integration Workflow"
```markdown
## MCP Integration Workflow

### ByteRover Memory-First Pattern (MANDATORY)
[Block 1 content with variables replaced]
```

**Step 2**: Add Block 5 for tool orchestration
```markdown
### Integrated Tool Orchestration
[Block 5 content with domain customization]
```

**Step 3**: Add Block 2 for protocol
```markdown
### Memory Management Protocol
[Block 2 content with domain specifics]
```

**Step 4**: Add Block 3 for workflows
```markdown
### [Domain]-Specific MCP Workflows
[Block 3 content with 3-5 actual workflows]
```

**Result**: Fully enhanced agent with complete memory integration

---

## Usage Example - Complete Command Enhancement

**Starting Point**: Command with basic MCP Integration

**Enhancement**: Add Block 4 under "## MCP Integration"
```markdown
## MCP Integration

### Primary Research Tools
[Existing content...]

### Knowledge & Memory
[Existing content...]

### Workflow Integration
[Block 4 content with variables replaced]
```

**Result**: Command with complete memory workflow

---

## Tips for Success

1. **Always start with Block 1** - It sets the foundation
2. **Customize, don't copy** - Replace ALL variables
3. **Be specific** - Use concrete domain terms, not generic placeholders
4. **Show tool chains** - Use → arrows for workflow clarity
5. **Test attribution** - Ensure "According to ByteRover memory layer" appears
6. **3-5 workflows minimum** - For Block 3 in agents

---

**Status**: ✅ Ready for use
**Last Updated**: 2025-10-02T19:32:24Z