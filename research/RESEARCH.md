# Research before building the Puzzle Jar website (2026-11-24)

How to rank on Google and get picked by ChatGPT, Gemini, Claude, Perplexity and Copilot, and how to write 500 answers
without being flagged as low-quality AI content. Reddit could not be checked (blocked for this agent). Pages marked
"not reached" were tried and failed.

## 1. Google's rules (verified, official)

| Fact | Source |
|---|---|
| "Scaled content abuse" = many pages made mainly to manipulate rankings, whether by AI, people or both. The test is purpose and value, not page count. | developers.google.com/search/docs/essentials/spam-policies ; blog 2024-03-05 core-update-spam-policies |
| Doorway pages: near-duplicate pages made to rank for similar queries. | same spam-policies page |
| Google judges "the quality of content, rather than how content is produced". AI use is allowed; fact-check everything, including titles, descriptions, alt text, structured data. | Search Central blog 2023-02-08; docs/fundamentals/using-gen-ai-content |
| Helpful-content warning signs: "extensive automation to produce content on many topics", "mainly summarizing what others have to say". | docs/fundamentals/creating-helpful-content |
| FAQ rich results were switched off for every site on 2026-05-07. FAQPage markup is harmless but gives no special result. | developers.google.com/search/updates ; seroundtable.com 41298 |
| QAPage markup is only for pages where users submit answers. Not for us. | docs/appearance/structured-data/qapage |
| AI Overviews / AI Mode: "no additional requirements", no special files or schema; page must be indexed and allowed a snippet. | docs/appearance/ai-features |
| New sites need time; Mueller (2026-11-10): "quality over quantity". Free shared hosting "attracts a lot of spam" (Mueller, 2026-01-19). | seroundtable.com 42489 ; searchenginejournal.com 565249 |

Practitioner evidence (opinion, labelled): Gary Illyes (2025): AI text should be "human curated", problems come from
content "extremely similar" to what exists. Zyppy 50-site study: winners wrote in first person, showed first-hand
experience and contact details; word count did not matter.

## 2. How AI assistants find and pick sources

| Assistant | Where it searches | Source |
|---|---|---|
| ChatGPT | OAI-SearchBot crawler + Bing + other sources (mixed evidence) | developers.openai.com/api/docs/bots ; Ahrefs 118,931 queries |
| Claude | Claude-SearchBot; results match Brave Search (not announced by Anthropic) | support.claude.com 8896518 ; simonwillison.net 2025-03-21 |
| Perplexity | PerplexityBot | docs.perplexity.ai/guides/bots |
| Gemini / AI Overviews | Google's normal index (Google-Extended does not affect Search) | developers.google.com/.../google-common-crawlers |
| Copilot | Bing index | widely reported |

Study findings:
- GEO paper (Aggarwal et al., KDD 2024, 10,000 queries): adding statistics +33%, quotations +41%, citing sources +28%
  visibility; keyword stuffing -9%. Smaller sites gained most.
- 44% of ChatGPT citations come from the first 30% of a page (Indig, 18,012 citations): answer first.
- Mentions of a brand on other sites correlate 0.664 with AI Overview mentions; backlinks only 0.218 (Ahrefs, 75K brands).
- Games (AppTweak, 125K ChatGPT recommendations, 2026-08): the App Store is cited 42.6% of the time and Google Play 16%; games get
  5x more Reddit/Wikipedia citations than other apps. Their advice: strong store listing + one web page per game covering
  what it is, who it is for and how it compares.
- "Best X" list pages are the most-cited page type (Wix, 75K answers: 21.9%); recently updated lists with 10-20 items do best (Seer).
- Schema markup showed no measurable citation lift (Ahrefs, 1,885 pages, 2026-05). llms.txt: 97% of files got zero
  requests (Ahrefs, 137K sites); Google says no AI system uses it.

## 3. Competitors and real questions

- Big rivals (Royal Match, Screw Jam, Tile Busters, Water Sort) keep help inside the app; their websites barely rank.
  "Games like Screw Jam", "best sorting games" and "best nuts and bolts game" show only thin list sites and store pages:
  an open gap.
- Best-practice help writing (Zynga, Sega, Common Sense Media, Qustodio): one question per heading, worded as players type
  it, short answer first, separate iPhone/Android steps, a parents section, an honest ads section.
- Player complaints across the genre (store reviews, articles): too many ads; levels that seem to need paid helpers;
  "remove ads" not removing all ads; lives and waiting; misleading ads (UK ASA banned several, 2026-11-04); games that
  say "offline" but need internet. Praise: no timers, undo, restart, calm play, levels proven winnable.
- Real search wording: 660 Google suggestions collected (research/google-suggestions-2026-11-24.txt), e.g.
  "puzzle games that don't need wifi", "sorting games with no timer", "best sorting games without ads",
  "games like nut sort", "best game for long flight", "do puzzle games help with anxiety", "games like candy crush with
  unlimited lives", "screw puzzle game no ads".

## 4. Decisions for this site (what the evidence says to do)

1. About 30 pages, each on one real topic: one page per game (20) plus 9 topic pages and the home page. No near-copy
   "games like X" pages; one comparison page instead.
2. Each question appears once on the whole site; game pages ask only questions specific to that game's rules.
   An answer counts toward 500 only if it says something no other answer says.
3. Answer in the first sentence, then detail. Question headings worded the way people search.
4. First-person, first-hand: "we made this game"; real screenshots; real numbers from the game (20 games, 3 free take backs,
   5-second ad notice, 106 MB, iOS 15 / Android 7).
5. Honest about ads, purchases and data (AdMob, tracking question, Android analytics). The genre's top complaints are
   answered head-on.
6. Other games named only in fair, factual comparison; nothing claimed about them from unverified sources.
7. Plain HTML text, internal links, visible "last updated" date, fast pages, no pop-ups.
8. Structured data: Organization, VideoGame/MobileApplication (price 0, no fake rating), BreadcrumbList. FAQPage kept
   (harmless, read by Bing). No llms.txt promises; a small one is kept because it costs nothing.
9. robots.txt (the root one at sultanofniyyat.github.io counts) allows every search and AI-search crawler and lists the sitemap.
10. After launch (owner's accounts): Google Search Console + Bing Webmaster Tools, submit sitemap; get the site mentioned
    on other sites and YouTube; consider a custom domain (about $10-15 a year).
