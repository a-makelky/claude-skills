# Claude Skills Collection

A curated collection of custom Claude skills for writing, workflow automation, and personal operating systems.

## Skills Overview

### 1. Aaron Personal Content Writer
**Path:** `aaron_personal_content_writer_skill/`

Expert ghostwriter for tech-focused thought leadership on LinkedIn and X (Twitter).

**Features:**
- Authentic, direct, unpretentious voice
- Proven copywriting frameworks (Pyramid Principle, PAS, PASTOR)
- Topics: AI tools (Notion, Cursor, Claude), tech-humanism
- Anti-patterns built in (no "game-changer," no emojis, no engagement bait)

**Files:**
- `SKILL.md` - Main skill definition
- `style_guide.md` - Comprehensive writing style guide

---

### 2. Laura Ghostwriter
**Path:** `laura-ghostwriter-skill/`

LinkedIn ghostwriter for Laura Burkhauser, CEO of Descript.

**Features:**
- Sharp, self-deprecating, unpolished voice
- Signature frameworks ("The burning platform and the beach," "Context is currency")
- Activates with `/lauraghostwriter` command
- Continuous learning protocol built-in

**Files:**
- `SKILL.md` - Main skill definition
- `voice_profile.md` - Detailed voice analysis
- `sample_posts.md` - Reference posts by content type

---

### 3. Descript Social Voice
**Path:** `DescriptBrandVoiceSKILL.md`

Social media brand voice for @Descript on X (Twitter) and LinkedIn.

**Core Principles:**
- Human: Conversational, never corporate
- Realistic: Honest, empathetic, self-aware
- Subversive: Surprising, uncomfortable, absurd

**Platforms:**
- X: Sharp, punchy, slightly unhinged
- LinkedIn: Professional but still human

---

### 4. LinkedIn Hook Writer
**Path:** `linkedin-hook-writer/` and `linkedin-hook-writer.skill`

Creates attention-grabbing LinkedIn hooks and openers.

**Files:**
- `SKILL.md` - Main skill definition
- `references/hook-templates.md` - Hook templates and patterns
- `scripts/validate_hook.py` - Validation script

---

### 5. AI Writing Audit Skills
**Path:** `ai writing audit skills/`

Writing quality checks and audits for AI-generated content.

**Files:**
- `SKILL.md` - Main skill definition
- `checklist.md` - Writing audit checklist
- `descript-voice.md` - Descript-specific voice guidelines
- `ai-writing-audit.skill` - Packaged skill file

---

### 6. Skill Creator
**Path:** `skill-creator/`

Meta-skill for creating new Claude skills with proper structure.

**Features:**
- Templates for new skills
- Best practices guide
- Initialization, validation, and packaging scripts

**Files:**
- `SKILL.md` - Main skill definition
- `templates/SKILL_TEMPLATE.md` - Skill template
- `references/best_practices.md` - Best practices guide
- `scripts/` - Utility scripts (init, validate, package)

---

### 7. Tax Return
**Path:** `tax-return/`

Organizes annual tax documents into a CPA-ready packet with intake, file naming, reconciliation workpapers, and a final handoff memo.

**Features:**
- Yearly tax workspace and intake workflow
- Standard naming and folder conventions
- Personal, business, and rental separation rules
- Workpaper guidance for income, expenses, occupancy, mileage, and manual form transcription
- Clean upload-package process for Drive-friendly handoff

**Files:**
- `SKILL.md` - Main skill definition
- `references/workflow.md` - Detailed yearly operating playbook
- `references/templates.md` - Folder, naming, memo, and checklist templates

---

## Usage

These skills are designed to work with Claude (claude.ai) and Claude Code. Each skill includes:
- A `SKILL.md` file with the skill definition
- Supporting files (style guides, templates, examples)
- Some skills include packaged `.skill` or `.claude.skill.zip` files

To use a skill:
1. Import the skill into Claude or Claude Code
2. Activate it according to its specific trigger (command or context)
3. Follow the skill's guidance and frameworks

## Repository Structure

```
claude-skills/
├── aaron_personal_content_writer_skill/
├── laura-ghostwriter-skill/
├── ai writing audit skills/
├── linkedin-hook-writer/
├── skill-creator/
├── tax-return/
├── DescriptBrandVoiceSKILL.md
├── linkedin-hook-writer.skill
└── README.md
```

## Updates

This repository is synced with a local iCloud folder. Any changes made locally will be committed and pushed to keep skills up to date.

---

*Maintained by Aaron Makelky*
