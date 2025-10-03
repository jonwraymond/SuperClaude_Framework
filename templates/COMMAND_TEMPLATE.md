# [COMMAND_NAME] Template

**Purpose**: Reusable template for creating consistent command documentation across the SuperClaude Framework

**Source**: Extracted from `research.md` (Gold Standard - Tier 1 Exemplary)

**Usage**: Copy this template and replace all `[VARIABLE]` placeholders with command-specific content

---

## Template Structure

```yaml
---
name: [command-name]
aliases: [[command-alias1], [command-alias2]]
description: "[Clear one-line description of command's purpose]"
category: [workflow|analysis|execution|utility|documentation]
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena]
personas: [[agent-name-if-specific]]
---
```

---

## Section 1: Command Header

```markdown
# /sc:[command] - [Command Display Name]

> **Context Framework Note**: [1-2 sentence description of what this command enables]

## Triggers
- [Trigger pattern 1 - when this command should be used]
- [Trigger pattern 2 - specific use cases]
- [Trigger pattern 3 - problem domains]
- [Trigger pattern 4 - requirements or scenarios]

## Context Trigger Pattern
\```
/sc:[command] \"[primary-arg]\" [--option1 value1] [--option2 value2]
\```
```

---

## Section 2: Behavioral Flow

```markdown
## Behavioral Flow

### 1. [Phase 1 Name] ([percentage]% effort)
- [Activity 1 description]
- [Activity 2 description]
- [Activity 3 description]
- [Activity 4 description]

### 2. [Phase 2 Name] ([percentage]% effort)
- [Activity 1 description]
- [Activity 2 description]
- [Activity 3 description]
- [Activity 4 description]

### 3. [Phase 3 Name] ([percentage]% effort)
- [Activity 1 description]
- [Activity 2 description]
- [Activity 3 description]
- [Activity 4 description]

### 4. [Phase 4 Name] ([percentage]% effort)
- **[Key Activity 1]**: [Description with emphasis]
- **[Key Activity 2]**: [Description with emphasis]
- **[Key Activity 3]**: [Description with emphasis]
- **[Key Activity 4]**: [Description with emphasis]

### 5. [Phase 5 Name] (Continuous)
- [Ongoing activity 1]
- [Ongoing activity 2]
- [Ongoing activity 3]
- [Ongoing activity 4]

### 6. [Phase 6 Name] ([percentage]% effort)
- [Final activity 1]
- [Final activity 2]
- [Final activity 3]
- [Final activity 4]
```

---

## Section 3: Key Patterns (Optional)

```markdown
## Key Patterns

### [Pattern Category 1]
- [Pattern detail 1]
- [Pattern detail 2]
- [Pattern detail 3]

### [Pattern Category 2]
- [Pattern detail 1]
- [Pattern detail 2]
- [Pattern detail 3]

### [Pattern Category 3]
- **[Level 1]**: [Description]
- **[Level 2]**: [Description]
- **[Level 3]**: [Description]
- **[Level 4]**: [Description]
```

---

## Section 4: MCP Integration (MANDATORY)

```markdown
## MCP Integration

### Primary [Domain] Tools
- **[MCP Server 1]**: [Purpose and specific use cases]
- **[MCP Server 2]**: [Purpose and specific use cases]
- **[MCP Server 3]**: [Purpose and specific use cases]
- **[MCP Server 4]**: [Purpose and specific use cases]

### Knowledge & Memory
- **ByteRover**: [How ByteRover is used in this command]
- **Basic-Memory**: [How Basic-Memory is used in this command]
- **[Additional Memory Tool]**: [Purpose]

### [Category] & [Category]
- **[MCP Server]**: [Purpose]
- **[MCP Server]**: [Purpose]
- **[MCP Server]**: [Purpose]

### Workflow Integration (MANDATORY - CRITICAL SECTION)
1. **Before [Command]**: Use byterover-retrieve-knowledge to gather [context-type]
2. **During [Command]**: Use basic-memory write_note to log [decision-type] with WikiLinks
3. **[Execution Phase]**: [Key MCP operations] for [specific purpose]
4. **After [Command]**: Store [findings-type] in byterover with timestamps and complete details

**Memory Attribution**: **According to ByteRover memory layer**, all [command-activity] follows this pattern.
```

---

## Section 5: Tool Coordination (Optional - if complex)

```markdown
## Tool Coordination

### [Workflow 1 Name]
\```
[Step 1] → [Step 2] → [Step 3] → [Step 4]
\```

### [Workflow 2 Name]
1. [Tool/Action 1] for [purpose]
2. [Tool/Action 2] for [purpose]
3. [Tool/Action 3] for [purpose]
4. [Tool/Action 4] for [purpose]

### [Workflow 3 Name]
- [Tool chain description] → [Next tool] → [Final tool]
- [Alternative path if needed]
```

---

## Section 6: Output Standards

```markdown
## Output Standards
- [Output requirement 1]
- [Output requirement 2]
- [Output requirement 3]
- [Output requirement 4]
```

---

## Section 7: Examples

```markdown
## Examples
\```
/sc:[command] \"[example 1]\"
/sc:[command] \"[example 2]\" --[option] [value]
/sc:[command] \"[example 3]\" --[option1] [value1] --[option2] [value2]
\```
```

---

## Section 8: Boundaries

```markdown
## Boundaries
**Will**: [Capability 1], [capability 2], [capability 3]
**Won't**: [Exclusion 1], [exclusion 2], [exclusion 3]
```

---

## Variable Substitution Guide

### Required Substitutions

| Variable | Description | Example |
|----------|-------------|---------|
| `[COMMAND_NAME]` | Display name | "Deep Research Command" |
| `[command]` | Lowercase slug | "research", "analyze", "build" |
| `[command-name]` | Kebab case | "deep-research", "code-analyze" |
| `[command-alias]` | Short forms | "r", "search", "investigate" |
| `[primary-arg]` | Main argument | "query", "target", "topic" |
| `[context-type]` | Context needed | "prior research", "design patterns" |
| `[decision-type]` | Decisions logged | "observations", "findings" |
| `[findings-type]` | Results stored | "insights", "analysis", "recommendations" |

### Optional Substitutions

| Variable | Description | Example |
|----------|-------------|---------|
| `[Phase X Name]` | Workflow phase | "Understand", "Execute", "Validate" |
| `[percentage]` | Effort estimate | "5-10", "50-60", "10-15" |
| `[Domain]` | Command domain | "Research", "Analysis", "Build" |
| `[Pattern Category]` | Pattern group | "Parallel Execution", "Evidence Management" |

---

## Quality Checklist

Before marking a command as complete, verify:

### Structure
- [ ] All 8 sections present (Header, Triggers, Behavioral Flow, MCP Integration, Output, Examples, Boundaries)
- [ ] YAML frontmatter complete with all relevant MCP servers
- [ ] Command syntax clearly documented

### MCP Integration (CRITICAL)
- [ ] "Workflow Integration" subsection present
- [ ] Attribution phrase "According to ByteRover memory layer" used
- [ ] Four-phase pattern documented (Before/During/Execution/After)
- [ ] ByteRover and Basic-Memory operations specified
- [ ] Memory operations include context/decision/findings types

### Content Quality
- [ ] byterover and basic-memory listed in frontmatter
- [ ] Memory operations show complete workflow
- [ ] Examples show actual usage patterns
- [ ] Boundaries clearly define scope
- [ ] All sections customized for command purpose

---

## Usage Instructions

### Step 1: Copy Template
```bash
cp templates/COMMAND_TEMPLATE.md SuperClaude/Commands/[command-name].md
```

### Step 2: Replace Variables
1. Update YAML frontmatter (name, aliases, description)
2. Customize MCP server list for command needs
3. Replace all `[VARIABLE]` placeholders
4. Ensure memory attribution present

### Step 3: Customize Workflow Integration
1. Define what context is retrieved (Before)
2. Specify what's logged during execution (During)
3. Detail execution phase MCP usage (Execution)
4. Define what findings are stored (After)

### Step 4: Validate
- Run through Quality Checklist
- Test memory operations
- Verify against ENHANCEMENT_CHECKLIST.md

---

## Example: Converting Template to Actual Command

**Before** (Template):
```markdown
### Workflow Integration (MANDATORY - CRITICAL SECTION)
1. **Before [Command]**: Use byterover-retrieve-knowledge to gather [context-type]
```

**After** (Research Command):
```markdown
### Workflow Integration
1. **Before Research**: Use byterover-retrieve-knowledge to gather prior context
```

---

## Notes

1. **ALWAYS** include "Workflow Integration" subsection in MCP Integration
2. **ALWAYS** include attribution: "According to ByteRover memory layer"
3. **ALWAYS** specify Before/During/Execution/After pattern
4. **ALWAYS** preserve existing command content when enhancing

---

**Status**: ✅ Ready for use
**Last Updated**: 2025-10-02T19:12:00Z