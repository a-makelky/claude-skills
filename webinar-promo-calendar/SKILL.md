---
name: webinar-promo-calendar
description: Recommend X and LinkedIn webinar promo slots from a Notion webinar brief, generate the standard Luma social UTM link, and create or draft platform-specific placeholder pages in the Notion social media calendar. Use when the user shares a webinar Notion page and wants promo scheduling, placeholder rows, or social calendar entries.
---

# Webinar Promo Calendar

Use this skill when the user provides a webinar brief in Notion and wants:
- the best 3 promo slots for `X` and `LinkedIn`
- a standard social UTM link for the webinar registration page
- placeholder pages created in the social media calendar

This skill is specific to Descript's webinar workflow.

## Fixed Notion config

Use these defaults unless the user explicitly says otherwise.

- Webinar database: [Webinars 2026](https://www.notion.so/descript/2c0abe2e1a508053ab89df85fec0baf0?v=2c0abe2e1a5081c28864000c155ff458&source=copy_link)
- Webinar data source: `collection://2c0abe2e-1a50-81ef-a3b2-000b641dbf4c`
- Social calendar database: [Social media cal](https://www.notion.so/descript/112abe2e1a5081a0bc0cc4afb3234923?v=112abe2e1a50815ba08d000c3f206642&source=copy_link)
- Social calendar data source: `collection://112abe2e-1a50-81ba-9967-000b4634aaca`

Use the webinar page link as the runtime input. The database links are configuration, not the per-run task input.

## Required inputs

From the webinar brief page, extract:
- webinar title
- webinar date
- speakers
- themes
- ICP / target audience
- event type / format
- raw Luma link or event URL
- LinkedIn event link when present
- main brief or supporting doc links
- run-of-show themes, promo angles, and email promo snippets

Useful source properties and sections already exist in the webinar brief:
- `Official Title`
- `date:Date:start`
- `Speakers`
- `THEME`
- `Main ICP`
- `Type`
- `Event URL`
- `Linkedin event link`
- body sections such as event description, email promos, and run of show

## Date precedence

Resolve the webinar date in this order:

1. Luma event structured data, if the webinar page includes a raw Luma link and the Luma page conflicts with the brief body prose.
2. The webinar database date property.
3. Body prose only if the database date is missing.

If the body text conflicts with the database date, do not silently average or guess. Call out the conflict and use the higher-confidence source.

Schedule promo slots in fixed `MST` (`America/Phoenix`). Do not switch to MDT.

## UTM generation

Default webinar CTA link:
- base Luma URL + `utm_campaign=webinar&utm_medium=social&utm_source=social`

Rules:
- If the base URL has no query string, append `?utm_campaign=webinar&utm_medium=social&utm_source=social`
- If the base URL already has query params, append `&utm_campaign=webinar&utm_medium=social&utm_source=social`
- If existing `utm_*` params are present, replace them with the standard social values unless the user explicitly asks for channel-specific tracking

Example:
- raw: `https://luma.com/5nz9bjoj`
- social UTM: `https://luma.com/5nz9bjoj?utm_campaign=webinar&utm_medium=social&utm_source=social`

## Scheduling model

These defaults come from native post performance for webinar promo content only.

### LinkedIn defaults

LinkedIn is the long-runway channel. Prefer earlier demand-building.

- `T-14 days` at `11:00 AM MST`
- `T-8 days` at `11:00 AM MST`
- `T-5 days` at `1:00 PM MST`

### X defaults

X is the short-runway reminder channel.

- `T-7 days` at `1:00 PM MST`
- `T-3 days` at `1:00 PM MST`
- `T-1 day` at `3:00 PM MST`

## Slot compression rules

Do not force the default matrix if the webinar is too close.

- If a slot falls on a weekend, shift it to the nearest prior weekday.
- If the webinar is less than 14 days away, keep the remaining LinkedIn slots as early as possible before the event.
- If the webinar is less than 7 days away, compress X to the remaining pre-event weekdays and prioritize `T-3` and `T-1`.
- Avoid same-day posts unless there are fewer than 3 pre-event days remaining.
- Same-day LinkedIn should be a last resort.

## Duplicate check

Before creating anything, search the social calendar for existing webinar promo pages tied to the same event.

Look for:
- the webinar title or short title
- the Luma slug
- the webinar Notion page reference
- subjects that already include offsets like `+2 weeks`, `+1 week`, `+48 hrs`

If a slot already exists, keep it and only create the missing slots. Do not create duplicate platform rows for the same offset unless the user explicitly asks for alternates.

## Output shape

Create `6` platform-specific pages by default:
- `3` for `LinkedIn`
- `3` for `X`

Do not bundle both platforms into one social calendar page. The scheduling logic differs by platform and each placeholder should map to one post.

## Social calendar properties

Use these properties when creating placeholder pages:

- `Subject`: `Webinar Promo: {short title} ({offset}) - {platform}`
- `Date`: scheduled post datetime in MST
- `Month`: month of the scheduled post date
- `Platform`: exactly one of `X Twitter 🐦` or `LinkedIn 💼`
- `Series`: `Webinar Promo`
- `Status`: `Backlog`
- `Asset type`: leave blank unless known

Prefer these offset labels:
- `+2 weeks` for 13-15 days out
- `+1 week` for 6-8 days out
- `+72 hrs` for 3 days out
- `+48 hrs` for 2 days out
- `+24 hrs` for 1 day out
- otherwise `+{n} days`

## Placeholder body template

Use a platform-specific body. Do not add irrelevant copy sections for other channels.

For LinkedIn pages:

```md
**LinkedIn Copy:**

---
**Webinar Reference:** {mention webinar page}
**Webinar Date:** {webinar date}
**Post Date:** {scheduled post date} ({offset})
---
**Webinar Title:** {official title}
**Speakers:** {speakers}
**Theme:** {themes}
**ICP:** {icp}
**Type:** {type}
---
**Key Links:**
- Social UTM link: {generated social link}
- Raw Luma link: {raw luma link}
- LinkedIn Event: {linkedin event link if present}
- Main Brief: {main brief link if present}
---
**Promo Angle ({offset}):**
{slot-specific angle}

**Suggested hooks from email promo:**
- {hook 1}
- {hook 2}

**Run-of-show angles to emphasize:**
- {angle 1}
- {angle 2}
```

For X pages:

```md
**X Copy:**

---
**Webinar Reference:** {mention webinar page}
**Webinar Date:** {webinar date}
**Post Date:** {scheduled post date} ({offset})
---
**Webinar Title:** {official title}
**Speakers:** {speakers}
**Theme:** {themes}
**ICP:** {icp}
**Type:** {type}
---
**Key Links:**
- Social UTM link: {generated social link}
- Raw Luma link: {raw luma link}
- LinkedIn Event: {linkedin event link if present}
- Main Brief: {main brief link if present}
---
**Promo Angle ({offset}):**
{slot-specific angle}

**Suggested hooks from email promo:**
- {hook 1}
- {hook 2}

**Run-of-show angles to emphasize:**
- {angle 1}
- {angle 2}
```

## Angle guidance by slot

Use the brief content, run of show, and email promo copy to choose the angle.

### LinkedIn

- Early slot: strategic value, audience fit, business outcome, why this matters
- Middle slot: practical framework, what attendees will walk away with
- Late slot: urgency, specifics, live demo, Q&A, register now

### X

- Early slot: curiosity and punchy hook
- Middle slot: real project, real edits, strong CTA
- Late slot: short reminder, urgency, CTA-first

## Execution workflow

1. Fetch the webinar brief page.
2. Extract the core fields and promo context.
3. Resolve the webinar date using the date precedence rules.
4. Generate the social UTM link from the raw Luma URL.
5. Search the social calendar for existing promo placeholders tied to the same webinar.
6. Compute the missing X and LinkedIn slots using the scheduling model and compression rules.
7. Create only the missing platform-specific pages in the social calendar.
8. If write tools are unavailable, return the exact placeholder specs instead of stopping.

## Fallback when Notion write tools are unavailable

If the session only exposes read/search tools for Notion:
- do the full analysis anyway
- return the `6` placeholder specs or the missing subset
- include final subject, platform, scheduled date/time, generated UTM link, and body template content

Do not pretend the pages were created if the environment is read-only.
