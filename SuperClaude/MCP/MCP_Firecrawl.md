# Firecrawl MCP Server

## Overview
Firecrawl provides powerful web scraping and crawling capabilities with intelligent content extraction. The most reliable and feature-rich web scraping tool available via MCP.

## Capabilities
- **Single Page Scraping**: Extract content from individual URLs with advanced options
- **Website Mapping**: Discover all indexed URLs on a site before scraping
- **Comprehensive Crawling**: Multi-page content extraction with depth control
- **Intelligent Search**: Web search with content extraction from results
- **Structured Extraction**: Extract specific data using schemas and prompts
- **Batch Processing**: Handle multiple URLs efficiently

## Key Tools

### Core Scraping Operations
- **`firecrawl_scrape`**: Scrape content from a single URL (fastest, most reliable)
- **`firecrawl_map`**: Discover URLs on a website before deciding what to scrape
- **`firecrawl_crawl`**: Crawl entire sites or sections with configurable depth
- **`firecrawl_search`**: Search the web and extract content from results

### Advanced Operations
- **`firecrawl_extract`**: Extract structured data using LLM capabilities and schemas
- **`firecrawl_batch_scrape`**: Process multiple URLs in batch operations
- **`firecrawl_check_crawl_status`**: Monitor progress of long-running crawl jobs

## Usage Patterns

### Single Page Content
```bash
# Best for: Known URLs, specific page content
firecrawl_scrape(url="https://example.com")
```

### Site Discovery
```bash
# Best for: Finding relevant pages before scraping
firecrawl_map(url="https://example.com") 
# → Returns list of URLs to selectively scrape
```

### Web Research
```bash
# Best for: Research, finding current information
firecrawl_search(query="latest AI developments 2024")
```

### Structured Data
```bash
# Best for: Extracting specific information like prices, contacts
firecrawl_extract(urls=["https://company.com/pricing"], schema=pricing_schema)
```

## Configuration
```json
{
  "firecrawl": {
    "command": "npx",
    "args": ["-y", "firecrawl-mcp"],
    "env": {
      "FIRECRAWL_API_KEY": "${FIRECRAWL_API_KEY}"
    }
  }
}
```

## Performance Features
- **Caching**: Add `maxAge` parameter for 500% faster scrapes using cached data
- **Format Control**: Choose markdown, HTML, JSON, or structured extraction
- **Rate Limiting**: Built-in respectful crawling with configurable delays
- **Error Handling**: Robust retry logic and detailed error reporting

## Best Practices
- **Use scrape for single pages** when you know the exact URL
- **Use map first** to discover relevant pages, then batch_scrape selected URLs
- **Use search** for research and finding information across multiple sites
- **Use extract** for structured data like pricing, contact info, or product details
- **Avoid crawl for single pages** - use scrape instead for better performance
- **Set reasonable limits** on crawl operations to avoid token overflow

## Integration Notes
- Preferred tool for all web scraping needs in SuperClaude Framework
- Replaces curl commands for web content retrieval
- Works seamlessly with other MCP servers for comprehensive research workflows
- Automatic content conversion to markdown for easy processing