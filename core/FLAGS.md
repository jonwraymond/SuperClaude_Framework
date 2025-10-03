# SuperClaude Framework Flags

**Version**: 5.0  
**Last Updated**: 2025-10-02

---

## 🎯 Purpose

Flags control framework behavior, feature toggles, and operational modes. They provide fine-grained control over how the framework processes requests, activates personas, and executes workflows.

---

## 📋 Global Flags

### `--wave-orchestration` | `-w`
**Enable/disable wave orchestration**

```bash
# Enable (default)
--wave-orchestration=true

# Disable (use direct execution)
--wave-orchestration=false
```

**Effect**: Controls whether complex tasks go through 5-wave progressive enhancement or execute directly.

---

### `--auto-activation` | `-a`
**Enable/disable automatic persona activation**

```bash
# Enable (default)
--auto-activation=true

# Disable (manual persona selection only)
--auto-activation=false
```

**Effect**: Controls whether personas activate automatically based on scoring or require manual selection.

---

### `--memory-check` | `-m`
**Force memory check before tasks**

```bash
# Enable (default)
--memory-check=true

# Disable (skip memory checks)
--memory-check=false
```

**Effect**: Controls whether the framework checks byterover/basic-memory before starting work.

---

### `--strict-rules` | `-s`
**Enable strict rule enforcement**

```bash
# Enable
--strict-rules=true

# Disable (allows rule bending)
--strict-rules=false  # Default
```

**Effect**: When enabled, prevents any rule overrides except explicit user commands.

---

### `--verbose` | `-v`
**Enable verbose output**

```bash
# Levels: 0=quiet, 1=normal, 2=verbose, 3=debug
--verbose=2
```

**Effect**: Controls logging detail level for troubleshooting and monitoring.

---

### `--dry-run` | `-d`
**Simulate without executing**

```bash
--dry-run=true
```

**Effect**: Shows what would be done without actually executing commands/changes.

---

## 🔧 Tool-Specific Flags

### `--prefer-zen`
**Prioritize zen MCP tools**

```bash
--prefer-zen=true  # Default
```

**Effect**: Routes complex reasoning to zen suite (thinkdeep, planner, debug, etc.) over alternatives.

---

### `--enable-firecrawl`
**Enable Firecrawl for web operations**

```bash
--enable-firecrawl=true  # Default
```

**Effect**: Uses Firecrawl MCP for web scraping/crawling instead of basic curl.

---

### `--enable-context7`
**Enable Context7 for documentation**

```bash
--enable-context7=true  # Default
```

**Effect**: Automatically fetches official library docs via Context7 MCP.

---

### `--enable-exa`
**Enable Exa for code search**

```bash
--enable-exa=true
```

**Effect**: Uses Exa MCP for deep code/research searches. **Note**: Requires configuration.

---

### `--enable-ref`
**Enable Ref for documentation search**

```bash
--enable-ref=true
```

**Effect**: Uses Ref MCP for private/public doc searches. **Note**: Requires configuration.

---

### `--repomix-compress`
**Enable repomix Tree-sitter compression**

```bash
--repomix-compress=false  # Default
```

**Effect**: When packing codebases, use Tree-sitter compression (70% token reduction).

---

### `--github-auto-pr`
**Automatically create PRs for changes**

```bash
--github-auto-pr=false  # Default
```

**Effect**: Automatically create GitHub PRs instead of asking user.

---

## 🎭 Persona Flags

### `--multi-persona`
**Allow multiple persona activation**

```bash
--multi-persona=true  # Default
```

**Effect**: Enables cross-persona collaboration on complex tasks.

---

### `--persona-confidence-threshold`
**Set minimum confidence for auto-activation**

```bash
--persona-confidence-threshold=0.7  # Default
```

**Effect**: Personas activate only if confidence score >= threshold (0.0 to 1.0).

---

### `--force-persona`
**Force specific persona activation**

```bash
--force-persona=architect
```

**Effect**: Bypasses auto-activation, always uses specified persona.

---

## 🌊 Wave Orchestration Flags

### `--max-wave`
**Limit wave depth**

```bash
--max-wave=3  # Default: 5
```

**Effect**: Stop after specified wave number. Useful for time/resource constraints.

---

### `--wave-timeout`
**Set wave execution timeout**

```bash
--wave-timeout=300  # 300 seconds (5 minutes)
```

**Effect**: Timeout (seconds) for each wave before moving to next.

---

### `--wave-parallel`
**Enable parallel wave execution**

```bash
--wave-parallel=false  # Default
```

**Effect**: Execute compatible wave tasks in parallel (experimental).

---

## 🧠 Memory Flags

### `--memory-dual-write`
**Write to both memory systems**

```bash
--memory-dual-write=true  # Default
```

**Effect**: Store knowledge in both byterover AND basic-memory for redundancy.

---

### `--memory-sync`
**Sync memory systems**

```bash
--memory-sync=true
```

**Effect**: Periodically sync byterover ↔ basic-memory for consistency.

---

### `--memory-ttl`
**Set memory time-to-live**

```bash
--memory-ttl=2592000  # 30 days in seconds
```

**Effect**: Auto-expire old memories after specified duration.

---

## 📝 Planning Flags

### `--require-plan`
**Require plan approval before execution**

```bash
--require-plan=true  # Default
```

**Effect**: Enforces Rule 2 (Plan Before Execute).

---

### `--plan-detail-level`
**Set plan granularity**

```bash
# Options: minimal, standard, detailed
--plan-detail-level=standard
```

**Effect**: Controls how detailed generated plans should be.

---

### `--auto-save-plans`
**Automatically save plans to memory**

```bash
--auto-save-plans=true  # Default
```

**Effect**: Saves approved plans to byterover immediately.

---

## 🔒 Security Flags

### `--security-strict`
**Enable strict security checks**

```bash
--security-strict=true  # Default
```

**Effect**: Block operations that could expose secrets or sensitive data.

---

### `--pre-commit-checks`
**Run pre-commit validation**

```bash
--pre-commit-checks=true  # Default
```

**Effect**: Validate commits for secrets, large files before accepting.

---

### `--secret-scan`
**Scan for secrets in code**

```bash
--secret-scan=true  # Default
```

**Effect**: Uses git-secrets/trufflehog to detect credentials.

---

## 🧪 Testing Flags

### `--auto-test`
**Run tests after changes**

```bash
--auto-test=true  # Default
```

**Effect**: Automatically run test suite after code modifications.

---

### `--test-coverage-threshold`
**Minimum code coverage required**

```bash
--test-coverage-threshold=80  # 80%
```

**Effect**: Reject changes that drop coverage below threshold.

---

### `--skip-tests`
**Skip test execution (danger!)**

```bash
--skip-tests=false  # Default
```

**Effect**: Skip test suite (use only for docs/non-code changes).

---

## 📊 Performance Flags

### `--token-budget`
**Set maximum token usage**

```bash
--token-budget=100000
```

**Effect**: Stop processing if token usage exceeds budget.

---

### `--rate-limit-pause`
**Pause on rate limit**

```bash
--rate-limit-pause=true  # Default
```

**Effect**: Wait/retry on API rate limits instead of failing.

---

### `--streaming`
**Enable streaming responses**

```bash
--streaming=true  # Default when supported
```

**Effect**: Stream output for faster perceived response time.

---

## 🎨 Output Flags

### `--format`
**Output format**

```bash
# Options: markdown, json, plain
--format=markdown  # Default
```

**Effect**: Controls response format.

---

### `--color`
**Enable colored output**

```bash
--color=true  # Default in terminal
```

**Effect**: Use ANSI colors for better readability.

---

### `--emoji`
**Enable emoji in output**

```bash
--emoji=true  # Default
```

**Effect**: Use emoji for visual indicators (✅, ❌, ⚠️, etc.).

---

## 🔄 Workflow Flags

### `--workflow-mode`
**Select workflow mode**

```bash
# Options: feature, bugfix, research, architecture, optimization, security
--workflow-mode=feature
```

**Effect**: Use predefined workflow from WORKFLOWS.md.

---

### `--checkpoint-frequency`
**Set checkpoint save frequency**

```bash
--checkpoint-frequency=high  # high, medium, low
```

**Effect**: How often to save progress during long workflows.

---

## 🎯 Mode-Specific Flags

### `--introspection-depth`
**Introspection analysis depth**

```bash
# Options: shallow, standard, deep
--introspection-depth=standard
```

**Effect**: How thoroughly to analyze past decisions (MODE_Introspection).

---

### `--research-max-sources`
**Maximum research sources**

```bash
--research-max-sources=10  # Default
```

**Effect**: Limit sources for deep research mode.

---

### `--task-auto-prioritize`
**Auto-prioritize tasks**

```bash
--task-auto-prioritize=true
```

**Effect**: Automatically order tasks by priority (MODE_Task_Management).

---

## 🐛 Debug Flags

### `--debug-orchestrator`
**Show orchestrator decisions**

```bash
--debug-orchestrator=false  # Default
```

**Effect**: Log routing decisions, persona scoring, wave transitions.

---

### `--debug-memory`
**Show memory operations**

```bash
--debug-memory=false  # Default
```

**Effect**: Log all memory reads/writes for debugging.

---

### `--trace-tools`
**Trace tool invocations**

```bash
--trace-tools=false  # Default
```

**Effect**: Log every MCP tool call with parameters.

---

## 🚀 Experimental Flags

### `--enable-caching`
**Enable response caching**

```bash
--enable-caching=false  # Default (experimental)
```

**Effect**: Cache similar queries for faster responses.

---

### `--enable-predictive-loading`
**Predictively load context**

```bash
--enable-predictive-loading=false  # Default (experimental)
```

**Effect**: Pre-load likely needed context based on patterns.

---

### `--enable-auto-refactor`
**Suggest refactorings automatically**

```bash
--enable-auto-refactor=false  # Default (experimental)
```

**Effect**: Proactively suggest code improvements.

---

## 📖 Usage Examples

### Example 1: Quick bug fix (skip planning)
```bash
--require-plan=false --max-wave=2 --auto-test=true
```

### Example 2: Deep architecture work
```bash
--wave-orchestration=true --max-wave=5 --verbose=2 --memory-dual-write=true
```

### Example 3: Research mode
```bash
--workflow-mode=research --enable-firecrawl=true --enable-exa=true --research-max-sources=20
```

### Example 4: Security audit
```bash
--workflow-mode=security --security-strict=true --secret-scan=true --verbose=3
```

### Example 5: Dry run for review
```bash
--dry-run=true --verbose=2 --debug-orchestrator=true
```

---

## 🎛️ Configuration Files

Flags can be set via:

1. **Command line** (highest priority)
2. **Environment variables** (`SUPERCLAUDE_*`)
3. **User config** (`~/.superclaude/config.toml`)
4. **Project config** (`.superclaude.toml`)
5. **Defaults** (lowest priority)

### Example config file (`.superclaude.toml`):

```toml
[global]
wave_orchestration = true
auto_activation = true
verbose = 1

[tools]
prefer_zen = true
enable_firecrawl = true
enable_context7 = true

[memory]
dual_write = true
sync = true

[security]
strict = true
pre_commit_checks = true

[performance]
token_budget = 100000
streaming = true
```

---

## 🔗 Related Documents

- **RULES.md**: Framework operation rules
- **ORCHESTRATOR.md**: Routing and wave orchestration
- **WORKFLOWS.md**: Workflow patterns
- **MCP_TOOLS.md**: Tool configurations

---

**Status**: Active  
**Configuration Priority**: CLI > ENV > User Config > Project Config > Defaults  
**Review**: Update as new features are added
