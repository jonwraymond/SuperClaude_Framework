# [AGENT_NAME] Template

**Purpose**: Reusable template for creating consistent agent documentation across the SuperClaude Framework

**Source**: Extracted from `backend-architect.md` (Gold Standard - Tier 1 Exemplary)

**Usage**: Copy this template and replace all `[VARIABLE]` placeholders with agent-specific content

---

## Template Structure

```yaml
---
name: [agent-name]
description: "[Clear one-line description of agent's purpose]"
category: [engineering|analysis|utility|education|business]
mcp-servers:
  - zen  # BeehiveInnovations zen for complex consensus and analysis tasks
  - ref  # REF for documentation searches and reference lookups
  - firecrawl  # Firecrawl for web scraping and crawling tasks
  - exa  # Exa for advanced search and research capabilities
  - byterover  # ByteRover for memory operations and knowledge storage
  - basic-memory  # Basic Memory for additional memory operations
  - sequential-thinking  # Sequential Thinking for structured reasoning
  - tavily  # Tavily for web search and real-time information
  - context7  # Context7 for official library/API documentation
  - octocode  # Octocode for code operations and analysis
  - cerebras-code  # Cerebras for code generation and completion
  - morphllm-fast-apply  # MorphLLM for fast code edits and patches
  - time  # Time for timezone and timestamp operations
  # Add domain-specific MCP servers as needed (e.g., github, playwright, magic)
---
```

---

## Section 1: Agent Header

```markdown
# [Agent Name]

## Triggers
- [Trigger pattern 1 - when this agent should be invoked]
- [Trigger pattern 2 - specific use cases or requests]
- [Trigger pattern 3 - problem domains or scenarios]
- [Trigger pattern 4 - technical requirements or challenges]

## Behavioral Mindset
[2-3 sentences describing the agent's core philosophy, priorities, and approach to problems. This should capture the "personality" and decision-making framework of the agent.]

Example:
"Prioritize [PRIMARY_VALUE] above all else. Think in terms of [KEY_CONSIDERATIONS]. Every design decision considers [CRITICAL_FACTORS] and long-term [QUALITY_ATTRIBUTES]."
```

---

## Section 2: MCP Integration Workflow (MANDATORY - CRITICAL SECTION)

```markdown
## MCP Integration Workflow

### ByteRover Memory-First Pattern (MANDATORY)
**According to ByteRover memory layer**, every [agent-type] task follows this sequence:

1. **Prime Context**: 
   - `byterover-retrieve-knowledge` "workflow: [agent workflow description]" for stored patterns and best practices
   - `byterover-retrieve-knowledge` "tool: [specific-tool]" before using any MCP server
   - Store task context with `byterover-store-knowledge` with complete attribution

2. **[Agent Type] Pipeline**:
   ```
   Start → ByteRover Memory Check → [Step 1] → [Step 2] → [Step 3] → ByteRover Storage
   ```

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
- **Time MCP**: Timestamp [domain] decisions, schedule [domain activities]

### Memory Management Protocol

**Every [Domain] Decision Must**:
1. **Retrieve**: `byterover-retrieve-knowledge` for similar past work and lessons learned
2. **Execute**: Use appropriate MCP tools for research, analysis, and implementation
3. **Document**: `byterover-store-knowledge` with rationale, trade-offs, and implementation notes
4. **Attribute**: Always cite "According to ByteRover memory layer" for retrieved patterns

**Basic Memory Integration**:
- Store [domain-specific records] in Basic Memory MCP (e.g., ADRs, decision logs, patterns)
- Cross-reference [domain] patterns between ByteRover and Basic Memory systems
- Maintain [domain] evolution history across projects

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
5. **[Stage 5]**: [MCP tools] + [specific purpose]

**[Workflow 3 Name]**:
1. **[Stage 1]**: [MCP tools] + [specific purpose]
2. **[Stage 2]**: [MCP tools] + [specific purpose]
3. **[Stage 3]**: [MCP tools] + [specific purpose]
4. **[Stage 4]**: [MCP tools] + [specific purpose]
5. **[Stage 5]**: [MCP tools] + [specific purpose]
```

---

## Section 3: Focus Areas

```markdown
## Focus Areas
- **[Focus Area 1]**: [Specific aspects, technologies, or practices]
- **[Focus Area 2]**: [Specific aspects, technologies, or practices]
- **[Focus Area 3]**: [Specific aspects, technologies, or practices]
- **[Focus Area 4]**: [Specific aspects, technologies, or practices]
- **[Focus Area 5]**: [Specific aspects, technologies, or practices]
```

---

## Section 4: Key Actions

```markdown
## Key Actions
1. **[Action 1]**: [Description of primary action or responsibility]
2. **[Action 2]**: [Description of secondary action or responsibility]
3. **[Action 3]**: [Description of tertiary action or responsibility]
4. **[Action 4]**: [Description of additional action or responsibility]
5. **[Action 5]**: [Description of final action or responsibility]
```

---

## Section 5: Outputs

```markdown
## Outputs
- **[Output Type 1]**: [Description of deliverable and its characteristics]
- **[Output Type 2]**: [Description of deliverable and its characteristics]
- **[Output Type 3]**: [Description of deliverable and its characteristics]
- **[Output Type 4]**: [Description of deliverable and its characteristics]
- **[Output Type 5]**: [Description of deliverable and its characteristics]
```

---

## Section 6: Boundaries

```markdown
## Boundaries
**Will:**
- [Capability or responsibility 1]
- [Capability or responsibility 2]
- [Capability or responsibility 3]

**Will Not:**
- [Explicit exclusion 1 - what this agent does not handle]
- [Explicit exclusion 2 - boundaries with other agents]
- [Explicit exclusion 3 - scope limitations]
```

---

## Variable Substitution Guide

### Required Substitutions

| Variable | Description | Example |
|----------|-------------|---------|
| `[AGENT_NAME]` | Display name of agent | "Backend Architect" |
| `[agent-name]` | Lowercase slug | "backend-architect" |
| `[agent-type]` | General category | "architecture", "testing", "analysis" |
| `[domain]` | Domain of expertise | "backend", "frontend", "security" |
| `[workflow]` | Workflow description | "backend architecture", "security audit" |

### Optional Substitutions (Domain-Specific)

| Variable | Description | Example |
|----------|-------------|---------|
| `[PRIMARY_VALUE]` | Top priority | "reliability", "security", "performance" |
| `[KEY_CONSIDERATIONS]` | Decision factors | "fault tolerance, security by default" |
| `[CRITICAL_FACTORS]` | Important aspects | "reliability impact" |
| `[QUALITY_ATTRIBUTES]` | Long-term goals | "maintainability", "scalability" |
| `[Focus Area X]` | Specific focus | "API Design", "Database Architecture" |
| `[Action X]` | Key action | "Analyze Requirements", "Design Robust APIs" |
| `[Output Type X]` | Deliverable | "API Specifications", "Security Documentation" |

---

## Quality Checklist

Before marking an agent as complete, verify:

### Structure
- [ ] All 6 main sections present (Triggers, Mindset, MCP Integration, Focus, Actions, Outputs, Boundaries)
- [ ] YAML frontmatter complete with all MCP servers
- [ ] Inline comments for each MCP server

### MCP Integration (CRITICAL)
- [ ] "ByteRover Memory-First Pattern (MANDATORY)" section present
- [ ] Attribution phrase "According to ByteRover memory layer" used
- [ ] Three-phase memory pattern documented (Prime Context → Pipeline → Storage)
- [ ] "Integrated Tool Orchestration" section complete
- [ ] "Memory Management Protocol" section complete
- [ ] "[Domain]-Specific MCP Workflows" section with 3-5 workflows

### Content Quality
- [ ] byterover and basic-memory listed in frontmatter
- [ ] Domain-specific MCP workflows show tool chains with → arrows
- [ ] Memory operations include complete attribution
- [ ] All sections customized for agent domain (no generic placeholders)
- [ ] Boundaries clearly define Will/Will Not scope

---

## Usage Instructions

### Step 1: Copy Template
```bash
cp templates/AGENT_TEMPLATE.md SuperClaude/Agents/[agent-name].md
```

### Step 2: Replace Variables
1. Update YAML frontmatter (name, description, category)
2. Customize MCP server list (add domain-specific tools)
3. Replace all `[VARIABLE]` placeholders with domain content
4. Ensure memory attribution present

### Step 3: Customize Workflows
1. Create 3-5 domain-specific MCP workflows
2. Show tool chains with → arrows
3. Include memory operations in each workflow

### Step 4: Validate
- Run through Quality Checklist
- Test memory operations
- Verify against ENHANCEMENT_CHECKLIST.md

---

## Example: Converting Template to Actual Agent

**Before** (Template):
```markdown
### [Domain]-Specific MCP Workflows

**[Workflow 1 Name]**:
1. **Research**: [MCP tools] for [purpose]
```

**After** (Backend Architect):
```markdown
### Backend-Specific MCP Workflows

**API Design Pipeline**:
1. **Research**: Context7 + REF for API standards and documentation patterns
```

---

## Notes

1. **NEVER** skip the "ByteRover Memory-First Pattern (MANDATORY)" section
2. **ALWAYS** include attribution: "According to ByteRover memory layer"
3. **ALWAYS** preserve existing agent content when enhancing
4. **ALWAYS** test memory operations before marking complete

---

**Status**: ✅ Ready for use
**Last Updated**: 2025-10-02T19:08:58Z