# Writing guide for the Puzzle Jar website (read in full before writing a page)

Facts: `/private/tmp/claude-501/-Users-bilalsultan-Documents-Unity-Workspace-iOS-Route-Duel/09ae1271-afb6-4cbb-b19b-4ce5204a9754/scratchpad/facts.md`
(copy kept in research/facts.md). Research: research/RESEARCH.md. Real Google search wording:
research/google-suggestions-2026-11-24.txt. Example page to copy in format and voice: content/10-bolts-and-jars.html.

## Why these rules
Google penalises "scaled content": many pages or answers that exist only to rank and add nothing. AI assistants quote
short, self-contained, factual answers that put the answer first. So every answer must be true, specific and useful,
and must not repeat another answer.

## Format (exactly)
- File: content/NN-name.html. Front matter between `---` lines: slug, group (game | topic | about), order, title
  (≤ 65 chars ideally), description (≤ 160 chars, no "{{" tokens over that), h1, related (2-4 slugs from the list below),
  and for game pages also name, blurb, image, alt, caption.
- Body: first `<p class="answer">` = the page's short answer (2-4 sentences, the most important facts first).
- Then questions: `<h2>Question?</h2>` followed by `<p>` (and optionally `<ul>` or a small `<table>`). The heading MUST end with "?".
  Every such heading counts as one question for the 500 total.
- Answer in the first sentence ("Yes.", "No.", "About 2 minutes.", "Tap a screw..."), then 1-4 more sentences of real detail.
  Most answers 40-110 words. Never under 15 words.
- Internal links: `<a href="../slug/">text</a>` (home is `../`). Only slugs from the list below.
- Tokens available: {{GAME_NAME}} {{STUDIO}} {{APPSTORE_URL}} {{PLAY_URL}} {{SUPPORT_EMAIL}} {{SUPPORT_URL}}
  {{PRIVACY_IOS_URL}} {{PRIVACY_ANDROID_URL}} {{MIN_IOS}} {{MIN_ANDROID}} {{IOS_SIZE}}. Writing "Puzzle Jar" directly is fine.
- If you are unsure a fact is true, write `<!-- VERIFY: what to check -->` next to it. The build refuses to publish
  until it is checked. Never guess silently.

## Voice
- We are the small studio that made the game ("we built", "we test every level"). Plain, warm, specific, everyday
  English; American spelling ("color"), but in-game names exactly as in the app ("Bolts & Jars", "Take back", "+1 hole").
- Write like a person who has played every level: concrete details, real numbers, real names of pieces.
- Banned: filler openers ("Great question", "In today's fast-paced world", "When it comes to", "Whether you're...",
  "dive into", "delve", "unleash", "elevate", "game-changer", "look no further", "in conclusion", "it's worth noting",
  "embark", "seamless", "plethora", "realm", "tapestry", "boasts"). No exclamation marks. No emoji. No marketing hype
  ("the best puzzle game ever", "addictive"). No word "narrow" or any word containing the letters a-r-r-o-w (the build
  rejects it; say "pointer", "tip", "slim").
- Be honest about the downsides: there are ads between levels (from the 3rd finished level, after a 5-second notice;
  removable for a one-time purchase), purchases exist, the app is English only, iPhone has no iPad version,
  no cloud save. Honesty is what makes the rest believable.
- Vary sentence length and structure from answer to answer. Do not start many answers the same way.

## Never claim (facts.md section C, plus)
- No removed games (four names listed in facts.md C). Exactly 20 games. No "4,200 levels"; say "thousands of levels"
  or the per-game numbers in facts.md.
- No "no ads", no "no data collected", no cloud save, accounts, multiplayer with real people, leaderboards, lives/energy
  (there are none — say so), iPad app, other languages in the app, iPhone 2.1.2 features (in-app rating box) as live.
- Nothing about OTHER companies' games unless it is common, well-known and stable knowledge (what the game is, its
  genre, who makes it); never their ad counts, prices, ratings or level numbers. Never say we are connected to them.
  Never say our game copies them. Our games are our own designs in well-known genres.
- Never repeat a question asked on another page. App-wide topics (free? ads? offline? kids? saving? iPhone/Android?)
  are answered ONLY on their topic page; a game page may link there in one sentence but must not ask those questions.
- Do not reuse another answer's sentences. Each answer must contain at least one fact the others don't.

## Pages and slugs (link only to these)
Home: `../` (slug index)
Games (order 10-29): bolts-and-jars-screw-puzzle, sweet-stacks-color-sort, button-tin-tile-match, nut-sort-nuts-and-bolts,
bead-swap-match-3, mosaic-tray-block-puzzle, toy-chest-block-jam, hop-on-bus-jam-puzzle, pencil-case-tap-away-puzzle,
snug-skeins-yarn-sort, shelf-sort-goods-sorting, treat-drop-merge-game, honey-hive-hexa-sort, fruit-tumble-tap-to-blast,
balloon-bunch-pop-game, tide-pool-blast-puzzle, garland-tangle-rope-untangle, bubble-picnic-bubble-shooter,
quilt-pins-logic-puzzle, route-duel-puzzle-duel
Topics (order 40-48): is-puzzle-jar-free, offline-puzzle-games-no-wifi, stuck-hints-and-difficulty,
kids-safety-and-privacy, help, best-puzzle-games, games-like-popular-puzzle-games, puzzle-game-types-explained, about

## Game page recipe (12-14 questions)
How do you play X? · rule questions players hit (why won't this move work, what does piece Y do) · how to win / how to
lose · 2-4 strategy questions that are genuinely true for THIS game's rules · what each special piece/obstacle does ·
what the hint / take back / rescue does in THIS game · how hard it gets (only facts for this game) · who it suits /
how it compares with the genre (by genre name; you may say "if you like games such as <well-known title>" once).
Image: img name = slug's first part, e.g. sweet-stacks.webp (files in static/img/games/). Alt text describes the screenshot
plainly. Look at the screenshot file before writing the alt text.
