# SuperClaude Framework - CI/CD Documentation

## 🔄 Continuous Integration

This directory contains GitHub Actions workflows for automated quality assurance.

### Workflows

#### `validate-commands.yml`
Automatically validates all command files on push and pull requests.

**Triggers**:
- Push to `main` or `develop` branches
- Pull requests targeting `main` or `develop`
- Only when commands or validator changes

**Validation Steps**:
1. ✅ Standard validation check
2. ✅ Strict validation (warnings as errors)
3. 📊 Generate validation report
4. 💬 Comment on PRs if validation fails

**Requirements**:
- Python 3.11+
- PyYAML package

### Local Development

#### Pre-commit Hook
A pre-commit hook is installed at `.git/hooks/pre-commit` that runs validation before every commit.

**To bypass** (not recommended):
```bash
git commit --no-verify
```

**To manually run validation**:
```bash
# Summary view
python scripts/validate_commands.py --summary

# Detailed view
python scripts/validate_commands.py

# Strict mode (warnings as errors)
python scripts/validate_commands.py --strict

# Single file
python scripts/validate_commands.py command-name.md
```

### Adding New Commands

When adding new commands:

1. **Use the template**:
   ```bash
   cp SuperClaude/Commands/TEMPLATE.md SuperClaude/Commands/new-command.md
   ```

2. **Fill in all required sections**:
   - YAML front matter
   - All 8 required sections
   - ByteRover workflow integration

3. **Validate locally**:
   ```bash
   python scripts/validate_commands.py new-command.md
   ```

4. **Commit** (triggers pre-commit hook):
   ```bash
   git add SuperClaude/Commands/new-command.md
   git commit -m "Add new-command"
   ```

5. **Push** (triggers GitHub Actions):
   ```bash
   git push origin feature/new-command
   ```

### Validation Standards

Commands must have:
- ✅ Valid YAML metadata
- ✅ All 8 required sections
- ✅ ByteRover workflow integration (3-step pattern)
- ✅ MCP Integration documentation
- ✅ Examples (3-5 recommended)

See `SuperClaude/Commands/README.md` for complete standards.

### Troubleshooting

**Pre-commit hook not running?**
```bash
chmod +x .git/hooks/pre-commit
```

**GitHub Actions failing?**
1. Check the Actions tab in GitHub
2. Review the validation report
3. Run validation locally to debug

**Need to update validation rules?**
Edit `scripts/validate_commands.py` and update:
- `REQUIRED_SECTIONS`
- `VALID_CATEGORIES`
- `VALID_COMPLEXITIES`
- `KNOWN_MCP_SERVERS`
- `KNOWN_PERSONAS`

---

**Maintained by**: SuperClaude Framework Team  
**Last Updated**: October 2, 2025
