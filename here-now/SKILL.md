---
name: here-now
description: here.now — publish websites and store private files in cloud Drives. Use when asked to "publish this", "host this", "deploy this", "share this on the web", "make a website", "put this online", "create a webpage", "save this to my Drive", "store this for later", "write this to cloud storage", "share a folder with another agent", or "use my here.now Drive". Also use for agent-to-agent file handoff via scoped Drive tokens.
---

# here.now

here.now lets agents publish websites and store private files in cloud Drives.

**Docs:** https://here.now/docs

## Two Modes

- **Sites** — publish files to `{slug}.here.now` (permanent with API key, 24h expiry without)
- **Drives** — private cloud storage with shared tokens for agent-to-agent collaboration

## Shared Drive (Aaron's Setup)

Both Hermes and Codex use the same Drive with full read/write access:

```
herenow_drive:
  id: drv_01kq8gfx0q0tazz8f071vzn9rj
  api_base: https://here.now/api/v1/drives/drv_01kq8gfx0q0tazz8f071vzn9rj
  token: drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo
  perms: write
  pathPrefix: null
  expiresAt: 2026-05-31T03:32:32.125Z
```

With here.now skill:
```bash
./scripts/drive.sh ls "My Drive" --token drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo
./scripts/drive.sh cat "My Drive" path/to/file.md --token drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo
./scripts/drive.sh put "My Drive" path/to/file.md --from /local/file.md --token drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo
```

Without skill (curl):
```bash
# Read
curl -sS "https://here.now/api/v1/drives/drv_01kq8gfx0q0tazz8f071vzn9rj/files/path" \
  -H "Authorization: Bearer drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo"

# Write (3-step: initiate → upload → finalize)
INIT=$(curl -sS -X POST "https://here.now/api/v1/drives/drv_01kq8gfx0q0tazz8f071vzn9rj/files/uploads" \
  -H "Authorization: Bearer drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo" \
  -H "content-type: application/json" \
  -d '{"path":"path","size":123,"contentType":"text/plain","sha256":"...","ifNoneMatch":"*"}')
curl -X PUT "$(echo $INIT | jq -r '.uploadUrl')" -H "Content-Type: text/plain" --data-binary @file.txt
curl -sS -X POST "https://here.now/api/v1/drives/drv_01kq8gfx0q0tazz8f071vzn9rj/files/finalize" \
  -H "Authorization: Bearer drv_live_Oa2Z84cokcMXazwYwbuQnp1aIfS_BzTLoUnUl1oTxOo" \
  -d "{\"uploadId\":\"$(echo $INIT | jq -r '.uploadId')\"}"
```

## Setup (First-time)

### 1. Get an API key

```bash
curl -sS https://here.now/api/auth/agent/request-code \
  -H "content-type: application/json" \
  -d '{"email": "you@example.com"}'
# Check email for code, then:
curl -sS https://here.now/api/auth/agent/verify-code \
  -H "content-type: application/json" \
  -d '{"email":"you@example.com","code":"XXXX-XXXX"}'
```

Save the returned `apiKey` to `~/.herenow/credentials`:
```bash
mkdir -p ~/.herenow && echo "YOUR_API_KEY" > ~/.herenow/credentials && chmod 600 ~/.herenow/credentials
```

### 2. Install the skill

```bash
npx skills add heredotnow/skill --skill here-now -g
```

## Publish a Site

```bash
# Basic (anonymous = 24h)
./scripts/publish.sh /path/to/index.html

# Authenticated (permanent)
./scripts/publish.sh /path/to/index.html --client your-agent

# Update existing
./scripts/publish.sh /path/to/index.html --slug existing-slug
```

## Drive Operations

```bash
# List drives
./scripts/drive.sh ls

# List files
./scripts/drive.sh ls "My Drive"
./scripts/drive.sh ls "My Drive" some/prefix/

# Upload
./scripts/drive.sh put "My Drive" path/file.md --from /local/file.md

# Download
./scripts/drive.sh cat "My Drive" path/file.md

# Delete
./scripts/drive.sh rm "My Drive" path/file.md
```

## Agent-to-Agent Handoff (scoped tokens)

Generate a limited token for specific collaboration:

```bash
# Read-only, path-prefixed, 7 day TTL
./scripts/drive.sh share "My Drive" --perms read --prefix project/ --ttl 7d

# Write token for reverse handoff
./scripts/drive.sh share "My Drive" --perms write --prefix handoff/ --ttl 1d
```

The `herenow_drive:` block in the output is passed to the receiving agent.

## Resources

- **Docs:** https://here.now/docs
- **Skill repo:** https://github.com/heredotnow/skill
- **here.now:** https://here.now
