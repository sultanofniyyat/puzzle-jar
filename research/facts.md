# Puzzle Jar: player-facing fact sheet (for the public website)

Compiled 2026-11-24 from the project at "/Users/bilalsultan/Documents/Unity Workspace/iOS/Route Duel" (branch `more-games`)
and the read-only store texts in ~/Desktop/"Route Duel Store Listing". Short cites: file:line. "Code" = Assets/RouteDuel/Code.
Where docs and code disagree, the CODE is used and the conflict is flagged with [CONFLICT].
Never write the banned word (route/head/line only). Note: the Android package name contains it (see A.2).

---------------------------------------------------------------------------------------------------
## A. App-wide facts

### A.1 Names and store text (English)
- App name inside the app: "Puzzle Jar" (Code/App/JarProgress.cs:15; Editor/RouteDuelProjectSetup.cs:17).
- App Store name (English US/UK): "Puzzle Jar: Unscrew & Untangle" (Store Listing/Smart Title and Keywords/2026-11-23 new names - PASTE.txt:9-13;
  changed back to this on 2026-11-23 evening, change log 135 second entry).
- App Store subtitle: "Sorting, Matching & Rope Games" (App Store v2.1.1/Puzzle Jar App Store Text 2.1.1.txt:79-80; 2.1.2 PASTE file: "Subtitles: do not change").
- App Store promotional text (2.1.2): "20 calm puzzle games in one jar: unscrew bolts, sort nuts, untangle ropes, match tiles,
  pop bubbles and more. Plays offline, no Wi-Fi needed." (App Store v2.1.2/...Text 2.1.2.txt:8-9).
- Google Play title: "Puzzle Jar: Unscrew & Untangle"; short description: "20 offline sorting & matching games: screw puzzles,
  rope tangles, hexa and yarn" (Play Store v2.1.0/Puzzle Jar Play Store Text 2.1.0.txt:37-41; Smart Title.../2026-11-19 google play.md:5-6).
  Not verified on the live Play page.
- Other App Store languages use different, local names (e.g. German "Puzzle Jar: Seile entwirren", French "Puzzle: Vis, Écrous et Blocs")
  (2026-11-23 new names - PASTE.txt:15-46). The website should use the English name.

### A.2 Store links and IDs
- App Store app ID: 6823780719 -> https://apps.apple.com/app/id6823780719 (found in the owner's playable ads,
  Store Listing/Ads/Playables/*/...html:9; not found in docs; confirm by opening the link).
- iPhone bundle ID: com.sultanofniyyat.routeduel (RouteDuelProjectSetup.cs:18).
- Google Play package: the value of `PlayPackage` in Editor/RouteDuelProjectSetup.cs:25 (Route Duel's old Play package; it contains
  the banned word, so it is not written here). URL = https://play.google.com/store/apps/details?id=<that value>.
- Privacy page (iPhone): https://sultanofniyyat.github.io/route-duel-privacy/ (App Store v2.0.0/...Text 2.0.0.txt:99).
- Privacy page (Android): https://sultanofniyyat.github.io/route-duel-privacy/android/ (Play Store v2.0.0/make_play_text_pdf.py:152; HANDOFF.md:49).
- Support page: https://sultanofniyyat.github.io/route-duel-privacy/support/ (...Text 2.0.0.txt:100).
- Marketing URL (also hosts app-ads.txt): https://sultanofniyyat.github.io (AGENTS.md:64).
- NOTE: the privacy page still lacks a line about Firebase analytics on Android (STATUS.md:22, "your OK to publish").

### A.3 Developer / seller
- Apple developer team: "bilal ahmed", Individual (RouteDuelProjectSetup.cs:30-31); App Store copyright line "2026 bilal ahmed"
  (App Store v1.0/Route Duel App Store Text.txt:27-28). Unity company name "sultanofniyyat" (RouteDuelProjectSetup.cs:39).
- Google Play developer display name: NOT FOUND in the project or store files. Ask the owner.

### A.4 Versions (as of 2026-11-23/24)
- iPhone: 2.1.1 (build 17) LIVE (STATUS.md:5; change log 133). 2.1.2 (build 18) sent for review 2026-11-23, releases itself
  once approved (STATUS.md:6; change log 134/135). Project version 2.1.2 / build 18 (RouteDuelProjectSetup.cs:19-20).
- Android: 2.1.1 (version code 22) LIVE on Google Play (STATUS.md:5; HANDOFF.md:20). 2.1.2 (23) built, not yet uploaded (STATUS.md:7, 21).
- Website should say "latest version" rather than a number, or check the stores on launch day.

### A.5 Price, purchases, ads
- Free to download; in-app purchases; no coins or other currency (AGENTS.md:62).
- In-app purchases (prices are the US fallback prices in code, Code/App/RouteDuelStore.cs:87-95; real prices show in local currency):
  - Remove Ads, $5.99, one-time (non-consumable): no full-screen ads in any game, AND take backs become unlimited
    (HintWallet.cs:51-61 "∞"; AGENTS.md:62). Rewarded ads stay available as the player's choice (RouteDuelController.cs:1226).
  - 10 Hints $0.99, 60 Hints $4.99, 150 Hints $9.99 (biggest tagged "BEST VALUE") (RouteDuelStore.cs:68-74, 87-95; ScrewScreen.cs:1027).
  - 30 Take Backs, $0.99 (product id "takebacks10" gives 30) (RouteDuelStore.cs:73).
  - 5 Rescues, $0.99 (RouteDuelStore.cs:74).
  - Starter Pack, $2.99, one-time: Remove Ads + 30 hints + 5 rescues (StarterPack.cs:15; RouteDuelStore.cs:90). Offered once, after
    winning road level 21, on Home; on sale for 48 hours from first shown, then gone for good; never shown to Remove Ads owners
    (Core/StarterOffer.cs:16-20; Game_Collection_Plan.md:178-200). Hints/rescues are given once (not again on Restore).
    [CONFLICT] its card in code still says "No more ads, in all 7 games" (Code/App/HomeScreen.cs:502): stale text, app has 20 games.
  - Old "unlimited hints" / "unlimited take backs" ($3.99) are no longer sold but still honoured and restored (AGENTS.md:62).
  - Hints, take backs and rescues are shared by all 20 games (HintWallet.cs; review notes 2.1.1 sec. 3).
  - Settings has "Restore purchases" (HomeScreen.cs:708-709).
  - Starter Pack existing as a Google Play product: id is in code for Android (RouteDuelStore.cs:30), not confirmed in Play Console.
- Ads (Google AdMob):
  - Full-screen ads only BETWEEN levels, never during one; not in the first levels: only once 3 levels have been finished
    (any game) (RouteDuelAds.cs:33-34, 137-139). Before the ad a 5-second "Ad loading" card with a Remove Ads button
    (ScrewScreen.cs:21, 1219; same AdCountdown = 5 in every game screen).
  - No full-screen ad within 20 seconds after a rewarded ad, nor right after the store rating box (RouteDuelAds.cs:35-36, 137-139).
  - Rewarded ads are always the player's choice: +1 hint / take back / rescue on the offer sheet ("WATCH AD · +1"); the first rescue
    of a level in most games; Solo Run +60 seconds once a run; saving a broken day streak (HintWallet.cs:27; ScrewScreen.cs:1031,1114;
    SoloRun.cs:12; HomeScreen.cs:604-611; DuelStreak.cs:6-9).
  - No banner ads (none in RouteDuelAds.cs; memory note: "Banner: none created").
  - Remove Ads removes the full-screen ads only; rewarded ads remain optional.
- Tracking: Apple's "Allow tracking?" (App Tracking Transparency) question at first launch, before the first ad
  (Code/App/Tracking.cs:10; RouteDuelAds.cs:40-41 AskAfter = 0; review notes 2.1.1 sec. 4). Europe/UK: Google's consent form, and
  "Privacy choices" in Settings (HomeScreen.cs:707-711).
- Analytics: Google Analytics for Firebase on ANDROID ONLY (events: purchase value, level_complete, level_5/10/20/50; ad revenue
  logged by Google's ad SDK); iPhone: off (Code/App/JarFirebase.cs:7-16). AdMob itself collects device ID, coarse location, usage
  and diagnostics for ads (App Store v2.0.0 text :103-108). So the website must NOT say "no data collected".

### A.6 Offline, saving, accounts
- Plays offline: every game, all levels, daily puzzles (levels ship inside the app, Resources/PuzzleJar/*.json). Store text:
  "Plays offline, no Wi-Fi needed. No account." (2.1.1 description; 2.1.2 promo text).
- Needs internet: ads (full-screen and rewarded), purchases and Restore purchases ("Couldn't reach the App Store/Google Play",
  HomeScreen.cs:709), the tracking/consent questions, the Starter Pack card (only when the store can be reached, StarterPack.cs:56).
- Progress is saved only on the phone (PlayerPrefs throughout JarProgress.cs). No cloud save, no iCloud, no Game Center, no login
  (no such code found). Deleting the app loses progress; purchases come back with Restore purchases (one-time ones; consumable
  hints/take backs/rescues are not restored).
- No account or login needed (review notes 2.1.1 sec. 2: "no account, no login").

### A.7 Languages, rating, devices, size
- The app itself is English only (review notes 2.1.1 sec. 5 "English only"; no localization package in Packages/manifest.json).
- App Store page text: 10 languages (English US, English UK, Spanish Mexico, Portuguese Brazil, German, French, Japanese, Arabic,
  Ukrainian, Russian) plus 4 extra pages with English text (Korean, Chinese Simplified/Traditional, Vietnamese) (change log 132-133;
  PASTE file :9-77). Google Play page: English only so far (Play in 8 languages is TODO 46, STATUS.md:16).
- Age rating: App Store expected 4+ (questionnaire answers "none", App Store v2.0.0 text :111-112); Google Play expected
  Everyone / PEGI 3, target audience 13+ (Play Store v1.3.0/Play Console steps.txt:39-49). Actual ratings not confirmed in files.
- iPhone only (no iPad build), iOS 15.0 or newer, full screen, portrait; supports both screens of iPhone Duo
  (RouteDuelProjectSetup.cs:47-58; 2.1.1 description "Made for every iPhone, including both screens of iPhone Duo").
- Android 7.0 or newer (API 24), target API 36, ARMv7 + ARM64 (RouteDuelProjectSetup.cs:71-73). Tablets: not restricted in
  settings, not confirmed tested.
- Size: Android upload bundle (AAB) 55 MB for 2.1.0 (change log 111). iPhone download size not recorded.

### A.8 The level road, jar, daily puzzles, Free play
- Home (top to bottom): name + Settings; big card with the jar, the next road level, the next 6 levels as bubbles, Play;
  "Today's puzzles" with the day streak; "Free play", one card per game (Route Duel also has Solo Run) (Game_Collection_Plan.md:282-285).
- One shared level number ("road"): 3 levels of one game (easy, medium, hard), then the next game, round and round through all 20
  (JarProgress.cs:21, 137, 236-264; Core/RoadRound.cs). Only road wins move the road number.
- Road order (JarProgress.cs:21): Bolts & Jars, Sweet Stacks, Button Tin, Nut Sort, Bead Swap, Mosaic Tray, Toy Chest, Hop On,
  Pencil Case, Snug Skeins, Shelf Sort, Treat Drop, Honey Hive, Fruit Tumble, Balloon Bunch, Tide Pool, Garland Tangle,
  Bubble Picnic, Quilt Pins, Route Duel (the two hardest last).
  [CONFLICT] AGENTS.md:15-17 still lists the old 7-game order; code wins.
- Every game is open from the first launch in Free play (AGENTS.md:18; HomeScreen.cs:208). Free play moves that game's own level
  on but not the road number (Game_Collection_Plan.md:291).
- The jar: every win in any game drops a piece in that game's colour; 10 pieces fill it and give +1 hint, +1 take back, +1 rescue,
  then a fresh jar starts (JarProgress.cs:137, 284-303; HomeScreen.cs:579-583).
- Daily puzzles: one per game per day ("Today's puzzles"); 60 dailies a game, the three level sets take turns so they repeat only
  after 180 days (Sort/SortContent.cs:27-31). Route Duel's daily is a picture board picked by the date. Dailies count for the jar
  and streak, not for the game's level (Game_Collection_Plan.md:292-294).
- Day streak: one day for each day in a row with a finished level in any game; a day with more wins than losses is a gold
  "winning day"; a broken streak of 2+ days can be saved with a rewarded ad that day or the next (Core/DuelStreak.cs:6-9;
  HomeScreen.cs:455-462, 604-611).
- Levels follow the player ("the dial"): two easy wins in a row (no help) = a step harder; a win that needed a retry or rescue =
  a step easier; the day's first new level is a step easier. 18 games pick each level from a normal, gentler or tougher set
  (150 levels each); Quilt Pins uses its own ladder; Route Duel's rival plays weaker or stronger (AGENTS.md:110-126; App/PlayerDial.cs).
- Rounds of three: easy, medium, hard; every 4th hard level is a "boss"; an easy level always follows a hard one; level 1 can't be
  lost; levels 1-5 only easy or medium (AGENTS.md:89-90). Every level is proved winnable with no help by computer (AGENTS.md:93).
- Level counts: 18 games have 150 road levels + 60 dailies in each of 3 sets (Resources/PuzzleJar/*.json, counted); past level 150
  a game replays from its level 51 (SortContent.cs:22-27). Quilt Pins: bank of 2,000 quilts (16,000 with turns/mirrors) + 60 dailies.
  Route Duel: 341 levels (guided first duel + 340 picture boards) + 340 Solo Run boards (AGENTS.md:28-31; boards.json/solo.json).
  Safe website wording: "thousands of levels". [CONFLICT] the 2.1.1 App Store description says "Over 4,200 levels" and still
  says "all seven games" in places (App Store v2.1.1 text :37-62); not traceable to code; avoid copying it.

### A.9 Helpers: hints, take backs, rescues
- Three separate counts shared by every game (HintWallet.cs). Welcome gift: 3 hints, 3 take backs, 1 rescue (HintWallet.cs:25).
- HINT: shows a safe next move from the game's solver. No per-level hint limit in code (none found; plan: limit removed, bug 37,
  Game_Collection_Plan.md:155-163). [CONFLICT] AGENTS.md:79 still says "cap 2 a level"; code has no cap.
- TAKE BACK: undoes the last move; the first 3 on every level are free, then from the count; unlimited with Remove Ads
  (HintWallet.cs:34, 51-61). Sweet Stacks: undo and restart always free and unlimited (SortScreen.cs:14, 742).
- RESCUE: the game's "so close" save after you get stuck (extra hole, jar, moves, hearts...). First rescue of a level may be a
  rewarded ad, the next costs a rescue; capped per level: 2 in most games, 1 in Sweet Stacks, Nut Sort, Pencil Case, Shelf Sort
  (each game's Screen.cs `MostRescues` / `MostExtra...`). Stuck screen always also offers TRY AGAIN and HOME (AGENTS.md:83-84).
- Out of a helper: the same offer sheet everywhere: packs, "WATCH AD · +1", "NOT NOW" (ScrewScreen.cs:1012-1036).
- Free supply otherwise only: +1 per rewarded ad, full jar gives 1 of each (AGENTS.md:87).

### A.10 Lives, timers, other
- NO lives / energy system and no waiting to play (no lives code; plan for Bead Swap/Fruit Tumble: "No lives and no waiting").
  Some games have hearts INSIDE a level (Quilt Pins, Pencil Case: 3 hearts; a loss just means retry).
- Only one real countdown clock in the app: Route Duel's Solo Run (Core/SoloRun.cs). Quilt Pins measures play time silently for the
  dial; no clock shown (QuiltScreen.cs:58-60, 370). Move/piece limits: Bead Swap, Fruit Tumble, Balloon Bunch, Toy Chest,
  Garland Tangle (moves); Mosaic Tray (pieces); Treat Drop (sweets); Bubble Picnic (bubbles); Tide Pool (rising rows).
  No limit at all (lose only when space fills/no move): Bolts & Jars, Sweet Stacks, Button Tin, Nut Sort, Hop On, Snug Skeins,
  Shelf Sort, Honey Hive.
- Settings: Sound, Music, Vibration, Reduce motion toggles; Remove ads; Restore purchases; Privacy choices (EEA/UK); version and
  credit "Picture shapes: Noto Emoji by Google (Apache 2.0)" (HomeScreen.cs:694-716).
- Each game shows its rules the first time and again from the "?" button (review notes 2.1.1 sec. 2; each Screen `ShowRules`).
- Design: shape-and-colour puzzles only: no word, number or card games (AGENTS.md:12-13; memory "no card games"). Colours also
  carry their own marks/shapes for colour-blind players (several plan sections). Rules cards do use short English text.
- Store rating box (Apple's / Google Play's own) asked once, after the first win once 3 levels (any game) are finished; the store
  decides if it really shows (Code/App/AppReview.cs:6-31). In 2.1.2 (iPhone in review, Android not yet uploaded).
- History: Route Duel (iPhone 1.0.0 uploaded 2026-10-17, change log 23) became Puzzle Jar in update 2.0.0 on the same App Store
  page and Play page, keeping players' levels and purchases (AGENTS.md:5-9). 2.0.0 uploaded 2026-11-08 (change log 76-77), approved
  by 2026-11-16 (change log 104); exact go-live date not recorded. 2.0.0 had 7 games; 2.1.0 grew it to 20 (Play notes 2.1.0);
  2.1.1 (2026-11-19) replaced 3 games and added levels that follow the player.

---------------------------------------------------------------------------------------------------
## B. The 20 games, in road order
Name + blurb: JarProgress.cs:23-69. Rules lines: each game's Screen.cs `ShowRules`. Details: Documentation/Game_Collection_Plan.md
"Built:" sections. Unless said, each has 150 road levels + 60 dailies x 3 sets, level 1 can't be lost, a glowing guide on level 1.

### 1. Bolts & Jars — "Unscrew bolts into colour jars" — screw puzzle
- Coloured plates lie on top of each other, held by screws. Tap a screw to take it out; a plate on top holds it in (ScrewScreen.cs:1186-1189).
- It flies into the open jar of its colour (2 jars open, next shown; 3 screws fill a jar), else waits in the tray (5 holes) (ScrewGame.cs:66; plan :296-299).
- Win: fill every jar. Lose: tray full AND no screw can go into a jar. No move limit, no clock.
- Each colour has its own mark (heart, shield, star, tick, bolt, eye) (plan :302-305).
- Hint: glowing safe screw. Take back: last screw. Rescue: "+1 hole" in the tray, up to 2 a level (ScrewScreen.cs:20, 1111-1114).
- Difficulty: levels grow about one jar per round of three (plan :313).

### 2. Sweet Stacks — "Sort sweets into jars by colour" — colour sort (ball/water sort style)
- Tap a jar to lift its top sweets, tap another to drop them on the same colour or an empty jar; 4 alike get a lid; lid every jar to win (SortScreen.cs rules).
- UNDO and AGAIN (restart) are always free and unlimited (SortScreen.cs:14, 742).
- From level 31 hard/boss levels have wrapped sweets that show their colour only at the top (plan :325-327).
- 10 colours, each with its own mark; a new colour about every six rounds (plan :332, 341).
- Hint: lifts the right jar and rings the target. Rescue: +1 JAR, one a level (SortScreen.cs:20).
- No move limit, no clock.

### 3. Button Tin — "Match three buttons from the tin" — tile match / triple match
- Buttons in up to 5 layers; tap a free one (nothing on top; covered ones shaded); it goes on the card below (7 spaces) (TileScreen.cs rules; TileGame.Tray).
- Three alike are sewn together and leave. Empty the tin to win; a full card with no three alike = stuck. A counter shows buttons left.
- From level 31 hard/boss levels have face-down buttons (plan :359-361). Up to 10 kinds (TileGame.cs:330); piles grow to ~70-96 buttons.
- Hint: glows a good button. Take back: puts the last button back. Rescue: +1 SPACE on the card, up to 2 a level (TileScreen.cs:20).
- No move limit, no clock.

### 4. Nut Sort — "Sort coloured nuts onto bolts" — nut sort
- Tap a bolt to lift its top nuts, tap another to drop them on the same colour or an empty bolt; 4 of a colour on one bolt get a cap; cap every colour to win (NutScreen.cs rules).
- Bolts differ: tall bolts hold 5, short helper bolts 2-3 (shown by notches, no numbers); board shape changes round by round from level 7 (plan :1369-1373).
- Dark nuts (colour hidden until on top) from level 16 on hard/boss, from 46 on some medium (plan :1373-1376).
- 10 colours with marks (NutGame.cs:478). Hint: lifts the right bolt, rings the target. Rescue: +1 BOLT (holds 4), one a level (NutScreen.cs:20; NutGame.cs:63). AGAIN restarts.
- Replaced Ribbon Box on 2026-11-19.

### 5. Bead Swap — "Swap beads to line up three" — match-3
- Swipe a bead onto its neighbour to line up 3+ of a colour; reach the goals at the top before moves run out (BeadScreen.cs rules).
- Specials: 4 in a row = needle (row/column), L or T = burst, 5 = rainbow bead; two specials swapped make a bigger blast.
- Obstacles: wax (lvl 3, thick 19), crates (7, strong 25), gaps (10), brass buttons to bring down (13) (plan :437-438).
- Move limit 15-38; a swap that matches nothing slides back and costs no move; dropping beads fixed per level (never rigged) (plan :439-457).
- Hint: best swap; free glow after 6 idle seconds. Take back gives the move back. Rescue: +5 moves (BeadGame.cs:74), up to 2 a level.
- Trays grow 7x7 to 9x9; 5 colours, 6 on later bosses.

### 6. Mosaic Tray — "Fill lines with tiles, free the jewels" — block puzzle
- Drag pieces onto an 8x8 tray; a full row or column clears; clear the lines holding jewels to collect them all (MosaicScreen.cs rules).
- Pieces come 3 at a time in a fixed order and are limited (9-45 a level); stuck when none fits or they run out (plan :650-654).
- Every level plays the same each time and is proved winnable (no unfair hands).
- Hint: a safe place for a piece. Take back: lifts the last piece (lines and jewels come back). Rescue: single tiles that fit anywhere + 10 more pieces, up to 2 a level (MosaicGame.cs:187-190; MosaicScreen.cs:21).
- Combo words and "Combo x2" for clears in a row.

### 7. Toy Chest — "Slide blocks out through matching doors" — colour block jam
- Drag a block: it slides through empty squares; at a door of its colour (wide enough) it slides out; get every block out (ToyScreen.cs rules).
- No clock; a number of moves, each drag = one move (plan :685-686).
- Obstacles one at a time: stones (7), two-colour blocks (16), ice (31), one-way blocks (46), locked blocks + key (61).
- Grid 5x5 to 8x8, blocks 1-6 squares.
- Hint: next move of a solver win. Rescue: +5 moves (or enough) and lift any one block off, up to 2 a level (ToyGame.cs:377; ToyScreen.cs:21).

### 8. Hop On — "Walk passengers to the bus of their colour" — bus jam (crowd kind)
- Tap a passenger with a free way to the stop; they board the bus of their colour or wait on the bench; full bus leaves, next pulls in (BusScreen.cs rules).
- Next buses always shown; stuck when the bench is full and nobody can board. No clock, no move limit, no bomb passengers.
- New things: planters (5), hidden passengers (8), doorways (20), frozen passengers (35), two stops (50), big buses (65) (plan :718-719).
- Square grows 3x4 to 7x8; bench 4-7 seats; buses 3 seats, big buses 6.
- Rescue: 2 more bench seats + one passenger of your choice hops out, up to 2 a level (BusGame.cs:341; BusScreen.cs:23).

### 9. Pencil Case — "Tap pencils out of the case, tips first" — tap-away puzzle
- Tap a pencil: it slides out the way its tip points; if something is in its path it bumps and you lose a heart (3 hearts) (PencilScreen.cs rules).
- Retapping a pencil that already bumped (with no pencil gone since) costs nothing (plan :1440-1441).
- Erasers (from 10) never move; clipped pencils (from 16) leave last of their colour (plan :1444-1447).
- Case grows from 4x4 to 9x12, changes shape (wide/square/tall); pencils 2-4 squares long; each colour has a mark.
- Hint: glows a pencil that can leave. Take back: also returns a heart. Rescue: hearts refilled + 2 golden hearts, once a level (PencilGame.cs:67-68; PencilScreen.cs:22).
- Replaced Pop Parade on 2026-11-19.

### 10. Snug Skeins — "Unwind woolly toys into baskets" — yarn unravel / wool sort
- Tap a felt toy: its outer layer of wool flies to the basket of its colour, or waits in the sewing tin; a full basket leaves (YarnScreen.cs rules).
- Each toy shows its next layer colour and layers left; next baskets shown. A tap that would overfill the tin is refused (not a loss); lost only when no tap is left. No clock.
- New things: tied toys (8), hidden wool (15), thick wool (25), pinned toys (40), big baskets (60) (plan :808-809).
- 3-12 toys, 1-7 layers; tin 4-7 spots.
- Rescue: 2 more tin spots + one more basket out + the most-waiting colour's basket comes out, up to 2 a level (YarnGame.cs:372; YarnScreen.cs:22).

### 11. Shelf Sort — "Sort goods on shelves, three alike pop" — goods sort / triple sort
- Drag an item to a shelf with a free spot (or tap item, then shelf); three of a kind in front pop; empty front = row behind steps forward (ShelfScreen.cs rules).
- Clear every shelf to win; lose when every spot is full. No timer, no move count. After 40 moves without a pop a friendly
  "Going round in circles?" card offers help or KEEP TRYING (plan :1524-1527).
- Locked shelves (from 10) open by play (rings light as goods pop), never by ad or payment; picky shelves (from 31) take one kind (plan :1533-1536).
- 12 kinds of goods with their own outline shapes; 3-7 shelves.
- Rescue: +1 SHELF, once a level (ShelfScreen.cs:21). Replaced Stitch Hoop on 2026-11-19.

### 12. Treat Drop — "Drop sweets, join two alike into bigger ones" — drop & merge (watermelon-style)
- Slide to aim, let go to drop; two of the same sweet that touch join into the next one (10 sizes, sprinkle up to rainbow lolly) (DropScreen.cs rules; plan :879-882).
- Goal: make the sweets shown (e.g. "make 2 tarts") before you run out of sweets; keep the jar below the dotted line.
- Real physics (rolls, bumps, small bounce); next sweet shown; only small kinds drop, in a fixed order per level.
- From level 10 some levels start with sweets already in the jar.
- Hint: best spot for this sweet (plays the next 4 ahead). Rescue: more sweets (3-18) and, after an overflow, small sweets lifted out; up to 2 a level (DropScreen.cs:22).

### 13. Honey Hive — "Stack honey tiles, collect 10 of a colour" — hexa sort / hexagon stack
- Drag a stack from the tray (3 offered) onto an empty comb cell; same top colour next door hops over, chains can follow (HiveScreen.cs rules).
- 10+ of one colour on top are collected towards the goal; a full comb = stuck. No clock, no move limit. Dealt stacks fixed per level.
- New things: stacks already on the comb (5), locked cells opened by collecting (12), iced stacks (25) (plan :955-957).
- Comb 12-21 cells, 4-7 colours; levels about two minutes.
- Rescue: bees lift the most mixed-up stacks (2-6) off the comb, up to 2 a level (HiveScreen.cs:22). No cell is ever opened by an ad.

### 14. Fruit Tumble — "Tap groups of fruit to pop them" — tap-to-blast (collapse / blast style)
- Tap 2+ touching fruit of one kind; reach the goals before moves run out; a lone-fruit tap costs nothing (FruitScreen.cs rules; plan :1012).
- Specials: 5 = fizz rocket, 7 = coconut, 9 = blender; side by side they blast bigger.
- Obstacles: ice (4; frosted 20), jam jars to bring down (8), gaps (11), netted fruit (14).
- Move limit 14-38; fruit that drops is fixed per level (never rigged); 7x7 to 9x9 crate, 4-6 kinds each with its own shape.
- Rescue: +5 moves (FruitGame.cs:79), up to 2 a level. Free glow after 6 idle seconds.

### 15. Balloon Bunch — "Pop bunches of floating balloons" — tap-to-blast with floating physics
- Tap 2+ touching balloons of one colour; they float UP, new ones rise from below; reach the goals before moves run out (BalloonScreen.cs rules).
- 5+ make a firework (small/medium/big); fireworks that touch join into a bigger one; tap to pop around it.
- Obstacles: clouds (4; dark 14), tied balloons (8). Move limit 12-34 (plan :1086, 1093).
- 4-6 colours, each wears its own picture.
- Rescue: +5 moves (BalloonGame.cs:257), up to 2 a level.

### 16. Tide Pool — "Pop sea creatures before the tide rises" — rising-rows blast puzzle
- Tap 2+ touching creatures of one kind; every few taps the tide pushes a new row up from the bottom (shown waiting) (TideScreen.cs rules).
- Reach the goals before a column is pushed past the top. No clock: the tide comes by taps, not time.
- Waves: 5 = small (row), 7 = medium, 9 = big. Goals: collect creatures, ride out rows (4); rocks (8; mossy 20), seaweed (14).
- 4-6 kinds of creature, each its own shape.
- Rescue: the tide goes out, bottom 4 rows drain away (TideGame.cs:79), up to 2 a level.

### 17. Garland Tangle — "Untangle the strings of lights" — rope untangle / tangle puzzle
- Drag a lantern to an empty post (or tap lantern, then post): one move; a string crossing no other lights up; light them all before moves run out (RopeScreen.cs rules).
- Steel (nailed) lanterns can't move (from 8); boards with only one empty post (from 14).
- 6-11 posts, 4-10 lanterns, 3-13 strings; levels give 4-24 moves. No timer, no lives.
- Hint rings lantern and post; free hint after 6 idle seconds. Rescue: +4 moves (RopeGame.cs:51), up to 2 a level.

### 18. Bubble Picnic — "Aim, shoot and pop the bubbles" — bubble shooter
- Touch and slide to aim (dotted path shows bounces and landing spot), let go to shoot; 3+ of a colour pop, unattached bubbles fall (BubbleScreen.cs rules).
- Tap the two bubbles at the bottom to swap them (free). Clear 8+ in one shot for a rainbow bubble.
- Goals: clear every bubble, or free the stars (from 4); stone bubbles only fall (from 8). Out of bubbles = lost.
- No lives, no timer, no descending ceiling; 9 wide, up to 13 rows, 3-6 colours with white marks.
- Rescue: +5 bubbles (BubbleGame.cs:62), up to 2 a level.

### 19. Quilt Pins — "One pin in every patch, row and column" — logic grid (Star Battle / "Queens"-type)
- Put one pin in every patch, row and column; pins can't touch, even diagonally (QuiltScreen.cs rules).
- Tap once for a cross (note), twice for a pin; drag to cross many. A pin on a wrong square costs a heart; lose all 3 = stuck.
- Every quilt has one answer and is solved by thinking alone, no guessing (plan :476-477).
- Levels follow a ladder from a bank of 2,000 quilts (4x4 to 11x11): small boards in levels 1-10, then 8-10; harder thinking from
  levels 6, 21, 51; a hard spike every 10th level from 30; extra-big 11x11 "Boss" at 35, 45, 55... (AGENTS.md:99-108; plan :528-533).
- Hint: places the next pin that can be worked out and says why (QuiltScreen.cs:982). Take back: the last mistake, heart back.
  Rescue: +3 hearts (QuiltGame.cs:53), up to 2 a level. No visible clock.

### 20. Route Duel — "Clear routes, beat the rival" — the original game; turn-based route clearing duel
- Take turns with a computer rival; launch one route with a clear path; it scores its length in cells; most cells wins (RouteDuelController.cs:57-60).
- Careful: your launch can free routes for the rival; a blocked tap loses your turn. A level must be won to move on.
- Level 1 is a guided duel that can't be lost; then 340 picture boards (outlines of Google's Noto Emoji) in easy/medium/hard rounds,
  every 4th hard a boss, breathers after hard ones (AGENTS.md:28-29; RouteDuelController.cs:546-547).
- Solo Run (opens at level 6): clear a packed picture board alone before the clock runs out (about 4 s a route, never under 2 min);
  a blocked tap costs 5 s; once per run a rewarded ad adds 60 s (AGENTS.md:29-31; SoloRun.cs:12; RouteDuelProgress.cs:17, 195).
- Hint: glows your best route. Take back: undo your last move. Rescue after a loss: back a few moves against a "tired" (weaker) rival (RouteDuelController.cs:1036).
- The rival plays weaker or stronger to follow the player (AGENTS.md:120).

---------------------------------------------------------------------------------------------------
## C. Things the website must NOT claim
- Removed games: Ribbon Box (connect the dots), Pop Parade (pixel shooter), Stitch Hoop (picture logic / nonogram), Picnic Peaks
  (card solitaire, never shipped). Not in the app (JarProgress.cs:7-10, 163-202; plan :390, 747, 832, 1304).
- No card, word, number-puzzle (sudoku), or jigsaw games. Exactly 20 games, not 7 (old store texts and the Starter Pack card say 7).
- Never name other companies' games as ours or as "like X" (rule 4.3; AGENTS.md:13). Genre words are fine (screw puzzle, nut sort,
  bus jam, bubble shooter, match-3...). Avoid brand names used in research (Candy Crush, Hexa Sort, Bus Jam, Queens, etc.).
- Not: "no ads" (ads exist; removable), "no data collected / no tracking" (AdMob + ATT; Firebase on Android), "no in-app purchases".
- Not: cloud save, cross-device sync, accounts, leaderboards, multiplayer against real people (Route Duel's rival is the computer),
  Game Center, events/leagues, coins, lives/energy, iPad version, other app languages besides English.
- Not: "no timers anywhere" (Solo Run has a clock) or "no limits" (many games have move/piece limits; Quilt and Pencil have hearts).
- Not: "unlimited free hints" (hints are limited and sold); "free undo in every game" (3 free a level; unlimited only in Sweet Stacks
  or with Remove Ads).
- Not a specific level count like "4,200+" unless re-checked; use "thousands of levels".
- Not the old kite icon or the old purple board icon (AGENTS.md:131-150); the app icon is the purple-square glass jar of puzzle pieces.
- Not iPhone 2.1.2 / Android 2.1.2 features as live until the stores show them (in-app rating box).
- Never write the banned word (including inside the Android package name/Play URL in visible text).
