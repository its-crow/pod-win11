# Changelog

All notable changes to this project will be documented in this file.

---

## [0.3] - 2026-03-17

### Added
- yt-dlp audio downloads now embed:
  - metadata (title, artist, etc.)
  - thumbnail (cover art)
- New `--changes` flag to display changelog from CLI
- Support for external `CHANGELOG.md` (no code edits needed for updates)

### Changed
- Switched yt-dlp output handling to use:
  - `-P` for directory
  - `-o` for filename template
- Improved Windows path reliability (no more duplicated paths)
- Audio downloads now explicitly use `bestaudio/best` for consistency

### Improved
- Cleaner CLI experience for media downloads
- Better compatibility with DAPs / music players (metadata + album art)
- More predictable file naming and structure

---

## [0.2] - 2026-03-16

### Added
- yt-dlp integration via `download-yt` command
- Audio extraction support (`mp3`, high quality)
- Optional video download mode
- Configurable YouTube download directory

### Improved
- CLI workflow for downloading external media alongside RSS feeds

---

## [0.1] - Initial Release

### Added
- RSS-only podcast support (strict validation, no Atom)
- Feed management:
  - add / remove / rename feeds
- Episode handling:
  - refresh, search, download
- Queue system for batch downloads
- Playlist support with export (M3U)
- SQLite-backed storage
- Per-feed download directories
- OPML import/export support
- Basic CLI structure and command system

---