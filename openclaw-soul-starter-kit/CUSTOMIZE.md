# SOUL.md Starter Kit — Customization Guide

## How to Use This Kit

1. **Pick the template closest to your use case:** Personal Assistant, Content Creator, or Dev/Ops.
2. **Copy it into your SOUL.md file.**
3. **Replace every `[BRACKET]` with your specifics.** Vague templates produce vague agents.
4. **Delete sections you don't need.** Shorter is better.
5. **Test it:** Give your agent 3 tasks. If it asks too many questions, your Operating Mode section is too vague. If it makes bad decisions, your Hard Rules need tightening.

## Section-by-Section Guide

### Name
Just a name. It's how you'll refer to your agent and how it identifies itself. Pick anything.

### Role
One sentence. "Personal assistant for [Name]" or "Content production agent for [Brand]." This single line sets the agent's entire frame of reference.

### Style
3-4 adjectives. This is your agent's personality dial. Examples:
- "Direct, terse, safety-first" → minimal output, no pleasantries
- "Conversational, witty, educational" → friendly but informative
- "Formal, precise, exhaustive" → thorough, no ambiguity

### Core Priorities
Rank 3 things. When your agent faces a tradeoff, it uses these to decide. Example: "Save time" beats "be thorough" if you rank them that way.

### Hard Rules
These are your kill switches — things the agent must NEVER do. Common additions:
- Maximum autonomous spending limit
- "Never contact real customers without my review"
- "Never modify these files: [list]"

### Operating Mode
This is the "how to work" section. The most important parts:
- **When to ask vs. act:** Be specific. "Ask before spending money" is better than "be careful."
- **Output format:** If you want bullet points, say so. If you want commands first, say so.

### Output Contract
What "done" looks like. This prevents the agent from writing essays when you want a one-liner. Key fields:
- Default response length
- Required evidence (commands run, files changed)
- How to handle uncertainty

## Common Mistakes

1. **Too long.** SOUL.md should be 50-100 lines. If it's 300 lines, the agent can't find the rules that matter.
2. **Too vague.** "Be helpful" tells the agent nothing. "Deliver draft blog posts, not outlines" tells it exactly what to do.
3. **No Hard Rules.** Without boundaries, agents will surprise you — usually at the worst time.
4. **Copied from someone else without customization.** The [BRACKETS] exist because your agent needs YOUR context, not generic advice.

## Iteration Loop

Your first SOUL.md won't be perfect. Here's how to improve it:

1. **Week 1:** Run with your template as-is. Note when the agent does something unexpected.
2. **Week 2:** For each surprise, add one Hard Rule or refine one Operating Mode instruction.
3. **Week 3:** Delete anything the agent never references. If a section doesn't change behavior, it's noise.
4. **Month 2+:** Your SOUL.md should stabilize at 40-80 lines. Most changes after this are small tweaks.

## Going Further

The $19 OpenClaw First Workflow Package includes a production-tested SOUL.md with advanced sections:
- Decision framework with explicit tradeoff scoring
- Model escalation triggers (when to use smarter/simpler models)
- Recovery instructions for context loss
- Production reliability patterns

→ [Get the full package](https://aaronmakelky.com/shop.html)
