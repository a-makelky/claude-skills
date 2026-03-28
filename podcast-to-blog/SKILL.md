---
name: podcast-to-blog
description: "Convert podcast guest appearance transcripts into publish-ready blog posts in Aaron's authentic voice. Use this skill whenever the user provides a podcast transcript, mentions converting a podcast episode to a blog post, references a guest appearance they want to write up, or says anything like 'turn this episode into a post,' 'write up my podcast appearance,' 'podcast blog,' or 'transcript to blog.' Also trigger when the user uploads a markdown file with speaker labels and timestamps alongside mentions of a podcast or episode."
---

# Podcast-to-Blog Converter

Transform podcast guest appearance transcripts into 1,500–2,500 word blog posts that recycle Aaron's spoken ideas into polished written content while providing backlinks to the host's ecosystem.

---

## Step 1: Gather Context

When the user provides a transcript (or says they will), ask for the following context before writing. Ask all at once in a single message — do not drip-feed questions:

1. **Episode link** — URL to the published episode (or "not live yet")
2. **Host name and their socials** — Twitter/X handle, LinkedIn, website, podcast homepage — whatever they want linked
3. **Topic focus** — What was the core discussion about? (e.g., "AI in education," "career pivots," "practical AI for non-technical people," "creator economy")
4. **Target keywords** — Any specific SEO terms they want to hit, or should you derive them from the topic?
5. **Anything to emphasize or skip?** — A specific moment they loved, or a tangent they'd rather not feature

If the user provides some of this upfront, only ask for what's missing.

---

## Step 2: Process the Transcript

Read the full transcript. Extract:

- **Aaron's key arguments and opinions** — These are the backbone of the post
- **Memorable phrasing** — Specific language, metaphors, or turns of phrase Aaron actually used (preserve these — they ARE the voice)
- **Narrative arc** — How the conversation progressed; what built on what
- **Concrete examples and stories** — Anecdotes, case studies, specific tools or experiences mentioned
- **Host contributions worth referencing** — Good questions or framing that contextualizes Aaron's points (attribute naturally, e.g., "When [Host] asked about X, it got me thinking...")

**Do NOT extract:**
- Filler, false starts, or conversational dead ends
- Points where Aaron was clearly riffing without substance
- The host's opinions (unless directly relevant to framing Aaron's response)

---

## Step 3: Write the Blog Post

### Structure

Every post follows this skeleton. Sections are conceptual — do not use these as literal headers in the output.

```
1. HOOK (2-3 sentences)
2. CONTEXT BRIDGE (1 short paragraph)
3. MEAT — 3 to 5 key ideas, each developed (bulk of the post)
4. SYNTHESIS / SO-WHAT (1-2 paragraphs)
5. LINKS BLOCK
```

#### 1. Hook
Open with the single most interesting, surprising, or provocative thing Aaron said on the show. Drop the reader into the idea immediately — no "I recently had the pleasure of joining [Host] on [Podcast]..." preamble.

Good hooks from Aaron's voice:
- A counterintuitive claim: "The most valuable thing AI did for my family had nothing to do with work."
- A specific image: "There's a handwritten recipe card in my mom's kitchen that's been slowly fading for 30 years."
- A direct challenge: "Most people using AI are solving the wrong problems."

#### 2. Context Bridge
After the hook lands, briefly establish where this conversation happened. One paragraph max. Name the podcast, name the host, link to the episode. Keep it tight — the reader came for the ideas, not the logistics.

Example tone: "I sat down with [Host] on [Podcast Name] to talk about [topic]. The conversation went places I didn't expect, and a few things I said have been rattling around in my head since."

#### 3. Meat (3-5 Key Ideas)
This is 70-80% of the word count. For each key idea:

- **Lead with the point**, not the setup. State what Aaron thinks, then support it.
- **Use Aaron's actual language** from the transcript, cleaned up for written form. Do not put his words in quotation marks as self-quotes — just write in first person as if he's writing the blog himself. Edit for sequence, grammar, and concision, but preserve his specific vocabulary and phrasing patterns.
- **Include concrete examples.** If Aaron told a story on the podcast, retell it tightly.
- **Transition naturally** between ideas. The post should read as a cohesive essay, not a listicle of disconnected takes.

Use H2 headers (`##`) to break up the key ideas. Headers should be short, specific, and reflect Aaron's voice — not generic topic labels.

Bad: `## The Importance of AI in Education`
Good: `## Teachers Don't Need Another Tool — They Need a Different Lens`
Good: `## The Recipe Card Problem`
Good: `## Why I Stopped Trying to Impress People With AI`

#### 4. Synthesis
Wrap up with 1-2 paragraphs that tie the ideas together. This is where Aaron steps back and says what the conversation meant to him, or what he wants the reader to take away. No forced inspiration. No "and that's why AI will change the world." Just a honest reflection or a forward-looking thought.

#### 5. Links Block
At the very end, after the prose is done, include a clean links section:

```markdown
---

**Where to find [Host Name]:**
- [Podcast Name](episode-url)
- [Website](url)
- [X/Twitter](url)
- [LinkedIn](url)
```

Only include links the user actually provided. Do not fabricate or guess URLs.

---

### Voice Rules

These are non-negotiable. Violating any of these produces content Aaron would reject.

**DO:**
- Write in first person throughout
- Use short paragraphs (1-3 sentences typical)
- Use specific details over abstract claims
- Let ideas breathe with white space
- Sound like a smart person talking to a friend, not a thought leader performing for an audience
- Use Aaron's actual words and phrasings from the transcript wherever they work in written form
- Be direct — state opinions as opinions, not as hedged suggestions

**DO NOT:**
- Use emojis
- Use hashtags
- Use "game-changer," "delve," "tapestry," "realm," "unlock potential," "this changes everything," "at the end of the day"
- Use "workflow" unless quoting a specific tool feature
- Use em dashes excessively (one per post max)
- Write a CTA at the end ("subscribe," "follow me," "let me know what you think")
- Use the phrase "I had the pleasure of" or any variation
- Start sentences with "Look," or "Listen," (overused podcast-to-text pattern)
- Use "deep dive" to describe the conversation
- Bold random phrases for emphasis
- Use rhetorical questions as transitions ("So what does this mean?")
- Reference "the conversation" or "the episode" more than twice after the context bridge

---

## Step 4: Generate SEO Metadata

After the blog post, output a metadata block:

```markdown
---

## SEO Metadata

**Title Tag:** [55-60 characters, includes primary keyword, sounds like Aaron not a marketer]
**Meta Description:** [150-160 characters, summarizes the post's core argument, includes primary keyword]
**Keywords:** [5-8 keywords/phrases derived from the topic focus and transcript content]
**Slug suggestion:** [url-friendly-slug-based-on-title]
```

Keywords should be derived from:
1. The topic focus the user provided
2. Specific tools, concepts, or themes from the transcript
3. Aaron's known content pillars: AI for non-technical people, career reinvention, creator playbook, education + AI

---

## Step 5: Self-Audit

Before presenting the final output, silently check:

- [ ] Opens with a hook, not a context dump
- [ ] 1,500-2,500 words (body only, excluding metadata)
- [ ] No banned words or phrases
- [ ] No emojis, hashtags, or CTAs
- [ ] First person throughout
- [ ] Host is named and linked but post is about Aaron's ideas
- [ ] At least 3 distinct ideas developed from the transcript
- [ ] Concrete examples or stories included
- [ ] Headers are specific and voice-appropriate
- [ ] Links block only contains URLs the user actually provided
- [ ] SEO metadata is present and complete
- [ ] Reads like something Aaron would actually publish, not like an AI summarized a podcast

If any check fails, fix it before outputting.

---

## Step 6: Run AI Writing Audit

**This step is mandatory. Do not skip it.**

After the blog post passes the self-audit in Step 5, immediately run the full post body through the `ai-writing-audit` skill (located at `/mnt/skills/user/ai-writing-audit/SKILL.md`). Read that skill's instructions and follow its two-phase workflow:

1. **Phase 1 (Audit):** Run the checklist against the blog post. Flag every offense.
2. **Phase 2 (Rewrite):** Fix all flagged issues in place, preserving meaning and Aaron's authentic voice.

Apply the corrected text as the final version of the blog post. Do not present the pre-audit draft to the user — only the cleaned version.

If the audit returns 0 issues, proceed directly to output.

**Important:** The AI audit skill's Descript brand voice filter is useful for catching generic AI patterns, but this is Aaron's personal blog, not Descript content. When applying fixes, prioritize Aaron's voice rules from Step 3 of THIS skill over Descript-specific brand voice guidance. The goal is to eliminate AI tells, not to make it sound like Descript marketing.

After the audit + rewrite, append a brief note at the bottom of your response (outside the Markdown document):

```
AI Audit: [n] issues found and corrected.
```

---

## Output Format

Deliver the complete blog post (post-audit) as a single Markdown document, structured as:

```
[Blog post content in Markdown — already cleaned by AI audit]

---

## SEO Metadata

**Title Tag:** ...
**Meta Description:** ...
**Keywords:** ...
**Slug suggestion:** ...
```

After outputting, ask: "Want me to adjust the hook, trim anything, or shift emphasis to a different part of the conversation?"
