# Claude Cowork Setup Guide

**Repo:** https://github.com/a-makelky/claude-skills
**Last Updated:** 2026-03-18

---

## What is Claude Cowork?

Claude Cowork is a project-based workspace inside Claude that maintains context across conversations. Unlike regular Claude chats that reset every time, Cowork remembers your work, your preferences, and your ongoing projects.

**The key difference:** You're not prompting from scratch every time. You're working alongside an assistant that already knows your context.

## Why Context Files Matter

Most people use Cowork like ChatGPT: open it, ask a question, close it. That works, but it misses the point.

The value comes from giving Cowork specific context about **you and your work** before you ask it to do anything. Without that context, you're just prompting a blank slate. With it, you're delegating to an assistant who already understands your voice, your projects, and your constraints.

### The Three Context Files You Need

Create these files in your Cowork project before doing anything else:

#### 1. about-me.md
Who you are, what you do, your background, your current role. This gives Cowork the context it needs to tailor responses to your situation.

**Example structure:**
```markdown
# About Me

## Background
[Your professional background, key career transitions]

## Current Role
[What you do now, who you work with, your primary responsibilities]

## Working Style
[How you prefer to work, communicate, make decisions]

## Constraints
[Time zone, availability, tools you use, tools you don't use]
```

#### 2. brand-voice.md
How you sound when you write. This is critical if you're using Cowork for content creation. Without it, Cowork will default to generic AI voice.

**What to include:**
- Tone descriptors (e.g., casual, credible, specific)
- Sentence patterns you actually use
- Words you never use (AI clichés, marketing speak)
- Platform differences (how you sound on X vs LinkedIn vs blog)
- Examples of your actual writing

**Pro tip:** If you already have a voice guide or style document, just drop it in here. Don't recreate from scratch.

#### 3. current-projects.md
What you're working on right now. Update this weekly. This is what makes Cowork feel like an assistant who's paying attention, not a chatbot you have to re-explain everything to.

**Example structure:**
```markdown
# Current Projects

## Active
- [Project name]: [status, next step, deadline if any]
- [Project name]: [status, next step]

## Queue
- [Project name]: [waiting on what]

## Completed (last 30 days)
- [Project name]: [outcome]
```

---

## The Meta-Prompt Pattern

Before running any workflow, prime Cowork with this:

> "Read my context files (about-me.md, brand-voice.md, current-projects.md) before responding. Tailor everything to my specific situation, voice, and current projects."

This takes 5 seconds and dramatically improves output quality.

---

## Four Workflows to Start With

### 1. Morning Dashboard
**Prompt:** "What should I focus on today?"

**What Cowork does:**
- Reviews your current projects
- Checks for deadlines or urgent items
- Surfaces top 3 priorities
- Suggests what to defer

**Time saved:** 10-15 minutes of morning planning

### 2. Meeting Prep
**Prompt:** "Prep for my meeting with [name]"

**What Cowork does:**
- Reviews past interactions with this person
- Pulls relevant project context
- Suggests topics to cover
- Prepares questions to ask

**Time saved:** 5-10 minutes per meeting

### 3. Content Repurposing
**Prompt:** "Take this [content] and repurpose it for [platform]"

**What Cowork does:**
- Adapts content to your voice (from brand-voice.md)
- Formats for target platform
- Maintains your perspective and specificity

**Time saved:** 15-30 minutes per piece of content

### 4. Decision Logging
**Prompt:** "Log a decision about [topic]"

**What Cowork does:**
- Captures context and options considered
- Documents why you chose what you chose
- Creates searchable record for future reference

**Value:** Institutional memory that compounds over time

---

## Folder Structure

```
cowork-project/
├── context/
│   ├── about-me.md
│   ├── brand-voice.md
│   └── current-projects.md
├── workflows/
│   ├── morning-dashboard.md
│   ├── meeting-prep.md
│   └── content-repurposing.md
├── decisions/
│   └── [decision records]
├── meetings/
│   └── [meeting notes]
└── projects/
    └── [project-specific files]
```

---

## Common Mistakes

1. **Skipping context files** — Cowork works fine without them, but you're leaving 80% of the value on the table
2. **Copying generic templates** — Your context files should reflect YOUR situation, not a template
3. **Not updating current-projects.md** — Stale context is worse than no context
4. **Using Cowork like ChatGPT** — If you're prompting from scratch every time, you're doing it wrong

---

## What This Looks Like in Practice

After 3 weeks with proper context files:

- **82 meeting notes** processed and filed
- **47 meetings** with full context prepped
- **35 action items** tracked automatically
- **11,000+ lines** of institutional knowledge captured

The system works because you never think about the system. You just talk to Cowork like an assistant, and it handles the organization as a side effect.

---

## Next Steps

1. Create your three context files (about-me.md, brand-voice.md, current-projects.md)
2. Run the meta-prompt before your first workflow
3. Test the Morning Dashboard prompt
4. Add workflows as you need them

The whole setup takes 30-60 minutes. The payoff compounds every day.

---

## Resources

- **This guide:** https://github.com/a-makelky/claude-skills/blob/main/claude-cowork-setup-guide.md
- **Corey Ganim's Starter Pack:** https://x.com/coreyganim/status/2033206539595461070
- **Nick Spisak on Shared Context:** https://x.com/NickSpisak_/status/2033243786097172798
- **Obie Fernandez's Executive Assistant:** https://x.com/obie/status/2013955736292704342

---

*Maintained by Aaron Makelky. Tested so you don't have to.*
