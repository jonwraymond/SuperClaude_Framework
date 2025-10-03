# Enhancement Quality Checklist

**Purpose**: Comprehensive validation checklist for ensuring all enhanced files meet SuperClaude Framework standards

**Usage**: Use this checklist before marking any agent, command, or MCP documentation as complete

---

## Agent Enhancement Checklist

### Structure Validation

- [ ] **YAML Frontmatter Complete**
  - [ ] `name` field present and correct
  - [ ] `description` field present (clear one-line description)
  - [ ] `category` field present (engineering|analysis|utility|education|business)
  - [ ] `mcp-servers` list present

- [ ] **MCP Server List Complete**
  - [ ] `zen` listed with inline comment
  - [ ] `ref` listed with inline comment
  - [ ] `firecrawl` listed with inline comment
  - [ ] `exa` listed with inline comment
  - [ ] `byterover` listed with inline comment (MANDATORY)
  - [ ] `basic-memory` listed with inline comment (MANDATORY)
  - [ ] `sequential-thinking` listed with inline comment
  - [ ] `tavily` listed with inline comment
  - [ ] `context7` listed with inline comment
  - [ ] `octocode` listed with inline comment
  - [ ] `cerebras-code` listed with inline comment
  - [ ] `morphllm-fast-apply` listed with inline comment
  - [ ] `time` listed with inline comment
  - [ ] Domain-specific MCPs added if applicable (github, playwright, magic, etc.)
  - [ ] ALL MCP servers have inline comments explaining usage

- [ ] **Six Main Sections Present**
  - [ ] "## Triggers" section
  - [ ] "## Behavioral Mindset" section
  - [ ] "## MCP Integration Workflow" section
  - [ ] "## Focus Areas" section
  - [ ] "## Key Actions" section
  - [ ] "## Outputs" section
  - [ ] "## Boundaries" section

### MCP Integration Workflow (CRITICAL)

- [ ] **"ByteRover Memory-First Pattern (MANDATORY)" Subsection**
  - [ ] Subsection header present exactly as shown
  - [ ] Attribution phrase "According to ByteRover memory layer" present
  - [ ] Three-phase pattern documented:
    - [ ] "Prime Context" with byterover-retrieve-knowledge
    - [ ] "[Agent Type] Pipeline" with visual pipeline
  - [ ] Pipeline shows: Start → ByteRover Memory Check → [Steps] → ByteRover Storage
  - [ ] Arrows use → symbol

- [ ] **"Integrated Tool Orchestration" Subsection**
  - [ ] Subsection present
  - [ ] Sequential Thinking section for domain activities
  - [ ] Research & Documentation section (Context7, REF, Exa, Firecrawl)
  - [ ] Code Operations section if applicable (Octocode, Cerebras, MorphLLM)
  - [ ] Consensus & Complex Decisions section (Zen, Tavily)
  - [ ] Infrastructure & Operations section if applicable (Time)
  - [ ] Each MCP has description of how it's used

- [ ] **"Memory Management Protocol" Subsection**
  - [ ] Subsection present
  - [ ] "Every [Domain] Decision Must" section with 4 steps:
    - [ ] 1. Retrieve: byterover-retrieve-knowledge
    - [ ] 2. Execute: Use MCP tools
    - [ ] 3. Document: byterover-store-knowledge
    - [ ] 4. Attribute: Cite "According to ByteRover memory layer"
  - [ ] "Basic Memory Integration" section present
  - [ ] Domain-specific records identified
  - [ ] Cross-reference pattern mentioned
  - [ ] Evolution history mentioned

- [ ] **"[Domain]-Specific MCP Workflows" Subsection**
  - [ ] Subsection present with domain name (e.g., "Backend-Specific MCP Workflows")
  - [ ] Minimum 3 workflows present
  - [ ] Maximum 5 workflows (unless justified)
  - [ ] Each workflow shows 5-stage pattern:
    - [ ] Stage 1: Research with MCP tools
    - [ ] Stage 2: Analysis with MCP tools
    - [ ] Stage 3: Implementation with MCP tools
    - [ ] Stage 4: Validation with MCP tools
    - [ ] Stage 5: Documentation/Storage via ByteRover
  - [ ] Workflows use + to connect MCPs (e.g., "Context7 + REF")
  - [ ] ByteRover storage mentioned in final stage

### Content Quality

- [ ] **No Generic Placeholders**
  - [ ] All `[VARIABLE]` placeholders replaced
  - [ ] Domain-specific terminology used throughout
  - [ ] Concrete examples, not abstract descriptions

- [ ] **Memory Attribution**
  - [ ] "According to ByteRover memory layer" appears at least once
  - [ ] Memory operations have clear purpose statements
  - [ ] Storage includes "with complete attribution"

- [ ] **Tool Chains**
  - [ ] Workflows show tool progression with → arrows
  - [ ] MCP combinations use + symbol (e.g., "Tool1 + Tool2")
  - [ ] Clear sequence from start to ByteRover storage

- [ ] **Behavioral Mindset**
  - [ ] 2-3 sentences present
  - [ ] Captures agent's philosophy and priorities
  - [ ] Identifies key decision-making factors

- [ ] **Boundaries Section**
  - [ ] "Will:" subsection with 3 items
  - [ ] "Will Not:" subsection with 3 items
  - [ ] Clear scope definition

### Existing Content Preservation

- [ ] **No Good Content Removed**
  - [ ] All original valuable content retained
  - [ ] Enhancements added, not replaced
  - [ ] Agent's unique characteristics preserved

---

## Command Enhancement Checklist

### Structure Validation

- [ ] **YAML Frontmatter Complete**
  - [ ] `name` field present
  - [ ] `aliases` field present (list format)
  - [ ] `description` field present
  - [ ] `category` field present (workflow|analysis|execution|utility|documentation)
  - [ ] `mcp-servers` list present (list format, no markdown)
  - [ ] `personas` field present if agent-specific

- [ ] **MCP Server List**
  - [ ] byterover present (MANDATORY)
  - [ ] basic-memory present (MANDATORY)
  - [ ] Other relevant MCPs listed
  - [ ] serena present if project memory needed

- [ ] **Eight Main Sections Present**
  - [ ] Command header with "# /sc:[command]" format
  - [ ] "## Triggers" section
  - [ ] "## Context Trigger Pattern" with code block
  - [ ] "## Behavioral Flow" section
  - [ ] "## MCP Integration" section
  - [ ] "## Output Standards" section
  - [ ] "## Examples" section
  - [ ] "## Boundaries" section

### MCP Integration (CRITICAL)

- [ ] **Tool Categories Present**
  - [ ] "### Primary [Domain] Tools" section
  - [ ] "### Knowledge & Memory" section
  - [ ] Additional categories as needed

- [ ] **"Workflow Integration" Subsection (MANDATORY)**
  - [ ] Subsection present under "## MCP Integration"
  - [ ] Four-phase pattern documented:
    - [ ] 1. **Before [Command]**: byterover-retrieve-knowledge with context type
    - [ ] 2. **During [Command]**: basic-memory write_note with decision type
    - [ ] 3. **[Execution Phase]**: Key MCP operations
    - [ ] 4. **After [Command]**: byterover-store-knowledge with findings
  - [ ] Memory Attribution phrase present: "According to ByteRover memory layer"
  - [ ] Attribution follows workflow steps

### Content Quality

- [ ] **No Generic Placeholders**
  - [ ] All `[VARIABLE]` placeholders replaced
  - [ ] Command-specific details throughout
  - [ ] Concrete context/decision/findings types specified

- [ ] **Behavioral Flow**
  - [ ] 4-6 numbered phases present
  - [ ] Each phase has percentage effort estimate
  - [ ] Activities listed under each phase
  - [ ] Key activities use bold emphasis

- [ ] **Examples Section**
  - [ ] Code block with command syntax examples
  - [ ] At least 2-3 examples showing different options
  - [ ] Examples are realistic and runnable

- [ ] **Boundaries**
  - [ ] "Will:" statement present
  - [ ] "Won't:" statement present
  - [ ] Clear scope definition

### Existing Content Preservation

- [ ] **No Good Content Removed**
  - [ ] All original sections retained
  - [ ] Workflow Integration added, not replaced
  - [ ] Command's unique characteristics preserved

---

## MCP Documentation Checklist

### Structure Validation

- [ ] **Nine Main Sections Present** (or justified omissions)
  - [ ] "# [MCP Server Name] MCP Server" header
  - [ ] "**Purpose**:" line
  - [ ] "## Triggers" section
  - [ ] "## Choose When" section
  - [ ] "## Works Best With" section
  - [ ] "## Key Features" section
  - [ ] "## Available Tools" section
  - [ ] "## Usage Patterns" section
  - [ ] "## Best Practices" section
  - [ ] "## Integration Notes" section
  - [ ] "## Troubleshooting" section
  - [ ] "## Complete Examples" section (optional but recommended)

### Tools Documentation (Section 4)

- [ ] **All Tools Documented**
  - [ ] Each tool has subsection (### tool_name)
  - [ ] One-line description for each tool
  - [ ] "**Use for**:" section with 3-4 use cases
  - [ ] "**Parameters**:" section with all params
    - [ ] Each param shows (required|optional)
    - [ ] Each param has description
  - [ ] "**Example**:" code block for each tool
  - [ ] "**Returns**:" description for each tool

### Usage Patterns (Section 5)

- [ ] **Minimum 3 Patterns**
  - [ ] Pattern 1 present with yaml code block
  - [ ] Pattern 2 present with yaml code block
  - [ ] Pattern 3 present with yaml code block
  - [ ] Each pattern has:
    - [ ] "Scenario:" description
    - [ ] "Steps:" numbered list
    - [ ] "Best for:" statement

### Integration Notes (Section 7 - CRITICAL)

- [ ] **Memory Integration Subsection**
  - [ ] Subsection present
  - [ ] Attribution "According to ByteRover memory layer" present
  - [ ] Three-phase pattern documented:
    - [ ] Before Use: byterover-retrieve-knowledge
    - [ ] During Use: Usage pattern
    - [ ] After Use: byterover-store-knowledge

- [ ] **Common Workflows Subsection**
  - [ ] At least 2 workflows documented
  - [ ] Workflows show tool chains with → arrows
  - [ ] ByteRover integration shown

- [ ] **Agent Integration Subsection**
  - [ ] Lists 3+ agents using this MCP
  - [ ] Describes how each agent uses it

- [ ] **Command Integration Subsection**
  - [ ] Lists 2+ commands using this MCP
  - [ ] Describes usage context

### Content Quality

- [ ] **Choose When Section**
  - [ ] Compares against 3+ alternative MCPs
  - [ ] Clear decision criteria for each comparison
  - [ ] "For [Use Case]" patterns present

- [ ] **Works Best With Section**
  - [ ] Lists 4+ complementary MCPs
  - [ ] Shows workflow patterns with → arrows
  - [ ] Explains synergies

- [ ] **Best Practices**
  - [ ] "Do's" section with ✅ emoji and 4+ practices
  - [ ] "Don'ts" section with ❌ emoji and 3+ anti-patterns
  - [ ] "Performance Tips" section with 3+ tips

- [ ] **Troubleshooting**
  - [ ] 3+ common issues documented
  - [ ] Each issue has Symptom/Cause/Solution
  - [ ] Error messages section present
  - [ ] Performance issues section present

### Examples Quality

- [ ] **Complete Examples Present**
  - [ ] At least 1 complete example
  - [ ] Each example has:
    - [ ] **Goal**: statement
    - [ ] **Approach**: steps
    - [ ] **Code**: runnable code block
    - [ ] **Result**: outcome description
  - [ ] Examples are realistic and practical

---

## Cross-Cutting Concerns

### For ALL Files (Agents, Commands, MCPs)

- [ ] **Memory Operations**
  - [ ] byterover-retrieve-knowledge documented
  - [ ] byterover-store-knowledge documented
  - [ ] Attribution phrase "According to ByteRover memory layer" present
  - [ ] Context/findings clearly specified

- [ ] **ByteRover Integration**
  - [ ] byterover listed in relevant sections
  - [ ] basic-memory listed where applicable
  - [ ] Memory workflow shows Before/During/After pattern
  - [ ] Storage includes "with complete attribution"

- [ ] **Tool Chains**
  - [ ] Workflows use → arrows for progression
  - [ ] MCP combinations use + symbol
  - [ ] Clear start and end points
  - [ ] ByteRover storage in final stages

- [ ] **No Placeholders**
  - [ ] No `[VARIABLE]` markers remaining
  - [ ] No "TODO" or "TBD" markers
  - [ ] All sections customized for specific domain/purpose
  - [ ] Concrete examples, not abstract templates

- [ ] **Quality Writing**
  - [ ] Clear and concise language
  - [ ] Professional tone
  - [ ] Proper markdown formatting
  - [ ] No spelling or grammar errors

---

## Pre-Commit Validation

### Before Marking Complete

- [ ] **Read Through**
  - [ ] Entire file read for coherence
  - [ ] Flow makes sense
  - [ ] No contradictions

- [ ] **Test Examples**
  - [ ] Code examples are syntactically correct
  - [ ] Tool calls use correct parameters
  - [ ] Workflows are logical and executable

- [ ] **Compare to Template**
  - [ ] All required sections from template present
  - [ ] Section order matches template
  - [ ] Quality criteria met

- [ ] **Compare to Gold Standard**
  - [ ] Matches quality of backend-architect.md (agents)
  - [ ] Matches quality of research.md (commands)
  - [ ] Matches quality of MCP_Exa.md (MCP docs)

- [ ] **ByteRover Update**
  - [ ] Store enhancement completion in ByteRover
  - [ ] Include file path, completion date, key changes
  - [ ] Attribute with "According to ByteRover memory layer"

---

## Rejection Criteria (MUST FIX)

### Immediate Rejection If:

❌ byterover OR basic-memory missing from frontmatter  
❌ "ByteRover Memory-First Pattern" section missing (agents)  
❌ "Workflow Integration" section missing (commands)  
❌ Memory Integration section missing (MCP docs)  
❌ Attribution phrase "According to ByteRover memory layer" missing  
❌ Generic `[VARIABLE]` placeholders remaining  
❌ No domain-specific MCP workflows (agents)  
❌ No Before/During/After pattern (commands)  
❌ Tool documentation incomplete (MCP docs)  
❌ Existing good content removed without justification  

### Quality Issues Requiring Fix:

⚠️ Inline MCP comments missing  
⚠️ Tool chains don't use → arrows  
⚠️ Workflows missing ByteRover storage  
⚠️ Examples are generic or non-functional  
⚠️ Less than 3 domain workflows (agents)  
⚠️ Less than 3 usage patterns (MCP docs)  
⚠️ Boundaries section incomplete  

---

## Sign-Off

### File Information
- **File Path**: _______________________
- **File Type**: [ ] Agent [ ] Command [ ] MCP Doc
- **Tier**: [ ] Tier 1 [ ] Tier 2 [ ] Tier 3

### Validation
- [ ] All applicable checklist items marked
- [ ] All rejection criteria avoided
- [ ] Quality issues resolved
- [ ] ByteRover memory updated with completion

### Status
- [ ] **APPROVED** - Ready for commit
- [ ] **NEEDS REVISION** - Issues to address

**Validator**: _______________________  
**Date**: _______________________

---

**Status**: ✅ Ready for use
**Last Updated**: 2025-10-02T19:32:24Z