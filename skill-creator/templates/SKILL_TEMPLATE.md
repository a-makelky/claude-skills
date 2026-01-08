---
name: [Skill Name - max 64 chars]
description: [What it does + when to use it - max 200 chars]
# Optional fields:
# dependencies: python>=3.8, requests
# allowed-tools: "Read,Write,Bash(specific-command:*)"
# model: claude-opus-4-20250514
# license: MIT
---

# [Skill Name]

[1-2 sentence purpose statement explaining what this skill does and the value it provides.]

## Overview

[Detailed explanation of:
- What problem this skill solves
- When Claude should use it (specific triggers)
- What outcomes users can expect]

## Prerequisites

[List requirements:]
- Required tools: Read, Write, etc.
- Required files or context
- Required environment or setup

## Instructions

### Step 1: [First Action Name]

[Imperative instructions for the first step. Use action verbs:]
1. Analyze the input to understand...
2. Validate that required conditions are met...
3. Prepare the processing environment...

### Step 2: [Second Action Name]

[Continue with the workflow:]
1. Execute the main processing logic...
2. Handle edge cases as follows...
3. Track progress and intermediate results...

### Step 3: [Third Action Name]

[Complete the workflow:]
1. Compile results into the final format...
2. Validate output meets requirements...
3. Present results to user...

## Output Format

[Describe how results should be structured:]

```
[Example output format]
```

## Error Handling

[Explain what to do when things fail:]

**If input is invalid:**
- Report specific validation errors
- Suggest corrections

**If processing fails:**
- Capture error details
- Attempt recovery if possible
- Report clear error message

**If output cannot be generated:**
- Explain what went wrong
- Provide partial results if available

## Examples

### Example 1: [Basic Use Case]

**Input:**
```
[Example user request]
```

**Actions:**
1. [What the skill does]
2. [Step by step]

**Output:**
```
[Expected result]
```

### Example 2: [Advanced Use Case]

**Input:**
```
[More complex request]
```

**Actions:**
1. [Handle complexity]
2. [Additional steps]

**Output:**
```
[Expected result]
```

## Resources

[Reference bundled files if any:]
- Scripts: `{baseDir}/scripts/`
- References: `{baseDir}/references/`
- Templates: `{baseDir}/templates/`

---

<!-- 
SKILL AUTHORING CHECKLIST:

Before publishing, verify:
☐ Name is ≤64 characters
☐ Description is ≤200 characters  
☐ Description explains WHEN to use (not just what)
☐ Instructions use imperative language
☐ Examples show concrete inputs/outputs
☐ All {baseDir} paths are correct
☐ No hardcoded sensitive information
☐ Error handling is comprehensive
☐ Total content is under ~5000 words
-->
