# [MCP Server Name] MCP Server

**Purpose**: [One-line description of MCP server's primary purpose and unique value proposition]

**Source**: Template for creating consistent MCP server documentation

**Usage**: Copy this template and replace all `[VARIABLE]` placeholders with MCP-specific content

---

## Section 1: Purpose and Triggers

```markdown
# [MCP Server Name] MCP Server

**Purpose**: [Detailed description of what this MCP server provides, its unique capabilities, and when it should be used]

## Triggers
- [Trigger pattern 1 - user request patterns that indicate this MCP should be used]
- [Trigger pattern 2 - specific keywords or phrases]
- [Trigger pattern 3 - problem domains or use cases]
- [Trigger pattern 4 - technical requirements or scenarios]
- [Trigger pattern 5 - additional trigger patterns]
```

**Example** (Exa MCP):
```markdown
# Exa MCP Server

**Purpose**: Deep code research, quality examples, and comprehensive web intelligence with AI-powered context retrieval

## Triggers
- Code example requests: "show me code", "example implementation", "how to code"
- Library/framework usage: "using X library", "implement with Y", "code pattern"
- Real-world implementations: "production code", "actual example", "working implementation"
- Company/technology research: "research company", "technology overview", "tech stack"
- Complex topic synthesis: "comprehensive analysis", "deep research", "investigate topic"
```

---

## Section 2: Decision Guidance

```markdown
## Choose When
- **Over [Alternative MCP 1]**: When [specific condition or requirement]
- **Over [Alternative MCP 2]**: When [specific condition or requirement]
- **Over [Alternative MCP 3]**: When [specific condition or requirement]
- **For [Use Case 1]**: When [specific scenario]
- **For [Use Case 2]**: When [specific scenario]

## Works Best With
- **[Complementary MCP 1]**: [How they work together and workflow pattern]
- **[Complementary MCP 2]**: [How they work together and workflow pattern]
- **[Complementary MCP 3]**: [How they work together and workflow pattern]
- **[Complementary MCP 4]**: [How they work together and workflow pattern]
```

**Example** (Exa MCP):
```markdown
## Choose When
- **Over native knowledge**: When you need real, current code examples
- **Over Context7**: When you need actual implementations vs API docs
- **Over Ref**: When you need code examples vs documentation
- **For research**: When gathering intelligence on companies/technologies
- **For synthesis**: When topic requires aggregating multiple perspectives

## Works Best With
- **Ref**: Ref for docs → Exa for code examples
- **Context7**: Context7 for APIs → Exa for implementations
- **Byterover**: Exa finds code → Byterover stores patterns
- **Firecrawl**: Exa for discovery → Firecrawl for deep extraction
```

---

## Section 3: Key Features

```markdown
## Key Features
- **[Feature 1]**: [Description of capability and value]
- **[Feature 2]**: [Description of capability and value]
- **[Feature 3]**: [Description of capability and value]
- **[Feature 4]**: [Description of capability and value]
- **[Feature 5]**: [Description of capability and value]
```

---

## Section 4: Available Tools (DETAILED)

```markdown
## Available Tools

### [tool_name_1]
[One-line description of what this tool does]

**Use for**:
- [Use case 1]
- [Use case 2]
- [Use case 3]
- [Use case 4]

**Parameters**:
- `[param1]` ([required|optional]): [Description and purpose]
- `[param2]` ([required|optional]): [Description, options, defaults]
- `[param3]` ([required|optional]): [Description and constraints]

**Example**:
\```javascript
[tool_name_1]({
  [param1]: \"[example value]\",
  [param2]: [example value]
})
\```

**Returns**: [Description of what the tool returns]

---

### [tool_name_2]
[One-line description of what this tool does]

**Use for**:
- [Use case 1]
- [Use case 2]
- [Use case 3]

**Parameters**:
- `[param1]` ([required|optional]): [Description]
- `[param2]` ([required|optional]): [Description]

**Example**:
\```javascript
[tool_name_2]({
  [param1]: \"[example value]\"
})
\```

**Returns**: [Description of return value]

---

[Repeat for all tools in the MCP server]
```

---

## Section 5: Usage Patterns

```markdown
## Usage Patterns

### Pattern 1: [Pattern Name]
\```yaml
Scenario: [Description of when to use this pattern]

Steps:
  1. [tool_name](params) - [Purpose of this step]
  2. [tool_name](params) - [Purpose of this step]
  3. [tool_name](params) - [Purpose of this step]
  4. [Optional: Additional steps]
  
Best for: [What this pattern is ideal for]
\```

### Pattern 2: [Pattern Name]
\```yaml
Scenario: [Description of when to use this pattern]

Steps:
  1. [tool_name](params) - [Purpose]
  2. [tool_name](params) - [Purpose]
  3. [tool_name](params) - [Purpose]
  
Best for: [What this pattern is ideal for]
\```

### Pattern 3: [Pattern Name]
\```yaml
Scenario: [Description of when to use this pattern]

Steps:
  1. [Action/Tool] - [Purpose]
  2. [Action/Tool] - [Purpose]
  3. [Action/Tool] - [Purpose]
  
Best for: [What this pattern is ideal for]
\```
```

---

## Section 6: Best Practices

```markdown
## Best Practices

### Do's
✅ **[Best Practice 1]**: [Why this is important and when to apply it]
✅ **[Best Practice 2]**: [Why this is important and when to apply it]
✅ **[Best Practice 3]**: [Why this is important and when to apply it]
✅ **[Best Practice 4]**: [Why this is important and when to apply it]

### Don'ts
❌ **[Anti-pattern 1]**: [Why to avoid this and what to do instead]
❌ **[Anti-pattern 2]**: [Why to avoid this and what to do instead]
❌ **[Anti-pattern 3]**: [Why to avoid this and what to do instead]

### Performance Tips
- [Tip 1 for optimal performance]
- [Tip 2 for optimal performance]
- [Tip 3 for optimal performance]
```

---

## Section 7: Integration Notes

```markdown
## Integration Notes

### Memory Integration
**According to ByteRover memory layer**, [MCP Server Name] usage should follow this pattern:

1. **Before Use**: `byterover-retrieve-knowledge` for "[MCP name] best practices"
2. **During Use**: [Specific usage pattern or workflow]
3. **After Use**: `byterover-store-knowledge` with [what to document]

### Common Workflows

**Workflow 1: [Workflow Name]**
\```
[MCP Tool 1] → [MCP Tool 2] → [MCP Tool 3] → ByteRover Storage
\```

**Workflow 2: [Workflow Name]**
\```
ByteRover Check → [MCP Tool] → [Other MCP] → ByteRover Update
\```

### Agent Integration
- **[Agent Name]**: Uses [MCP Server] for [specific purpose]
- **[Agent Name]**: Uses [MCP Server] for [specific purpose]
- **[Agent Name]**: Uses [MCP Server] for [specific purpose]

### Command Integration
- **[Command Name]**: Uses [MCP Server] in [phase/step]
- **[Command Name]**: Uses [MCP Server] for [purpose]
```

---

## Section 8: Troubleshooting

```markdown
## Troubleshooting

### Common Issues

**Issue 1: [Problem Description]**
- **Symptom**: [What the user experiences]
- **Cause**: [Why this happens]
- **Solution**: [How to fix it]

**Issue 2: [Problem Description]**
- **Symptom**: [What the user experiences]
- **Cause**: [Why this happens]
- **Solution**: [How to fix it]

**Issue 3: [Problem Description]**
- **Symptom**: [What the user experiences]
- **Cause**: [Why this happens]
- **Solution**: [How to fix it]

### Error Messages

**Error**: \"[Error message text]\"
- **Meaning**: [What this error indicates]
- **Fix**: [How to resolve]

**Error**: \"[Error message text]\"
- **Meaning**: [What this error indicates]
- **Fix**: [How to resolve]

### Performance Issues

**Slow Response Times**
- Check: [Diagnostic steps]
- Optimize: [Performance improvements]

**Rate Limiting**
- Check: [How to identify]
- Resolve: [How to handle]
```

---

## Section 9: Examples (Optional but Recommended)

```markdown
## Complete Examples

### Example 1: [Scenario Name]
**Goal**: [What we're trying to accomplish]

**Approach**:
\```
1. [First step with tool call]
2. [Second step with tool call]
3. [Third step with tool call]
\```

**Code**:
\```javascript
// Step 1: [Description]
const result1 = [tool_name]({
  param1: "value"
});

// Step 2: [Description]
const result2 = [tool_name]({
  param1: result1.data
});

// Step 3: [Description]
byterover-store-knowledge({
  messages: `Complete findings: ${result2}`
});
\```

**Result**: [What this accomplishes]

---

### Example 2: [Scenario Name]
[Similar structure as Example 1]
```

---

## Variable Substitution Guide

### Required Replacements

| Variable | Description | Example |
|----------|-------------|---------|
| `[MCP Server Name]` | Server name | "Exa", "Firecrawl", "Zen" |
| `[tool_name]` | Actual tool names | "get_code_context_exa", "web_search_exa" |
| `[param1]`, `[param2]` | Parameter names | "query", "tokensNum", "url" |
| `[Feature 1-5]` | Key capabilities | "Dynamic Code Context", "Web Intelligence" |
| `[Use Case 1-4]` | When to use | "Finding real implementations", "Research" |

### Optional Replacements

| Variable | Description | Example |
|----------|-------------|---------|
| `[Alternative MCP]` | Other MCPs | "Context7", "Ref", "native knowledge" |
| `[Complementary MCP]` | MCPs it works with | "Byterover", "Firecrawl", "Ref" |
| `[Agent Name]` | Agents using this | "backend-architect", "deep-research-agent" |
| `[Command Name]` | Commands using this | "research", "analyze", "build" |

---

## Quality Checklist

Before marking MCP documentation as complete:

### Structure
- [ ] All 9 sections present (or justify omissions)
- [ ] Purpose clearly stated
- [ ] Triggers comprehensive and specific

### Tools Documentation
- [ ] All tools documented with descriptions
- [ ] Parameters listed with required/optional status
- [ ] Examples provided for each tool
- [ ] Return values described

### Usage Guidance
- [ ] "Choose When" section helps decide vs alternatives
- [ ] "Works Best With" shows complementary MCPs
- [ ] Usage patterns show real workflows
- [ ] Best practices include do's and don'ts

### Integration
- [ ] Memory integration pattern documented
- [ ] Attribution "According to ByteRover memory layer" present
- [ ] Common workflows with → arrows shown
- [ ] Agent and command integration listed

### Completeness
- [ ] Troubleshooting section covers common issues
- [ ] Examples are complete and runnable
- [ ] All variables replaced (no `[placeholder]` remaining)

---

## Usage Instructions

### Step 1: Research MCP Server
1. Review MCP server documentation
2. Test all available tools
3. Document parameters and return values
4. Identify common use cases

### Step 2: Copy and Customize
1. Copy this template to `SuperClaude/MCP/MCP_[Name].md`
2. Replace `[MCP Server Name]` throughout
3. Document all tools in detail
4. Create usage patterns from real workflows

### Step 3: Add Integration
1. Document memory integration pattern
2. List agents and commands using this MCP
3. Show common tool chains with → arrows
4. Add ByteRover attribution

### Step 4: Validate
- Test all examples
- Verify tool parameters
- Run through checklist
- Validate against ENHANCEMENT_CHECKLIST.md

---

## Template Notes

1. **Section 4 (Tools)** is usually the longest - be thorough
2. **Section 5 (Patterns)** should show real-world workflows
3. **Section 7 (Integration)** must include ByteRover memory pattern
4. **Section 8 (Troubleshooting)** saves users from common pitfalls
5. Use actual code examples, not pseudo-code

---

**Status**: ✅ Ready for use
**Last Updated**: 2025-10-02T19:32:24Z