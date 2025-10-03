# Exa MCP Server

**Purpose**: Deep code research, quality examples, and comprehensive web intelligence with AI-powered context retrieval

## Triggers
- Code example requests: "show me code", "example implementation", "how to code"
- Library/framework usage: "using X library", "implement with Y", "code pattern"
- Real-world implementations: "production code", "actual example", "working implementation"
- Company/technology research: "research company", "technology overview", "tech stack"
- Complex topic synthesis: "comprehensive analysis", "deep research", "investigate topic"

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

## Key Features
- **Dynamic Code Context**: Retrieves 100-1000+ relevant tokens efficiently
- **Web Intelligence**: Real-time web search with content extraction
- **Company Research**: Comprehensive company and technology analysis
- **Deep Research**: Async research for complex topic synthesis
- **Crawling**: Intelligent URL content extraction

## Available Tools

### get_code_context_exa
Retrieve relevant code context for programming tasks.

**Use for**:
- Finding real code implementations
- Getting code examples from GitHub
- Understanding how libraries are used in practice
- Discovering design patterns in production code

**Parameters**:
- `query` (required): Search query for code context
- `tokensNum` (optional): `"dynamic"` (default) or 1000-50000

**Example**:
```javascript
// Dynamic mode (recommended)
get_code_context_exa({
  query: "Next.js middleware authentication with JWT tokens",
  tokensNum: "dynamic"
})

// Fixed token count (only when needed)
get_code_context_exa({
  query: "React custom hooks for data fetching",
  tokensNum: 5000
})
```

**Returns**: Most relevant code snippets with context

### web_search_exa
Perform real-time web searches with intelligent content extraction.

**Use for**:
- Finding current information
- Technology trend research
- Latest best practices
- Recent developments

**Parameters**:
- `query` (required): Search query
- `numResults` (optional): Number of results (default: 5)

**Example**:
```javascript
web_search_exa({
  query: "React Server Components best practices 2025",
  numResults: 5
})
```

**Returns**: Search results with extracted content

### company_research
Research company information, tech stack, and background.

**Use for**:
- Understanding tech companies
- Technology stack analysis
- Company background research
- Competitive intelligence

**Parameters**:
- `company_name` (required): Name of company

**Example**:
```javascript
company_research({
  company_name: "Anthropic"
})
```

**Returns**: Company information, tech stack, and context

### crawling_exa
Crawl and extract content from specific URLs.

**Use for**:
- Extracting content from known URLs
- Getting structured data from web pages
- Documentation extraction

**Parameters**:
- `url` (required): URL to crawl

**Example**:
```javascript
crawling_exa({
  url: "https://docs.anthropic.com/claude/docs"
})
```

**Returns**: Extracted and structured content

### deep_researcher_start
Start asynchronous deep research on complex topics.

**Use for**:
- Complex topic synthesis
- Multi-source research aggregation
- Comprehensive analysis
- Long-form research

**Parameters**:
- `query` (required): Research query

**Example**:
```javascript
const research_id = deep_researcher_start({
  query: "Kubernetes security best practices and threat mitigation 2025"
})
```

**Returns**: Research ID for status checking

### deep_researcher_check
Check status and results of deep research.

**Use for**:
- Checking research completion
- Retrieving research results
- Monitoring research progress

**Parameters**:
- `research_id` (required): ID from deep_researcher_start

**Example**:
```javascript
deep_researcher_check({
  research_id: "abc123..."
})
```

**Returns**: Research status and results (if complete)

## Usage Patterns

### Pattern 1: Code Discovery
```yaml
Scenario: Need implementation examples

Steps:
  1. get_code_context_exa(
       query="React Server Components data fetching patterns",
       tokensNum="dynamic"
     )
  2. Review code snippets
  3. Refine query if needed for more specific examples
  
Best for: Finding real code implementations
```

### Pattern 2: Technology Research
```yaml
Scenario: Research new framework or tool

Steps:
  1. web_search_exa("Framework X latest features and adoption")
  2. company_research("Framework X maintainer organization")
  3. get_code_context_exa("Framework X production examples")
  4. deep_researcher_start("Framework X best practices and gotchas")
  5. Wait 30-60 seconds
  6. deep_researcher_check(research_id)
  
Best for: Comprehensive technology evaluation
```

### Pattern 3: Complete Research Workflow
```yaml
Multi-tool comprehensive research:

Steps:
  1. exa.web_search_exa() → Find overview and current state
  2. ref.ref_search_documentation() → Get official documentation
  3. exa.get_code_context_exa() → Find real implementations
  4. context7.get-library-docs() → Get API reference details
  5. exa.deep_researcher_start() → Synthesize comprehensive analysis
  6. byterover.store-knowledge() → Save all findings
  
Best for: Feature implementation with research
```

## Configuration
```json
{
  "exa": {
    "command": "npx",
    "args": ["-y", "exa-mcp-server"],
    "env": {
      "EXA_API_KEY": "${EXA_API_KEY}"
    }
  }
}
```

## Best Practices

### Token Efficiency
- ✅ **Always start with** `tokensNum: "dynamic"`
- ❌ **Don't specify** exact token count unless needed
- ✅ **Dynamic mode** returns 100-1000+ most useful tokens
- ⚠️ **Fixed count** only when you need complete context

### Query Specificity
- ✅ **Good**: "Next.js 14 middleware authentication JWT cookies"
- ❌ **Bad**: "next auth"
- ✅ **Good**: "React custom hooks data fetching error handling"
- ❌ **Bad**: "react hooks"

### Tool Combination
1. **Exa for code** → Find implementations
2. **Ref for docs** → Understand concepts
3. **Context7 for APIs** → Get official references
4. **Complete triangle** for thorough understanding

### Deep Research Strategy
- Use for complex topics requiring synthesis
- Allow 30-60 seconds for completion
- Check status before assuming failure
- Store results in Byterover for future reference

## Comparison with Other Tools

| Use Case | Exa | Ref | Context7 | Firecrawl |
|----------|-----|-----|----------|-----------|
| Code examples | ✅ Best | ❌ No | ⚠️ Some | ⚠️ Mixed |
| Documentation | ❌ No | ✅ Best | ✅ APIs | ⚠️ Verbose |
| Token efficiency | ✅ Dynamic | ✅ 4k | ✅ Focused | ❌ 20k+ |
| Web search | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| Company info | ✅ Yes | ❌ No | ❌ No | ⚠️ Manual |
| Deep research | ✅ Async | ❌ No | ❌ No | ❌ No |

## Examples

### Example 1: Finding Code Patterns
```javascript
// Find authentication implementation
get_code_context_exa({
  query: "Express.js JWT authentication middleware with refresh tokens",
  tokensNum: "dynamic"
})

// Refine for specific framework
get_code_context_exa({
  query: "Express.js passport JWT strategy configuration example",
  tokensNum: "dynamic"
})
```

### Example 2: Technology Research
```javascript
// Research framework
web_search_exa({
  query: "Remix framework vs Next.js comparison 2025",
  numResults: 5
})

// Get company background
company_research({
  company_name: "Remix Software"
})

// Find production examples
get_code_context_exa({
  query: "Remix framework production deployment examples",
  tokensNum: "dynamic"
})
```

### Example 3: Complex Topic Analysis
```javascript
// Start deep research
const id = deep_researcher_start({
  query: "Microservices architecture security patterns and implementation strategies"
})

// Wait 30-60 seconds, then check
deep_researcher_check({
  research_id: id
})
// Returns comprehensive analysis with multiple perspectives
```

### Example 4: URL Content Extraction
```javascript
// Extract from specific URL
crawling_exa({
  url: "https://github.com/vercel/next.js/tree/canary/examples/auth"
})
```

## Integration Notes
- Critical tool for code-focused workflows
- Complements documentation tools (Ref, Context7)
- Essential for finding real-world implementations
- Use for technology evaluation and research
- Store findings in Byterover for team knowledge base

## Performance Tips
- Default to `dynamic` mode for optimal token usage
- Use deep researcher sparingly (30-60s wait time)
- Combine with other tools for complete picture
- Cache results in Byterover to minimize API calls
- Refine queries based on initial results

## Troubleshooting

**Problem**: Code context too generic
- **Solution**: Add specific framework/library to query
- **Solution**: Include use case or pattern name in query

**Problem**: Web search returns too broad results
- **Solution**: Add year/version to query (e.g., "2025", "latest")
- **Solution**: Specify technology stack in query

**Problem**: Deep researcher timeout
- **Solution**: Wait full 30-60 seconds before checking
- **Solution**: Check status multiple times with delays

**Problem**: Not finding code examples
- **Solution**: Try alternative phrasing (e.g., "implementation" vs "example")
- **Solution**: Add "production" or "real-world" to query

## Resources
- Documentation: https://docs.exa.ai/
- Dashboard: https://dashboard.exa.ai/
- API Reference: https://docs.exa.ai/reference/
