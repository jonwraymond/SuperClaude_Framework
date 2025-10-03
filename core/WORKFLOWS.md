# WORKFLOWS.md - SuperClaude Framework Common Workflows

Standard workflow patterns for common development scenarios with tool orchestration and best practices.

---

## 🎯 Core Workflow Patterns

### 1. Feature Implementation Workflow

**Complexity**: Moderate  
**Duration**: 1-4 hours  
**Wave Mode**: Auto (if >5 files)

```yaml
Phase 1 - Discovery:
  tools: [serena, repomix]
  actions:
    - Understand existing codebase structure
    - Identify related components
    - Map dependencies
  outputs: Context map, affected files list

Phase 2 - Research:
  tools: [context7, firecrawl, octocode]
  actions:
    - Look up framework patterns
    - Find similar implementations
    - Research best practices
  outputs: Pattern examples, documentation references

Phase 3 - Planning:
  tools: [zen (planner), sequential-thinking]
  actions:
    - Create detailed implementation plan
    - Identify potential issues
    - Define testing strategy
  outputs: Implementation plan, task list

Phase 4 - Implementation:
  tools: [morphllm-fast-apply, serena]
  actions:
    - Make code changes
    - Follow established patterns
    - Maintain consistency
  outputs: Modified code files

Phase 5 - Testing:
  tools: [playwright, zen (codereview)]
  actions:
    - Run E2E tests
    - Validate functionality
    - Code quality review
  outputs: Test results, review findings

Phase 6 - Documentation:
  tools: [byterover, basic-memory]
  actions:
    - Store implementation insights
    - Document patterns used
    - Update project knowledge
  outputs: Knowledge entries, linked notes
```

---

### 2. Bug Investigation & Fix Workflow

**Complexity**: Variable (Simple to Complex)  
**Duration**: 30min - 4 hours  
**Wave Mode**: Auto (if complexity >0.7)

```yaml
Phase 1 - Initial Investigation:
  tools: [serena, repomix]
  actions:
    - Reproduce the issue
    - Gather error logs/stack traces
    - Identify affected components
  outputs: Issue description, initial hypothesis

Phase 2 - Deep Analysis:
  tools: [zen (debug), sequential-thinking]
  actions:
    - Systematic root cause analysis
    - Test hypotheses
    - Trace execution flow
  outputs: Root cause identification, evidence

Phase 3 - Research Solutions:
  tools: [context7, firecrawl, octocode]
  actions:
    - Look up similar issues
    - Find proven solutions
    - Review framework docs
  outputs: Solution approaches, examples

Phase 4 - Implementation:
  tools: [morphllm-fast-apply, serena]
  actions:
    - Implement fix
    - Add regression tests
    - Validate solution
  outputs: Fixed code, test coverage

Phase 5 - Verification:
  tools: [playwright, zen (codereview)]
  actions:
    - Test fix in isolation
    - Run full test suite
    - Verify no side effects
  outputs: Verification results

Phase 6 - Knowledge Capture:
  tools: [byterover, basic-memory]
  actions:
    - Document root cause
    - Store solution pattern
    - Link related issues
  outputs: Troubleshooting knowledge
```

---

### 3. Code Review Workflow

**Complexity**: Simple to Moderate  
**Duration**: 30min - 2 hours  
**Wave Mode**: Optional

```yaml
Phase 1 - Context Gathering:
  tools: [github, serena, repomix]
  actions:
    - Fetch PR changes
    - Understand modifications
    - Map affected components
  outputs: Change summary, file list

Phase 2 - Quality Analysis:
  tools: [zen (codereview), sequential-thinking]
  actions:
    - Code quality assessment
    - Security review
    - Performance implications
  outputs: Review findings, severity levels

Phase 3 - Testing Validation:
  tools: [playwright, serena]
  actions:
    - Verify test coverage
    - Run E2E tests
    - Check edge cases
  outputs: Test results, coverage gaps

Phase 4 - Feedback & Documentation:
  tools: [github, byterover]
  actions:
    - Provide review comments
    - Document patterns
    - Suggest improvements
  outputs: PR comments, knowledge entries
```

---

### 4. Research & Documentation Workflow

**Complexity**: Simple to Moderate  
**Duration**: 1-3 hours  
**Wave Mode**: Optional

```yaml
Phase 1 - Information Gathering:
  tools: [context7, firecrawl, exa, ref, tavily]
  actions:
    - Official documentation
    - Web research
    - Code examples
    - Community patterns
  outputs: Research materials, references

Phase 2 - Analysis & Synthesis:
  tools: [zen (thinkdeep), sequential-thinking]
  actions:
    - Analyze findings
    - Identify patterns
    - Synthesize insights
  outputs: Comprehensive understanding

Phase 3 - Documentation:
  tools: [serena, basic-memory]
  actions:
    - Create documentation
    - Add code examples
    - Link related concepts
  outputs: Documentation files, notes

Phase 4 - Knowledge Storage:
  tools: [byterover, basic-memory]
  actions:
    - Store validated patterns
    - Link to sources
    - Tag appropriately
  outputs: Durable knowledge entries
```

---

### 5. Architecture Design Workflow

**Complexity**: Complex  
**Duration**: 2-8 hours  
**Wave Mode**: Required

```yaml
Phase 1 - Requirements Analysis:
  tools: [serena, repomix, sequential-thinking]
  actions:
    - Understand current architecture
    - Identify constraints
    - Define requirements
  outputs: Requirements document

Phase 2 - Research:
  tools: [context7, firecrawl, octocode]
  actions:
    - Study architectural patterns
    - Review similar systems
    - Best practices research
  outputs: Pattern catalog, examples

Phase 3 - Design Planning:
  tools: [zen (thinkdeep/planner), sequential-thinking]
  actions:
    - Create architectural design
    - Evaluate trade-offs
    - Consider alternatives
  outputs: Architecture design document

Phase 4 - Consensus Building:
  tools: [zen (consensus)]
  actions:
    - Multi-model validation
    - Evaluate alternatives
    - Risk assessment
  outputs: Validated design, decision record

Phase 5 - Documentation:
  tools: [byterover, basic-memory]
  actions:
    - Document decisions
    - Create ADR
    - Store rationale
  outputs: Architecture documentation, ADRs
```

---

### 6. Performance Optimization Workflow

**Complexity**: Moderate to Complex  
**Duration**: 2-6 hours  
**Wave Mode**: Auto (if >3 files)

```yaml
Phase 1 - Profiling:
  tools: [playwright, serena]
  actions:
    - Measure current performance
    - Identify bottlenecks
    - Collect metrics
  outputs: Performance baseline, hotspots

Phase 2 - Analysis:
  tools: [zen (thinkdeep), sequential-thinking]
  actions:
    - Analyze bottlenecks
    - Prioritize optimizations
    - Plan improvements
  outputs: Optimization strategy

Phase 3 - Research:
  tools: [context7, firecrawl, octocode]
  actions:
    - Look up optimization patterns
    - Find proven techniques
    - Review best practices
  outputs: Optimization approaches

Phase 4 - Implementation:
  tools: [morphllm-fast-apply, serena]
  actions:
    - Apply optimizations
    - Maintain correctness
    - Preserve readability
  outputs: Optimized code

Phase 5 - Validation:
  tools: [playwright, zen (codereview)]
  actions:
    - Measure improvements
    - Verify correctness
    - Check for regressions
  outputs: Performance improvements verified

Phase 6 - Documentation:
  tools: [byterover, basic-memory]
  actions:
    - Document optimizations
    - Store techniques
    - Link metrics
  outputs: Optimization knowledge
```

---

### 7. Security Audit Workflow

**Complexity**: Complex  
**Duration**: 4-8 hours  
**Wave Mode**: Required

```yaml
Phase 1 - Scope Definition:
  tools: [serena, repomix]
  actions:
    - Map attack surface
    - Identify sensitive areas
    - Define audit scope
  outputs: Audit scope document

Phase 2 - Vulnerability Scanning:
  tools: [zen (secaudit), serena]
  actions:
    - OWASP Top 10 check
    - Dependency vulnerabilities
    - Code pattern analysis
  outputs: Vulnerability findings

Phase 3 - Threat Modeling:
  tools: [zen (thinkdeep), sequential-thinking]
  actions:
    - Identify threat vectors
    - Assess risk levels
    - Prioritize remediation
  outputs: Threat model, risk assessment

Phase 4 - Remediation:
  tools: [morphllm-fast-apply, context7]
  actions:
    - Fix vulnerabilities
    - Harden security controls
    - Update dependencies
  outputs: Security patches

Phase 5 - Validation:
  tools: [zen (secaudit), playwright]
  actions:
    - Re-scan for issues
    - Test security controls
    - Verify fixes
  outputs: Security validation report

Phase 6 - Documentation:
  tools: [byterover, basic-memory]
  actions:
    - Document findings
    - Store remediation patterns
    - Update security knowledge
  outputs: Security documentation
```

---

## 🔄 Memory Workflow (Applied to All)

**Before Every Task**:
```yaml
1. byterover_retrieve_knowledge(query, limit=5)
   - Gather relevant prior knowledge
   - Identify related patterns
   
2. basic_memory__search_notes(query)
   - Find related notes
   - Build context graph
   
3. basic_memory__build_context(url, depth=1)
   - Construct working context
```

**During Task**:
```yaml
1. basic_memory__write_note(...)
   - Log ≥3 observations
   - Add ≥2 [[WikiLinks]]
   - Apply canonical #tags
   
2. (Continue work with tools)
```

**After Task**:
```yaml
1. basic_memory__write_note(summary)
   - Capture outcomes
   - Link related concepts
   - Note follow-ups
   
2. byterover_store_knowledge(insights)
   - Store with timestamps
   - Include code in triple backticks
   - Add provenance (URLs, paths)
```

---

## 🎨 Persona-Specific Workflows

### Architect Persona
- Emphasizes design and long-term thinking
- Uses zen (thinkdeep) + sequential-thinking heavily
- Focus on system-wide impacts

### Frontend Persona
- Prioritizes Magic MCP + playwright
- Accessibility and performance focused
- User-centric validation

### Backend Persona
- Relies on context7 + zen (thinkdeep)
- Security and reliability first
- API design emphasis

### Analyzer Persona
- Evidence-based investigation
- zen (debug) + sequential-thinking
- Systematic root cause focus

---

## 🚨 Emergency Protocols

### Critical Bug (P0)
```yaml
1. Immediate triage with zen (debug)
2. Skip planning, focus on fix
3. Minimal validation before deploy
4. Document post-mortem after
```

### Production Incident
```yaml
1. Gather logs/metrics immediately
2. zen (debug) for quick diagnosis
3. Implement hotfix
4. Full investigation follows
```

---

**Version**: 5.0 (SuperClaude Framework Full Transformation)  
**Last Updated**: 2025-10-02  
**Status**: Production Ready
