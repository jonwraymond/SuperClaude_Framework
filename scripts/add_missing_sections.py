#!/usr/bin/env python3
"""
Add missing sections to commands that need them
"""

import re
from pathlib import Path

COMMANDS_DIR = Path("SuperClaude/Commands")

# Templates for missing sections
TEMPLATES = {
    "MCP Integration": """
## MCP Integration

### Knowledge & Memory Integration
- **ByteRover MCP**: Primary memory layer for storing implementation knowledge
  - Before: `byterover-retrieve-knowledge` for relevant context
  - During: Track progress and decisions
  - After: `byterover-store-knowledge` with complete implementation details
- **Basic-Memory MCP**: Session notes and cross-session context

### Workflow Integration (per AGENTS.md)
```
Before Command:
  → byterover-retrieve-knowledge(query="relevant context")

During Command:
  → Track decisions and progress
  → Document key findings

After Command:
  → byterover-store-knowledge(messages="implementation details with code")
  → Include timestamps and full context
```

### Tool Coordination
- **Analysis & Research**: Sequential-thinking, Exa, Context7 for deep investigation
- **Development**: Morphllm, Serena for code changes and project memory
- **Documentation**: Ref, Context7 for framework-specific docs
""",
    
    "Tool Coordination": """
## Tool Coordination
- **Read/Write/Edit**: File operations and content management
- **TodoWrite**: Progress tracking for multi-step operations  
- **Task**: Parallel execution and delegation
- **WebSearch**: Research and external information gathering
""",
    
    "Key Patterns": """
## Key Patterns
- **Systematic Execution**: Structured approach → comprehensive results
- **Memory Integration**: ByteRover retrieve → process → store pattern
- **Progressive Enhancement**: Iterative refinement with persistent context
- **Cross-Session Continuity**: Serena MCP for long-running operations
""",

    "Usage": """
## Usage
```
/sc:command [options] [arguments]
```
**Usage**: Type this pattern in your Claude Code conversation to activate this command's behavioral mode.
""",
    
    "Examples": """
## Examples

### Basic Usage
```
/sc:command "basic example"
```

### Advanced Usage
```
/sc:command "advanced example" --with-options
```

### Complex Scenario
```
/sc:command "complex multi-step example" --comprehensive
```
"""
}

def add_section_before_boundaries(filepath: Path, section_name: str):
    """Add a missing section before the Boundaries section"""
    content = filepath.read_text()
    
    # Find where to insert (before ## Boundaries)
    boundaries_match = re.search(r'^## Boundaries', content, re.MULTILINE)
    if not boundaries_match:
        print(f"  ⚠️  No Boundaries section found in {filepath.name}, appending to end")
        content += "\n\n" + TEMPLATES[section_name]
    else:
        # Insert before Boundaries
        insert_pos = boundaries_match.start()
        content = content[:insert_pos] + TEMPLATES[section_name] + "\n\n" + content[insert_pos:]
    
    filepath.write_text(content)
    print(f"  ✓ Added {section_name} to {filepath.name}")

def main():
    print("Adding missing sections to commands...")
    print("=" * 50)
    print("")
    
    # git.md - needs MCP Integration
    git_file = COMMANDS_DIR / "git.md"
    if git_file.exists():
        print("Processing git.md...")
        add_section_before_boundaries(git_file, "MCP Integration")
        print("")
    
    # help.md - needs Usage, MCP Integration, Tool Coordination, Key Patterns, Examples
    help_file = COMMANDS_DIR / "help.md"
    if help_file.exists():
        print("Processing help.md...")
        for section in ["Usage", "MCP Integration", "Tool Coordination", "Key Patterns", "Examples"]:
            add_section_before_boundaries(help_file, section)
        print("")
    
    # research.md - needs Tool Coordination
    research_file = COMMANDS_DIR / "research.md"
    if research_file.exists():
        print("Processing research.md...")
        add_section_before_boundaries(research_file, "Tool Coordination")
        print("")
    
    # spec-panel.md - needs Key Patterns
    spec_file = COMMANDS_DIR / "spec-panel.md"
    if spec_file.exists():
        print("Processing spec-panel.md...")
        add_section_before_boundaries(spec_file, "Key Patterns")
        print("")
    
    print("=" * 50)
    print("✓ All missing sections added!")
    print("")
    print("Run validation: python scripts/validate_commands.py --summary")
    print("")

if __name__ == "__main__":
    main()
