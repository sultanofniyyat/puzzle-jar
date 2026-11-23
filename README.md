# Puzzle Jar website

Questions-and-answers website for Puzzle Jar (iPhone and Android), made for Google and AI assistants.
Live at https://sultanofniyyat.github.io/puzzle-jar/

- Every app-wide fact: `site.json`. Pages: `content/`. Styles and pictures: `static/`.
- How pages are written and what must never be claimed: `WRITING-GUIDE.md`. Research behind it: `research/`.
- Build: `python3 build.py` → `docs/` (served by GitHub Pages). It refuses to build if a question repeats, two answers
  are near copies, a banned word or a removed game appears, or a `<!-- VERIFY -->` note is left. Then commit and push.
- When the game changes (games, prices, ads, versions), update `site.json` and the affected pages, rebuild, push.
- Note: every build stamps today's date as "Last updated" and in the sitemap, so rebuild and push only when something really changed.
