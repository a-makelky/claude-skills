---
name: here-now
description: here.now — publish websites and store private files in cloud Drives. Use when asked to "publish this", "host this", "deploy this", "share this on the web", "make a website", "put this online", "create a webpage", "save this to my Drive", "store this for later", "write this to cloud storage", "share a folder with another agent", or "use my here.now Drive". Also use for agent-to-agent file handoff via scoped Drive tokens.
---

# here.now

here.now lets agents publish websites and store private files in cloud Drives.

**Docs:** https://here.now/docs

## Two Modes

- **Sites** — publish files to `{slug}.here.now` (permanent with API key, 24h expiry without)
- **Drives** — private cloud storage with scoped share tokens for agent-to-agent handoff

## Setup

### 1. Authenticate (one-time)

here.now uses agent-assisted auth. Get an API key:

```bash
# Request a sign-in code (sent to your email)
curl -sS https://here.now/api/auth/agent/request-code \
  -H "content-type: application/json" \
  -d '{"email": "you@example.com"}'

# After receiving the code, verify and capture the API key
curl -sS https://here.now/api/auth/agent/verify-code \
  -H "content-type: application/json" \
  -d '{"email":"you@example.com","code":"XXXX-XXXX"}'
```

**Alternative:** Sign in at https://here.now, the API key appears in the dashboard menu.

### 2. Save the API key

```bash
mkdir -p ~/.herenow
echo "YOUR_API_KEY" > ~/.herenow/credentials
chmod 600 ~/.herenow/credentials
```

### 3. Install the skill

```bash
npx skills add heredotnow/skill --skill here-now -g
```

The skill installs `scripts/publish.sh` and `scripts/drive.sh`.

## Publish a site

```bash
# Basic publish (anonymous = 24h expiry)
./scripts/publish.sh /path/to/index.html

# Authenticated publish (permanent)
./scripts/publish.sh /path/to/index.html --client your-agent-name

# Update an existing site
./scripts/publish.sh /path/to/index.html --slug existing-slug
```

Output: `https://{slug}.here.now/`

## Use Drives

Every signed-in account has a default Drive named "My Drive".

```bash
# List drives
./scripts/drive.sh ls

# List files in a drive
./scripts/drive.sh ls "My Drive"
./scripts/drive.sh ls "My Drive" some/prefix/

# Upload a file
./scripts/drive.sh put "My Drive" path/in/drive.md --from /local/file.md

# Read a file
./scripts/drive.sh cat "My Drive" path/in/drive.md

# Delete a file
./scripts/drive.sh rm "My Drive" path/in/file.md
```

## Agent-to-Agent Handoff via Drive Tokens

The core collaboration primitive: generate a scoped, time-limited token another agent uses to read (or read+write) a specific Drive path.

```bash
# Generate a read-only token, 7 day TTL, path-prefixed
./scripts/drive.sh share "My Drive" \
  --perms read \
  --prefix notes/ \
  --ttl 7d \
  --label "Project notes for Codex"

# Generate a write token
./scripts/drive.sh share "My Drive" \
  --perms write \
  --prefix handoff/ \
  --ttl 1d \
  --label "Hermes → Codex handoff"
```

Output includes a `herenow_drive:` block:

```yaml
herenow_drive:
  id: drv_xxxxxxxxxxxx
  api_base: https://here.now/api/v1/drives/drv_xxxxxxxxxxxx
  token: drv_live_yXFFbNe4fgl2PzbNeamlWcueYwCK4jhDZZ5GEh0aST0
  perms: read
  pathPrefix: notes/
  expiresAt: 2026-05-07T23:02:55.068Z
```

Pass this block to the receiving agent in its task prompt. The agent uses the token as a Bearer auth header:

```bash
# Read using token
curl -sS "https://here.now/api/v1/drives/DRIVE_ID/files/path" \
  -H "Authorization: Bearer drv_live_..."
```

Or with the skill (if available):
```bash
./scripts/drive.sh cat "My Drive" notes/file.md --token drv_live_...
```

## Workflows

### Hermes → Codex handoff
1. Hermes writes files to here.now Drive
2. Hermes generates scoped read token: `--perms read --prefix handoff/ --ttl 7d`
3. Hermes passes `herenow_drive:` block to Codex in task prompt
4. Codex reads files, processes task, writes output back to its own Drive or publishes a site
5. Codex shares its Drive token back to Hermes (reverse handoff)

### Shared project Drive
1. Create a shared Drive: `./scripts/drive.sh create "Project-X"`
2. Both agents get write tokens: `./scripts/drive.sh share "Project-X" --perms write --ttl 30d`
3. Both agents read/write to the same Drive without exposing API keys

### Publish agent output as a site
1. Agent generates HTML output (report, dashboard, visualization)
2. Agent writes files locally, publishes: `./scripts/publish.sh ./output-dir/ --client agent-name`
3. Live URL shared with user or other agents

## API Key Priority

The skill reads credentials from (first match wins):
1. `--api-key` flag (CI/scripting only)
2. `$HERENOW_API_KEY` environment variable
3. `~/.herenow/credentials` file (recommended)

## Notes

- here.now Skills: https://github.com/heredotnow/skill
- here.now Docs: https://here.now/docs
- Sites are public by default but URLs are unguessable
- Add `--ttl` to site publish requests to control expiry
- Drive tokens with `manageTokens: true` allow the holder to create more tokens
