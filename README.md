# podcast

RSS-first podcast downloader with queues, playlists, and yt-dlp integration.

Lightweight CLI tool for managing podcast feeds, downloading episodes, and organizing audio locally.

---

## Features

- RSS-only parsing (Atom rejected)
- Feed management (add / remove / rename)
- SQLite-backed episode tracking
- Flexible downloads (latest / all / by ID / since date)
- Queue system
- Playlist support (M3U export)
- Full-text search (FTS5 optional)
- OPML import/export
- yt-dlp integration (audio + video)
- Per-feed and global download directories
- YouTube compatibility fixes (cookies + JS runtime support)

---

## Installation

### Using pipx (recommended)

pipx install git+https://github.com/its-crow/pod-win11.git

### Local install (dev)

pipx install -e .

### Using pip

pip install .

---

## Command

podcast

---

## Quick Start

# Initialize config + database
podcast init

# Add a feed
podcast add-feed tdz https://example.com/rss.xml

# Refresh episodes
podcast refresh --feed tdz

# Download latest episode
podcast download --feed tdz

---

## Commands

### Feeds

podcast list-feeds
podcast add-feed <name> <rss_url>
podcast remove-feed <name>
podcast rename-feed <old> <new>
podcast refresh --feed <name>
podcast refresh --all

---

### Downloads

podcast download --feed <name>
podcast download-title --feed <name> --title "keyword"

Options:
--latest N
--all
--ids 1,2,3
--since YYYY-MM-DD
--jobs N

---

### Search

podcast search --feed <name> --query "keyword"
podcast search-all --query "keyword"
podcast search-all --query "keyword" --fts

---

### Queue

podcast queue-add --feed <name> --episode-id <id>
podcast queue-list
podcast queue-download
podcast queue-remove --queue-id <id>
podcast queue-reset

---

### Playlists

podcast playlist create mylist
podcast playlist add mylist --episode-id <id>
podcast playlist show mylist
podcast playlist export mylist --out playlist.m3u

---

### yt-dlp Integration

podcast download-yt --link <url>
podcast download-yt --link <url> --video

Optional flags:
--cookies-from-browser firefox
--js-runtime node

Defaults:
- cookies: firefox
- runtime: node

---

### OPML

podcast opml import feeds.opml
podcast opml export feeds.opml

---

### Settings

podcast set --download-dir ~/pods
podcast set --download-yt-dir ~/yt

podcast set --change-feed-dir tdz --dir ~/custom/tdz
podcast set --unset-feed-dir tdz

podcast set --show

---

### Utility

podcast info <feed>
podcast clean <feed>
podcast dirs
podcast --changes
podcast --version

---

## Storage

Config: PODFILE.ini
Database: SQLite
Audio: per-feed dirs

---

## Notes

- RSS feeds only (Atom rejected)
- SQLite used for persistence
- Optional FTS5 support
- SSL verification disabled in code (intentional for compatibility)
- Windows Media Player compatibility handled via format selection (mp4 + m4a)

---

## Version

0.4

---

## Changelog

podcast --changes

---

## License

MIT (or add your license)
