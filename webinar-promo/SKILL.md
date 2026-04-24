---
name: webinar-promo
description: "Use for /webinar-promo or requests to create Descript webinar/livestream promo copy for X and LinkedIn using brand voice, Notion campaign context, and UTM rules."
---

# Webinar Promo Post Generator

Generate a full promotional post sequence for an upcoming Descript webinar or livestream, for **X (Twitter)** and **LinkedIn**.

---

## Inputs

Collect these from the user (via `$ARGUMENTS` or by asking):

| Input | Required | Example |
|-------|----------|---------|
| **Webinar date & time** | Yes | "Feb 18, 1pm PT" |
| **Topic** | Yes | "AI translation & dubbing workflows" |
| **Post sequence / cadence** | Yes | "+2 weeks, +1 week, 48hrs, day-of" |
| **Content brief or context** | Recommended | Run of show, key features, guest speakers, target audience, sign-up link |
| **Tone override** | Optional | Default: Descript brand voice. Override with e.g. "more serious", "extra weird" |

If the user provides `$ARGUMENTS`, parse them for the above fields. If any required input is missing, ask before generating.

---

## Reference Files

Before generating copy, load and apply:

1. **Pattern data**: `~/.claude/skills/webinar-promo/webinar-promo-patterns.md`
   - What works, what doesn't, cadence benchmarks, top-performing examples
2. **Brand voice**: The Descript brand voice principles below (sourced from DescriptBrandVoiceSKILL.md)

### Live campaign data (Notion)

Fetch these when the user references an existing webinar or asks you to match conventions from a prior campaign:

| Resource | URL / ID | Use for |
|----------|----------|---------|
| Webinars 2026 DB | https://www.notion.so/2c0abe2e1a508053ab89df85fec0baf0 | Look up event date, title, speakers, ICP, theme, features |
| Social media cal | https://www.notion.so/112abe2e1a5081a0bc0cc4afb3234923 | Write drafted posts here (filter Series = "Webinar Promo") |
| X Ads Playbook | https://www.notion.so/33dabe2e1a50807e93cfeb9048b84aac | Audiences, topics, lookalike accounts for paid X ads |
| UTM Builder | https://www.notion.so/233abe2e1a5080d6a6bbfb6dea871dca | Full UTM conventions across channels |

**Discovery pattern:** Before generating, search Notion for `"Webinar Promo: [topic]"` to find any existing +2wk / +1wk posts for the same webinar. Match their conventions (time format, UTM variant, speaker tagging).

### UTM conventions for Luma sign-up links

Always append UTMs to the Luma URL. Shared params: `utm_campaign=webinar&utm_medium=social`.

| Channel | `utm_source` value |
|---------|-------------------|
| Organic social (X, LI, FB, Threads) | `social` |
| Paid X ads | `xad` (current) — older posts use `socialxad` |
| Email | `email` (confirm in UTM Builder if unsure) |

When in doubt, check the `Key Links` section of a prior promo page for the same webinar — the canonical link is typically listed there as "Social UTM link" and "Ad UTM link".

### Notion page conventions

When drafting individual posts, create a page in the Social media cal DB with:
- **Series:** `Webinar Promo`
- **Platform:** `X Twitter 🐦` and/or `LinkedIn 💼` etc.
- **Asset type:** `Text`
- **Status:** `Draft`
- **Date:** the scheduled post date (not the webinar date)
- **Subject:** `Webinar Promo: [Topic] ([+Xwk] or [+Xhr])` for organic, or `X Ads — [Topic] (Thu M/D)` for paid

---

## Brand Voice (Descript)

### Core Principles
- **Human**: Write like a real person talks. Never sound like a brand or SaaS company. No jargon, no memes, no hyper-online language.
- **Realistic**: Honest, empathetic, self-aware. No positive spin. Acknowledge how creators actually feel.
- **Subversive**: Surprising, uncomfortable, inobvious, absurd. Say what you wouldn't expect from a brand.

### Hard Rules
- Never punch down, be mean, condescending, or dismissive
- Never cynical or discouraging
- Never "conspicuously authentic" or faux-enthusiastic
- No hyperbole about the reader's content
- Assume intelligence and noble intentions

### X Voice
- Sharp, punchy, slightly unhinged. Lean into subversive.
- Lowercase acceptable. Line breaks for rhythm. No hashtags.
- Embrace awkwardness. Slightly off-kilter outperforms polished.

### LinkedIn Voice
- Still human and realistic but more measured, less chaotic.
- Subversion = cutting through LinkedIn's sea of performative positivity.
- Empathy for professional creator struggle: stakeholder feedback, revision hell, tight timelines.
- Longer-form OK. Bold sparingly. No emoji spam. Links in comments when possible.

---

## Generation Rules

### For each post in the sequence, generate:

1. **X version** (primary)
2. **LinkedIn version** (adapted for the platform)

### Apply these proven patterns (from analytics data):

**ALWAYS do:**
- Lead with a pain point or relatable frustration, not the event name
- Include the specific date/time in every post
- Include a sign-up link placeholder `[LINK]` in every post (never skip this)
- Use the specificity formula when possible: pain + promise + date + link
- Vary the copy across the sequence — never reuse the same hook or phrasing between posts
- Each post in the sequence should feel like it could stand alone

**NEVER do:**
- Open with "Join our webinar" or "We're hosting a webinar"
- Use the same hook/opening across multiple posts in the sequence
- Post promo content framed for weekends (note this in the output if a cadence date falls on Sat/Sun)
- Write posts without a link/CTA
- Use corporate announcement tone ("We're thrilled to announce...")
- Use hashtags on X

### Cadence-specific guidance:

**2 weeks out (Awareness)**
- Role: Plant the seed. Make them feel the pain.
- Approach: Lead with an uncomfortable truth or absurd observation about the problem the webinar solves. The event is secondary — mention it at the end.
- Tone: Most subversive post in the sequence. This is your attention-grabber.

**1 week out (Specificity)**
- Role: Give them a reason to care. Be concrete.
- Approach: Name specific things they'll learn, see, or be able to do. If there's a guest speaker or partner, name-drop them here. Reference trending topics or tools if relevant.
- Tone: Still human and interesting, but more informational. The "here's what you'll actually get" post.

**48 hours out (Urgency)**
- Role: Create FOMO. This is the "last call before tomorrow" energy.
- Approach: "Tomorrow" or "This [day]" framing. Short, direct. Acknowledge that they've been putting this off. Make the CTA feel low-friction ("Save your seat", "takes 60 min").
- Tone: Punchy, direct, slightly urgent without being desperate.

**Day-of pre-stream (Clean link)**
- Role: Conversion. Make it dead simple to click.
- Approach: Can be minimal. "[Topic]. Going live at [time]. Join us: [LINK]" works. Or a one-line hook + link. Don't overthink it.
- Tone: Clean, direct, welcoming.

**Day-of stream start (NOW)**
- Role: Last-second reach grab.
- Approach: "Starting now", "Going live", "We're on" energy. Keep it to 1-2 lines. MUST include link (the data shows these posts get high impressions but low engagement — the link gives them somewhere to go).
- Tone: Excited but not performative.

**Post-event / recap (if requested)**
- Role: Extend the value. Drive sign-ups for next one.
- Approach: Pull a specific insight, quote, or moment from the webinar. Use it as a standalone valuable post that happens to link to the recording or next event.
- Tone: Reflective, value-forward.

---

## Output Format

For each post in the sequence, output:

```
### [Timing Label] — [Calendar Date]

**X:**
[post copy]

**LinkedIn:**
[post copy]

---
```

After all posts, include:

### Sequence Notes
- Flag any posts that fall on weekends (recommend moving to nearest weekday)
- Note which post in the sequence is the "swing for the fences" creative risk
- If a guest/partner is mentioned, note which posts should tag them for co-amplification
- Suggest one optional bonus post if there's a natural content hook (trending topic, product launch, partner event happening nearby)

---

## Process

1. Parse inputs (date, topic, cadence, brief)
2. Read pattern data from `webinar-promo-patterns.md`
3. Calculate calendar dates for each post in the sequence based on webinar date
4. Generate X + LinkedIn copy for each post, applying cadence-specific guidance
5. Run each draft through the brand voice final check:
   - Does this sound like a human, not a brand?
   - Is it honest? Or are we spinning?
   - Is there something surprising, uncomfortable, or absurd?
   - Would we be embarrassed if this got screenshotted? (Maybe good — or rethink)
   - Are we assuming the best about our audience?
   - Does this feel native to the platform?
6. Output the full sequence with notes

---

## Example Invocation

```
/webinar-promo

Date: Feb 18, 1pm PT
Topic: AI translation & dubbing in Descript
Cadence: +2 weeks, +1 week, 48hrs, day-of
Brief: Live demo of Descript's AI translation workflow — lip sync, native-sounding audio,
translated text layers, branded term protection, bulk export to 20+ languages.
Target audience: video teams localizing content. Live Q&A at the end.
Sign-up link: https://example.com/register
```
