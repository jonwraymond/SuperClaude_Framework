---
name: command-name                    # Replace with command name (lowercase, hyphenated)
description: "Brief one-sentence description of command purpose"
category: workflow|analysis|documentation|session|utility  # Choose one
complexity: low|basic|standard|advanced  # Choose one
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena]  # Add/remove as needed
personas: []  # Add relevant personas: [architect, frontend, backend, security, qa-specialist, devops, analyzer, project-manager, deep-research-agent, mentor]
---

# /sc:command-name - Command Title

> **Context Framework Note**: Brief explanation of when this command activates and what behavioral patterns it provides. This note helps Claude understand the command's role in the framework.

## Triggers
- Specific use case or scenario 1
- Specific use case or scenario 2
- Specific use case or scenario 3
- Specific use case or scenario 4
- Specific use case or scenario 5

## Usage
```
/sc:command-name [arguments] [--flags] [--options]
```

**Arguments**:
- `[argument1]` - Description of first argument
- `[argument2]` - Description of second argument (optional)

**Common Flags**:
- `--flag1` - Description of flag behavior
- `--flag2` - Description of flag behavior

## Behavioral Flow
1. **Step 1 Name**: Action taken and expected outcome
2. **Step 2 Name**: Action taken and expected outcome
3. **Step 3 Name**: Action taken and expected outcome
4. **Step 4 Name**: Action taken and expected outcome
5. **Step 5 Name**: Action taken and expected outcome

Key behaviors:
- Key behavioral pattern or principle 1
- Key behavioral pattern or principle 2
- Key behavioral pattern or principle 3
- Key behavioral pattern or principle 4

## MCP Integration

### Primary Tools
- **Primary MCP Server 1**: Purpose and usage patterns
- **Primary MCP Server 2**: Purpose and usage patterns
- **Primary MCP Server 3**: Purpose and usage patterns

### Analysis & Reasoning (if applicable)
- **Zen**: Deep reasoning (zen_thinkdeep), code review (zen_codereview), consensus building (zen_consensus)
- **Sequential-thinking**: Multi-step reasoning and structured analysis workflows

### Knowledge & Memory Integration
- **ByteRover**: Retrieve [context type] patterns and store [output type] with timestamps
- **Basic-Memory**: Document [activity type] decisions with WikiLinks in Obsidian

### Research & Documentation (if applicable)
- **Firecrawl**: Advanced web scraping for [specific use case]
- **Tavily**: Real-time web search for [specific information type]
- **Ref**: Search documentation for [specific guidance type]
- **Context7**: Official library/API documentation and code examples
- **Octocode**: GitHub code exploration for [specific pattern type]

### Development Tools (if applicable)
- **Morphllm-fast-apply**: Rapid code edits for [specific transformation type]
- **Cerebras-code**: Comprehensive code generation for [specific feature type]
- **Playwright**: Browser automation for [specific testing/validation type]
- **Magic**: UI component generation for [specific interface type]

### Workflow Integration (per AGENTS.md)
1. **Before [Command Action]**: Use byterover-retrieve-knowledge to gather relevant [context type]:
   - Prior [pattern/solution] implementations
   - Known [issue/challenge] types and solutions
   - Best practices for [domain/technology]
   - Relevant architectural decisions

2. **During [Command Action]**: Use basic-memory write_note to log [activity type] with WikiLinks:
   - Key decisions and rationale
   - Technical challenges encountered
   - Solution approaches explored
   - Implementation patterns used

3. **[Specific Operations]**: Use [specific MCP tools] for [specific purposes]:
   - [Tool name] for [specific action]
   - [Tool name] for [specific analysis]

4. **After [Command Action]**: Store verified [output type] in byterover with complete details:
   - Complete code snippets with context
   - Verified solutions with timestamps
   - Lessons learned and insights
   - Cross-references to related work

## Tool Coordination
- **Read**: [Purpose and usage pattern for this command]
- **Write**: [Purpose and usage pattern for this command]
- **Edit/MultiEdit**: [Purpose and usage pattern for this command]
- **Grep**: [Purpose and usage pattern for this command]
- **Glob**: [Purpose and usage pattern for this command]
- **Bash**: [Purpose and usage pattern for this command]
- **TodoWrite**: [Purpose and usage pattern for this command] (if multi-step)
- **Task**: [Purpose and usage pattern for this command] (if requires delegation)

## Key Patterns
- **Pattern Name 1**: Input → Process → Output description
- **Pattern Name 2**: Input → Process → Output description
- **Pattern Name 3**: Input → Process → Output description
- **Pattern Name 4**: Input → Process → Output description

## Examples

### Example 1: [Descriptive Title]
```
/sc:command-name example-argument --flag
# What this example demonstrates
# Expected outcome and behavior
```

### Example 2: [Descriptive Title]
```
/sc:command-name "complex example" --flag1 --flag2
# What this example demonstrates with multiple flags
# Expected outcome and behavior with combinations
```

### Example 3: [Descriptive Title]
```
/sc:command-name path/to/file --advanced-option
# Advanced usage scenario
# Expected sophisticated behavior and outcomes
```

### Example 4: [Descriptive Title] (Optional but recommended)
```
/sc:command-name --edge-case-scenario
# Edge case or special scenario handling
# Expected behavior in unusual situations
```

### Example 5: [Descriptive Title] (Optional but recommended)
```
/sc:command-name comprehensive-example --all-features
# Comprehensive example showing multiple capabilities
# Expected full-featured behavior demonstration
```

## Boundaries

**Will:**
- Clear statement of what this command does and guarantees
- Another capability or feature provided by the command
- Specific outcomes users can expect from this command
- Quality guarantees or standards this command maintains

**Will Not:**
- Clear limitation or constraint of what command cannot do
- Scenarios or use cases that are explicitly out of scope
- Operations that require user intervention or external tools
- Assumptions or decisions command won't make automatically

---

## Development Notes

### Before Implementation
- [ ] Verify all MCP servers in metadata exist in framework
- [ ] Confirm personas match those available in Agents directory
- [ ] Ensure category and complexity are appropriate
- [ ] Review similar commands for consistency patterns

### Documentation Checklist
- [ ] All required sections present (see README.md)
- [ ] Minimum 3 examples provided (5 recommended)
- [ ] ByteRover workflow integration documented
- [ ] MCP integration patterns clearly explained
- [ ] Boundaries clearly define scope

### Testing Checklist
- [ ] Run validation script: `python scripts/validate_commands.py [filename].md`
- [ ] Test examples in Claude Code environment
- [ ] Verify MCP server integration works as expected
- [ ] Confirm persona activation behaves correctly
- [ ] Validate ByteRover knowledge storage and retrieval

### Integration Checklist
- [ ] Update help.md with new command entry
- [ ] Add command to appropriate category in README.md
- [ ] Create backup (.bak file) of original if updating
- [ ] Test cross-command coordination if applicable
- [ ] Document any new patterns or conventions established

---

## Template Usage Instructions

1. **Copy this template**: `cp TEMPLATE.md new-command.md`
2. **Replace all placeholder text** marked with [brackets] or described above
3. **Delete sections** that don't apply to your command (mark N/A if keeping structure)
4. **Customize MCP Integration** based on command needs
5. **Add minimum 3 examples**, ideally 5 for comprehensive coverage
6. **Validate**: Run `python scripts/validate_commands.py new-command.md`
7. **Review**: Check against Command Quality Checklist in README.md
8. **Test**: Try command in Claude Code with realistic scenarios
9. **Document**: Update help.md and README.md
10. **Submit**: Create PR with validation results and testing notes

## Additional Resources

- **Commands README**: `SuperClaude/Commands/README.md` - Comprehensive standards
- **AGENTS.md**: Framework-level agent and MCP integration patterns  
- **Validation Script**: `scripts/validate_commands.py` - Automated checking
- **Command Quality Checklist**: See README.md for Tier 1/2/3 criteria
- **Example Commands**: Reference `research.md`, `implement.md`, `analyze.md` for best practices

---

**Template Version**: 1.0  
**Last Updated**: October 2, 2025  
**Maintainer**: SuperClaude Framework Team
