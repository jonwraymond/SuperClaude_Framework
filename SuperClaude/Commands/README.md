# SuperClaude Commands Directory

**Version**: 4.2.0+  
**Last Updated**: October 2, 2025  
**Maintainers**: SuperClaude Framework Team

---

## Overview

The Commands directory contains the complete SuperClaude command interface - behavioral instructions that activate when users type `/sc:` patterns in Claude Code. These are **context triggers**, not executable scripts. When Claude reads these files, it gains specialized capabilities and behavioral patterns.

### Architecture

```
SuperClaude/Commands/
├── README.md                 # This file - command taxonomy and standards
├── TEMPLATE.md              # Command template for new commands
├── __init__.py              # Python package initialization
├── *.md                     # 25 command implementation files
└── *.md.bak                 # Backup files (automatic versioning)
```

### Core Principles

1. **Context Framework**: Commands are behavioral instructions, not executable code
2. **MCP Integration**: Commands orchestrate MCP servers for specialized capabilities
3. **Persona Coordination**: Commands activate domain expert personas
4. **Memory Management**: Commands integrate with ByteRover and Basic-Memory for cross-session persistence
5. **Progressive Enhancement**: Commands adapt complexity based on task requirements

---

## Command Taxonomy

### Command Categories

#### 1. Workflow Commands (8 commands)
**Purpose**: Orchestrate multi-step development processes

- `implement.md` - Feature and code implementation with intelligent persona activation
- `build.md` - Build, compile, and package projects with error handling
- `design.md` - System architecture and API design with comprehensive specifications
- `improve.md` - Apply systematic improvements to code quality and maintainability
- `workflow.md` - Generate structured implementation workflows from requirements
- `task.md` - Execute complex tasks with intelligent workflow management
- `spawn.md` - Meta-system task orchestration with intelligent breakdown
- `troubleshoot.md` - Diagnose and resolve issues in code, builds, and systems

**Complexity**: Standard to Advanced  
**MCP Focus**: Sequential-thinking, Context7, Morphllm, Serena, Zen

#### 2. Analysis Commands (5 commands)
**Purpose**: Deep analysis and multi-expert evaluation

- `analyze.md` - Code analysis across quality, security, performance, architecture
- `business-panel.md` - Multi-expert business analysis with adaptive modes
- `spec-panel.md` - Multi-expert specification review and improvement
- `estimate.md` - Development estimates with intelligent analysis
- `select-tool.md` - Intelligent MCP tool selection based on complexity scoring

**Complexity**: Basic to Advanced  
**MCP Focus**: Zen, Sequential-thinking, Context7, ByteRover

#### 3. Documentation Commands (4 commands)
**Purpose**: Generate and maintain project documentation

- `document.md` - Generate focused documentation for components and APIs
- `index.md` - Generate comprehensive project documentation and knowledge base
- `explain.md` - Provide clear explanations of code and concepts
- `help.md` - List all available SuperClaude commands and functionality

**Complexity**: Low to Standard  
**MCP Focus**: Context7, Ref, Basic-Memory

#### 4. Session Management Commands (4 commands)
**Purpose**: Manage session lifecycle and cross-session persistence

- `load.md` - Session context loading with Serena MCP integration
- `save.md` - Session context persistence with Serena MCP integration
- `reflect.md` - Task reflection and validation using Serena analysis
- `brainstorm.md` - Interactive requirements discovery through Socratic dialogue

**Complexity**: Standard to Advanced  
**MCP Focus**: Serena, ByteRover, Basic-Memory, Sequential-thinking

#### 5. Utility Commands (4 commands)
**Purpose**: Specialized tools and operations

- `cleanup.md` - Systematically clean up code and optimize project structure
- `git.md` - Git operations with intelligent commit messages
- `test.md` - Execute tests with coverage analysis and quality reporting
- `research.md` - Deep web research with adaptive planning and intelligent search

**Complexity**: Basic to Advanced  
**MCP Focus**: Tavily, Firecrawl, Exa, Context7, Playwright

---

## Complexity Levels

### Low Complexity
**Characteristics**:
- Single-step operations
- Minimal MCP coordination
- No persona activation required
- Direct tool usage

**Examples**: `help.md`, `explain.md`, `git.md`

**Typical Execution**: < 30 seconds

### Basic Complexity
**Characteristics**:
- 2-3 step operations
- Simple MCP coordination
- Optional persona activation
- Standard tool patterns

**Examples**: `test.md`, `cleanup.md`, `document.md`

**Typical Execution**: 30 seconds - 2 minutes

### Standard Complexity
**Characteristics**:
- Multi-step workflows (3-5 steps)
- Coordinated MCP usage
- Single persona activation
- Tool orchestration required

**Examples**: `implement.md`, `load.md`, `save.md`, `build.md`

**Typical Execution**: 2-5 minutes

### Advanced Complexity
**Characteristics**:
- Complex workflows (5+ steps)
- Advanced MCP coordination
- Multi-persona orchestration
- Sophisticated tool delegation

**Examples**: `brainstorm.md`, `research.md`, `business-panel.md`, `spec-panel.md`

**Typical Execution**: 5-15 minutes

---

## Metadata Standards

### Required YAML Front Matter

All commands must include complete YAML front matter:

```yaml
---
name: command-name                    # Command identifier (lowercase, hyphenated)
description: "Brief description"      # Single-sentence purpose statement
category: workflow|analysis|documentation|session|utility
complexity: low|basic|standard|advanced
mcp-servers: [server1, server2, ..., serena]  # Required MCP servers
personas: [persona1, persona2, ...]   # Domain expert personas (if applicable)
---
```

### MCP Server Standards

#### Core MCP Servers (Required for All Commands)
```yaml
mcp-servers: [
  byterover,           # Memory retrieval and knowledge storage
  basic-memory,        # Obsidian note management with WikiLinks
  serena,              # Project memory and session persistence
  time                 # Timestamp generation
]
```

#### Analysis MCP Servers
```yaml
# Add for analysis, review, and reasoning tasks
[zen, sequential-thinking, context7]
```

#### Research MCP Servers
```yaml
# Add for web research and content retrieval
[tavily, firecrawl, exa, ref, octocode]
```

#### Development MCP Servers
```yaml
# Add for code generation and editing
[morphllm-fast-apply, cerebras-code, playwright, magic]
```

### Persona Standards

#### Available Personas
- `architect` - System design and architecture
- `frontend` - Frontend development and UI/UX
- `backend` - Backend development and APIs
- `security` - Security analysis and best practices
- `qa-specialist` - Testing and quality assurance
- `devops` - DevOps and infrastructure
- `analyzer` - Code and system analysis
- `project-manager` - Project coordination
- `deep-research-agent` - Research orchestration
- `mentor` - Learning and skill development

#### Persona Activation Rules
1. **Single Domain**: Activate one primary persona
2. **Multi-Domain**: Coordinate 2-3 personas maximum
3. **Complex Tasks**: Use `spawn.md` for multi-agent orchestration
4. **Documentation**: Always specify activated personas in front matter

---

## Command Structure Standards

### Required Sections

Every command file must include:

#### 1. Command Header
```markdown
# /sc:command-name - Command Title

> **Context Framework Note**: Brief explanation of activation pattern
```

#### 2. Triggers Section
```markdown
## Triggers
- Specific use case 1
- Specific use case 2
- Specific use case 3
```

#### 3. Usage Section
```markdown
## Usage
```
/sc:command-name [arguments] [--flags]
```
```

#### 4. Behavioral Flow Section
```markdown
## Behavioral Flow
1. **Step 1**: Action and outcome
2. **Step 2**: Action and outcome
3. **Step 3**: Action and outcome
...

Key behaviors:
- Key pattern 1
- Key pattern 2
- Key pattern 3
```

#### 5. MCP Integration Section
```markdown
## MCP Integration

### Primary Tools
- **Server Name**: Purpose and usage patterns

### Knowledge & Memory Integration
- **ByteRover**: Retrieve [type] and store [type] with timestamps
- **Basic-Memory**: Document [type] with WikiLinks in Obsidian

### Workflow Integration (per AGENTS.md)
1. **Before**: Retrieve relevant knowledge from byterover
2. **During**: Log decisions with basic-memory write_note
3. **After**: Store verified findings in byterover with complete details
```

#### 6. Tool Coordination Section
```markdown
## Tool Coordination
- **Tool Name**: Usage pattern and purpose
```

#### 7. Key Patterns Section
```markdown
## Key Patterns
- **Pattern Name**: Input → Process → Output
```

#### 8. Examples Section
```markdown
## Examples

### Example 1: Title
```
/sc:command example
# Description of what happens
# Expected outcome
```
```

#### 9. Boundaries Section
```markdown
## Boundaries

**Will:**
- Clear statement of capability
- Another capability

**Will Not:**
- Clear limitation
- Another limitation
```

### Optional Sections

- **Context Trigger Pattern**: For complex activation patterns
- **Auto-Persona Activation**: For automatic persona selection
- **Integration Notes**: For cross-command coordination
- **Performance Notes**: For execution time expectations

---

## MCP Integration Patterns

### ByteRover Knowledge Management

#### Before Command Execution
```markdown
1. **Knowledge Retrieval**: Use byterover-retrieve-knowledge to gather:
   - Prior implementation patterns
   - Relevant architectural decisions
   - Known issues and solutions
   - Best practices and conventions
```

#### During Command Execution
```markdown
2. **Progress Logging**: Use basic-memory write_note to document:
   - Key decisions and rationale
   - Technical challenges encountered
   - Solution approaches explored
   - Implementation patterns used
```

#### After Command Execution
```markdown
3. **Knowledge Storage**: Use byterover-store-knowledge to save:
   - Complete code snippets with context
   - Verified solutions with timestamps
   - Lessons learned and insights
   - Cross-references to related work
```

### Basic-Memory Integration

#### Note Creation Pattern
```markdown
# Use write_note for persistent documentation
- Format: Markdown with WikiLinks
- Location: Obsidian graph integration
- Tags: Relevant categorization
- Links: [[Project]], [[Feature]], [[Issue]]
```

#### Note Retrieval Pattern
```markdown
# Use read_note or search_notes for context
- Query: Semantic search across notes
- Context: Related notes via WikiLinks
- History: Temporal relationship tracking
```

### Serena Session Management

#### Project Activation
```markdown
# Load project context
- activate_project: Establish project environment
- list_memories: Retrieve cross-session context
- read_memory: Access specific project memories
```

#### Session Persistence
```markdown
# Save session state
- write_memory: Store session discoveries
- think_about_collected_information: Validate insights
- summarize_changes: Document progress
```

---

## Development Guidelines

### Creating New Commands

#### 1. Use the Template
Copy `TEMPLATE.md` and customize for your command:
```bash
cp SuperClaude/Commands/TEMPLATE.md SuperClaude/Commands/new-command.md
```

#### 2. Define Command Metadata
- Choose appropriate category
- Set complexity level accurately
- List all required MCP servers
- Specify persona requirements

#### 3. Document Behavioral Flow
- Clear step-by-step execution
- Key behavioral patterns
- Decision points and branching

#### 4. Add MCP Integration
- ByteRover workflow integration
- Basic-Memory note patterns
- Serena session management (if applicable)

#### 5. Provide Examples
- Minimum 3 realistic examples
- Show different usage patterns
- Include expected outcomes

#### 6. Define Boundaries
- Clear capability statements
- Explicit limitations
- Error handling expectations

### Testing Requirements

#### Manual Testing Checklist
- [ ] YAML metadata validates
- [ ] All MCP servers exist
- [ ] All personas are valid
- [ ] Examples execute successfully
- [ ] ByteRover integration works
- [ ] Basic-Memory notes created
- [ ] Documentation is clear

#### Automated Testing
Use `scripts/validate_commands.py`:
```bash
python scripts/validate_commands.py SuperClaude/Commands/new-command.md
```

### Validation Rules

#### Metadata Validation
- Name matches filename (without .md)
- Description is 1 sentence < 100 chars
- Category is valid enum
- Complexity is valid enum
- All MCP servers exist in framework
- All personas exist in Agents directory

#### Content Validation
- All required sections present
- ByteRover workflow documented
- At least 3 examples provided
- Boundaries clearly defined
- No broken internal links

#### Integration Validation
- MCP servers properly referenced
- Personas match activation patterns
- Tool coordination documented
- Memory patterns consistent

---

## Command Quality Checklist

### Tier 1: Exemplary (9-10/10)
- ✅ Complete YAML metadata
- ✅ Comprehensive MCP integration with workflow patterns
- ✅ ByteRover knowledge management documented
- ✅ Basic-Memory note creation patterns
- ✅ 5+ realistic examples
- ✅ Clear boundaries and limitations
- ✅ Cross-command coordination documented

**Examples**: `research.md`, `implement.md`, `analyze.md`

### Tier 2: Strong (8-9/10)
- ✅ Complete YAML metadata
- ✅ Good MCP integration
- ⚠️ Partial ByteRover integration
- ✅ 3+ examples
- ✅ Clear boundaries

**Examples**: `brainstorm.md`, `load.md`, `save.md`, `help.md`

### Tier 3: Needs Improvement (7-8/10)
- ✅ Complete YAML metadata
- ✅ Basic MCP integration
- ❌ Missing ByteRover integration
- ✅ 2-3 examples
- ⚠️ Boundaries could be clearer

**Action Required**: Add ByteRover workflow integration section

---

## Contribution Process

### 1. Propose New Command
- Open GitHub issue with command proposal
- Include use cases and examples
- Specify required MCP servers
- Define persona requirements

### 2. Draft Command
- Use TEMPLATE.md as starting point
- Follow metadata standards
- Document MCP integration
- Add comprehensive examples

### 3. Submit for Review
- Create pull request with command file
- Include test results from validation script
- Document testing approach
- Provide usage examples

### 4. Review Requirements
- Maintainer review within 3 days
- Validation script must pass
- Manual testing required
- Documentation review

### 5. Merge and Deploy
- Approved commands merged to main
- Automatic backup created (.bak file)
- help.md updated with new command
- Documentation regenerated

---

## Maintenance

### Regular Maintenance Tasks

#### Weekly
- [ ] Validate all command metadata
- [ ] Check for broken MCP references
- [ ] Review command execution logs
- [ ] Update examples if APIs changed

#### Monthly
- [ ] Audit command quality scores
- [ ] Review and update help.md
- [ ] Check for deprecated MCP servers
- [ ] Update persona references

#### Quarterly
- [ ] Comprehensive command review
- [ ] Update taxonomy and categories
- [ ] Review complexity ratings
- [ ] Update integration patterns

### Version Control

#### Backup Strategy
- Automatic .bak files created on save
- Manual backups before major changes
- Git history for all modifications

#### Deprecation Process
1. Mark command as deprecated in metadata
2. Add deprecation notice in command header
3. Maintain for 2 minor versions
4. Remove and update help.md
5. Provide migration guide to replacement

---

## FAQ

### General Questions

**Q: What is the difference between a command and an agent?**  
A: Commands are behavioral instructions that orchestrate agents. Agents are domain experts with specialized capabilities. Commands coordinate multiple agents and MCP servers to accomplish tasks.

**Q: Can commands be executed directly?**  
A: No. Commands are context files that Claude reads. When you type `/sc:command` in Claude Code, Claude activates the behavioral patterns defined in the command file.

**Q: How do I test a new command?**  
A: Use the validation script (`scripts/validate_commands.py`), then test in Claude Code with realistic examples. Verify MCP integration, persona activation, and output quality.

### Technical Questions

**Q: What MCP servers should I use?**  
A: Start with core servers (byterover, basic-memory, serena, time). Add specialized servers based on command category and complexity. Reference existing commands in same category.

**Q: How do I handle errors?**  
A: Document expected error conditions in Boundaries section. Use try/catch patterns in behavioral flow. Provide recovery guidance in command documentation.

**Q: Can commands call other commands?**  
A: Yes, via cross-command coordination. Document in Integration Notes section. Use `spawn.md` for complex multi-command orchestration.

### Integration Questions

**Q: How do I integrate with ByteRover?**  
A: Follow the ByteRover workflow pattern: retrieve before, log during, store after. Include complete code snippets, timestamps, and context in stored knowledge.

**Q: When should I use Basic-Memory vs ByteRover?**  
A: Use Basic-Memory for persistent documentation and cross-session notes with WikiLinks. Use ByteRover for code patterns, solutions, and verified implementations.

**Q: What if a required MCP server is unavailable?**  
A: Commands should gracefully degrade. Document fallback behavior in command file. Provide alternative approaches using native tools.

---

## Resources

### Framework Documentation
- **AGENTS.md**: Comprehensive agent and MCP integration patterns
- **MODES.md**: Behavioral mode specifications
- **MCP_INTEGRATION.md**: Detailed MCP server documentation
- **PERSONAS.md**: Domain expert persona definitions

### Command References
- **AUDIT_COMMANDS.md**: Complete directory audit and quality assessment
- **TEMPLATE.md**: Standard command template for new commands
- **help.md**: Complete command listing and flag documentation

### Development Tools
- **scripts/validate_commands.py**: Automated command validation
- **scripts/test_commands.sh**: Command smoke testing
- **scripts/generate_help.py**: Automatic help.md generation

### External Resources
- [SuperClaude Framework GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- [MCP Documentation](https://modelcontextprotocol.io/docs)
- [Claude Code Documentation](https://docs.anthropic.com/claude/docs)

---

## Version History

### 4.2.0 (October 2, 2025)
- Added comprehensive README documentation
- Standardized command taxonomy and categories
- Documented MCP integration patterns
- Added ByteRover workflow standards
- Created validation infrastructure

### 4.1.4 (September 2025)
- Added research.md command
- Enhanced MCP integration documentation
- Updated help.md with flag documentation

### 4.1.0 (August 2025)
- Added business-panel.md command
- Added spec-panel.md command
- Improved MCP coordination patterns

---

**For Questions or Contributions**: Open an issue on [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)

**Maintained by**: SuperClaude Framework Team  
**Last Updated**: October 2, 2025
