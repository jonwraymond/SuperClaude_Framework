---
name: design
description: "Design system architecture, APIs, and component interfaces with comprehensive specifications"
category: utility
complexity: basic
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena]
personas: [system-architect, backend-architect, frontend-architect, security-engineer]
---

# /sc:design - System and Component Design

## Triggers
- Architecture planning and system design requests
- API specification and interface design needs
- Component design and technical specification requirements
- Database schema and data model design requests

## Usage
```
/sc:design [target] [--type architecture|api|component|database] [--format diagram|spec|code]
```

## Behavioral Flow
1. **Analyze**: Examine target requirements and existing system context
2. **Plan**: Define design approach and structure based on type and format
3. **Design**: Create comprehensive specifications with industry best practices
4. **Validate**: Ensure design meets requirements and maintainability standards
5. **Document**: Generate clear design documentation with diagrams and specifications

Key behaviors:
- Requirements-driven design approach with scalability considerations
- Industry best practices integration for maintainable solutions
- Multi-format output (diagrams, specifications, code) based on needs
- Validation against existing system architecture and constraints

## MCP Integration

### Design & Planning Tools
- **Zen**: Consensus building (zen_consensus), architectural decisions (zen_planner), deep design analysis (zen_thinkdeep)
- **Sequential-thinking**: Multi-step design workflows and systematic planning
- **Serena**: Project context understanding and architectural memory

### Knowledge & Memory Integration
- **ByteRover**: Retrieve architectural patterns and store verified design decisions with timestamps
- **Basic-Memory**: Document design decisions and architectural patterns with WikiLinks

### Research & Documentation
- **Context7**: Official framework documentation and architectural best practices
- **Ref**: Search documentation for design patterns and architectural guidelines
- **Firecrawl**: Web scraping for architectural examples and design patterns
- **Octocode**: GitHub exploration for architectural examples and design implementations

### Workflow Integration (per AGENTS.md)
1. **Before Design**: Use byterover-retrieve-knowledge to gather relevant architectural patterns
2. **Design Process**: Use zen_consensus for architectural decisions and zen_planner for systematic design
3. **Research**: Use context7 and ref for framework-specific design patterns
4. **Validation**: Use zen_thinkdeep for comprehensive design analysis
5. **Documentation**: Use basic-memory write_note to document design decisions with WikiLinks
6. **After Design**: Store validated architectural patterns in byterover with complete specifications

## Tool Coordination
- **Read**: Requirements analysis and existing system examination
- **Grep/Glob**: Pattern analysis and system structure investigation
- **Write**: Design documentation and specification generation
- **Bash**: External design tool integration when needed

## Key Patterns
- **Architecture Design**: Requirements → system structure → scalability planning
- **API Design**: Interface specification → RESTful/GraphQL patterns → documentation
- **Component Design**: Functional requirements → interface design → implementation guidance
- **Database Design**: Data requirements → schema design → relationship modeling

## Examples

### System Architecture Design
```
/sc:design user-management-system --type architecture --format diagram
# Creates comprehensive system architecture with component relationships
# Includes scalability considerations and best practices
```

### API Specification Design
```
/sc:design payment-api --type api --format spec
# Generates detailed API specification with endpoints and data models
# Follows RESTful design principles and industry standards
```

### Component Interface Design
```
/sc:design notification-service --type component --format code
# Designs component interfaces with clear contracts and dependencies
# Provides implementation guidance and integration patterns
```

### Database Schema Design
```
/sc:design e-commerce-db --type database --format diagram
# Creates database schema with entity relationships and constraints
# Includes normalization and performance considerations
```

## Boundaries

**Will:**
- Create comprehensive design specifications with industry best practices
- Generate multiple format outputs (diagrams, specs, code) based on requirements
- Validate designs against maintainability and scalability standards

**Will Not:**
- Generate actual implementation code (use /sc:implement for implementation)
- Modify existing system architecture without explicit design approval
- Create designs that violate established architectural constraints