# SuperClaude Framework Rules

**Version**: 5.0  
**Last Updated**: 2025-10-02

---

## 🎯 Purpose

This document defines the operational rules and governance principles for the SuperClaude Framework. These rules ensure consistent, safe, and effective agent behavior across all personas, modes, and workflows.

---

## 📋 Core Operating Rules

### Rule 1: Memory First
**Always check memory before starting work**

```
BEFORE any task:
1. byterover-retrieve-knowledge (check for prior context)
2. Check for active plans (byterover-retrieve-active-plans)
3. Review relevant modules (byterover-search-modules)
4. Only then proceed with task
```

**Rationale**: Avoids duplicate work, maintains continuity, leverages institutional knowledge.

---

### Rule 2: Plan Before Execute
**No code changes without an approved plan**

```
WORKFLOW:
1. Analyze problem thoroughly
2. Create detailed plan with checkable items
3. Get explicit user approval
4. Execute minimal, simple changes
5. Document and review
```

**Exceptions**: 
- Emergency fixes (security vulnerabilities)
- Trivial changes (typo fixes, formatting)
- Explicit user override

---

### Rule 3: Memory Persistence
**Store all significant work in memory**

**What to store** (byterover-store-knowledge):
- Implementation decisions and rationale
- Bug fixes and root causes
- Architecture patterns discovered
- Integration insights
- Code snippets (complete, not fragments)
- Failure modes and solutions

**What NOT to store**:
- Trivial information (common knowledge)
- Temporary state
- Credentials or secrets
- User-specific data

**When to store**:
- After completing tasks
- After discovering important patterns
- Before switching contexts
- When asked to remember something

---

### Rule 4: Tool Selection Priority
**Use the right tool for the job**

```
Priority order:
1. zen suite (thinkdeep, planner, debug, codereview) - for complex reasoning
2. byterover - for memory operations
3. basic-memory - for graph-based knowledge
4. serena - for code navigation
5. repomix - for codebase packaging
6. context7 - for official docs
7. firecrawl - for web scraping
8. github - for git operations
```

**Selection rules**:
- Check ORCHESTRATOR.md routing tables first
- Use wave orchestration for complex tasks
- Prefer specialized tools over general ones
- Combine tools when beneficial (see WORKFLOWS.md)

---

### Rule 5: Persona Activation
**Let the orchestrator select personas**

```
DO:
- Trust auto-activation scoring
- Allow multi-persona collaboration
- Follow persona specializations (see PERSONAS.md)

DON'T:
- Force persona selection
- Mix persona concerns inappropriately
- Bypass orchestrator logic
```

**Manual override**: User can explicitly request specific personas.

---

### Rule 6: Progressive Enhancement
**Use wave orchestration for complex tasks**

```
Wave 1 (Rapid): Quick wins, obvious fixes
Wave 2 (Standard): Core implementation
Wave 3 (Enhanced): Optimization, edge cases
Wave 4 (Deep): Architecture, security
Wave 5 (Expert): Final polish, documentation

Exit early if complexity doesn't warrant later waves.
```

---

### Rule 7: Safety First
**Never compromise security or data integrity**

```
FORBIDDEN:
- Committing secrets to version control
- Exposing credentials in logs/memory
- Destructive operations without confirmation
- Force-pushing to protected branches
- Bypassing code review

REQUIRED:
- Validate all external input
- Sanitize before database operations
- Review security implications
- Use prepared statements/parameterized queries
- Implement proper authentication/authorization
```

---

### Rule 8: Minimal Impact
**Make the smallest change that solves the problem**

```
PREFER:
- Targeted fixes over broad refactors
- Single-purpose commits
- Incremental improvements
- Reversible changes

AVOID:
- Scope creep
- Opportunistic refactoring (unless approved)
- Breaking changes without migration path
- Changing unrelated code
```

---

### Rule 9: Test-Driven Quality
**Ensure quality at every step**

```
BEFORE committing:
1. Write/update tests
2. Run existing test suite
3. Verify no regressions
4. Check code coverage
5. Run linters/formatters

FOR critical paths:
- Unit tests (required)
- Integration tests (required)
- Edge case coverage
- Error handling tests
```

---

### Rule 10: Documentation Discipline
**Keep documentation in sync with code**

```
UPDATE when changing:
- Function signatures → docstrings
- APIs → API docs
- Architecture → ADRs
- Workflows → process docs
- Config → README/setup guides

FORMATS:
- Code comments for "why", not "what"
- README for setup/usage
- ADR for decisions (see .claude/docs/)
- Inline for complex algorithms
```

---

### Rule 11: Git Workflow Discipline
**Follow branching and commit conventions**

```
BRANCH naming:
- feature/description
- fix/bug-description
- refactor/description
- docs/description

COMMITS:
- Clear, descriptive messages
- Reference issues/tickets
- Atomic (one concern per commit)
- Signed (if required)

PULL REQUESTS:
- Create from feature branch
- Request review (don't self-merge)
- Address all comments
- Squash/merge appropriately
```

---

### Rule 12: Context Preservation
**Maintain session continuity**

```
AT session start:
- Check for LAST_SESSION, ACTIVE_TODOS
- Load context from .claude/ or sessions/
- Review recent changes (git log)

DURING session:
- Update progress regularly
- Store intermediate findings
- Track decision rationale

AT session end:
- Save session state
- Update ACTIVE_TODOS
- Store key learnings in byterover
```

---

### Rule 13: Error Handling
**Graceful degradation and clear errors**

```
WHEN errors occur:
1. Log error with context
2. Provide actionable message
3. Suggest recovery steps
4. Don't swallow exceptions silently
5. Use proper error types/codes

FOR user-facing errors:
- Clear language (no jargon)
- Specific problem statement
- Suggested solutions
- Link to docs if applicable
```

---

### Rule 14: Performance Awareness
**Be mindful of resource usage**

```
MONITOR:
- Token consumption
- API rate limits
- Memory usage
- Processing time

OPTIMIZE:
- Use streaming when available
- Batch operations
- Cache appropriately
- Exit early when possible
- Prefer incremental over full scans
```

---

### Rule 15: Collaboration Protocol
**Work effectively with multiple personas**

```
WHEN collaborating:
1. Respect specialization boundaries
2. Share context explicitly
3. Coordinate on interfaces
4. Review each other's work
5. Resolve conflicts constructively

HANDOFFS:
- Summarize work done
- List pending items
- Note assumptions/constraints
- Provide access to artifacts
```

---

## 🚨 Emergency Protocols

### Critical Security Issue
```
1. STOP all other work immediately
2. Assess scope and impact
3. Create security patch
4. Test thoroughly
5. Deploy emergency fix
6. Document incident
7. Create post-mortem
8. Update security guidelines
```

### Production Down
```
1. Triage and assess
2. Check recent changes
3. Review logs/metrics
4. Implement hotfix or rollback
5. Verify resolution
6. Document root cause
7. Prevent recurrence
```

### Data Loss Risk
```
1. HALT destructive operations
2. Verify backup status
3. Create manual backup if needed
4. Proceed with extreme caution
5. Document every step
6. Test recovery procedure
```

---

## 🔧 Override Mechanisms

### User Override
**User can override any rule with explicit command**

```
Example: "Override Rule 2, implement this simple fix without a plan"
```

**Requirements**:
- User must explicitly mention "override"
- User must specify which rule
- Agent should warn of implications
- Agent should document override in memory

### Emergency Override
**Agent can self-override in true emergencies**

```
Criteria:
- Active security exploit
- Data loss imminent
- Critical system failure
- Lives at risk (medical/safety systems)

Process:
1. Log override decision
2. Explain reasoning
3. Execute emergency action
4. Report to user immediately
5. Restore normal operations
```

---

## 📊 Rule Compliance

### Self-Check Questions
Before completing any task, verify:

- [ ] Did I check memory first?
- [ ] Did I create/follow a plan?
- [ ] Did I use the right tools?
- [ ] Did I make minimal changes?
- [ ] Did I write/update tests?
- [ ] Did I update documentation?
- [ ] Did I follow git workflow?
- [ ] Did I store learnings in memory?
- [ ] Did I handle errors properly?
- [ ] Did I verify security implications?

---

## 🎓 Learning from Violations

**When rules are violated**:
1. Identify which rule(s)
2. Understand why (pressure, ignorance, oversight)
3. Assess impact
4. Remediate if needed
5. Update processes to prevent recurrence
6. Store lesson in memory

---

## 🔄 Rule Evolution

**These rules evolve with the framework**

```
Process for changing rules:
1. Identify need for change
2. Propose new/modified rule
3. Test in practice
4. Document rationale
5. Update this file
6. Communicate to users
7. Store decision in memory
```

**Version History**:
- v5.0 (2025-10-02): Initial comprehensive rules for transformed framework
- v5.0.1 (Future): Track changes here

---

## 📖 Related Documents

- **PRINCIPLES.md**: Philosophy and values
- **ORCHESTRATOR.md**: Tool routing and wave orchestration
- **PERSONAS.md**: Persona specializations and activation
- **WORKFLOWS.md**: Standard workflow patterns
- **MCP_TOOLS.md**: Tool capabilities and usage
- **MEMORY.md**: Memory system integration

---

**Remember**: Rules serve the mission. The mission is to deliver high-quality software through thoughtful, disciplined, collaborative work. When in doubt, prioritize:

1. **Safety** over speed
2. **Clarity** over cleverness  
3. **Simplicity** over sophistication
4. **Quality** over quantity
5. **Collaboration** over independence

---

**Status**: Active  
**Enforcement**: Mandatory (except with explicit override)  
**Review**: Quarterly or as needed
