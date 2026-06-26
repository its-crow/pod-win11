# Changelog

All notable changes to this project will be documented in this file.

---

## 0.5.1 - 4/12/26

Dev:
- Updated pyproject.toml and packaging
- Bumped version to 0.5.1
- GitHub tag v0.5.1

---

## 4/11/26
v0.4

Added:
- yt-dlp video support with mp4/m4a compatibility
- new CLI flags:
  - --cookies-from-browser <browser>
  - --js-runtime <runtime>
- automatic defaults:
  - cookies → firefox
  - JS runtime → node
- pyproject.toml packaging
- GitHub pipx install support

Changed:
- improved yt-dlp format selection to avoid AV1/Opus
- updated CLI to support yt-dlp runtime/auth options
- updated README

Fixed:
- no audio in downloads (Opus codec issue)
- yt-dlp 429 / bot detection errors
- entry point import path
- git SSH + .gitignore issues

Dev:
- removed setup.py
- added version tag v0.4

---

## [0.3] - 2026-03-17
- refer to README.md for all features previous to v0.4