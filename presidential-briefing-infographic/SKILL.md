---
name: presidential-briefing-infographic
description: "Use to create Cold War-style executive briefing infographic prompts from real weekly work context, with date checks and optional depersonalization."
---

# Presidential Briefing Infographic

Use this skill when the user wants a CIA-adjacent, Cold War-era, President's Daily Brief-style infographic that turns real weekly work context into a cinematic executive operations brief.

## Workflow

1. Gather the real source context before writing.
   - Use the user's provided notes, task board, calendar, meeting notes, project files, or workspace artifacts.
   - Separate confirmed facts from inference.
   - Do not invent accomplishments, meetings, names, links, blockers, or outcomes.

2. Confirm the reporting window.
   - Identify the exact week or date range.
   - Verify weekday/date mapping before rendering any calendar strip.
   - Use absolute dates when the user references today, this week, tomorrow, or the weekend.

3. Choose privacy mode.
   - If the user asks for a personal version, preserve real names, companies, links, and work details.
   - If the user asks for a stock, shareable, or depersonalized version, replace names, companies, URLs, and private context with generic role labels.

4. Structure the brief.
   - Operations Completed: 3 shipped or completed items.
   - Strategic Intelligence: 3 opportunities, decisions, meeting insights, or follow-ups.
   - Assets Secured: 3 artifacts, links, files, tools, calendar blocks, or resources captured.
   - Launch Watch: 3 project, campaign, product, or operational signals being monitored.
   - Active Risks / Unfinished Business: 3 unresolved blockers, missed tasks, or next priorities.
   - Commander's Readout: 3 large metrics that make the week legible at a glance.
   - Assessment: 1 grounded sentence that explains the strategic shape of the week.

5. Keep the intelligence aesthetic fictional.
   - Use "FOR YOUR EYES ONLY, MR. PRESIDENT" as cinematic briefing language.
   - Do not use real government seals, official agency letterhead, watermarks, or claims that the artifact is an actual classified document.
   - Favor dossier, typewriter, redaction, grease-pencil, map-grid, and manila-folder cues over official insignia.

## Prompt Template

```text
Create a single-page vertical briefing infographic in a fictional Cold War-era intelligence dossier style, like a 1960s President's Daily Brief prepared for the Oval Office.

Goal: make the viewer feel like POTUS reading a high-stakes weekly operations brief.

Use the user's real week-in-review context from their workspace, calendar, task board, notes, or project files. Ground the content in actual completed work, active risks, follow-ups, and next priorities. Do not invent accomplishments.

Visual style:
- Aged off-white paper
- Typewriter typography
- Red grease-pencil circles and arrows
- Black redaction bars
- Blue/black map-grid lines
- Rubber-stamp textures
- Halftone photo boxes
- Paperclip shadows
- Manila folder / Cold War briefing-board atmosphere
- Coffee ring, fingerprints, marginalia, dossier tabs
- No real government seal, no official agency letterhead, no watermark

Main title:
"FOR YOUR EYES ONLY, MR. PRESIDENT"

Subtitle:
"WEEKLY OPERATIONS BRIEF - [USER / TEAM / DESK NAME]"

Dateline:
"WEEK OF [DATE RANGE] - [FIELD OFFICE OR WORKSPACE] - [TIMEZONE]"

Include a corrected mini calendar or week strip for the relevant week. Verify the weekday/date mapping before rendering.

Layout:
Create a dense but readable intelligence infographic with 5 sections and a right-side command readout.

Section 1: "OPERATIONS COMPLETED"
Summarize 3 major shipped/completed items from the user's real week.

Section 2: "STRATEGIC INTELLIGENCE"
Summarize 3 important opportunities, meetings, insights, or follow-ups that emerged.

Section 3: "ASSETS SECURED"
Summarize 3 artifacts, resources, links, tools, calendar blocks, or files captured/prepared.

Section 4: "LAUNCH WATCH"
Summarize 3 product, project, campaign, or operational signals being monitored.

Section 5: "ACTIVE RISKS / UNFINISHED BUSINESS"
Summarize 3 unresolved blockers, missed tasks, or next priorities.

Right-side panel:
Title: "COMMANDER'S READOUT"
Include 3 large typewriter-style metrics, for example:
"[N]+ PLATFORM MOVES"
"[N] ACTIVE WORKSTREAMS"
"[N] CRITICAL BLOCKER"

Bottom footer:
"ASSESSMENT: [One sentence that makes the week feel strategically coherent and presidential, grounded in the real work.]"

Tone:
Serious, cinematic, executive, intelligence-briefing energy. Slightly dramatic but not parody. Make the work feel consequential.

Accuracy rules:
- Use real work from the provided context.
- Do not fabricate names, dates, meetings, or outcomes.
- Keep dates and calendar weekday mappings correct.
- If the user wants depersonalized output, replace names/companies/URLs with generic role labels.
```

## Output

Return either:
- A ready-to-run image generation prompt, if the user asks for a prompt.
- A generated image, if image generation is available and the user asks to make the artifact.
- A depersonalized stock version, if the user asks to share the concept with others.
