# Updating Webinar Promo Patterns

## When to Update
After each webinar campaign wraps, or quarterly — whichever comes first.

## What You Need
- A CSV export of X account analytics covering the period since the last update
- The date range of the export

## Steps

### 1. Export Analytics
Download the content analytics CSV from X (Analytics > Content). Make sure it covers at least from the last update date (check the top of `webinar-promo-patterns.md`) through today.

### 2. Run the Analysis
Open a Claude Code conversation and provide the CSV:

```
Here is our updated X analytics CSV [attach or @-reference the file].
Update the webinar promo patterns file at ~/.claude/skills/webinar-promo/webinar-promo-patterns.md with new findings.
```

Claude will:
- Identify all new webinar/livestream promotional posts in the data
- Compare performance against existing benchmarks
- Add new top performers to the ranked list
- Revise benchmark tables (median, top 25%, top 5) with combined data
- Confirm, revise, or retire existing "what works" and "what doesn't work" patterns based on new evidence
- Update the "Last updated" date and data source range at the top

### 3. Review the Changes
Skim the updated `webinar-promo-patterns.md` to make sure nothing looks off. Pay attention to:
- Did any previously strong patterns stop working?
- Are there new patterns emerging that weren't in the original analysis?
- Do the benchmark numbers still feel right given your experience?

### 4. Sync Your Copies
After confirming the update looks good:

```
Copy the updated skill files to my iCloud Claude Skills folder
```

Then push to your private GitHub repo if you want that backup current too.

## File Roles

| File | Purpose | Update Frequency |
|------|---------|-----------------|
| `SKILL.md` | Skill logic, voice rules, generation instructions | Rarely — only if you change platforms, tone, or cadence strategy |
| `webinar-promo-patterns.md` | Analytics data, benchmarks, ranked examples, pattern findings | Every update cycle (post-campaign or quarterly) |
| `UPDATE-INSTRUCTIONS.md` | This file — documents the update process | Only if the process itself changes |
