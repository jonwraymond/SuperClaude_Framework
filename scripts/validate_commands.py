#!/usr/bin/env python3
"""
SuperClaude Framework - Command Validation Script
Validates command metadata, structure, and integration patterns.

Usage:
    python scripts/validate_commands.py                     # Validate all commands
    python scripts/validate_commands.py command.md          # Validate specific command
    python scripts/validate_commands.py --summary           # Summary report only
    python scripts/validate_commands.py --strict            # Fail on warnings
"""

import sys
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """Stores validation results for a command"""
    filename: str
    passed: bool = True
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)


class CommandValidator:
    """Validates SuperClaude command files"""
    
    # Valid enum values
    VALID_CATEGORIES = ['workflow', 'analysis', 'documentation', 'session', 'utility', 'command', 'orchestration']
    VALID_COMPLEXITIES = ['low', 'basic', 'standard', 'advanced']
    
    # Known MCP servers (based on framework documentation)
    KNOWN_MCP_SERVERS = [
        'zen', 'ref', 'firecrawl', 'exa', 'byterover', 'basic-memory', 
        'sequential-thinking', 'tavily', 'context7', 'octocode', 
        'cerebras-code', 'morphllm-fast-apply', 'time', 'serena', 
        'magic', 'playwright'
    ]
    
    # Known personas (based on Agents directory)
    KNOWN_PERSONAS = [
        'architect', 'frontend', 'backend', 'security', 'qa-specialist',
        'devops', 'analyzer', 'project-manager', 'deep-research-agent',
        'mentor', 'technical-writer', 'system-architect', 'quality-engineer',
        'performance-engineer', 'security-engineer'
    ]
    
    # Required sections
    REQUIRED_SECTIONS = [
        'Triggers', 'Usage', 'Behavioral Flow', 'MCP Integration',
        'Tool Coordination', 'Key Patterns', 'Examples', 'Boundaries'
    ]
    
    def __init__(self, commands_dir: Path):
        self.commands_dir = commands_dir
        self.results: List[ValidationResult] = []
    
    def validate_file(self, filepath: Path) -> ValidationResult:
        """Validate a single command file"""
        result = ValidationResult(filename=filepath.name)
        
        try:
            content = filepath.read_text()
            
            # Extract and validate YAML front matter
            metadata = self._extract_metadata(content, result)
            if metadata:
                self._validate_metadata(metadata, filepath, result)
            
            # Validate command structure
            self._validate_structure(content, result)
            
            # Validate MCP integration patterns
            self._validate_mcp_integration(content, result)
            
            # Validate ByteRover workflow
            self._validate_byterover_workflow(content, result)
            
            # Validate examples
            self._validate_examples(content, result)
            
            # Set overall pass/fail
            result.passed = len(result.errors) == 0
            
        except Exception as e:
            result.errors.append(f"Failed to validate file: {str(e)}")
            result.passed = False
        
        return result
    
    def _extract_metadata(self, content: str, result: ValidationResult) -> Optional[Dict]:
        """Extract YAML front matter"""
        # Match YAML front matter
        yaml_pattern = r'^---\s*\n(.*?)\n---'
        match = re.search(yaml_pattern, content, re.MULTILINE | re.DOTALL)
        
        if not match:
            result.errors.append("Missing YAML front matter")
            return None
        
        try:
            metadata = yaml.safe_load(match.group(1))
            return metadata
        except yaml.YAMLError as e:
            result.errors.append(f"Invalid YAML syntax: {str(e)}")
            return None
    
    def _validate_metadata(self, metadata: Dict, filepath: Path, result: ValidationResult):
        """Validate metadata completeness and correctness"""
        
        # Check required fields
        required_fields = ['name', 'description', 'category', 'complexity', 'mcp-servers']
        for field in required_fields:
            if field not in metadata:
                result.errors.append(f"Missing required field: {field}")
        
        # Validate name matches filename
        if 'name' in metadata:
            expected_name = filepath.stem  # filename without .md
            if metadata['name'] != expected_name:
                result.errors.append(
                    f"Name mismatch: metadata '{metadata['name']}' != filename '{expected_name}'"
                )
        
        # Validate description
        if 'description' in metadata:
            desc = metadata['description']
            if len(desc) > 100:
                result.warnings.append(f"Description too long ({len(desc)} chars, max 100)")
            if desc.count('.') > 1:
                result.warnings.append("Description should be a single sentence")
        
        # Validate category
        if 'category' in metadata:
            if metadata['category'] not in self.VALID_CATEGORIES:
                result.errors.append(
                    f"Invalid category '{metadata['category']}'. "
                    f"Must be one of: {', '.join(self.VALID_CATEGORIES)}"
                )
        
        # Validate complexity
        if 'complexity' in metadata:
            if metadata['complexity'] not in self.VALID_COMPLEXITIES:
                result.errors.append(
                    f"Invalid complexity '{metadata['complexity']}'. "
                    f"Must be one of: {', '.join(self.VALID_COMPLEXITIES)}"
                )
        
        # Validate MCP servers
        if 'mcp-servers' in metadata:
            servers = metadata['mcp-servers']
            if not isinstance(servers, list):
                result.errors.append("mcp-servers must be a list")
            else:
                unknown_servers = [s for s in servers if s not in self.KNOWN_MCP_SERVERS]
                if unknown_servers:
                    result.warnings.append(
                        f"Unknown MCP servers: {', '.join(unknown_servers)}"
                    )
                
                # Check for core servers
                core_servers = ['byterover', 'basic-memory', 'serena', 'time']
                missing_core = [s for s in core_servers if s not in servers]
                if missing_core:
                    result.warnings.append(
                        f"Missing recommended core servers: {', '.join(missing_core)}"
                    )
        
        # Validate personas (optional field)
        if 'personas' in metadata:
            personas = metadata['personas']
            if not isinstance(personas, list):
                result.errors.append("personas must be a list")
            else:
                unknown_personas = [p for p in personas if p not in self.KNOWN_PERSONAS]
                if unknown_personas:
                    result.warnings.append(
                        f"Unknown personas: {', '.join(unknown_personas)}"
                    )
    
    def _validate_structure(self, content: str, result: ValidationResult):
        """Validate command structure and required sections"""
        
        # Check for command header
        if not re.search(r'^# /sc:\w+', content, re.MULTILINE):
            result.errors.append("Missing command header (# /sc:command-name)")
        
        # Check for Context Framework Note
        if '> **Context Framework Note**:' not in content:
            result.warnings.append("Missing Context Framework Note in header")
        
        # Check for required sections
        for section in self.REQUIRED_SECTIONS:
            pattern = rf'^## {re.escape(section)}'
            if not re.search(pattern, content, re.MULTILINE):
                result.errors.append(f"Missing required section: {section}")
        
        # Check for subsections in MCP Integration
        if '## MCP Integration' in content:
            if 'Knowledge & Memory Integration' not in content:
                result.warnings.append(
                    "Missing 'Knowledge & Memory Integration' subsection in MCP Integration"
                )
            if 'Workflow Integration (per AGENTS.md)' not in content:
                result.warnings.append(
                    "Missing 'Workflow Integration (per AGENTS.md)' subsection in MCP Integration"
                )
    
    def _validate_mcp_integration(self, content: str, result: ValidationResult):
        """Validate MCP integration documentation"""
        
        # Check for MCP Integration section
        if '## MCP Integration' not in content:
            result.errors.append("Missing MCP Integration section")
            return
        
        # Extract MCP Integration section
        mcp_match = re.search(
            r'## MCP Integration.*?(?=^## |\Z)', 
            content, 
            re.MULTILINE | re.DOTALL
        )
        
        if mcp_match:
            mcp_section = mcp_match.group(0)
            
            # Check for knowledge management mentions
            if 'ByteRover' not in mcp_section:
                result.warnings.append("MCP Integration missing ByteRover mention")
            if 'Basic-Memory' not in mcp_section and 'basic-memory' not in mcp_section:
                result.warnings.append("MCP Integration missing Basic-Memory mention")
    
    def _validate_byterover_workflow(self, content: str, result: ValidationResult):
        """Validate ByteRover workflow integration"""
        
        # Check for workflow integration pattern
        has_workflow = False
        workflow_patterns = [
            'Workflow Integration (per AGENTS.md)',
            'byterover-retrieve-knowledge',
            'byterover-store-knowledge',
            'Before.*byterover',
            'After.*byterover'
        ]
        
        for pattern in workflow_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                has_workflow = True
                break
        
        if not has_workflow:
            result.warnings.append(
                "Missing ByteRover workflow integration (retrieve before, store after pattern)"
            )
        
        # Check for comprehensive integration (3-step pattern)
        has_before = bool(re.search(r'Before.*byterover', content, re.IGNORECASE))
        has_during = bool(re.search(r'During.*basic-memory', content, re.IGNORECASE))
        has_after = bool(re.search(r'After.*byterover', content, re.IGNORECASE))
        
        if has_before and has_during and has_after:
            result.info.append("✓ Complete ByteRover workflow integration (3-step pattern)")
        elif any([has_before, has_during, has_after]):
            result.warnings.append("Partial ByteRover workflow integration (missing steps)")
    
    def _validate_examples(self, content: str, result: ValidationResult):
        """Validate examples section"""
        
        # Check for Examples section
        if '## Examples' not in content:
            result.errors.append("Missing Examples section")
            return
        
        # Extract Examples section
        examples_match = re.search(
            r'## Examples.*?(?=^## |\Z)',
            content,
            re.MULTILINE | re.DOTALL
        )
        
        if examples_match:
            examples_section = examples_match.group(0)
            
            # Count example subsections
            example_count = len(re.findall(r'^###.*Example', examples_section, re.MULTILINE))
            
            if example_count < 3:
                result.warnings.append(
                    f"Only {example_count} example(s) provided (minimum 3 recommended)"
                )
            elif example_count >= 5:
                result.info.append(f"✓ Excellent examples section ({example_count} examples)")
            else:
                result.info.append(f"✓ Good examples section ({example_count} examples)")
    
    def validate_all(self, specific_file: Optional[str] = None) -> List[ValidationResult]:
        """Validate all commands or a specific command"""
        
        if specific_file:
            filepath = self.commands_dir / specific_file
            if not filepath.exists():
                print(f"Error: File not found: {filepath}")
                sys.exit(1)
            result = self.validate_file(filepath)
            self.results = [result]
        else:
            # Validate all .md files except README and TEMPLATE
            md_files = [
                f for f in self.commands_dir.glob('*.md')
                if f.name not in ['README.md', 'TEMPLATE.md'] and not f.name.endswith('.bak')
            ]
            
            print(f"Validating {len(md_files)} command files...\n")
            
            for filepath in sorted(md_files):
                result = self.validate_file(filepath)
                self.results.append(result)
        
        return self.results
    
    def print_results(self, summary_only: bool = False):
        """Print validation results"""
        
        if not self.results:
            print("No validation results to display")
            return
        
        # Statistics
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed
        total_errors = sum(len(r.errors) for r in self.results)
        total_warnings = sum(len(r.warnings) for r in self.results)
        
        if not summary_only:
            # Detailed results
            for result in self.results:
                status = "✅ PASS" if result.passed else "❌ FAIL"
                print(f"\n{status} - {result.filename}")
                print("-" * 60)
                
                if result.errors:
                    print("\n  ERRORS:")
                    for error in result.errors:
                        print(f"    ❌ {error}")
                
                if result.warnings:
                    print("\n  WARNINGS:")
                    for warning in result.warnings:
                        print(f"    ⚠️  {warning}")
                
                if result.info and not result.errors:
                    print("\n  INFO:")
                    for info in result.info:
                        print(f"    ℹ️  {info}")
        
        # Summary
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Total Commands:   {total}")
        print(f"Passed:           {passed} ({passed/total*100:.1f}%)")
        print(f"Failed:           {failed} ({failed/total*100:.1f}%)")
        print(f"Total Errors:     {total_errors}")
        print(f"Total Warnings:   {total_warnings}")
        print("=" * 60)
        
        if failed > 0:
            print("\n❌ VALIDATION FAILED")
            print("\nFailed commands:")
            for result in self.results:
                if not result.passed:
                    print(f"  - {result.filename}")
        else:
            print("\n✅ ALL COMMANDS PASSED VALIDATION")
        
        # ByteRover integration statistics
        with_byterover = sum(
            1 for r in self.results 
            if not any('ByteRover workflow' in w for w in r.warnings)
        )
        print(f"\nByteRover Integration: {with_byterover}/{total} commands ({with_byterover/total*100:.1f}%)")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate SuperClaude command files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/validate_commands.py                    # Validate all commands
  python scripts/validate_commands.py analyze.md         # Validate specific command
  python scripts/validate_commands.py --summary          # Summary only
  python scripts/validate_commands.py --strict           # Fail on warnings
        """
    )
    
    parser.add_argument(
        'file',
        nargs='?',
        help='Specific command file to validate (optional)'
    )
    parser.add_argument(
        '--summary',
        action='store_true',
        help='Show summary only (no detailed output)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors (fail validation)'
    )
    parser.add_argument(
        '--commands-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'SuperClaude' / 'Commands',
        help='Path to Commands directory'
    )
    
    args = parser.parse_args()
    
    # Validate commands directory exists
    if not args.commands_dir.exists():
        print(f"Error: Commands directory not found: {args.commands_dir}")
        sys.exit(1)
    
    # Run validation
    validator = CommandValidator(args.commands_dir)
    results = validator.validate_all(specific_file=args.file)
    
    # Print results
    validator.print_results(summary_only=args.summary)
    
    # Exit with appropriate code
    if any(not r.passed for r in results):
        sys.exit(1)
    
    if args.strict and any(r.warnings for r in results):
        print("\n❌ STRICT MODE: Warnings treated as errors")
        sys.exit(1)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
