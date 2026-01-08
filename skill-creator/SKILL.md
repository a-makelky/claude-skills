---
name: Skill Creator
description: Guide for creating effective Claude skills. Use when users want to create a new skill, improve an existing skill, or learn skill authoring best practices.
---

# Skill Creator

This skill helps you create well-structured, effective Claude skills that follow Anthropic's official guidelines and best practices.

## Overview

Claude Skills are specialized prompt templates that extend Claude's capabilities through organized folders of instructions, scripts, and resources. Skills operate through **progressive disclosure**—showing just enough information to help Claude decide what to do, then revealing more details as needed.

**Key Insight**: Skill = Prompt Template + Conversation Context Injection + Execution Context Modification + Optional data files and Python Scripts

## When to Use This Skill

- Creating a new skill from scratch
- Improving or refactoring an existing skill
- Learning skill authoring best practices
- Validating a skill's structure and content
- Packaging a skill for distribution

## Skill Creation Process

### Step 1: Define the Purpose

Before writing any code, answer these questions:

1. **What specific, repeatable task does this skill solve?**
   - Skills should be focused on ONE workflow, not everything
   - If your skill does multiple unrelated things, split it into separate skills

2. **When should Claude invoke this skill?**
   - Write this as a clear trigger condition
   - This becomes your `description` field (max 200 characters)

3. **What does success look like?**
   - Define concrete examples of inputs and expected outputs
   - These examples will guide your instructions

### Step 2: Create the Directory Structure

Run the initialization script to create a properly structured skill:

```bash
python {baseDir}/scripts/init_skill.py <skill-name> --path <output-directory>
```

This creates:
```
<skill-name>/
├── SKILL.md           # Core prompt and instructions (REQUIRED)
├── scripts/           # Executable Python/Bash scripts
├── references/        # Documentation loaded into context
└── templates/         # Templates and static files (assets)
```

### Step 3: Write the SKILL.md File

The SKILL.md file has two parts:

#### Part 1: YAML Frontmatter (Metadata)

```yaml
---
name: <skill-name>                    # REQUIRED: Human-friendly name (max 64 chars)
description: <what-and-when>          # REQUIRED: What it does + when to use (max 200 chars)
dependencies: python>=3.8, pandas     # OPTIONAL: Required packages
allowed-tools: "Read,Write,Bash"      # OPTIONAL: Pre-approved tools for this skill
model: claude-opus-4-20250514         # OPTIONAL: Specific model override
license: MIT                          # OPTIONAL: License information
---
```

**Critical**: The `description` field is how Claude decides to invoke your skill. Make it specific and action-oriented:

✅ Good: "Generate Python unit tests for functions. Use when user wants to create pytest tests for their code."
❌ Bad: "Testing helper"

#### Part 2: Markdown Body (Instructions)

Use this recommended structure:

```markdown
# <Skill Name>

Brief 1-2 sentence purpose statement.

## Overview
What this skill does, when to use it, what it provides.

## Prerequisites
Required tools, files, or context.

## Instructions

### Step 1: [First Action]
Imperative instructions (use "Analyze...", "Generate...", not "You should...")
Include examples if needed.

### Step 2: [Next Action]
Continue with clear, actionable steps.

## Output Format
How to structure results.

## Error Handling
What to do when things fail.

## Examples
Concrete usage examples with inputs and expected outputs.

## Resources
Reference scripts/, references/, templates/ if bundled.
```

### Step 4: Bundle Resources (If Needed)

#### scripts/ Directory
Contains executable code Claude runs via the Bash tool:
- Python scripts for complex operations
- Shell scripts for automation
- Data processors and validators

Reference in SKILL.md:
```markdown
Run the analysis script:
`python {baseDir}/scripts/analyzer.py --input "$FILE"`
```

#### references/ Directory
Contains documentation that Claude reads into context:
- Detailed specifications
- API schemas
- Pattern libraries

Reference in SKILL.md:
```markdown
Load the style guide: Read {baseDir}/references/style_guide.md
```

#### templates/ Directory
Contains files Claude references by path but doesn't load into context:
- HTML/CSS templates
- Configuration boilerplate
- Binary files

Reference in SKILL.md:
```markdown
Use the template at {baseDir}/templates/report.html
```

**Key Distinction**:
- `references/` → Text loaded INTO Claude's context (uses tokens)
- `templates/` → Files referenced BY PATH only (no token cost)

### Step 5: Configure Tool Permissions

The `allowed-tools` field specifies pre-approved tools:

```yaml
# ✅ Specific and minimal
allowed-tools: "Read,Write,Bash(git status:*),Bash(git diff:*)"

# ✅ Scoped bash commands
allowed-tools: "Bash(python {baseDir}/scripts/*:*),Read,Write"

# ❌ Too broad - security risk
allowed-tools: "Bash,Read,Write,Edit,Glob,Grep,WebSearch"
```

**Principle**: Only include tools your skill actually needs.

### Step 6: Validate Your Skill

Run the validation script:
```bash
python {baseDir}/scripts/validate_skill.py <skill-directory>
```

This checks:
- Required frontmatter fields present
- Description under 200 characters
- Name under 64 characters
- Referenced files exist
- Markdown structure is valid

### Step 7: Package for Distribution

```bash
python {baseDir}/scripts/package_skill.py <skill-directory> --output <output.zip>
```

Correct ZIP structure:
```
my-skill.zip
└── my-skill/
    ├── SKILL.md
    ├── scripts/
    ├── references/
    └── templates/
```

## Best Practices

### Do:
- **Keep it focused**: One skill = one workflow. Multiple focused skills compose better.
- **Use imperative language**: "Analyze the code..." not "You should analyze..."
- **Include examples**: Show concrete inputs and expected outputs.
- **Use {baseDir}** for all paths: Never hardcode absolute paths.
- **Keep SKILL.md under 5,000 words**: Use references/ for detailed content.
- **Test incrementally**: Validate after each change.
- **Write clear descriptions**: Claude uses these to decide when to invoke.

### Don't:
- Hardcode sensitive information (API keys, passwords)
- List every possible tool in allowed-tools
- Try to solve multiple unrelated problems
- Embed large reference content directly in SKILL.md
- Use hardcoded absolute paths (always use `{baseDir}` instead)

## Common Patterns

### Pattern 1: Script Automation
```markdown
Run scripts/processor.py on the input:
`python {baseDir}/scripts/processor.py --input "$INPUT" --output report.json`
Parse the generated report.json and present findings.
```

### Pattern 2: Read-Process-Write
```markdown
1. Read input file using Read tool
2. Transform content following specifications
3. Write output using Write tool
4. Report completion with summary
```

### Pattern 3: Search-Analyze-Report
```markdown
1. Use Grep to find relevant patterns
2. Read each matched file for context
3. Analyze findings
4. Generate structured report
```

### Pattern 4: Template-Based Generation
```markdown
1. Read template from {baseDir}/templates/template.html
2. Parse user requirements
3. Fill template placeholders
4. Write filled template to output
```

## Troubleshooting

**Skill not being invoked?**
- Check that description clearly states when to use it
- Verify description is under 200 characters
- Test with prompts that match your description exactly

**Tools not working?**
- Verify tools are listed in allowed-tools
- Check bash command patterns match your usage
- Ensure {baseDir} is used correctly

**Context too large?**
- Move detailed content to references/
- Keep SKILL.md focused on workflow, not data
- Use templates/ for files referenced by path only

## Resources

- Initialization script: `{baseDir}/scripts/init_skill.py`
- Validation script: `{baseDir}/scripts/validate_skill.py`
- Packaging script: `{baseDir}/scripts/package_skill.py`
- SKILL.md template: `{baseDir}/templates/SKILL_TEMPLATE.md`
- Best practices reference: `{baseDir}/references/best_practices.md`
