---
name: product-demo-storytelling
description: Turn product features into hero-centric demo stories using the Pixar Story Spine, then produce a record-ready three-column script (screen + narration + clickpath). Use when writing, structuring, or rescuing any product demo — video demo, sales demo, launch video, webinar walkthrough, conference stage demo, customer demo, or screen-recording script. Trigger phrases include "demo script," "product demo," "walk through our product," "pitch this feature," "launch video," "demo storyline," "feature tour" (an anti-pattern this skill fixes), or any request to restructure a feature list into something customer-facing. Voice-neutral — does not apply a brand voice.
source: Jodi Innerfield, Product Demo Storytelling framework
version: 1.0
---

# Product Demo Storytelling — From Feature List to Record-Ready Script

**Skill:** `product-demo-storytelling`
**Source:** Jodi Innerfield (8 years & 9 launches at Salesforce; product storytelling consultant)
**Version:** 1.0

---

## What this skill does

Turns whatever the user has — a feature list, a PRD, a rough draft, a persona doc, a half-written demo, or nothing but an idea — into a **hero-centric product demo story** using the Pixar Story Spine, then produces a **three-column script** (screen + narration + clickpath) ready to record.

Most demos fail the same way: they're feature tours dressed up as stories. The customer is missing, the transformation is missing, and every sentence is "now I click here." This skill fixes that by treating the customer as the hero and the product as the helper that gets them to their goal.

Two stages, two user checkpoints:

1. **Structure** — fill in the Pixar Story Spine worksheet (hero, challenge, goal, 3 product-enabled wins, transformation)
2. **Script** — convert the worksheet into a three-column script applying tight scripting rules

---

## Instructions for the AI

You are guiding a demo writer through a two-stage storytelling workflow. **Never skip Stage 1.** Writing a demo script without a filled-in story spine is how feature tours get created — the whole point of this skill is to force the structural work first.

**Hard rules:**

- The **customer is the hero.** The product is the helper. Never let the product become the subject of the story.
- Every beat must tie back to the hero's goal. If it doesn't, cut it — even if the feature is cool.
- The spine has **three "Because of that" beats**, not seven. Pick the three features that best advance the hero toward their goal. Demos that try to show everything show nothing.
- **Stop between stages for user review.** Do not steamroll from spine into script without an explicit approval from the user.
- **Voice-neutral.** Do not apply a specific brand voice unless the user asks for one. Write in clear, plain language.
- If the user pushes back on a structural choice, revise — do not defend. The user knows their customer better than you do.

---

## Stage 1 — Structure: Fill the Story Spine

### Step 1.1 — Gather inputs

Ask the user for whatever they have. Don't demand a specific format. Useful inputs include:

- **Hero** — who's the customer? Role, company size, industry, seniority. If they don't know, ask.
- **Hero's goal** — what does the customer want to accomplish? (Not "use our product" — the real underlying outcome.)
- **Hero's everyday challenge** — what's broken or painful in their current workflow?
- **Product / feature(s)** — what are you demoing? Be specific.
- **Supporting material** — PRD, feature list, prior demo script, persona doc, competitive positioning, customer quote, raw brainstorm. Anything helps.
- **Format & length** — recorded video? Live demo? Conference stage? 60 seconds? 10 minutes?
- **Audience context** — are they cold, warm, existing customer? What do they already know?

If the user hands you very little, work with it. Ask one round of clarifying questions. Don't demand a PRD before you'll start.

### Step 1.2 — Fill in the Pixar Story Spine

Use this exact structure. Fill each beat with 1–3 sentences. This is a **working document**, not final copy — be thorough, not tight.

| Prompt | Fill in with |
|---|---|
| **What if…?** | The hero's end goal / desired future state |
| **Once upon a time** | Introduce the hero (the customer) |
| **And every day…** | The hero's everyday challenge |
| **Until one day** | Introduce the helper (your product) |
| **Because of that** | Win #1 the hero can now achieve toward their goal |
| **And because of that** | Win #2 |
| **And because of that** | Win #3 |
| **Until finally…** | The hero reaches their goal |
| **And the moral of the story is** | The outcomes / transformation the hero now enjoys |

**Constraints:**

- Exactly **three "Because of that"** beats. If the product has ten features, you still pick three. Ruthlessness here is the skill.
- Each "Because of that" must be framed as **what the hero can now do** — not what the feature is.
- The three wins should build on each other. They're steps toward the goal, not a parallel feature list.
- The "moral" is the transformation, not a marketing tagline.

### Step 1.3 — Present the worksheet and get checkpoint approval

Present the filled-in spine to the user. Ask explicitly:

> Does this hero, challenge, and goal feel right? Are these the three wins you want to showcase? Anything to swap before we write the script?

**Revise until the user approves.** Do not move to Stage 2 until they sign off. Common edits at this checkpoint:

- Wrong hero (too junior, too senior, wrong industry)
- Goal stated as product-use instead of real outcome
- Wrong three features picked
- Wins don't build on each other
- Moral is a tagline, not a transformation

---

## Stage 2 — Script: The Three-Column Deliverable

### Step 2.1 — Confirm screens and clickpath

Before writing narration, ask the user what screens / product surfaces they'll actually show. Each "Because of that" beat should map to one or two screens. If the user doesn't know yet, propose screens based on the features picked.

### Step 2.2 — Write the three-column script

Deliver as a markdown table:

| Screen / Visual | Narration | Clickpath notes |
|---|---|---|
| What's on screen at this moment | What the presenter says | What to click, when to cut, what to highlight |

Map the spine to the script in this order:

1. **Hook** — "What if…?" + "Once upon a time" + "And every day…" compressed into an opening that introduces the hero and their pain. Usually 15–30 seconds of narration.
2. **Setup** — "Until one day" introduces the product as helper.
3. **Three product beats** — one "Because of that" per screen/section. Show the win, tie it to the goal.
4. **Payoff** — "Until finally…" shows the hero at their goal.
5. **Close** — "And the moral of the story is" lands the transformation.

### Step 2.3 — Pick a narration voice

Before writing narration, pick the voice based on the demo format. Both "right" answers depend on who's speaking and to whom:

| Format | Default voice | Example |
|---|---|---|
| Customer testimonial / hero speaking | First person ("I") | "I don't rebuild the plan anymore — I drag the milestone and it reschedules itself." |
| Launch announcement / product trailer | Second person ("you") | "Click any cut and every transition shows up as a looping preview." |
| Sales demo / presenter-led walkthrough | First or second person | Depends on whether the presenter is narrating their own workflow or the viewer's. |
| Customer story (third-party narration) | Third person (hero's name) | "Maya stopped reacting to deadline changes and started running ahead of them." |
| Internal / training demo | Second or third person | "When a designer goes on PTO, the team sees workload rebalance suggestions…" |

Pick one voice and hold it. Mixing voices within a single script is the most common script-review flag.

### Step 2.4 — Apply the scripting rules

Run every line of narration through these filters:

- **Two-cent words.** Replace jargon and long words with simple ones. "Utilize" → "use." "Leverage" → "use." "Optimize" → "speed up" or "clean up."
- **Short sentences.** If a sentence runs past ~15 words, break it. Spoken copy is not written copy.
- **Outcomes, not clicks.** "This lets me publish to three channels at once" ✅. "Now I click the publish button and select my channels" ❌. Clickpath notes go in column 3, not narration.
- **Know your screens.** Narration must match what's visible. Don't describe features the viewer can't see.
- **Tie every beat to the hero.** Sentence-level test: does this line reference the hero's goal or a step toward it? If no, rewrite or cut.

### Step 2.5 — Return-to-hero pass

After the first draft, read the whole script ignoring the product. If the hero's journey still makes sense without product names, you're good. If it falls apart, the story is product-first, not hero-first — go back and rewrite.

Show your work: quote the narration with product names stripped, then state whether the arc holds.

### Step 2.6 — Deliver and offer revision

Return the three-column script and ask:

> Want me to tighten any section, adjust pacing for a specific runtime, or swap out a feature beat?

---

## Worked example

Use this pattern when the user's request is vague or as a reference for what "good" looks like. **Do not reuse this example verbatim** — it's a pattern, not a template.

**Input from user:** "We have a new project management tool called Kiln. Main features are auto-scheduling, team workload balancing, and cross-project dependencies. Our audience is operations leads at 50–200 person companies. Help me write a 3-minute demo video."

### Stage 1 output — Story Spine

| Prompt | Fill in |
|---|---|
| **What if…?** | Maya could ship every project on time without another 9pm rescheduling marathon. |
| **Once upon a time** | Maya is Head of Operations at a 120-person design agency. She runs 14 active client projects across 6 teams. |
| **And every day…** | She spends hours reshuffling schedules in spreadsheets every time a client shifts a deadline or a designer goes on PTO. Projects still slip. Her team is burned out. |
| **Until one day** | Maya's team starts using Kiln. |
| **Because of that (Win 1)** | When a deadline shifts, Kiln reschedules every downstream task automatically — Maya stops rebuilding the plan from scratch. |
| **And because of that (Win 2)** | Kiln shows her who's overloaded before the week starts, so she rebalances workload on Monday instead of firefighting on Thursday. |
| **And because of that (Win 3)** | Kiln surfaces cross-project dependencies — when one project's blocker hits, Maya sees which other projects are about to stall and reroutes ahead of time. |
| **Until finally…** | Maya's agency ships projects on time for six consecutive quarters. |
| **Moral of the story** | Maya stopped reacting to deadline changes and started running ahead of them. Her team works 40-hour weeks again. |

### Stage 2 output — Three-Column Script (excerpt)

| Screen / Visual | Narration | Clickpath notes |
|---|---|---|
| Maya's face, talking head intro | "Running an operations team used to mean one thing: reshuffling schedules at 9pm on a Thursday because a client moved a deadline. I know, because I did it for five years." | 0:00–0:12. Talking head full frame. |
| Cut to overloaded spreadsheet, color-coded chaos | "Every project in a spreadsheet. Every dependency in my head. Every shift in plans — a Tuesday night spent rebuilding the plan." | 0:12–0:25. Zoom in on a cell with 14 stacked comments. Highlight one red row. |
| Kiln project view, clean timeline | "Now when a client shifts a deadline, I don't rebuild anything. I drag the milestone. Every downstream task reschedules itself." | 0:25–0:40. Drag milestone from Fri to next Tue. Let the auto-reschedule animation play. Don't narrate the click — let it speak. |
| Workload heatmap view | "Monday morning, I can see who's overloaded before they know it themselves. I rebalance the week in about ten minutes." | 0:40–1:00. Hover a teammate's row to show the tooltip. Click "rebalance suggestion." |
| Cross-project dependency graph | "And when one project hits a blocker, I see which other projects are about to stall. I can reroute before anyone misses a Slack." | 1:00–1:25. Pan across the graph. Highlight the red-flagged dependency. |
| Dashboard — 6 green quarters | "Six quarters in a row, every project on time." | 1:25–1:40. Let the viewer read the numbers. Don't over-narrate. |
| Maya, talking head close | "I'm not reacting to deadline changes anymore. I'm running ahead of them. And my team works 40-hour weeks." | 1:40–2:00. Warm lighting. Smile. |

Note: feature names (auto-scheduling, workload balancing, dependencies) **never appear in the narration**. The viewer experiences them through Maya's wins.

---

## Key principles

- **Customer is the hero. Product is the helper.** This is the single biggest reframe and the hardest habit to break. Teams default to making the product the hero because they're proud of it. The skill's job is to hold the line.
- **"What does this let me do" beats "Where do I click next."** Narrate outcomes. Put clicks in the clickpath column.
- **Three beats, not ten.** The spine has three "Because of that" slots on purpose. Most demo failures come from trying to cram in more.
- **Tie every sentence to the hero's goal.** If you can't, it doesn't belong.
- **Tour guide rule.** A guide can point out landmarks ("here's the Empire State Building, here's Ellis Island") or tell the story of an immigrant crossing the harbor. Same landmarks, completely different experience. Tell the journey.
- **If the story still works without the product name, you got the hero right.** The product is a vehicle for the hero's transformation, not the subject of the story.
- **Tighten relentlessly.** Two-cent words. Short sentences. Cut everything that doesn't advance the hero.

---

## Common anti-patterns to flag and fix

| Anti-pattern | What it sounds like | Fix |
|---|---|---|
| **Feature tour** | "Let me show you the five main features of our product." | Pick three, bind each to a hero win, drop the rest. |
| **Click-path narration** | "Now I click on the settings icon, then I navigate to the workflow tab…" | Move clicks to column 3. Narrate what the click accomplishes for the hero. |
| **Product as hero** | "Kiln is an AI-powered project management platform that…" | Rewrite: "Maya runs 14 projects across 6 teams…" |
| **Missing transformation** | Script ends with a feature demo and a "Thanks for watching." | Add the "Until finally" and "Moral" beats — show the hero at the goal. |
| **Jargon stack** | "Leverage our AI-powered workflow orchestration to optimize cross-functional throughput." | Two-cent words. "Ship projects on time without rebuilding the plan every Tuesday." |
| **Generic hero** | "Imagine a busy professional…" | Specific hero beats generic every time. Give them a name, role, and number of projects. |
| **Too many wins** | Seven "Because of that" beats. | Cut to three. The features you cut aren't gone — they're just not in this demo. |
| **Tagline as moral** | "…and that's why Kiln is the future of work." | Moral = transformation. "Maya's team works 40-hour weeks again." |

---

## What this skill does NOT do

- **Doesn't pick which features to demo.** The user decides. The skill holds the three-beat limit.
- **Doesn't record or produce video.** It produces a record-ready script. Production is separate.
- **Doesn't apply a brand voice.** Output is voice-neutral. If the user wants it routed through a specific voice, they can send it through a voice skill after.
- **Doesn't write marketing copy, ads, emails, or social posts.** Different jobs, different skills.
- **Doesn't second-guess the user's customer knowledge.** If they tell you the hero is Maya the ops lead, you write for Maya, not for who you think the hero should be.

---

## Source

Based on the **Product Demo Storytelling** framework developed by [Jodi Innerfield](https://linkedin.com/in/jinnerfield) — marketing strategist and product storytelling consultant. Eight years and nine product launches at Salesforce. The framework adapts Matthew Luhn's Pixar Story Spine (from *The Best Story Wins*) for product demos.

The core insight: the same structural principles that make Pixar films memorable — hero, challenge, helper, escalating wins, transformation — make product demos memorable. Feature tours are the demo equivalent of a movie that's "total escapism without a shred of believability" (an actual Rotten Tomatoes quote about *Gigli*, cited in Jodi's deck).

Walt Disney said it first: *"If the story is good, the picture may be good. But if the story is weak, good color, top actors, music, and animation cannot save it."* Same goes for demos.
