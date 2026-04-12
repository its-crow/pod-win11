# podcast

RSS-first podcast downloader with queues, playlists, and yt-dlp integration.

---

## Features

* RSS-only parsing (Atom feeds not supported)
* Feed management (add, remove, rename)
* SQLite-backed episode tracking
* Flexible downloads (latest, all, by ID, since a date)
* Queue system
* Playlist support (M3U export)
* Full-text search (FTS5 optional)
* OPML import/export
* yt-dlp integration (audio + video)
* Per-feed and global download directories
* YouTube compatibility fixes (cookies + JS runtime support, default cookies=firefox, JS runtime=node)

---

## Installation

### Using pipx (recommended)

pipx install git+[https://github.com/its-crow/podcast.git](https://github.com/its-crow/podcast.git)

### Local / development install

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

podcast add-feed tdz [https://example.com/rss.xml](https://example.com/rss.xml)

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
--cookies-from-browser <browser> (default: firefox)
--js-runtime <runtime> (default: node)

This fixes YouTube blocking issues and supports proper audio/video download.

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
Audio: per-feed directories

---

## Notes

* RSS feeds only (Atom unsupported)
* SQLite used for persistence
* Optional FTS5 support
* SSL verification disabled in code (intentional)
* Windows Media Player compatibility handled via format selection (mp4 + m4a)

---

## Version

0.4.1

---

## Changelog

* Added yt-dlp video support with mp4/m4a compatibility
* Added new CLI flags:

  * --cookies-from-browser <browser>
  * --js-runtime <runtime>
* Automatic defaults:

  * cookies → firefox
  * JS runtime → node
* Pyproject.toml packaging
* GitHub pipx install support
* Improved yt-dlp format selection
* Updated CLI to support runtime/auth options
* Fixed no audio in downloads (Opus codec issue)
* Fixed yt-dlp 429 / bot detection errors
* Fixed entry point import path
* Fixed git SSH + .gitignore issues
* Removed setup.py
* Added version tag v0.4

Use `podcast --changes` to see full changelog.

---

## License

MIT (or your chosen license)
