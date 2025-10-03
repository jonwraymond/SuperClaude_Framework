# Exa and Ref MCP Server Setup Guide

**Date**: 2025-10-02  
**Status**: ✅ Configured and Active  
**Framework**: SuperClaude Framework v5.0

---

## Overview

This guide documents the setup and usage of two critical research and documentation MCP servers:

1. **Ref** - Token-efficient documentation search
2. **Exa** - Deep code research and web intelligence

Both servers are now fully configured and operational in both global Claude config (`~/.claude.json`) and desktop config.

---

## 1. Ref MCP Server

### Purpose
Ref provides token-efficient, agentic documentation search that minimizes context rot and maximizes relevance.

### Key Features
- **Token Efficiency**: Returns ~4k tokens vs 20k+ with raw web scraping
- **Agentic Search**: Filters repeated results across session
- **Smart Extraction**: Returns only relevant 5k token sections
- **Multi-Source**: Searches public docs, GitHub, private repos, PDFs
- **Session Context**: Uses search history to refine results

### Tools Available

#### 1. `ref_search_documentation(query)`
Search for technical documentation across all indexed sources.

**Parameters:**
- `query` (required): Full sentence or question about the topic

**Example:**
```javascript
ref_search_documentation({
  query: "React hooks useState and useEffect lifecycle"
})
```

**Returns:**
- URLs of relevant documentation
- Snippets with context
- Relevance scores

#### 2. `ref_read_url(url)`
Fetch content from a URL and convert to markdown with intelligent section extraction.

**Parameters:**
- `url` (required): The full URL to fetch

**Example:**
```javascript
ref_read_url({
  url: "https://react.dev/reference/react/useState"
})
```

**Returns:**
- Up to 5k tokens of most relevant content
- Markdown formatted
- Contextually filtered based on search history

### Usage Patterns

#### Pattern 1: Simple Search
```yaml
Goal: Find specific API documentation

Steps:
  1. Search: ref_search_documentation("API authentication methods")
  2. Review: Check returned URLs and snippets
  3. Read: ref_read_url(most_relevant_url)
```

#### Pattern 2: Iterative Research
```yaml
Goal: Deep understanding of complex topic

Steps:
  1. Broad Search: "Kubernetes networking"
  2. Read Results: Top 2-3 URLs
  3. Refined Search: "Kubernetes CNI plugins comparison"
  4. Read Results: Specific implementation docs
  5. Final Search: "Kubernetes CNI security best practices"
```

#### Pattern 3: Integration with Other Tools
```yaml
Workflow:
  1. ref_search_documentation() → Find documentation
  2. context7.get-library-docs() → Get code examples
  3. exa.get_code_context_exa() → Find real implementations
  4. byterover.store-knowledge() → Save findings
```

### Best Practices

1. **Use Full Sentences**
   - ❌ Bad: `react hooks`
   - ✅ Good: `React hooks best practices for managing state`

2. **Leverage Session Context**
   - Ref filters out previously returned results
   - Refine queries to dig deeper without repetition

3. **Combine Tools**
   - Start with ref for docs
   - Use context7 for official library docs
   - Use exa for code examples

4. **Token Management**
   - Ref automatically limits to 5k tokens per read
   - Much more efficient than raw scraping (20k+ tokens)

### Configuration

**Desktop Config** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
"ref": {
  "command": "npx",
  "args": ["-y", "ref-tools-mcp@latest"],
  "env": {
    "REF_API_KEY": "ref-f8784ab7c8347c7d3453"
  }
}
```

**Global Config** (`~/.claude.json`):
```json
"ref": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "ref-tools-mcp@latest"],
  "env": {
    "REF_API_KEY": "ref-f8784ab7c8347c7d3453"
  }
}
```

---

## 2. Exa MCP Server

### Purpose
Exa provides deep code research, quality examples, and comprehensive web intelligence.

### Key Features
- **Code Context**: Retrieve 100-1000+ useful tokens dynamically
- **Web Search**: Real-time web searches with content scraping
- **Company Research**: Gather company information
- **Crawling**: Extract content from specific URLs
- **Deep Research**: Async research for complex topics

### Tools Available

#### 1. `get_code_context_exa(query, tokensNum?)`
Retrieve relevant code context for programming tasks.

**Parameters:**
- `query` (required): Search query for code context
- `tokensNum` (optional): `"dynamic"` (default) or 1000-50000

**Examples:**
```javascript
// Dynamic mode (recommended)
get_code_context_exa({
  query: "Next.js middleware authentication with JWT",
  tokensNum: "dynamic"
})

// Fixed token count
get_code_context_exa({
  query: "React custom hooks for API calls",
  tokensNum: 5000
})
```

**Returns:**
- Most relevant code snippets
- 100-1000+ useful tokens in dynamic mode
- Complete context in fixed mode

#### 2. `web_search_exa(query, numResults?)`
Perform real-time web searches.

**Parameters:**
- `query` (required): Search query
- `numResults` (optional): Number of results (default: 5)

**Example:**
```javascript
web_search_exa({
  query: "TypeScript 5.7 new features",
  numResults: 5
})
```

#### 3. `company_research(company_name)`
Research company information.

**Parameters:**
- `company_name` (required): Name of company

**Example:**
```javascript
company_research({
  company_name: "Anthropic"
})
```

#### 4. `crawling_exa(url)`
Crawl and extract content from a URL.

**Parameters:**
- `url` (required): URL to crawl

**Example:**
```javascript
crawling_exa({
  url: "https://docs.anthropic.com/claude/docs"
})
```

#### 5. `deep_researcher_start(query)`
Start asynchronous deep research.

**Parameters:**
- `query` (required): Research query

**Example:**
```javascript
const research_id = deep_researcher_start({
  query: "Kubernetes security best practices 2025"
})
```

#### 6. `deep_researcher_check(research_id)`
Check status of deep research.

**Parameters:**
- `research_id` (required): ID from deep_researcher_start

**Example:**
```javascript
deep_researcher_check({
  research_id: "abc123..."
})
```

### Usage Patterns

#### Pattern 1: Code Discovery
```yaml
Goal: Find implementation examples

Steps:
  1. get_code_context_exa(
       query="React Server Components data fetching",
       tokensNum="dynamic"
     )
  2. Review code snippets
  3. Refine query if needed
```

#### Pattern 2: Technology Research
```yaml
Goal: Research new framework

Steps:
  1. web_search_exa("Framework X latest features")
  2. company_research("Framework X maintainer")
  3. deep_researcher_start("Framework X production use cases")
  4. Wait 30-60 seconds
  5. deep_researcher_check(research_id)
```

#### Pattern 3: Comprehensive Research Workflow
```yaml
Multi-Tool Workflow:
  1. exa.web_search_exa() → Find overview
  2. ref.ref_search_documentation() → Get official docs
  3. exa.get_code_context_exa() → Find code examples
  4. context7.get-library-docs() → Get API reference
  5. firecrawl.scrape() → Extract specific pages
  6. byterover.store-knowledge() → Save findings
```

### Best Practices

1. **Use Dynamic Tokens**
   - Default to `tokensNum: "dynamic"`
   - Only specify exact count when needed

2. **Combine with Other Tools**
   - Exa for code + Ref for docs + Context7 for APIs
   - Complete research triangle

3. **Deep Research for Complex Topics**
   - Use async deep researcher for topics needing synthesis
   - Allow 30-60 seconds for results

4. **Cache Results**
   - Store findings in Byterover
   - Avoid redundant API calls

### Configuration

**Desktop Config** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
"exa": {
  "command": "npx",
  "args": ["-y", "exa-mcp-server"],
  "env": {
    "EXA_API_KEY": "4e794a0d-ad65-4e89-8753-ed4ba1cffd96"
  }
}
```

**Global Config** (`~/.claude.json`):
```json
"exa": {
  "type": "http",
  "url": "https://mcp.exa.ai/mcp?exaApiKey=4e794a0d-ad65-4e89-8753-ed4ba1cffd96&enabledTools=%5B%22get_code_context_exa%22%2C%20%22web_search_exa%22%2C%20%22company_research%22%2C%20%22crawling_exa%22%2C%20%22deep_researcher_start%22%2C%20%22deep_researcher_check%22%5D",
  "headers": {}
}
```

---

## Comparison: When to Use Which

| Use Case | Tool | Reason |
|----------|------|--------|
| Official docs | **ref** | Token-efficient, focused results |
| Code examples | **exa** | Deep code context retrieval |
| API reference | **context7** | Library-specific documentation |
| General research | **exa** | Web search + company research |
| Private repos | **ref** | Supports private source search |
| Complex topics | **exa** | Deep researcher for synthesis |
| Quick answers | **ref** | Fast, filtered results |
| Real code | **exa** | Actual implementation examples |

---

## Integration with SuperClaude Framework

### Research Workflow
```
exa → ref → context7 → firecrawl → byterover
```

### Code Implementation
```
ref (docs) → context7 (API) → exa (examples) → implement
```

### Deep Analysis
```
exa (broad) → ref (specific) → firecrawl (deep) → synthesize
```

---

## Tool Selection Matrix Update

| Task Type | Primary | Secondary | Tertiary |
|-----------|---------|-----------|----------|
| Documentation | **ref** | context7 | firecrawl |
| Code Research | **exa** | context7 | octocode |
| General Research | firecrawl | **exa** | **ref** |
| API Docs | context7 | **ref** | - |
| Examples | **exa** | octocode | github |

---

## Verification

Both servers are now configured and can be verified:

### Test Ref
```javascript
ref_search_documentation({
  query: "Python async/await best practices"
})
```

### Test Exa
```javascript
get_code_context_exa({
  query: "React custom hooks useState",
  tokensNum: "dynamic"
})
```

---

## API Keys Management

### Current Keys
- **Ref API Key**: `ref-f8784ab7c8347c7d3453`
- **Exa API Key**: `4e794a0d-ad65-4e89-8753-ed4ba1cffd96`

### Key Storage
- Stored in Bitwarden CLI (`bw`)
- Referenced in both Claude configs
- Environment variables injected at runtime

### Key Rotation
To rotate keys:
1. Get new key from provider dashboard
2. Update Bitwarden entry
3. Update both config files
4. Restart Claude

---

## Troubleshooting

### Ref Issues

**Problem**: No results returned
- **Solution**: Use more specific, full-sentence queries

**Problem**: Too much irrelevant content
- **Solution**: Use session context to filter, refine queries

### Exa Issues

**Problem**: Code context too generic
- **Solution**: Add language/framework to query

**Problem**: Deep researcher timeout
- **Solution**: Wait 30-60 seconds, check status

---

## Resources

### Ref
- Documentation: https://ref.tools/
- GitHub: https://github.com/ref-tools/ref-tools-mcp
- Dashboard: https://ref.tools/dashboard

### Exa
- Documentation: https://docs.exa.ai/
- Dashboard: https://dashboard.exa.ai/
- API Reference: https://docs.exa.ai/reference/

---

**Version**: 1.0  
**Last Updated**: 2025-10-02  
**Status**: Production Ready ✅
