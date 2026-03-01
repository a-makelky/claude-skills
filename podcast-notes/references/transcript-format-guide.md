# Recommended Transcript Format for LLM Processing

## Best Format: Plain Markdown with Speaker Labels

This is the most token-efficient format that preserves all needed information.

```markdown
**Aaron Makelky** [00:00:00]
Welcome to FutureProof You. Today we're talking about something that's been on my mind for a while.

**Dan Yu** [00:00:10]
Yeah, and I think this connects to what we were discussing last week about the job market shifts.

**John Lovig** [00:00:20]
The interesting part is how fast this is accelerating. Six months ago this wasn't even a conversation.
```

### Why this format works:

1. **Speaker labels are bold** — easy for an LLM to parse with simple pattern matching (`**Name**`)
2. **Timestamps in brackets** — unambiguous, parseable, don't interfere with the text
3. **10-second intervals** — enough granularity for accurate show notes timestamps without drowning in timecodes
4. **Plain paragraph text** — no extra markup, no numbered blocks, no arrow notation
5. **Token efficient** — ~40% fewer tokens than SRT format for the same content

### Formats to avoid:

**SRT (SubRip)** — Adds numbered blocks and arrow timestamps (`00:00:10,000 --> 00:00:20,000`) that waste tokens. The block numbering is meaningless for our purposes.

**VTT (WebVTT)** — Similar overhead to SRT with an extra header line.

**JSON transcript** — Extremely token-heavy due to key-value pair syntax for every utterance.

### Converting from other formats:

If your transcript tool exports SRT or VTT, convert to the markdown format above before dropping it in the episode folder. Most transcription tools (Descript, Otter, etc.) can export plain text with speaker labels — use that and add timestamps manually or via script.

### Speaker label variations:

The skill will attempt to map common variations:
- "Aaron" → "Aaron Makelky"
- "Dan" → "Dan Yu"
- "John" → "John Lovig"
- "Speaker 1/2/3" → Will ask user to map these
