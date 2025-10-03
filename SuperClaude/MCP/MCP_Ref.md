# Ref MCP Server

**Purpose**: Token-efficient documentation search with agentic filtering and intelligent section extraction

## Triggers
- Documentation lookup: "find docs for", "documentation on", "official guide"
- API reference queries: "how to use", "API for", "method signature"
- Best practices: "recommended approach", "best way to", "proper usage"
- Framework/library questions requiring official docs
- Need for token-efficient research (minimize context rot)

## Choose When
- **Over WebSearch**: When you need focused, relevant documentation without noise
- **Over Firecrawl**: When you need token-efficient extraction (~4k vs 20k+ tokens)
- **Over native knowledge**: When documentation must be current and accurate
- **For official docs**: When you need definitive, authoritative information
- **For iterative research**: Session-based filtering prevents repeated results

## Works Best With
- **Context7**: Ref for broad docs → Context7 for specific library APIs
- **Exa**: Ref for documentation → Exa for real code examples
- **Firecrawl**: Ref for initial research → Firecrawl for deep extraction
- **Byterover**: Ref finds info → Byterover stores findings

## Key Features
- **Token Efficiency**: Returns ~4k tokens vs 20k+ with raw web scraping
- **Agentic Search**: Automatically filters previously returned results
- **Smart Extraction**: Returns only the most relevant 5k token sections
- **Multi-Source**: Searches public docs, GitHub, private repos, PDFs
- **Session Context**: Uses search history to refine and focus results

## Available Tools

### ref_search_documentation
Search for technical documentation across indexed sources.

**Use for**:
- Finding official documentation pages
- Locating API references
- Discovering best practices guides
- Searching private repos and PDFs

**Parameters**:
- `query` (required): Full sentence or question describing what you need

**Example**:
```javascript
ref_search_documentation({
  query: "React hooks useState and useEffect best practices for managing component state"
})
```

**Returns**: URLs, snippets, and relevance scores

### ref_read_url
Fetch content from a URL and convert to markdown with intelligent extraction.

**Use for**:
- Reading specific documentation pages
- Extracting relevant sections from large docs
- Getting clean markdown from web pages

**Parameters**:
- `url` (required): The complete URL to fetch

**Example**:
```javascript
ref_read_url({
  url: "https://react.dev/reference/react/useState"
})
```

**Returns**: Up to 5k tokens of most relevant content in markdown

## Usage Patterns

### Pattern 1: Quick Documentation Lookup
```yaml
Scenario: Need specific API documentation

Steps:
  1. ref_search_documentation("API authentication methods with JWT")
  2. Review returned URLs and snippets
  3. ref_read_url(most_relevant_url)
  
Best for: Specific, well-defined questions
```

### Pattern 2: Iterative Deep Research
```yaml
Scenario: Understanding complex topic

Steps:
  1. Broad search: "Kubernetes container networking"
  2. Read top 2-3 results
  3. Refined search: "Kubernetes CNI plugins comparison"
  4. Read specific implementation docs
  5. Final search: "Kubernetes network policies security"
  
Best for: Complex topics requiring progressive understanding
```

### Pattern 3: Multi-Tool Research Workflow
```yaml
Complete research approach:

Steps:
  1. ref_search_documentation() → Find documentation
  2. ref_read_url() → Extract relevant content
  3. context7.get-library-docs() → Get API specifics
  4. exa.get_code_context_exa() → Find code examples
  5. byterover.store-knowledge() → Save findings
  
Best for: Comprehensive feature implementation research
```

## Configuration
```json
{
  "ref": {
    "command": "npx",
    "args": ["-y", "ref-tools-mcp@latest"],
    "env": {
      "REF_API_KEY": "${REF_API_KEY}"
    }
  }
}
```

## Best Practices

### Query Formation
- ✅ **Good**: "React hooks best practices for managing state"
- ❌ **Bad**: "react hooks"
- ✅ **Good**: "Python async/await error handling patterns"
- ❌ **Bad**: "async python"

### Session Management
- Ref automatically filters out previously returned results
- Refine queries to dig deeper without repetition
- Use session context to progressively narrow research

### Token Efficiency
- Ref limits reads to 5k most relevant tokens
- Much more efficient than raw web scraping (20k+ tokens)
- Reduces context rot and improves model accuracy

### Integration Strategy
1. **Start with Ref** for documentation discovery
2. **Use Context7** for library-specific APIs
3. **Use Exa** for real-world code examples
4. **Store in Byterover** for future reference

## Comparison with Other Tools

| Use Case | Ref | Firecrawl | Context7 | Exa |
|----------|-----|-----------|----------|-----|
| Official docs | ✅ Best | ⚠️ Verbose | ⚠️ Limited | ❌ No |
| Token efficiency | ✅ 4k | ❌ 20k+ | ✅ Focused | ✅ Dynamic |
| Private repos | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Code examples | ❌ No | ⚠️ Mixed | ✅ Some | ✅ Best |
| Quick answers | ✅ Fast | ⚠️ Slow | ✅ Fast | ✅ Fast |

## Examples

### Example 1: Framework Documentation
```javascript
// Find Next.js middleware docs
ref_search_documentation({
  query: "Next.js 14 middleware authentication and route protection"
})

// Read the official guide
ref_read_url({
  url: "https://nextjs.org/docs/app/building-your-application/routing/middleware"
})
```

### Example 2: API Reference
```javascript
// Search for database ORM docs
ref_search_documentation({
  query: "Prisma schema relations and queries documentation"
})

// Extract specific section
ref_read_url({
  url: "https://www.prisma.io/docs/concepts/components/prisma-schema/relations"
})
```

### Example 3: Best Practices Research
```javascript
// Progressive research
ref_search_documentation({
  query: "TypeScript generic constraints best practices"
})
// Read results, then refine:
ref_search_documentation({
  query: "TypeScript conditional types with generic constraints"
})
```

## Integration Notes
- Essential tool for documentation-heavy workflows
- Complements Context7 (official APIs) and Exa (code examples)
- Preferred for research that requires current, accurate information
- Reduces token usage and improves research efficiency
- Session-based filtering eliminates redundant results

## Troubleshooting

**Problem**: No results found
- **Solution**: Use more specific, complete sentence queries
- **Solution**: Try alternative phrasing or broader initial search

**Problem**: Results too generic
- **Solution**: Add framework/language specifics to query
- **Solution**: Use session context - refine query based on previous results

**Problem**: Content not relevant
- **Solution**: Check if using full URL in ref_read_url
- **Solution**: Try ref_search_documentation first to find better URLs

## Resources
- Documentation: https://ref.tools/
- GitHub: https://github.com/ref-tools/ref-tools-mcp
- Dashboard: https://ref.tools/dashboard
