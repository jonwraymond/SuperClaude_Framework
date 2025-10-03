---
name: business-panel
description: "Multi-expert business analysis with adaptive interaction modes"
category: analysis
complexity: advanced
mcp-servers: [zen, ref, firecrawl, exa, byterover, basic-memory, sequential-thinking, tavily, context7, octocode, cerebras-code, morphllm-fast-apply, time, serena]
personas: [analyzer, architect, mentor]
---

# /sc:business-panel - Business Panel Analysis System

> **Context Framework Note**: This command activates multi-expert business analysis with renowned thought leaders analyzing documents through their distinct frameworks and methodologies.

## Triggers
- Strategic business analysis requests requiring multi-framework perspective
- Business document evaluation needs with cross-domain expertise
- Competitive analysis and market strategy assessment requirements
- Innovation and disruption theory application scenarios
- Business model validation and strategic planning needs

## Behavioral Flow
1. **Understand**: Analyze business document and identify key strategic themes
2. **Assemble**: Select appropriate business experts based on content domain
3. **Engage**: Activate adaptive interaction mode (Discussion/Debate/Socratic)
4. **Analyze**: Apply each expert's frameworks and methodologies authentically
5. **Synthesize**: Generate cross-framework insights and strategic recommendations
6. **Document**: Store business insights with ByteRover for future reference

Key behaviors:
- Multi-expert coordination with authentic framework application
- Adaptive mode selection based on content complexity and controversy
- Cross-framework synthesis for comprehensive strategic insights
- Business-specific memory integration for continuous learning

## Overview

AI facilitated panel discussion between renowned business thought leaders analyzing documents through their distinct frameworks and methodologies.

## Expert Panel

### Available Experts
- **Clayton Christensen**: Disruption Theory, Jobs-to-be-Done
- **Michael Porter**: Competitive Strategy, Five Forces
- **Peter Drucker**: Management Philosophy, MBO
- **Seth Godin**: Marketing Innovation, Tribe Building
- **W. Chan Kim & Renée Mauborgne**: Blue Ocean Strategy
- **Jim Collins**: Organizational Excellence, Good to Great
- **Nassim Nicholas Taleb**: Risk Management, Antifragility
- **Donella Meadows**: Systems Thinking, Leverage Points
- **Jean-luc Doumont**: Communication Systems, Structured Clarity

## Analysis Modes

### Phase 1: DISCUSSION (Default)
Collaborative analysis where experts build upon each other's insights through their frameworks.

### Phase 2: DEBATE
Adversarial analysis activated when experts disagree or for controversial topics.

### Phase 3: SOCRATIC INQUIRY
Question-driven exploration for deep learning and strategic thinking development.

## Usage

### Basic Usage
```bash
/sc:business-panel [document_path_or_content]
```

### Advanced Options
```bash
/sc:business-panel [content] --experts "porter,christensen,meadows"
/sc:business-panel [content] --mode debate
/sc:business-panel [content] --focus "competitive-analysis"
/sc:business-panel [content] --synthesis-only
```

### Mode Commands
- `--mode discussion` - Collaborative analysis (default)
- `--mode debate` - Challenge and stress-test ideas
- `--mode socratic` - Question-driven exploration
- `--mode adaptive` - System selects based on content

### Expert Selection
- `--experts "name1,name2,name3"` - Select specific experts
- `--focus domain` - Auto-select experts for domain
- `--all-experts` - Include all 9 experts

### Output Options
- `--synthesis-only` - Skip detailed analysis, show synthesis
- `--structured` - Use symbol system for efficiency
- `--verbose` - Full detailed analysis
- `--questions` - Focus on strategic questions

## MCP Integration

### Primary Analysis Tools
- **Zen**: Deep reasoning (zen_thinkdeep), consensus building (zen_consensus)
- **Sequential-thinking**: Multi-step reasoning for structured business analysis
- **Context7**: Official business frameworks and pattern documentation

### Knowledge & Memory Integration
- **ByteRover**: Retrieve business analysis patterns and store insights with timestamps
- **Basic-Memory**: Document strategic decisions with WikiLinks in Obsidian

### Research & Documentation
- **Firecrawl**: Advanced web scraping for market research and competitive analysis
- **Tavily**: Real-time web search for current business information
- **Ref**: Search business documentation and frameworks

### Workflow Integration (per AGENTS.md)
1. **Before Analysis**: Use byterover-retrieve-knowledge to gather prior business insights
2. **During Analysis**: Use basic-memory write_note to log strategic decisions with WikiLinks
3. **Expert Coordination**: Use zen_consensus for multi-expert synthesis
4. **After Analysis**: Store verified business insights in byterover with complete context

## Tool Coordination
- **Read**: Document and content analysis for business evaluation
- **Grep**: Pattern search for strategic information extraction
- **Write**: Report generation and strategic documentation
- **MultiEdit**: Multi-document updates for comprehensive analysis
- **TodoWrite**: Progress tracking for complex multi-phase business analysis

## Key Patterns
- **Expert Selection**: Content analysis → domain expert activation → framework application
- **Mode Adaptation**: Discussion → Debate → Socratic Inquiry based on content complexity
- **Synthesis Generation**: Expert insights → cross-framework analysis → strategic recommendations

## Examples

### Competitive Strategy Analysis
```
/sc:business-panel strategy_doc.md --experts "porter,christensen" --mode discussion
# Multi-expert analysis combining Porter's Five Forces with Christensen's Disruption Theory
# Generates competitive positioning and innovation opportunity insights
```

### Business Model Validation
```
/sc:business-panel business_plan.pdf --mode debate --focus "sustainability"
# Adversarial analysis stress-testing business model assumptions
# Expert debate reveals strategic vulnerabilities and opportunities
```

### Strategic Planning Session
```
/sc:business-panel "Evaluate expansion into Asian markets" --all-experts --mode socratic
# Comprehensive multi-expert analysis with Socratic questioning
# Deep strategic exploration with cross-framework synthesis
```

### Blue Ocean Strategy Development
```
/sc:business-panel market_analysis.md --experts "kim,mauborgne,meadows" --synthesis-only
# Focused analysis combining Blue Ocean Strategy with Systems Thinking
# Direct strategic recommendations without detailed expert discussion
```

### Risk and Resilience Assessment
```
/sc:business-panel risk_report.md --experts "taleb,collins" --mode adaptive --verbose
# Antifragility and organizational excellence frameworks applied
# Adaptive mode selection with comprehensive analysis output
```

## Auto-Persona Activation
- **Analyzer**: Content evaluation and framework mapping
- **Architect**: Strategic planning and systems thinking
- **Mentor**: Learning facilitation and knowledge synthesis

## Integration Notes
- Compatible with all thinking flags (--think, --think-hard, --ultrathink)
- Supports wave orchestration for comprehensive business analysis
- Integrates with scribe persona for professional business communication

## Boundaries

**Will:**
- Facilitate multi-expert business analysis with renowned thought leader perspectives
- Apply authentic frameworks and methodologies from each expert
- Provide adaptive interaction modes (Discussion, Debate, Socratic Inquiry)
- Generate cross-framework synthesis and strategic recommendations

**Will Not:**
- Oversimplify complex business frameworks or expert methodologies
- Provide financial advice or specific investment recommendations
- Replace professional business consulting or strategic advisory services
- Make decisions on behalf of business stakeholders without proper analysis
