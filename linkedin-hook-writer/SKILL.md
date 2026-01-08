---
name: linkedin-hook-writer
description: Rewrite LinkedIn post hooks to maximize engagement. Use when a user provides a draft LinkedIn post and wants the opening lines (hook) optimized for clicks and engagement. Transforms any post opening into a high-performing hook using proven templates and strict character/spacing rules for LinkedIn's mobile display.
---

# LinkedIn Hook Writer

Transform draft LinkedIn posts into high-engagement hooks. The hook (first 3 lines before "see more") determines 90% of a post's performance.

## Process

1. Analyze the draft to identify: core topic, target audience, value proposition, and dream outcome
2. Select the best-fit hook type and template from references/hook-templates.md
3. Generate 3 distinct hook options using different approaches
4. Validate each option against spacing and character rules
5. Present options with character counts displayed

## Formatting Rules (Critical)

### Spacing Structure

LinkedIn shows 3 lines before "see more". Only use 2 lines for text:

```
[LINE 1]
[EMPTY LINE]
[LINE 2]
```

OR

```
[LINE 1]
[LINE 2]
[EMPTY LINE]
```

### Character Limits (Strict)

- Line 1: Max 62 characters
- Line 2: Max 62 characters  
- Line 3: Max 50 characters

Exceeding these causes text spillover on mobile, killing engagement.

### Style Rules

- NO bold text
- NO italics
- NO unnecessary emojis
- Keep language short, snappy, curiosity-inducing
- NO cliche CTAs at the end (e.g., "What do you think?", "Share your thoughts", "Which resonates with you?")
- Content should be punchy and powerful enough to drive engagement without begging for it
- End with impact, not questions

## Output Format

Present each hook option as:

```
**Option [N]: [Hook Type Used]**

[Line 1] (XX chars)

[Line 2] (XX chars)
```

For detailed hook types, power phrases, and templates, see references/hook-templates.md.

## Validation

To validate hook character counts, run:

```bash
python scripts/validate_hook.py "Line 1 text" "Line 2 text"
```
