---
name: help
description: "List all available /sc commands and their functionality"
category: utility
complexity: low
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena, playwright, serena]
personas: []
---

# /sc:help - Command Reference Documentation

> **Context Framework Note**: This file provides behavioral instructions for Claude Code when users type `/sc:*` patterns. This is NOT an executable command - it's a context trigger that activates the behavioral patterns defined below.

## Triggers
- Command discovery and reference lookup requests
- Framework exploration and capability understanding needs
- Documentation requests for available SuperClaude commands

## Behavioral Flow
1. **Display**: Present complete command list with descriptions
2. **Complete**: End interaction after displaying information

Key behaviors:
- Information display only - no execution or implementation
- Reference documentation mode without action triggers

Here is a complete list of all available SuperClaude (`/sc`) commands.

| Command | Description |
|---|---|
| `/sc:analyze` | Comprehensive code analysis across quality, security, performance, and architecture domains |
| `/sc:brainstorm` | Interactive requirements discovery through Socratic dialogue and systematic exploration |
| `/sc:build` | Build, compile, and package projects with intelligent error handling and optimization |
| `/sc:business-panel` | Multi-expert business analysis with adaptive interaction modes |
| `/sc:cleanup` | Systematically clean up code, remove dead code, and optimize project structure |
| `/sc:design` | Design system architecture, APIs, and component interfaces with comprehensive specifications |
| `/sc:document` | Generate focused documentation for components, functions, APIs, and features |
| `/sc:estimate` | Provide development estimates for tasks, features, or projects with intelligent analysis |
| `/sc:explain` | Provide clear explanations of code, concepts, and system behavior with educational clarity |
| `/sc:git` | Git operations with intelligent commit messages and workflow optimization |
| `/sc:help` | List all available /sc commands and their functionality |
| `/sc:implement` | Feature and code implementation with intelligent persona activation and MCP integration |
| `/sc:improve` | Apply systematic improvements to code quality, performance, and maintainability |
| `/sc:index` | Generate comprehensive project documentation and knowledge base with intelligent organization |
| `/sc:load` | Session lifecycle management with Serena MCP integration for project context loading |
| `/sc:reflect` | Task reflection and validation using Serena MCP analysis capabilities |
| `/sc:save` | Session lifecycle management with Serena MCP integration for session context persistence |
| `/sc:select-tool` | Intelligent MCP tool selection based on complexity scoring and operation analysis |
| `/sc:spawn` | Meta-system task orchestration with intelligent breakdown and delegation |
| `/sc:spec-panel` | Multi-expert specification review and improvement using renowned specification and software engineering experts |
| `/sc:task` | Execute complex tasks with intelligent workflow management and delegation |
| `/sc:test` | Execute tests with coverage analysis and automated quality reporting |
| `/sc:troubleshoot` | Diagnose and resolve issues in code, builds, deployments, and system behavior |
| `/sc:workflow` | Generate structured implementation workflows from PRDs and feature requirements |

## SuperClaude Framework Flags

SuperClaude supports behavioral flags to enable specific execution modes and tool selection patterns. Use these flags with any `/sc` command to customize behavior.

### Mode Activation Flags

| Flag | Trigger | Behavior |
|------|---------|----------|
| `--brainstorm` | Vague project requests, exploration keywords | Activate collaborative discovery mindset, ask probing questions |
| `--introspect` | Self-analysis requests, error recovery | Expose thinking process with transparency markers |
| `--task-manage` | Multi-step operations (>3 steps) | Orchestrate through delegation, systematic organization |
| `--orchestrate` | Multi-tool operations, parallel execution | Optimize tool selection matrix, enable parallel thinking |
| `--token-efficient` | Context usage >75%, large-scale operations | Symbol-enhanced communication, 30-50% token reduction |

### MCP Server Flags

| Flag | Trigger | Behavior |
|------|---------|----------|
| `--c7` / `--context7` | Library imports, framework questions | Enable Context7 for curated documentation lookup |
| `--seq` / `--sequential` | Complex debugging, system design | Enable Sequential for structured multi-step reasoning |
| `--magic` | UI component requests (/ui, /21) | Enable Magic for modern UI generation from 21st.dev |
| `--morph` / `--morphllm` | Bulk code transformations | Enable Morphllm for efficient multi-file pattern application |
| `--serena` | Symbol operations, project memory | Enable Serena for semantic understanding and session persistence |
| `--play` / `--playwright` | Browser testing, E2E scenarios | Enable Playwright for real browser automation and testing |
| `--all-mcp` | Maximum complexity scenarios | Enable all MCP servers for comprehensive capability |
| `--no-mcp` | Native-only execution needs | Disable all MCP servers, use native tools |

### Analysis Depth Flags

| Flag | Trigger | Behavior |
|------|---------|----------|
| `--think` | Multi-component analysis needs | Standard structured analysis (~4K tokens), enables Sequential |
| `--think-hard` | Architectural analysis, system-wide dependencies | Deep analysis (~10K tokens), enables Sequential + Context7 |
| `--ultrathink` | Critical system redesign, legacy modernization | Maximum depth analysis (~32K tokens), enables all MCP servers |

### Execution Control Flags

| Flag | Trigger | Behavior |
|------|---------|----------|
| `--delegate [auto\|files\|folders]` | >7 directories OR >50 files | Enable sub-agent parallel processing with intelligent routing |
| `--concurrency [n]` | Resource optimization needs | Control max concurrent operations (range: 1-15) |
| `--loop` | Improvement keywords (polish, refine, enhance) | Enable iterative improvement cycles with validation gates |
| `--iterations [n]` | Specific improvement cycle requirements | Set improvement cycle count (range: 1-10) |
| `--validate` | Risk score >0.7, resource usage >75% | Pre-execution risk assessment and validation gates |
| `--safe-mode` | Resource usage >85%, production environment | Maximum validation, conservative execution |

### Output Optimization Flags

| Flag | Trigger | Behavior |
|------|---------|----------|
| `--uc` / `--ultracompressed` | Context pressure, efficiency requirements | Symbol communication system, 30-50% token reduction |
| `--scope [file\|module\|project\|system]` | Analysis boundary needs | Define operational scope and analysis depth |
| `--focus [performance\|security\|quality\|architecture\|accessibility\|testing]` | Domain-specific optimization | Target specific analysis domain and expertise application |

### Flag Priority Rules

- **Safety First**: `--safe-mode` > `--validate` > optimization flags
- **Explicit Override**: User flags > auto-detection
- **Depth Hierarchy**: `--ultrathink` > `--think-hard` > `--think`
- **MCP Control**: `--no-mcp` overrides all individual MCP flags
- **Scope Precedence**: system > project > module > file

### Usage Examples

```bash
# Deep analysis with Context7 enabled
/sc:analyze --think-hard --context7 src/

# UI development with Magic and validation
/sc:implement --magic --validate "Add user dashboard"

# Token-efficient task management
/sc:task --token-efficient --delegate auto "Refactor authentication system"

# Safe production deployment
/sc:build --safe-mode --validate --focus security
```


## Usage
```
/sc:command [options] [arguments]
```
**Usage**: Type this pattern in your Claude Code conversation to activate this command's behavioral mode.



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

### Tool Coordination
- **Analysis & Research**: Sequential-thinking, Exa, Context7 for deep investigation
- **Development**: Morphllm, Serena for code changes and project memory
- **Documentation**: Ref, Context7 for framework-specific docs



## Tool Coordination
- **Read/Write/Edit**: File operations and content management
- **TodoWrite**: Progress tracking for multi-step operations  
- **Task**: Parallel execution and delegation
- **WebSearch**: Research and external information gathering



## Key Patterns
- **Systematic Execution**: Structured approach → comprehensive results
- **Memory Integration**: ByteRover retrieve → process → store pattern
- **Progressive Enhancement**: Iterative refinement with persistent context
- **Cross-Session Continuity**: Serena MCP for long-running operations



## Examples

### Basic Usage
```
/sc:command "basic example"
```

### Advanced Usage
```
/sc:command "advanced example" --with-options
```

### Complex Scenario
```
/sc:command "complex multi-step example" --comprehensive
```


## Boundaries

**Will:**
- Display comprehensive list of available SuperClaude commands
- Provide clear descriptions of each command's functionality
- Present information in readable tabular format
- Show all available SuperClaude framework flags and their usage
- Provide flag usage examples and priority rules

**Will Not:**
- Execute any commands or create any files
- Activate implementation modes or start projects
- Engage TodoWrite or any execution tools

---

## 📚 See Also

### For Developers
- **[Commands README](README.md)** - Complete command taxonomy, standards, and development guidelines
- **[TEMPLATE.md](TEMPLATE.md)** - Template for creating new commands with all required sections
- **[Validation Script](../../scripts/validate_commands.py)** - Automated quality assurance tool
- **[CI/CD Documentation](../../.github/README.md)** - GitHub Actions and pre-commit hook setup

### Quick Reference

#### By Category
- **Workflow**: implement, build, task, workflow, load, save
- **Analysis**: analyze, research, brainstorm, estimate, explain, troubleshoot
- **Documentation**: document, index, help
- **Orchestration**: spawn, select-tool
- **Utility**: cleanup, design, git, improve, reflect, test
- **Special Panels**: business-panel, spec-panel

#### By Complexity
- **Low**: help, load, save
- **Basic**: cleanup, document, explain, git
- **Standard**: design, estimate, improve, index, reflect, test, troubleshoot
- **Advanced**: analyze, brainstorm, build, business-panel, implement, research, select-tool, spawn, spec-panel, task, workflow

#### Most Used Commands
1. **`/sc:implement`** - For feature development and code implementation
2. **`/sc:analyze`** - For code analysis and quality assessment
3. **`/sc:research`** - For information gathering and investigation
4. **`/sc:help`** - For command reference (you are here!)
5. **`/sc:troubleshoot`** - For debugging and issue resolution

### Contributing
To add or modify commands, see the [Commands README](README.md) for:
- Command development standards
- Metadata requirements
- ByteRover workflow integration patterns
- Validation and testing procedures

---

**Framework Version**: 1.0.0  
**Last Validated**: October 2, 2025  
**Quality Score**: 9.5/10  

**Note:** This list is manually generated and may become outdated. If you suspect it is inaccurate, please consider regenerating it or contacting a maintainer.
