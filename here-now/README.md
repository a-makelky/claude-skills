# here.now

Publish websites and store private agent files in cloud Drives. Use here.now when you need to publish files to a live URL, share files between agents, or store persistent agent context.

## What here.now Does

**Sites** — Publish HTML, documents, images, PDFs, videos, and static files to live URLs at `{slug}.here.now`. Sites are permanent with an API key, or 24-hour temporary without one.

**Drives** — Private cloud storage for agent files: context, memory, plans, code, assets, research. Drives support scoped share tokens for secure agent-to-agent file handoff without exposing API keys.

## Quick Start

### 1. Get an API key

```bash
curl -sS https://here.now/api/auth/agent/request-code \
  -H "content-type: application/json" \
  -d '{"email": "you@example.com"}'
```

Check your email for the code, then:

```bash
curl -sS https://here.now/api/auth/agent/verify-code \
  -H "content-type: application/json" \
  -d '{"email":"you@example.com","code":"XXXX-XXXX"}'
```

Save the returned `apiKey` to `~/.herenow/credentials`:

```bash
mkdir -p ~/.herenow
echo "YOUR_API_KEY" > ~/.herenow/credentials
chmod 600 ~/.herenow/credentials
```

Or sign in at https://here.now and copy the key from the dashboard menu.

### 2. Install the skill

```bash
npx skills add heredotnow/skill --skill here-now -g
```

### 3. Publish a site

```bash
./scripts/publish.sh ./my-site/   # basic (24h)
./scripts/publish.sh ./my-site/ --client my-agent   # permanent
```

### 4. Store files in Drive

```bash
./scripts/drive.sh put "My Drive" notes/today.md --from ./today.md
./scripts/drive.sh ls "My Drive" notes/
```

## Agent-to-Agent Handoff

The most powerful feature: here.now Drives let agents share files securely without exposing API keys.

```bash
# Agent A: Share a read-only token for a specific folder, 7 days
./scripts/drive.sh share "My Drive" --perms read --prefix project/ --ttl 7d
```

Agent B receives the `herenow_drive:` token block and uses it to read shared files.

See the SKILL.md for full details on:
- Scoped read/write tokens with path prefixes
- Reverse handoff (Agent B → Agent A)
- Shared project Drives
- Publishing agent output as a site

## Resources

- **Docs:** https://here.now/docs
- **Skill repo:** https://github.com/heredotnow/skill
- **here.now main site:** https://here.now

## Requirements

- `curl`
- `jq`
- `file`
- Optional: `npx` (for skill install)
