# Exa & Ref MCP Quick Reference

**Status**: ✅ Configured | **Date**: 2025-10-02

## Quick Access

Both tools are now available in Claude. Use them directly!

## Ref - Documentation Search

### When to Use
- Finding official documentation
- Token-efficient research
- Private repo/PDF search
- Iterative documentation deep-dives

### Quick Commands
```javascript
// Search for docs
ref_search_documentation({
  query: "React hooks best practices for state management"
})

// Read specific URL
ref_read_url({
  url: "https://docs.example.com/api"
})
```

### Pro Tips
- Use full sentences for queries
- Leverage session context (no repeated results)
- Returns only 5k most relevant tokens
- Filters intelligently based on search history

---

## Exa - Code Research & Web Intelligence

### When to Use
- Finding code examples
- Deep code context
- Company research
- Complex topic synthesis

### Quick Commands
```javascript
// Get code context (use dynamic!)
get_code_context_exa({
  query: "Next.js middleware authentication",
  tokensNum: "dynamic"
})

// Web search
web_search_exa({
  query: "TypeScript 5.7 features",
  numResults: 5
})

// Deep research (async)
const id = deep_researcher_start({
  query: "Kubernetes security 2025"
})
// Wait 30-60s then check
deep_researcher_check({ research_id: id })
```

### Pro Tips
- Always use `tokensNum: "dynamic"` first
- Combine with ref for complete picture
- Store findings in Byterover
- Use deep research for complex synthesis

---

## Comparison Table

| Need | Use | Why |
|------|-----|-----|
| Official docs | **ref** | Token-efficient, smart filtering |
| Code examples | **exa** | Real implementations |
| API reference | **context7** | Library-specific |
| Quick answer | **ref** | Fast, focused |
| Deep research | **exa** | Async synthesis |

---

## Common Workflows

### 1. Feature Implementation
```
ref (docs) → context7 (API) → exa (examples) → code
```

### 2. Technology Research
```
exa (overview) → ref (details) → context7 (specs)
```

### 3. Problem Solving
```
ref (docs) → exa (solutions) → byterover (save)
```

---

## Configuration Locations

- **Desktop**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Global**: `~/.claude.json`
- **Full Docs**: `core/docs/EXA_REF_SETUP.md`

---

## Need Help?

See full documentation: `core/docs/EXA_REF_SETUP.md`
