# Laura Ghostwriter

A Claude skill for drafting LinkedIn posts in Laura Burkhauser's authentic voice. Produces 80-90% publication-ready content.

## Who Is This For?

Anyone drafting LinkedIn content on Laura's behalf—whether from bullet points, transcripts, rough ideas, or fully-formed briefs.

## Quick Start

**Draft a post:**
```
/lauraghostwriter post about our new Underlord v2 release
```

**Review session and improve the skill:**
```
/lauraghostwriter feedback
```

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Core skill instructions (load this) |
| `voice_profile.md` | Detailed voice analysis and patterns |
| `sample_posts.md` | Reference examples by content type |
| `README.md` | This file |

## How to Use

### Slash Command (Recommended)

```
/lauraghostwriter [your brief here]
```

### Natural Language

The skill also activates when you:
- Ask to draft LinkedIn content for Laura
- Ask to write something in Laura's voice
- Provide a brief and mention Laura

### Example Prompts

**From an idea:**
> `/lauraghostwriter post about how we think about building AI features at Descript—specifically the decision between buttons vs. chat interfaces`

**From bullet points:**
> `/lauraghostwriter post about our new Underlord feature:
> - It's an AI agent that edits video for you
> - We focused on making it controllable, not autonomous
> - Early users are loving it for rough cuts`

**From a vague brief:**
> `/lauraghostwriter something about the January cold outbound season and how annoying it is`

**Informal/quick:**
> `/lauraghostwriter short post asking which of these 4 logo options people prefer`

## Voice Summary

Laura's voice is:
- **Authentically unpolished** — self-deprecating, slightly absurdist
- **Sharp & direct** — no preamble, gets to the point
- **Framework-oriented** — thinks in mental models
- **Pop culture savvy** — unexpected references (Matrix, Dark Kermit)
- **Builder-first** — product person who happens to be CEO

## What This Skill Avoids

- Corporate-speak and press release energy
- "I'm thrilled to announce" openers
- Hashtag spam and emoji overload
- Engagement bait CTAs
- Performative vulnerability
- Buzzwords: "unlock," "leverage," "synergy," "game-changer"

## Continuous Learning

The skill learns from your edits and feedback automatically.

### Passive Learning (Always On)
- Observes what you change in drafts
- Tracks patterns across multiple posts
- Notes new vocabulary you add

### Explicit Feedback
When you want to review learnings and update the skill:

```
/lauraghostwriter feedback
```

This triggers a session review with:
- Summary of what was drafted
- Observed patterns and corrections
- Suggested updates (copy-paste ready)

### How Updates Work

The skill proposes updates at natural breakpoints:
- After you make significant edits to a draft
- When you say something didn't work
- When you wrap up a session
- When you explicitly ask with `/lauraghostwriter feedback`

Updates are provided as **copy-paste ready text** so you can easily add them to the skill files.

## Updating the Skill

When the skill suggests updates (or you discover new patterns):

1. Add new examples to `sample_posts.md`
2. Update patterns in `voice_profile.md`
3. Adjust rules in `SKILL.md` if needed

Updates persist across sessions once saved to the files.

## Packaging

To create a `.claude.skill.zip` for distribution:

```bash
cd skill-creator/scripts
python package_skill.py ../../laura-ghostwriter-skill
```

This will create `laura-ghostwriter.claude.skill.zip` in the skill folder.

