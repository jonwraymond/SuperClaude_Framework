# Basic Memory MCP Server

## Overview
Basic Memory provides seamless integration with your Obsidian knowledge base, enabling AI assistants to interact with your personal notes and knowledge graph through MCP tools.

## Capabilities
- **Note Management**: Create, read, edit, and delete markdown notes
- **Knowledge Graph**: Build and navigate relationships through WikiLinks
- **Project Management**: Switch between different knowledge projects
- **Search & Discovery**: Semantic search across all notes and content
- **Activity Tracking**: Monitor recent changes and updates
- **Canvas Creation**: Generate visual concept maps and connections

## Key Tools

### Core Note Operations
- **`write_note`**: Create new markdown notes with tags and metadata
- **`read_note`**: Read existing notes by title or permalink  
- **`edit_note`**: Modify notes using various operations (append, prepend, find_replace)
- **`search_notes`**: Advanced search across all content with syntax support
- **`delete_note`**: Remove notes by title or permalink

### Project Management
- **`create_memory_project`**: Create new projects with specified paths
- **`list_memory_projects`**: View all available projects and their status
- **`switch_project`**: Change active project context
- **`get_current_project`**: Display currently active project info

### Context & Discovery
- **`build_context`**: Follow up on previous discussions with related topics
- **`recent_activity`**: Get recent activity across the knowledge base
- **`sync_status`**: Check file synchronization and background operations
- **`canvas`**: Create visual concept maps and relationship diagrams

## Usage Pattern

### Mandatory Workflow (Every Task)
**Before**:
- Use `search_notes` to find related notes and observations
- Use `build_context` to construct working graph from retrieved info

**During**:
- Use `write_note` / `edit_note` to log ≥3 observations and ≥2 `[[WikiLinks]]` per update
- Apply canonical `#tags` and relation verbs (`implements`, `relates_to`, etc.)

**After**:
- Use `write_note` to capture outcomes, relations, and follow-ups
- Document guiding keywords/tags for future retrieval

## Configuration
```json
{
  "basic-memory": {
    "command": "/Users/jraymond/.local/bin/basic-memory",
    "args": ["mcp"]
  }
}
```

## Integration with Obsidian
- **Path**: `/Users/jraymond/Library/Mobile Documents/iCloud~md~obsidian/Documents/Jon's Notes/`
- **Format**: Standard Obsidian markdown with WikiLinks support
- **Sync**: Automatic synchronization with iCloud and Obsidian backend
- **Graph**: Maintains bidirectional links and knowledge relationships

## Context Stack Integration
Works seamlessly with ByteRover for dual-memory approach:
- **Basic Memory**: Maintains the Obsidian graph and immediate context
- **ByteRover**: Preserves durable patterns for future sessions
- **Combined**: Comprehensive context management ensuring efficient, traceable research