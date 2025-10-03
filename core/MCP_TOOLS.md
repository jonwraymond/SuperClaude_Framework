# MCP_TOOLS.md - SuperClaude Framework Tool Reference

Comprehensive reference for all 15 configured MCP servers (+ 2 available to configure: exa, ref) with usage patterns, capabilities, and integration strategies.

---

## 🎯 Tool Categories

### Code Generation & Editing
- morphllm-fast-apply
- Magic MCP
- serena

### Analysis & Investigation
- zen
- sequential-thinking
- repomix
- serena

### Research & Documentation
- context7
- firecrawl
- exa (to configure)
- ref (to configure)
- tavily
- octocode

### Memory & Knowledge
- byterover
- basic-memory
- serena

### Testing & Validation
- playwright
- github

### Utilities
- time
- github

---

## 1. zen (BeehiveInnovations)

**Type**: Advanced reasoning and analysis suite  
**Status**: ✅ Configured  
**Priority**: Primary for complex tasks

### Capabilities

#### Core Tools
- **thinkdeep**: Multi-stage investigation and root cause analysis
- **planner**: Sequential planning with revision capabilities
- **consensus**: Multi-model consensus building
- **codereview**: Systematic code review with expert validation
- **precommit**: Pre-commit validation and change impact assessment
- **debug**: Systematic debugging and root cause analysis
- **tracer**: Code execution tracing (precision/dependencies modes)
- **challenge**: Critical thinking validation
- **chat**: General collaborative thinking
- **analyze**: Comprehensive code and architecture analysis
- **testgen**: Test generation with edge cases
- **refactor**: Refactoring analysis and recommendations
- **docgen**: Documentation generation
- **secaudit**: Security audits

### Usage Patterns

```yaml
Deep Analysis:
  command: zen_thinkdeep
  use_for: [architectural decisions, complex bugs, performance issues]
  thinking_mode: [minimal, low, medium, high, max]
  
Planning:
  command: zen_planner
  use_for: [feature planning, migration strategies]
  supports: [revision, branching, multi-step plans]
  
Code Review:
  command: zen_codereview
  use_for: [PR reviews, quality assessment]
  review_types: [full, security, performance, quick]
  
Debugging:
  command: zen_debug
  use_for: [bug investigation, root cause analysis]
  confidence_levels: [exploring, low, medium, high, very_high, certain]
```

### Best Practices
- Use appropriate thinking_mode for task complexity
- Provide continuation_id for multi-turn conversations
- Set use_assistant_model=true for expert validation
- Enable use_websearch when research is needed

---

## 2. serena (Oraios)

**Type**: Code navigation and symbol analysis  
**Status**: ✅ Configured  
**Priority**: Primary for code operations

### Capabilities
- Symbol finding and analysis (find_symbol, get_symbols_overview)
- Reference tracking (find_referencing_symbols)
- Code modification (replace_symbol_body, insert_before/after_symbol)
- Pattern search (search_for_pattern)
- File operations (read_file, list_dir, find_file)
- Project memory (write_memory, read_memory, list_memories)
- Impact analysis (analyze_impact)

### Usage Patterns

```yaml
Code Navigation:
  - find_symbol(name_path, relative_path?, depth?)
  - get_symbols_overview(relative_path)
  - find_referencing_symbols(name_path, relative_path)
  
Code Modification:
  - replace_symbol_body(name_path, relative_path, body)
  - insert_after_symbol(name_path, relative_path, body)
  - insert_before_symbol(name_path, relative_path, body)
  
Analysis:
  - search_for_pattern(substring_pattern, relative_path?)
  - analyze_impact(symbol_name, relative_path)
```

### Best Practices
- Start with get_symbols_overview for new files
- Use find_symbol for specific symbols
- Call think_about_collected_information after searches
- Store important findings in memory

---

## 3. sequential-thinking

**Type**: Structured reasoning  
**Status**: ✅ Configured  
**Priority**: Secondary for systematic analysis

### Capabilities
- Step-by-step problem decomposition
- Thought branching and revision
- Chain-of-thought reasoning
- Hypothesis generation and testing

### Usage Patterns

```yaml
Problem Solving:
  thought: "Current reasoning step"
  thought_number: 1
  total_thoughts: 5
  next_thought_needed: true
  is_revision: false
  branch_id?: "alternative-approach"
```

### Best Practices
- Adjust total_thoughts as understanding evolves
- Use branching for exploring alternatives
- Mark revisions explicitly with revises_thought
- Don't hesitate to add more thoughts if needed

---

## 4. context7 (Upstash)

**Type**: Official library/API documentation  
**Status**: ✅ Configured  
**Priority**: Primary for documentation

### Capabilities
- Resolve library IDs from names
- Fetch up-to-date documentation
- Version-specific documentation
- Framework and API references

### Usage Patterns

```yaml
Documentation Lookup:
  1. resolve-library-id(libraryName)
  2. get-library-docs(context7CompatibleLibraryID, topic?, tokens?)
  
Examples:
  - "/mongodb/docs"
  - "/vercel/next.js/v14.3.0"
  - "/supabase/supabase"
```

### Best Practices
- Always call resolve-library-id first
- Cache results for repeated lookups
- Specify version for consistency
- Use topic parameter to focus results

---

## 5. firecrawl

**Type**: Web scraping and crawling  
**Status**: ✅ Configured (API key required)  
**Priority**: Primary for web research

### Capabilities
- Single page scraping (firecrawl_scrape)
- Site mapping (firecrawl_map)
- Multi-page crawling (firecrawl_crawl)
- Web search (firecrawl_search)
- Structured extraction (firecrawl_extract)
- Batch operations (firecrawl_batch_scrape)

### Usage Patterns

```yaml
Single Page:
  firecrawl_scrape(url, formats?, maxAge?)
  
Site Discovery:
  firecrawl_map(url) → list of URLs
  
Multi-Page:
  firecrawl_crawl(url, maxDiscoveryDepth?, limit?)
  
Web Search:
  firecrawl_search(query, limit?, sources?)
```

### Best Practices
- Use maxAge for faster cached results
- Start with map to discover structure
- Use scrape for known URLs
- Use search for open-ended research
- Batch operations for multiple URLs

---

## 6. playwright

**Type**: Browser automation and testing  
**Status**: ✅ Configured  
**Priority**: Primary for UI testing

### Capabilities
- E2E testing and workflow validation
- Visual testing and screenshots
- Performance measurement
- User interaction simulation
- Accessibility testing

### Usage Patterns

```yaml
Testing:
  - E2E test scenarios
  - User workflow validation
  - Performance metrics collection
  - Visual regression testing
  
Performance:
  - Core Web Vitals measurement
  - Load time analysis
  - Resource utilization
```

### Best Practices
- Use for user-facing validation
- Combine with Magic MCP for UI development
- Measure performance metrics
- Test accessibility compliance

---

## 7. repomix

**Type**: Codebase packing  
**Status**: ✅ Configured  
**Priority**: Primary for context preparation

### Capabilities
- Pack local codebases (pack_codebase)
- Pack remote repositories (pack_remote_repository)
- Attach packed output (attach_packed_output)
- Grep packed content (grep_repomix_output)
- Read packed output (read_repomix_output)

### Usage Patterns

```yaml
Local Pack:
  pack_codebase(directory, style?, compress?)
  
Remote Pack:
  pack_remote_repository(remote, style?, compress?)
  
Search:
  grep_repomix_output(outputId, pattern, contextLines?)
```

### Best Practices
- Use XML style for structured processing
- Enable compression for large repos
- Use grep for incremental retrieval
- Pack before deep analysis tasks

---

## 8. morphllm-fast-apply

**Type**: Fast code editing  
**Status**: ✅ Configured (API key required)  
**Priority**: Primary for code changes

### Capabilities
- Fast surgical edits (edit_file)
- Tiny line-based edits (tiny_edit_file)
- File operations (read, write, list)
- Directory management

### Usage Patterns

```yaml
Quick Edits:
  edit_file(path, code_edit, instruction)
  
Line Edits:
  tiny_edit_file(path, edits[])
  
File Ops:
  read_file(path), write_file(path, content)
```

### Best Practices
- Use for focused, surgical changes
- Include context with // ... existing code ...
- Provide clear instructions
- Use tiny_edit for single-line changes

---

## 9. octocode

**Type**: GitHub code exploration  
**Status**: ✅ Configured (GitHub token required)  
**Priority**: Primary for code examples

### Capabilities
- Search code across GitHub (githubSearchCode)
- Get file contents (githubGetFileContent)
- View repository structure (githubViewRepoStructure)
- Search repositories (githubSearchRepositories)

### Usage Patterns

```yaml
Code Search:
  githubSearchCode(query, repo?, language?, path?)
  
File Content:
  githubGetFileContent(owner, repo, path, branch?)
  
Structure:
  githubViewRepoStructure(owner, repo, path?, branch?)
```

### Best Practices
- Use for finding real-world examples
- Combine with context7 for patterns
- Filter by language and stars
- Check multiple repos for patterns

---

## 10. byterover

**Type**: Durable knowledge storage  
**Status**: ✅ Configured  
**Priority**: Primary for memory

### Capabilities
- Retrieve knowledge (byterover_retrieve_knowledge)
- Store knowledge (byterover_store_knowledge)

### Usage Patterns

```yaml
Retrieve:
  byterover_retrieve_knowledge(query, limit?)
  
Store:
  byterover_store_knowledge(messages)
  - Include timestamps
  - Preserve code in triple backticks
  - Add context and provenance
```

### Best Practices
- Retrieve at start of every task
- Store insights with timestamps
- Include complete code/commands
- Add provenance (URLs, file paths)
- Surface conflict resolution URLs

---

## 11. basic-memory (Obsidian)

**Type**: Graph-based memory  
**Status**: ✅ Configured  
**Priority**: Primary for knowledge graph

### Capabilities
- Create/edit/delete notes (write_note, edit_note, delete_note)
- Search notes (search_notes)
- Build context (build_context)
- Recent activity (recent_activity)
- Project management (create/list/switch projects)

### Usage Patterns

```yaml
Note Operations:
  write_note(title, content, folder, tags?)
  edit_note(identifier, operation, content)
  
Search:
  search_notes(query, page?, page_size?)
  
Context:
  build_context(url, depth?, max_related?)
```

### Best Practices
- Use WikiLinks [[...]] for connections
- Apply canonical tags from index
- Write ≥3 observations per note
- Include ≥2 WikiLinks per update
- Cross-reference with byterover

---

## 12. Magic MCP

**Type**: UI component generation  
**Status**: ✅ Configured (API key required)  
**Priority**: Primary for frontend

### Capabilities
- Modern UI component generation
- Design system integration
- React/Vue/Angular support
- Responsive design patterns

### Usage Patterns

```yaml
Component Generation:
  - Describe desired component
  - Specify framework (React/Vue/etc.)
  - Include design requirements
  - Request accessibility features
```

### Best Practices
- Use for UI components only
- Combine with playwright for testing
- Specify design system if available
- Request WCAG compliance

---

## 13. github

**Type**: Repository operations  
**Status**: ✅ Configured (PAT required)  
**Priority**: Primary for VCS

### Capabilities
- Search repositories/code/issues
- File operations (read, create, update)
- Branch management
- Pull request workflows
- Issue management

### Usage Patterns

```yaml
File Ops:
  create_or_update_file(owner, repo, path, content, branch, message)
  
PR Workflow:
  create_branch() → push_files() → create_pull_request()
  
Issues:
  create_issue(title, body?) → add_issue_comment()
```

### Best Practices
- Always branch before changes
- Create PR for review
- Never commit directly to main
- Include descriptive messages

---

## 14. tavily

**Type**: Web search  
**Status**: ✅ Configured (API key in URL)  
**Priority**: Secondary for general search

### Capabilities
- General web search
- News and current information
- Broad topic research

### Usage Patterns

```yaml
Search:
  Use for general queries
  Supplement with firecrawl for deep research
```

### Best Practices
- Use for general queries
- Combine with firecrawl for details
- Verify results with multiple sources

---

## 15. time

**Type**: Time operations  
**Status**: ✅ Configured  
**Priority**: Utility

### Capabilities
- Get current time (get_current_time)
- Convert timezones (convert_time)

### Usage Patterns

```yaml
Current:
  get_current_time(timezone?)
  
Convert:
  convert_time(datetime, from_timezone, to_timezone)
```

### Best Practices
- Use IANA timezone names
- Store timestamps with timezone info
- Use for logging and scheduling

---

## 16. ref

**Type**: Documentation search  
**Status**: ✅ Configured  
**Priority**: High for documentation

### Capabilities
- Token-efficient documentation search
- Agentic search with context filtering
- Searches public docs (web/GitHub)
- Supports private repos and PDFs
- Intelligent page section extraction
- Minimizes context rot

### Tools Provided
- `ref_search_documentation(query)` - Search for technical documentation
- `ref_read_url(url)` - Fetch and convert URL content to markdown

### Usage Patterns

```yaml
Search:
  ref_search_documentation(query="React hooks useState best practices")
  # Returns relevant URLs and snippets
  
Read:
  ref_read_url(url="https://docs.example.com/api/endpoint")
  # Returns up to 5k tokens of most relevant content
  
Iterative:
  1. Search with broad query
  2. Read relevant results
  3. Refine search based on findings
  4. Repeat until answer found
```

### Best Practices
- Use full sentences for queries
- Leverage session history for filtering
- Combine search + read for deep research
- Token-efficient (~4k vs 20k+ with raw scraping)
- Integrates with OpenAI Deep Research

### Configuration
```json
"ref": {
  "command": "npx",
  "args": ["-y", "ref-tools-mcp@latest"],
  "env": {
    "REF_API_KEY": "ref-f8784ab7c8347c7d3453"
  }
}
```

---

## 17. exa

**Type**: Deep code research & web search  
**Status**: ✅ Configured  
**Priority**: High for research

### Capabilities
- Deep code context retrieval
- Quality code examples
- Company research
- Web crawling
- Deep researcher (async research)
- Best practices and patterns

### Tools Provided
- `get_code_context_exa(query, tokensNum?)` - Retrieve relevant code context
- `web_search_exa(query, numResults?)` - Perform web searches
- `company_research(company_name)` - Research companies
- `crawling_exa(url)` - Crawl websites
- `deep_researcher_start(query)` - Start async deep research
- `deep_researcher_check(research_id)` - Check research status

### Usage Patterns

```yaml
Code Context:
  get_code_context_exa(
    query="Next.js middleware authentication",
    tokensNum="dynamic"  # or 1000-50000
  )
  
Web Search:
  web_search_exa(
    query="latest React 19 features",
    numResults=5
  )
  
Deep Research:
  # Start research
  research_id = deep_researcher_start(
    query="Kubernetes security best practices 2025"
  )
  # Check later
  results = deep_researcher_check(research_id)
```

### Best Practices
- Use `dynamic` tokens for optimal efficiency
- Specify exact token count only if needed
- Combine with context7 for comprehensive research
- Use deep researcher for complex topics
- Cache results to minimize API calls

### Configuration
```json
"exa": {
  "command": "npx",
  "args": ["-y", "exa-mcp-server"],
  "env": {
    "EXA_API_KEY": "4e794a0d-ad65-4e89-8753-ed4ba1cffd96"
  }
}
```

---

## 🎯 Tool Selection Matrix

| Task Type | Primary | Secondary | Tertiary |
|-----------|---------|-----------|----------|
| Architecture | zen (thinkdeep) | sequential-thinking | repomix |
| Frontend | Magic MCP | playwright | morphllm-fast-apply |
| Backend | context7 | zen (thinkdeep) | serena |
| Research | firecrawl | context7 | exa/ref |
| Analysis | zen (debug) | serena | repomix |
| Code Edits | morphllm-fast-apply | serena | - |
| Testing | playwright | zen (codereview) | - |
| Memory | byterover | basic-memory | serena |
| Documentation | context7 | byterover | firecrawl |

---

## 🔄 Common Workflows

### Research Workflow
```
context7 → firecrawl → exa → ref → octocode → byterover
```

### Code Implementation
```
serena → context7 → morphllm-fast-apply → playwright → byterover
```

### Deep Analysis
```
repomix → zen:thinkdeep → sequential-thinking → serena → byterover
```

### Complex Feature
```
Wave 1: serena + repomix (discovery)
Wave 2: zen:planner + sequential-thinking (planning)
Wave 3: context7 + firecrawl (research)
Wave 4: morphllm-fast-apply + Magic MCP (implementation)
Wave 5: playwright + zen:codereview (validation)
Wave 6: byterover + basic-memory (documentation)
```

---

**Version**: 5.0 (SuperClaude Framework Full Transformation)  
**Last Updated**: 2025-10-02  
**Status**: Production Ready
