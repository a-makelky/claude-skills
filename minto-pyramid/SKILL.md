---
name: minto-pyramid
description: "Use when /minto or /pyramid is invoked to pressure-test a draft or idea with the Minto Pyramid Principle, then produce an HTML pyramid, opener, evidence gaps, and restructuring plan."
---

# Minto Pyramid

Use this skill to turn a rough idea or existing draft into an answer-first structure. The output is not a full rewrite. It is a structural diagnosis and repair plan the writer can act on.

This skill is adapted from Ole Lehmann's Minto skill pattern:
https://github.com/olelehmann1337/claude-skills/blob/main/skills/minto/SKILL.md

## Triggers

Use this skill when the user invokes `/minto`, `/pyramid`, or asks to:
- minto this
- pyramid this
- apply the Minto Pyramid Principle
- find the one-sentence answer
- check whether the structure is MECE
- pressure-test the logic before drafting or rewriting

Do not use this skill for voice editing, platform formatting, copy compression, or full drafting unless the user explicitly asks for that after the structure is settled.

## Input handling

Work from the actual conversation input.

- If the user provides a raw idea, build a recommended pyramid from scratch.
- If the user provides a draft, extract the pyramid from the draft and diagnose where the draft fails to support it.
- If the user says only `/minto` or `/pyramid`, use the most recent obvious draft or topic in the conversation.
- If there are two plausible targets, ask one short clarifying question before proceeding.
- Do not pull in unrelated memory or invent missing evidence.

## Build the pyramid

Create a three-level pyramid.

### Level 1: Answer

Write one sentence that states the main claim. It must take a position.

A weak answer usually has one of these problems:
- It names a topic without making a claim.
- It hedges.
- It is so broad that no reasonable reader would disagree.
- It asks a question instead of answering one.
- It tries to cover too much territory.

For a draft, identify whether the answer is stated directly, buried, or missing. For a raw idea, compress the idea until one sentence can carry the point. If that is impossible, stop and explain what choice the user needs to make before a pyramid can exist.

### Level 2: Supporting Arguments

Create two to four full-sentence supporting claims. Three is usually best.

The arguments must be MECE:
- Mutually exclusive: each argument does distinct work.
- Collectively exhaustive: together, they handle the most obvious skeptical pushback.

For a draft, map each argument to the section or paragraph that supports it. Flag sections that support no argument and arguments that have no supporting section.

### Level 3: Evidence

Attach one concrete evidence target to each argument.

Use evidence already present in the conversation first. Acceptable evidence types:
- A named statistic from a named source.
- A specific company, product, person, case, or event.
- A specific stated position from a named person.
- A concrete anecdote with enough detail to verify what happened.

Mark evidence as:
- `strong`: concrete, named, and specific.
- `weak`: present but vague, decorative, or underpowered.
- `missing`: needed but absent.

Do not fabricate evidence. If evidence is missing, say exactly what kind of proof would close the gap.

## Diagnose the structure

Run these checks before writing the plan.

- Answer: Is the main claim stated early, buried, missing, too safe, or too broad?
- Arguments: Do the supporting claims overlap, leave a gap, or fail to prove the answer?
- Evidence: Is each proof point concrete enough to carry its branch?
- Shape: Is this a principle piece or a case-study piece?
- Draft map: Which sections should move, merge, split, or be cut?

Default to treating the piece as a principle piece unless the specific case is clearly the subject. This matters because principle pieces should lead with the claim, while case studies may lead with the concrete case.

## Build the repair plan

Give specific, ordered instructions. The plan should feel like film review: name the breakdown, then call the next play.

Include:
- The exact opener the piece should use.
- The recommended order of sections or arguments.
- Sections, paragraphs, or sentences to cut because they do not serve the pyramid.
- Evidence gaps and the exact kind of proof needed.
- Sharpened argument sentences when a branch is soft.

For a raw idea with no draft, skip reordering and cutting. Provide the pyramid, opener, evidence targets, and draft skeleton.

## Create the artifact

The deliverable is an HTML file, not a long chat response.

Save the file as:

```text
minto-pyramid-{short-topic-slug}.html
```

Use the current workspace, an `outputs/` folder, or the environment's normal shared output folder. If the renderer script is available, prefer it:

```text
python {baseDir}/scripts/render_minto_pyramid.py input.json output.html
```

The input JSON shape is:

```json
{
  "topic_title": "Pricing Change",
  "level_1_answer": "The one-sentence answer goes here.",
  "arguments": [
    {
      "claim": "Argument one is a full-sentence claim.",
      "evidence": "Specific proof or the missing evidence target.",
      "strength": "strong"
    }
  ],
  "opener_context": "State the principle first, then let the example prove it.",
  "opener_quote": "Exact opener sentence.",
  "opener_note": "Why this opener works better.",
  "plan": [
    {
      "headline": "Move the claim to sentence one.",
      "body": "Explain the concrete change.",
      "example": "Optional exact sentence or phrase."
    }
  ]
}
```

If you do not use the script, manually create equivalent HTML with:
- answer at the top
- arguments in the middle
- evidence boxes below, color-coded by strength
- opener section
- numbered restructuring plan

## Chat response

After creating the artifact, reply with only:
- a link to the HTML file
- a two to four line summary naming the biggest structural issue and the fix

Do not paste the full pyramid or plan into chat.

## Guardrails

- Do not rewrite the full draft.
- Do not apply a personal voice or brand voice.
- Do not recommend a platform or format.
- Do not produce more than four supporting arguments.
- Do not produce a pyramid without a one-sentence answer.
- Do not fabricate proof, credentials, examples, or sources.
- Keep the prose direct and concrete.
