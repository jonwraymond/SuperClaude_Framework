# Memory Integration Guide

**Version**: 5.0  
**Last Updated**: 2025-10-02

---

## 🎯 Overview

The SuperClaude Framework uses a **dual memory system** combining:

1. **Byterover**: Durable knowledge storage with semantic search
2. **Basic Memory**: Graph-based knowledge with Obsidian backend

This architecture provides both deep semantic understanding and relationship-based knowledge management.

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────┐
│                 SuperClaude Framework                 │
│                                                       │
│  ┌────────────┐          ┌────────────────────────┐ │
│  │   Byterover│◄────────►│    Basic Memory        │ │
│  │  (Semantic)│          │  (Graph/Obsidian)      │ │
│  └──────┬─────┘          └────────┬───────────────┘ │
│         │                         │                  │
│         ▼                         ▼                  │
│  ┌──────────────────────────────────────────┐       │
│  │         Unified Memory Interface         │       │
│  └──────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────┘
```

---

## 🧠 Byterover Memory System

### Purpose
**Durable, searchable knowledge storage for implementation patterns, decisions, and learnings**

### Key Features
- **Semantic Search**: Find knowledge by meaning, not just keywords
- **Plan Management**: Store and track implementation plans
- **Module Knowledge**: Organize knowledge by code modules
- **Handbook System**: Project-specific knowledge bases
- **Timestamps**: Track when knowledge was created/updated

### Core Tools

#### `byterover-retrieve-knowledge`
**Retrieve knowledge from memory**

```
Usage: Before starting ANY task
Purpose: Get relevant context, avoid duplicate work
Arguments:
  - query: What to search for (semantic)
  - limit: Max results (default: 3)

Example:
byterover-retrieve-knowledge(
  query="authentication JWT implementation",
  limit=5
)
```

#### `byterover-store-knowledge`
**Store knowledge for future use**

```
Usage: After completing significant work
Purpose: Preserve learnings and patterns
Arguments:
  - messages: Complete knowledge with code snippets

What to store:
✅ Implementation decisions and rationale
✅ Bug fixes and root causes
✅ Architecture patterns
✅ Complete code snippets (not fragments)
✅ Integration insights
✅ Failure modes and solutions

What NOT to store:
❌ Trivial information
❌ Temporary state
❌ Credentials/secrets
❌ Common knowledge

Example:
byterover-store-knowledge(
  messages=\"\"\"
# JWT Authentication Implementation - 2025-10-02

## Context
Implemented JWT-based authentication for API endpoints.

## Approach
Used fastapi-jwt-auth library with RS256 algorithm:

\```python
from fastapi_jwt_auth import AuthJWT

@app.post(\"/login\")
async def login(credentials: LoginRequest, Authorize: AuthJWT):
    if verify_credentials(credentials):
        access_token = Authorize.create_access_token(
            subject=credentials.username,
            expires_time=timedelta(hours=1)
        )
        return {\"access_token\": access_token}
\```

## Key Decisions
- RS256 for asymmetric verification (supports multiple services)
- 1-hour access token lifetime
- Refresh tokens stored in Redis with 7-day expiration

## Gotchas
- Must set JWT_SECRET_KEY in environment
- Requires pyjwt[crypto] for RS256
- Token refresh must validate old token hasn't been revoked
  \"\"\"
)
```

#### `byterover-retrieve-active-plans`
**Check for unfinished work**

```
Usage: At session start
Purpose: Continue incomplete implementations
Arguments: None

Returns: Active plans with progress
```

#### `byterover-save-implementation-plan`
**Save approved plans**

```
Usage: IMMEDIATELY after user approves plan
Purpose: Track work and enable resumption
Arguments:
  - plan_name: Unique identifier
  - plan_description: What the plan does
  - tasks: List of checkable items

Example:
byterover-save-implementation-plan(
  plan_name="Add OAuth Provider Support",
  plan_description="Integrate Google/GitHub OAuth",
  tasks=[
    "Setup OAuth provider configuration",
    "Implement OAuth callback handlers",
    "Add user account linking logic",
    "Update database schema",
    "Write integration tests"
  ]
)
```

#### `byterover-update-plan-progress`
**Mark tasks/plan complete**

```
Usage: After completing tasks
Purpose: Track progress, mark work done
Arguments:
  - plan_name: Which plan
  - task_name: Which task (optional)
  - is_completed: true/false

Examples:
# Mark task complete
byterover-update-plan-progress(
  plan_name="Add OAuth",
  task_name="Setup OAuth provider configuration",
  is_completed=true
)

# Mark entire plan complete
byterover-update-plan-progress(
  plan_name="Add OAuth",
  is_completed=true
)
```

#### Module Management Tools

```
byterover-list-modules()
- Get all known code modules

byterover-search-modules(query="authentication")
- Find modules by semantic search

byterover-store-modules(module_info={...})
- Register new modules

byterover-update-modules(module_id="auth", updates={...})
- Update module info (CRITICAL: use immediately on changes)
```

#### Handbook Tools

```
byterover-check-handbook-existence()
- Check if handbook exists for project

byterover-create-handbook()
- Initialize handbook (onboarding)

byterover-check-handbook-sync()
- Analyze gaps between code and handbook

byterover-update-handbook()
- Sync handbook with codebase changes
```

---

## 📚 Basic Memory System

### Purpose
**Graph-based knowledge with Obsidian backend for relationship management**

### Key Features
- **Graph Structure**: Knowledge nodes with explicit relationships
- **Obsidian Integration**: Use your existing Obsidian vault
- **Link Tracking**: Bidirectional links between notes
- **Project-Based**: Multiple projects, switch contexts
- **Recent Activity**: Track what's been modified

### Configuration

**Obsidian Path** (from rules):
```
/Users/jraymond/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jon's Notes/
```

### Core Tools

#### `write_note`
**Create or update markdown notes**

```
Usage: Document decisions, create ADRs, store context
Arguments:
  - title: Note title
  - content: Markdown content
  - folder: Where to organize
  - tags: Optional tags
  - entity_type: "note" (default)
  - project: Optional project name

Example:
write_note(
  title="OAuth Implementation Decision",
  content="""
# OAuth Provider Selection

## Context
Need to support social login for user convenience.

## Decision
Use Google and GitHub as initial OAuth providers.

## Rationale
- Most users have Google/GitHub accounts
- Well-documented APIs
- Industry standard
- Good security practices

## Consequences
- Need to handle account linking
- Must store OAuth tokens securely
- Requires callback URL configuration
  """,
  folder="decisions/auth",
  tags=["oauth", "authentication", "adr"]
)
```

#### `read_note`
**Read existing notes**

```
Usage: Retrieve documented decisions/context
Arguments:
  - identifier: Title or permalink
  - project: Optional project name

Example:
read_note(identifier="OAuth Implementation Decision")
```

#### `search_notes`
**Search across all notes**

```
Usage: Find related knowledge
Arguments:
  - query: Search terms
  - search_type: "text" (default), "semantic"
  - types: Filter by note type
  - entity_types: Filter by entity type

Example:
search_notes(
  query="authentication security patterns",
  search_type="semantic"
)
```

#### `build_context`
**Build context from memory URIs**

```
Usage: Continue conversations naturally
Arguments:
  - url: Memory URL pattern
  - timeframe: "7d", "last week", etc.
  - depth: Relationship depth (default: 1)

Example:
build_context(
  url="auth/*",
  timeframe="30d"
)
```

#### `recent_activity`
**Get recent changes**

```
Usage: See what's been updated
Arguments:
  - timeframe: "7d", "today", etc.
  - type: Filter by activity type

Example:
recent_activity(timeframe="7d")
```

#### Project Management

```
list_memory_projects()
- List all available projects

get_current_project()
- Show active project

switch_project(project_name="work-notes")
- Change active project

create_memory_project(project_name, project_path)
- Create new project

set_default_project(project_name)
- Set default project (requires restart)
```

---

## 🔄 Dual Memory Workflow

### Standard Workflow

#### 1. **Session Start**
```
# Check for active work
byterover-retrieve-active-plans()

# Check recent context
recent_activity(timeframe="7d")

# Get relevant knowledge
byterover-retrieve-knowledge(query="current task context")
```

#### 2. **During Work**
```
# Search for patterns
byterover-search-modules(query="relevant module")

# Check for related decisions
search_notes(query="similar context")

# Store intermediate findings
byterover-store-knowledge(messages="...")
```

#### 3. **After Completion**
```
# Mark plan complete
byterover-update-plan-progress(plan_name="...", is_completed=true)

# Store implementation knowledge
byterover-store-knowledge(messages="complete details with code")

# Document decision
write_note(
  title="Implementation Decision",
  content="...",
  folder="decisions"
)

# Update module info if changed
byterover-update-modules(module_id="...", updates={...})
```

---

## 📊 Memory Strategy Matrix

| Scenario | Use Byterover | Use Basic Memory | Why |
|----------|---------------|------------------|-----|
| **Implementation patterns** | ✅ Primary | ⚠️ Optional | Semantic search for similar code |
| **Architecture decisions** | ✅ Yes | ✅ Yes (ADR) | Both for search + documentation |
| **Bug fixes** | ✅ Primary | ⚠️ Optional | Root cause + solution patterns |
| **Project plans** | ✅ Required | ❌ No | Plan tracking system |
| **Code modules** | ✅ Required | ❌ No | Module knowledge system |
| **Design decisions** | ⚠️ Optional | ✅ Primary (ADR) | Formal decision records |
| **Meeting notes** | ❌ No | ✅ Yes | Not code-related |
| **Personal notes** | ❌ No | ✅ Yes | Use Obsidian directly |
| **Relationships** | ⚠️ Limited | ✅ Primary | Graph structure |
| **Quick lookup** | ✅ Yes | ⚠️ Slower | Semantic search faster |

---

## 🚨 Memory Best Practices

### DO:
✅ **Check memory before starting** (Rule 1)  
✅ **Store complete code snippets** with context  
✅ **Include timestamps** in all stored knowledge  
✅ **Use both systems** for comprehensive coverage  
✅ **Update immediately** after significant changes  
✅ **Attribute sources** ("According to Byterover memory...")  
✅ **Mark plans complete** when done  

### DON'T:
❌ **Store secrets** or credentials  
❌ **Store trivial info** (common knowledge)  
❌ **Skip memory checks** (wastes time)  
❌ **Forget to save plans** immediately after approval  
❌ **Leave stale data** (update module info promptly)  
❌ **Mix personal/work** in Basic Memory (use projects)  

---

## 🔍 Troubleshooting

### Problem: "Can't find previous work"
**Solution**: Use semantic search in Byterover, not keyword search
```
# Instead of:
byterover-retrieve-knowledge(query="JWT code")

# Do:
byterover-retrieve-knowledge(query="JSON Web Token authentication implementation")
```

### Problem: "Memory conflicts detected"
**Solution**: Basic Memory shows conflict resolution URL - always display to user
```
When you see conflict warnings, MUST show the URL to user for resolution
```

### Problem: "Plans not persisting"
**Solution**: Save immediately after approval (Rule from Byterover guidelines)
```
# RIGHT after user says "approved" or "yes":
byterover-save-implementation-plan(...)
```

### Problem: "Module info out of sync"
**Solution**: Update immediately when module changes
```
# After changing module purpose/functionality:
byterover-update-modules(module_id="auth", updates={
  "purpose": "Updated purpose...",
  "critical_insights": "New pattern discovered..."
})
```

### Problem: "Too many results"
**Solution**: Narrow query or reduce limit
```
byterover-retrieve-knowledge(
  query="specific technical detail not general topic",
  limit=3  # Start small
)
```

---

## 🎯 Quick Reference

### Memory Retrieval Priority
```
1. byterover-retrieve-active-plans (check unfinished work)
2. byterover-retrieve-knowledge (get semantic context)
3. byterover-search-modules (find relevant modules)
4. search_notes (check documented decisions)
5. recent_activity (see recent changes)
```

### Memory Storage Priority
```
1. byterover-save-implementation-plan (immediately after approval)
2. byterover-update-plan-progress (after each task)
3. byterover-store-knowledge (after significant work)
4. write_note (for formal decisions/ADRs)
5. byterover-update-modules (immediately on module changes)
```

---

## 🔗 Integration Points

### With ORCHESTRATOR.md
- Memory checks happen in Wave 1 (Rapid Response)
- Deep memory search in Wave 4 (Deep Analysis)
- Knowledge storage in Wave 5 (Expert Validation)

### With RULES.md
- Rule 1: Memory First (mandatory memory checks)
- Rule 3: Memory Persistence (storage requirements)
- Rule 12: Context Preservation (session continuity)

### With WORKFLOWS.md
- Every workflow starts with memory retrieval
- Every workflow ends with knowledge storage
- Plans tracked through byterover system

### With PERSONAS.md
- Each persona has memory tool preferences
- Personas use memory for specialization knowledge
- Cross-persona collaboration via shared memory

---

**Status**: Production Ready  
**Dual Write**: Enabled by default (--memory-dual-write=true)  
**Sync**: Optional (--memory-sync=true)  
**See Also**: RULES.md (Rule 1, 3, 12), WORKFLOWS.md (all workflows)
