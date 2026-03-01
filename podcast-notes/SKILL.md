---
name: podcast-notes
description: "Generate show notes, speaker transcripts, and LinkedIn posts from a FutureProof You podcast transcript. Triggers: /podcast-notes, 'process podcast transcript', 'create show notes', 'podcast show notes'."
---

# Podcast Notes Generator

Process a FutureProof You podcast episode transcript into show notes, per-speaker transcripts, and LinkedIn post suggestions.

---

## Podcast Info (Hardcoded)

| Field | Value |
|-------|-------|
| **Podcast** | FutureProof You — Go F Yourself |
| **Website** | https://futureproof-you.com |
| **LinkedIn (Company)** | https://www.linkedin.com/company/futureproof-you |
| **Co-host 1** | Aaron Makelky — https://www.linkedin.com/in/aaron-makelky-m-a-ed-038b852a3/ |
| **Co-host 2** | Dan Yu — https://www.linkedin.com/in/danoyu/ |
| **Co-host 3** | John Lovig — https://www.linkedin.com/in/johnlovig/ |

---

## Inputs

Collect these from the user (via `$ARGUMENTS` or by asking):

| Input | Required | Example |
|-------|----------|---------|
| **Episode folder path** | Yes | Path to the episode folder under `~/Library/Mobile Documents/com~apple~CloudDocs/FU Podcast/EP 25 - Episode Name/` |
| **Episode number** | Yes | `EP 25` |
| **Episode title** | Yes | `"The Future of Remote Work"` |
| **Episode date** | Yes | `2026-02-28` |
| **Episode URL** | Recommended | Link to the published episode (used in LinkedIn posts). If not available yet, use placeholder `[EPISODE LINK]`. |

If the user provides `$ARGUMENTS`, parse them for the above fields. If any required input is missing, ask before proceeding.

The transcript file will be inside the episode folder. Look for `.md`, `.txt`, or `.srt` files. If multiple files exist, ask which one to use.

---

## Recommended Transcript Format

For best results, the transcript should be plain markdown with speaker labels and timestamps at ~10-second intervals:

```
**Aaron Makelky** [00:00:00]
Welcome to FutureProof You. Today we're talking about...

**Dan Yu** [00:00:10]
Yeah, this is a topic I've been thinking about a lot...

**John Lovig** [00:00:20]
I think the interesting thing is...
```

This format is the most token-efficient and easiest to parse. Avoid SRT format if possible — the numbered block overhead adds tokens without value.

---

## Process

### Step 1: Read and Parse Transcript

1. Read the transcript file from the episode folder.
2. Identify all segments by speaker label (Aaron Makelky, Dan Yu, John Lovig).
3. If speaker labels don't match these names exactly, map them (e.g., "Aaron" → "Aaron Makelky", "Dan" → "Dan Yu", "John" → "John Lovig").
4. Note timestamps throughout for use in show notes.

### Step 2: Generate Show Notes

Write show notes grounded in what was actually said. Do not fabricate topics or use generic descriptions.

**Structure:**

```markdown
# EP [NUMBER] — [TITLE]

**Date:** [DATE]
**Co-hosts:** Aaron Makelky, Dan Yu, John Lovig

## Episode Summary

[2-4 sentences describing what the episode actually covers, written from the real conversation. Be specific about the topics discussed. No generic filler like "In this episode, the hosts dive deep into..." — just say what they talked about and why it matters.]

## Timestamps

- [HH:MM:SS] — [Topic description in plain language]
- [HH:MM:SS] — [Topic description in plain language]
...

(Up to 10 timestamps. Do NOT include 0:00:00 as an intro timestamp. Start with the first real topic shift. Each description should be a short, specific phrase — not a sentence. Write them the way a human skimming would, not the way AI summarizes.)

## Co-hosts

- **Aaron Makelky** — [LinkedIn](https://www.linkedin.com/in/aaron-makelky-m-a-ed-038b852a3/)
- **Dan Yu** — [LinkedIn](https://www.linkedin.com/in/danoyu/)
- **John Lovig** — [LinkedIn](https://www.linkedin.com/in/johnlovig/)

## Links

- [FutureProof You Website](https://futureproof-you.com)
- [FutureProof You on LinkedIn](https://www.linkedin.com/company/futureproof-you)
```

**Rules for timestamps:**
- Identify up to 10 genuine topic shifts in the conversation.
- Use the actual timecodes from the transcript — do not estimate or round to clean numbers.
- Descriptions should be specific to what was said, not generic labels. "Why Aaron quit his teaching job" is good. "Career transitions" is bad.
- If the episode naturally has fewer than 10 distinct topics, use fewer. Don't pad.

**Rules for the summary:**
- Write it like a human who actually listened would describe it to a friend.
- Reference specific things that were discussed, not vague themes.
- Keep it 2-4 sentences.

### Step 3: AI Audit the Show Notes

Run the AI Writing Audit skill against the show notes content.

1. Load the audit checklist from: `~/Library/Mobile Documents/com~apple~CloudDocs/Windsurf Projects Coding/Claude Skills/ai-writing-audit-shared/references/checklist.md`
2. Perform a full Phase 1 audit on the show notes (summary and timestamp descriptions only — skip the structured metadata).
3. If issues are found, perform a Phase 2 rewrite, applying fixes per the audit tags.
4. Replace the show notes content with the corrected version.

### Step 4: Write Show Notes File

Save the final show notes to the episode folder:

**Filename:** `Show Notes - EP [NUMBER] - [TITLE] - [YYYY-MM-DD].md`

Example: `Show Notes - EP 25 - The Future of Remote Work - 2026-02-28.md`

### Step 5: Split Speaker Transcripts

Create three separate transcript files, one per co-host. Each file contains only that speaker's segments from the full transcript, in chronological order, with timestamps preserved.

**Filenames:**
- `Aaron Makelky - EP [NUMBER] - [TITLE].md`
- `Dan Yu - EP [NUMBER] - [TITLE].md`
- `John Lovig - EP [NUMBER] - [TITLE].md`

**Format for each file:**

```markdown
# [Speaker Name] — EP [NUMBER]: [TITLE]

[00:00:10]
Welcome to FutureProof You. Today we're talking about...

[00:01:30]
I think the key thing people miss is...

...
```

### Step 6: Generate LinkedIn Posts per Speaker

For each co-host, generate up to 5 LinkedIn post suggestions appended to their speaker transcript file.

**Process:**
1. Review that speaker's transcript segments.
2. Identify their strongest standalone insights — moments where they said something worth sharing on its own.
3. Write each post as an insight-forward LinkedIn post:
   - Lead with the takeaway or insight, not "I was on a podcast."
   - Build the post around the idea, attributing it naturally to the conversation.
   - Write in a professional but conversational tone appropriate for LinkedIn.
   - End with a link to the episode and tags for the other two co-hosts.
4. Each post should stand alone — someone who never listens to the podcast should still find it valuable.

**Append to each speaker file under this header:**

```markdown
---

## LinkedIn Post Suggestions

### Post 1

[Post copy]

[EPISODE LINK]

Aaron Makelky | Dan Yu | John Lovig
FutureProof You

---

### Post 2

...
```

**Rules for LinkedIn posts:**
- Maximum 5 posts per speaker. If a speaker had fewer strong moments, write fewer posts. Don't pad.
- Each post must trace back to something the speaker actually said. Do not invent insights.
- Tag the other two co-hosts by name at the bottom (LinkedIn doesn't support @-tagging in plain text, so just list names — the speaker will tag manually).
- Include `[EPISODE LINK]` as a placeholder if no URL was provided. If a URL was given, use it.
- Do not use "I had the pleasure of...", "Excited to share...", or any LinkedIn cliche openers.
- Posts should be 100-200 words. Not one-liners, not essays.

### Step 7: AI Audit the LinkedIn Posts

Run the AI Writing Audit against all 15 (or fewer) LinkedIn posts.

1. Audit all posts together (Phase 1).
2. Rewrite any that have issues (Phase 2).
3. Update the speaker files with corrected versions.

### Step 8: Summary

After all files are written, output a summary to the user:

```
Done. Files written to [episode folder path]:

- Show Notes - EP [NUMBER] - [TITLE] - [DATE].md
- Aaron Makelky - EP [NUMBER] - [TITLE].md (X LinkedIn posts)
- Dan Yu - EP [NUMBER] - [TITLE].md (X LinkedIn posts)
- John Lovig - EP [NUMBER] - [TITLE].md (X LinkedIn posts)

[Any notes about the episode — e.g., "Dan had the most quotable moments this episode" or "Only 7 distinct topics identified, so timestamps reflect that."]
```

---

## Error Handling

- **Transcript not found:** List files in the episode folder and ask the user to confirm which file to use.
- **Speaker labels don't match:** If labels are ambiguous (e.g., "Speaker 1"), ask the user to map them before proceeding.
- **Fewer than 3 speakers detected:** Warn the user and proceed with however many speakers are found.
- **Episode folder doesn't exist:** Ask for the correct path.

---

## Example Invocation

```
/podcast-notes

Episode folder: ~/Library/Mobile Documents/com~apple~CloudDocs/FU Podcast/EP 25
Episode number: EP 25
Episode title: The Future of Remote Work
Episode date: 2026-02-28
Episode URL: https://futureproof-you.com/ep-25
```
