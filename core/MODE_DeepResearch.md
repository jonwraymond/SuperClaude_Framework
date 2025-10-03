# MODE: Deep Research

**Version**: 5.0  
**Last Updated**: 2025-10-02  
**Status**: Production Ready

---

## 🎯 Purpose

Enable autonomous, comprehensive research across web sources, documentation, and code repositories using MCP tools optimized for discovery and analysis.

---

## 🔬 Research Capabilities

### Web Research (Firecrawl MCP)
**For**: General web content, documentation sites, blogs, tutorials

**Tools**:
- `firecrawl_search`: Real-time web search with content extraction
- `firecrawl_scrape`: Extract content from specific URLs
- `firecrawl_map`: Discover site structure and links
- `firecrawl_crawl`: Deep crawl for comprehensive coverage

**Use Cases**:
- Finding best practices and patterns
- Discovering framework documentation
- Researching solutions to problems
- Gathering multiple perspectives

### Code/Documentation Search (Exa MCP) ⚠️ **Requires Configuration**
**For**: Code examples, technical documentation, API references

**Tools**:
- `get_code_context_exa`: High-quality code examples and SDK documentation
- `web_search_exa`: Technical web search with code context

**Use Cases**:
- Finding implementation examples
- API usage patterns
- Library-specific solutions
- Framework best practices

### Documentation Search (Ref MCP) ⚠️ **Requires Configuration**
**For**: Official documentation, public/private repos, PDFs

**Tools**:
- `ref_search_documentation`: Search public and private docs
- `ref_read_url`: Read documentation content

**Use Cases**:
- Official library documentation
- Private repository docs
- Technical specifications
- Framework guides

### Official Docs (Context7 MCP)
**For**: Official library/API documentation with version specificity

**Tools**:
- `resolve-library-id`: Find correct library identifier
- `get-library-docs`: Fetch up-to-date documentation

**Use Cases**:
- Official API references
- Framework documentation
- Library-specific guides
- Version-specific information

---

## 🌊 Research Workflow

### Wave 1: Initial Discovery (5-10 min)
**Goal**: Identify research scope and primary sources

```
1. Define research question clearly
2. Identify primary tool:
   - Web content → Firecrawl
   - Code examples → Exa (if configured) or Context7
   - Official docs → Context7 → Ref (if configured)
   - Private docs → Ref (if configured)
3. Perform initial searches (2-3 queries)
4. Assess quality and relevance
5. Decide on depth needed
```

**Tools**: firecrawl_search, context7 (resolve-library-id)

**Exit Criteria**: Clear understanding of information landscape

---

### Wave 2: Deep Dive (10-20 min)
**Goal**: Gather comprehensive information from identified sources

```
1. Scrape/crawl primary sources
2. Extract code examples
3. Read official documentation
4. Gather multiple perspectives
5. Organize findings by topic
```

**Tools**: 
- firecrawl_scrape/crawl
- get-library-docs (Context7)
- get_code_context_exa (if configured)
- ref_read_url (if configured)

**Exit Criteria**: Sufficient information collected for analysis

---

### Wave 3: Synthesis (5-15 min)
**Goal**: Analyze and synthesize research findings

```
1. Compare approaches across sources
2. Identify patterns and best practices
3. Note trade-offs and caveats
4. Validate against multiple sources
5. Form recommendations
```

**Tools**: sequential_thinking, zen (thinkdeep)

**Exit Criteria**: Clear recommendations with rationale

---

### Wave 4: Documentation (5-10 min)
**Goal**: Store research findings for future use

```
1. Store in byterover with complete context
2. Create note in Basic Memory if formal decision
3. Tag and categorize appropriately
4. Link to related knowledge
```

**Tools**: byterover-store-knowledge, write_note

**Exit Criteria**: Research preserved and discoverable

---

## 📋 Research Patterns

### Pattern 1: Best Practice Discovery
**When**: Need to understand current best practices

```
1. firecrawl_search("current best practices for X")
2. firecrawl_search("X anti-patterns and pitfalls")
3. context7: get official documentation
4. Synthesize with zen (thinkdeep)
5. Store with byterover-store-knowledge
```

### Pattern 2: Implementation Research
**When**: Need code examples for specific functionality

```
1. context7: resolve-library-id → get-library-docs
2. exa: get_code_context_exa (if configured)
3. firecrawl_search("X implementation examples")
4. Compare approaches
5. Store with complete code snippets
```

### Pattern 3: Problem Solution Research
**When**: Troubleshooting specific issue

```
1. firecrawl_search("X error message solution")
2. firecrawl_search("X troubleshooting guide")
3. ref_search_documentation (if configured for relevant repos)
4. Validate solution applicability
5. Store root cause + solution
```

### Pattern 4: Comparative Analysis
**When**: Evaluating alternatives (libraries, approaches, patterns)

```
1. For each option:
   - firecrawl_search("X vs Y comparison")
   - context7: get official docs
   - firecrawl_map: discover community resources
2. zen (consensus) for multi-model analysis
3. Create comparison matrix
4. write_note with decision rationale
```

### Pattern 5: Deep Technical Dive
**When**: Need comprehensive understanding of complex topic

```
1. context7: official documentation (foundation)
2. firecrawl_crawl: comprehensive site coverage
3. exa: code examples and patterns (if configured)
4. ref: private docs if available (if configured)
5. zen (thinkdeep): deep analysis
6. write_note: formal knowledge document
```

---

## 🎯 Tool Selection Matrix

| Research Need | Primary Tool | Secondary | Tertiary |
|---------------|-------------|-----------|----------|
| **Official docs** | Context7 | Ref | Firecrawl |
| **Code examples** | Exa ⚠️ | Context7 | Firecrawl |
| **Web content** | Firecrawl | Ref | - |
| **Private docs** | Ref ⚠️ | - | - |
| **Best practices** | Firecrawl | Context7 | Exa |
| **API reference** | Context7 | Ref | Firecrawl |
| **Troubleshooting** | Firecrawl | Exa | Context7 |
| **Comparisons** | Firecrawl | Multiple | All |

⚠️ = Requires configuration (see MCP_TOOLS.md)

---

## 🚨 Research Best Practices

### DO:
✅ **Start with official docs** (Context7) when available  
✅ **Validate across multiple sources** (3+ sources minimum)  
✅ **Store complete findings** with code/examples  
✅ **Attribute sources** clearly in research notes  
✅ **Use semantic search** for better discovery  
✅ **Limit initial scope** then expand as needed  
✅ **Check publication dates** for currency  

### DON'T:
❌ **Trust single source** without validation  
❌ **Skip official documentation** check  
❌ **Store without context** (date, source, rationale)  
❌ **Over-crawl** (respect rate limits)  
❌ **Ignore version specificity** (libraries change!)  
❌ **Mix research types** without clear goals  
❌ **Forget to store findings** in memory  

---

## 🔧 Configuration Requirements

### Firecrawl (Ready)
✅ **Status**: Configured and ready  
**Setup**: None needed

### Context7 (Ready)
✅ **Status**: Configured and ready  
**Setup**: None needed

### Exa (Needs Configuration) ⚠️
❌ **Status**: Not configured  
**Setup Required**:
```
1. Get Exa API key from https://exa.ai
2. Configure in MCP settings
3. Test with: get_code_context_exa(query="test")
```

### Ref (Needs Configuration) ⚠️
❌ **Status**: Not configured  
**Setup Required**:
```
1. Configure Ref MCP server
2. Add documentation sources
3. Test with: ref_search_documentation(query="test")
```

---

## 📊 Research Quality Checklist

Before concluding research:

- [ ] Checked official documentation (Context7)
- [ ] Validated across 3+ independent sources
- [ ] Found code examples (if applicable)
- [ ] Identified version-specific considerations
- [ ] Noted trade-offs and caveats
- [ ] Checked publication dates/currency
- [ ] Stored findings with complete context
- [ ] Tagged and categorized for discovery
- [ ] Linked to related knowledge
- [ ] Attributed all sources

---

## 🎯 Quick Start Examples

### Example 1: Research FastAPI authentication patterns
```
1. context7: resolve-library-id("FastAPI") → get-library-docs()
2. firecrawl_search("FastAPI authentication best practices 2025")
3. firecrawl_scrape(top 3 results)
4. exa: get_code_context_exa("FastAPI JWT authentication") [if configured]
5. zen (thinkdeep): analyze and synthesize
6. byterover-store-knowledge() with complete examples
```

### Example 2: Compare state management libraries
```
1. For each: Redux, Zustand, Jotai
   - context7: get-library-docs()
   - firecrawl_search("X vs Y comparison 2025")
2. zen (consensus): multi-model analysis
3. Create comparison matrix
4. write_note() with decision rationale
```

### Example 3: Troubleshoot specific error
```
1. firecrawl_search("exact error message")
2. firecrawl_search("framework + error troubleshooting")
3. context7: get relevant framework docs
4. ref_search_documentation() [if configured for repo]
5. Validate solution applicability
6. byterover-store-knowledge() with root cause + fix
```

---

## 🔗 Integration

### With Other Modes
- **MODE_Introspection**: Research past decisions and their outcomes
- **MODE_Brainstorming**: Research to feed ideation
- **MODE_Task_Management**: Research as task prerequisite

### With Personas
- **requirements-analyst**: Research for requirement elicitation
- **architect**: Research architectural patterns
- **security**: Research security best practices
- **python-expert**: Research Python-specific solutions

### With Workflows
- Every workflow can trigger research
- Research findings stored in memory
- Research quality gates before decisions

---

## 📖 Related Documents

- **MCP_TOOLS.md**: Tool-specific configuration
- **WORKFLOWS.md**: Research workflow patterns
- **MEMORY.md**: Storing research findings
- **RULES.md**: Research quality standards

---

**Activation**: Use `--workflow-mode=research` or mention "research", "investigate", "find information"  
**Quality Standard**: Multi-source validation required  
**Storage**: All research must be stored in memory with attribution
