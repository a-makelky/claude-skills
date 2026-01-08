# Skill Authoring Best Practices

This document provides detailed guidance on creating effective Claude skills based on Anthropic's official guidelines and the Agent Skills architecture.

## Understanding How Skills Work

### The Skill Meta-Tool Architecture

Skills operate through a **meta-tool architecture** where a tool named `Skill` acts as a container and dispatcher for all individual skills. This is fundamentally different from traditional tools:

| Aspect | Normal Tools | Skills |
|--------|--------------|--------|
| Purpose | Perform specific operations | Guide complex workflows |
| Execution | Direct action | Prompt expansion + context modification |
| Return | Immediate results | Conversation context + execution context changes |
| Token Overhead | Minimal (~100 tokens) | Significant (~1,500+ tokens per turn) |

### Progressive Disclosure

The most important concept for skills is **progressive disclosure**:

1. **Level 1 - Frontmatter**: Minimal metadata (name, description) shown to help Claude decide which skill to use
2. **Level 2 - SKILL.md body**: Comprehensive instructions loaded when skill is invoked
3. **Level 3 - Resources**: Helper scripts, references, and templates loaded during execution

This system prevents context bloat while maintaining discoverability.

### How Claude Selects Skills

There is **no algorithmic skill selection**. Claude reads all skill descriptions from the `<available_skills>` section and uses pure language model reasoning to match user intent. This means:

- **Your description is critical** - it's the primary signal Claude uses
- **Be specific about triggers** - describe WHEN to use the skill
- **Use action-oriented language** - "Generate...", "Create...", "When user wants to..."

## Writing Effective Descriptions

### The 200-Character Challenge

Your description must:
1. Explain what the skill does
2. Explain when to use it
3. Fit in 200 characters

### Description Patterns

**Pattern 1: Action + Trigger**
```
Generate Python unit tests. Use when user wants pytest tests for their code or asks to test functions.
```

**Pattern 2: Domain + Capability**
```
Apply Acme Corp brand guidelines to presentations and documents, including colors, fonts, and logo usage.
```

**Pattern 3: Tool + Use Case**
```
Extract and process text from PDF documents. Use when user needs to read, analyze, or convert PDF files.
```

### Bad Descriptions

```
❌ "Testing helper" - Too vague
❌ "Does lots of things with code" - Unclear trigger
❌ "A skill for helping users" - No specificity
❌ "Use this for everything related to..." - Too broad
```

## Structuring Instructions

### Use Imperative Language

Write instructions as commands, not suggestions:

```markdown
✅ "Analyze the input file for syntax errors"
✅ "Generate a comprehensive report including..."
✅ "Validate all required fields are present"

❌ "You should analyze the input file"
❌ "It would be good to generate a report"
❌ "The skill will validate fields"
```

### Step-by-Step Workflows

Break complex tasks into discrete steps:

```markdown
### Step 1: Validate Input
1. Check that the input file exists
2. Verify the file format matches expectations
3. Report any validation errors

### Step 2: Process Data
1. Parse the input using the appropriate parser
2. Apply transformations according to rules
3. Handle edge cases gracefully

### Step 3: Generate Output
1. Format results according to output specification
2. Write to the designated output location
3. Provide summary of actions taken
```

### Include Examples

Examples dramatically improve skill reliability:

```markdown
## Examples

### Example 1: Basic Usage

**User Request:**
"Create tests for my calculator.py file"

**Expected Actions:**
1. Read calculator.py
2. Identify functions: add, subtract, multiply, divide
3. Generate test_calculator.py with pytest tests
4. Include edge cases: division by zero, large numbers

**Expected Output:**
```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
...
```
```

## Managing Context Size

### The 5,000-Word Guideline

Keep SKILL.md under 5,000 words (~800 lines). Larger skills cause:
- Increased token costs per turn
- Slower response times
- Potential context overflow

### Use References for Detail

Move detailed content to `references/`:

```markdown
# In SKILL.md
For detailed API specifications, load:
Read {baseDir}/references/api_spec.md

# In references/api_spec.md
[Detailed 3000-word specification here]
```

### Lazy Loading Pattern

Only load what you need:

```markdown
## Processing Rules

For basic processing, apply these core rules:
1. Rule A
2. Rule B

For advanced processing with edge cases, load:
Read {baseDir}/references/advanced_rules.md
```

## Security Best Practices

### Scoped Tool Permissions

Principle of least privilege:

```yaml
# ✅ Specific commands only
allowed-tools: "Bash(git status:*),Bash(git diff:*),Read"

# ✅ Scoped to skill scripts
allowed-tools: "Bash(python {baseDir}/scripts/*:*),Read,Write"

# ❌ Too broad - security risk
allowed-tools: "Bash"
```

### Never Hardcode Secrets

```markdown
❌ api_key = "sk-1234567890abcdef"
❌ password = "mysecretpassword"

✅ Read API key from environment: $API_KEY
✅ Prompt user for credentials when needed
```

### Validate Inputs

```python
# In your scripts
def process_file(path):
    # Validate path is within expected directory
    if not path.startswith(ALLOWED_DIR):
        raise ValueError("Path outside allowed directory")
    
    # Validate file type
    if not path.endswith('.txt'):
        raise ValueError("Only .txt files allowed")
```

## Common Patterns

### Pattern: Configuration Wizard

For multi-step setup processes:

```markdown
## Setup Wizard

### Phase 1: Gather Requirements
1. Ask user for project type
2. Confirm technology stack
3. Identify integration points

Wait for user confirmation.

### Phase 2: Generate Configuration
1. Create config files based on inputs
2. Set up directory structure
3. Initialize required dependencies

Present results and ask for approval.

### Phase 3: Validate Setup
1. Run validation checks
2. Report any issues
3. Provide next steps
```

### Pattern: Analysis Pipeline

For data processing workflows:

```markdown
## Analysis Pipeline

### Stage 1: Data Collection
Gather data from specified sources:
`python {baseDir}/scripts/collect.py --source "$SOURCE"`

### Stage 2: Processing
Transform and clean the data:
`python {baseDir}/scripts/process.py --input data.json`

### Stage 3: Analysis
Generate insights:
`python {baseDir}/scripts/analyze.py --data processed.json`

### Stage 4: Reporting
Create final report:
`python {baseDir}/scripts/report.py --format markdown`
```

### Pattern: Code Generation

For generating code from specifications:

```markdown
## Code Generation

### Input Analysis
1. Parse the specification document
2. Extract entities, relationships, and constraints
3. Validate completeness

### Generation Rules
Apply these rules when generating code:
- Follow language-specific conventions
- Include type hints where applicable
- Add docstrings for public interfaces
- Generate corresponding tests

### Output Structure
Generate files in this structure:
```
output/
├── src/
│   └── [generated source files]
├── tests/
│   └── [generated test files]
└── README.md
```
```

## Testing Your Skill

### Pre-Upload Checklist

1. ☐ SKILL.md has valid frontmatter
2. ☐ Name is ≤64 characters
3. ☐ Description is ≤200 characters
4. ☐ Description explains WHEN to use
5. ☐ All referenced files exist
6. ☐ No hardcoded paths (use {baseDir})
7. ☐ No sensitive information
8. ☐ Scripts are executable
9. ☐ Examples are included

### Test Prompts

Create test prompts that:
- Should trigger your skill
- Should NOT trigger your skill
- Are edge cases

```
# Should trigger
"Create a unit test for my login function"
"Generate pytest tests for utils.py"
"I need tests for this code"

# Should NOT trigger
"Tell me about unit testing best practices"
"What is pytest?"
"Review my existing tests"

# Edge cases
"Test this" (ambiguous)
"Make sure my code works" (vague)
```

### Iteration Process

1. Upload skill and test with trigger prompts
2. Check Claude's thinking to confirm skill loaded
3. If not loading, revise description
4. If loading incorrectly, clarify instructions
5. Repeat until reliable

## Troubleshooting

### Skill Not Being Invoked

**Cause**: Description doesn't match user intent
**Fix**: Make description more specific about triggers

**Cause**: Description too long (truncated)
**Fix**: Ensure under 200 characters

**Cause**: Another skill matching better
**Fix**: Make your trigger conditions more distinct

### Instructions Not Being Followed

**Cause**: Instructions too vague
**Fix**: Add specific examples and expected outputs

**Cause**: Too many options confusing Claude
**Fix**: Simplify to clear decision tree

**Cause**: Missing context
**Fix**: Add prerequisite checks at start

### Scripts Failing

**Cause**: Wrong path
**Fix**: Use {baseDir} for all paths

**Cause**: Missing dependencies
**Fix**: Add to dependencies field or check in script

**Cause**: Permission denied
**Fix**: Ensure script is executable, add to allowed-tools

## Resources

- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Agent Skills Specification](https://agentskills.io)
- [Claude Documentation](https://docs.anthropic.com)
