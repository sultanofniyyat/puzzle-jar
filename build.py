#!/usr/bin/env python3
"""Builds the Puzzle Jar website into docs/ (served by GitHub Pages).

Standard library only.   python3 build.py          final build (strict: stops on any failed check)
                         python3 build.py --draft  preview build (reports problems, still builds)

  site.json       every app-wide fact ({{KEY}} tokens in pages)
  content/*.html  one file per page: front matter, then the body
  static/         copied as-is (style.css, img/)

A page body is: an opening <p class="answer"> (the page's short answer), then questions, each written as
<h2>Question?</h2> followed by its answer. Every <h2> ending in "?" counts as one question.

Checks (strict build stops):
  - unknown {{TOKEN}}, TODO in site.json, <!-- VERIFY --> notes left in a page
  - the same question asked twice anywhere on the site
  - two answers that are near copies of each other (shared 6-word runs)
  - banned words and removed-game names in visible text (see BANNED)
  - broken internal links and related-page names
"""
import datetime
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
DRAFT = "--draft" in sys.argv
TODAY = datetime.date.today().isoformat()

# Never shown anywhere on the site (whole words, any case). The first is the game's banned name word.
BANNED = [r"\barr" + r"ows?\b", r"ribbon box", r"pop parade", r"stitch hoop", r"picnic peaks", r"4,200",
          r"seven games", r"\b7 games", r"kite", r"\bsolitaire\b in puzzle jar"]
# Printed for a human check (allowed, but each use must be true).
REVIEW = [r"\bno ads\b", r"\bipad\b", r"\bcloud\b", r"multiplayer", r"leaderboard", r"\blives\b", r"\btimer",
          r"unlimited", r"\bnever\b", r"\balways\b", r"\bevery level\b", r"guarantee"]


def fail(msg):
    print("BUILD STOPPED:\n" + msg)
    sys.exit(1)


def load_site():
    data = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    site = {k: v for k, v in data.items() if not k.startswith("_")}
    site["SITE_URL"] = site["SITE_URL"].rstrip("/")
    site["YEAR"] = str(datetime.date.today().year)
    site["UPDATED"] = TODAY
    todo = [k for k, v in site.items() if "TODO" in str(v)]
    if todo and not DRAFT:
        fail("site.json values still contain TODO:\n  " + "\n  ".join(todo))
    return site


def parse_page(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    if not m:
        fail(f"{path.name}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    meta["body"] = m.group(2)
    meta["file"] = path.name
    meta["order"] = int(meta.get("order", "999"))
    meta["related"] = [s.strip() for s in meta.get("related", "").split(",") if s.strip()]
    for k in ("slug", "title", "description", "h1"):
        if k not in meta:
            fail(f"{path.name}: front matter needs '{k}'")
    if meta["slug"] == "index":
        meta["slug"] = ""
    return meta


def fill(text, site, where):
    def rep(m):
        key = m.group(1)
        if key not in site:
            fail(f"{where}: unknown token {{{{{key}}}}} (add it to site.json)")
        return str(site[key])
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", rep, text)


def plain(fragment):
    t = re.sub(r"<[^>]+>", " ", fragment)
    return " ".join(html.unescape(t).split())


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", plain(text).lower()).strip("-")
    return s[:70].rstrip("-")


def split_questions(body):
    """Returns (body with ids on every question heading, [(question, answer_html, id)])."""
    parts = re.split(r"(<h2[^>]*>.*?</h2>)", body, flags=re.S)
    pairs, used, out = [], set(), []
    for i, part in enumerate(parts):
        hm = re.match(r"<h2([^>]*)>(.*?)</h2>", part, re.S)
        if hm and plain(hm.group(2)).endswith("?"):
            idm = re.search(r'id="([^"]+)"', hm.group(1))
            qid = idm.group(1) if idm else slugify(hm.group(2))
            base, n = qid, 2
            while qid in used:
                qid, n = f"{base}-{n}", n + 1
            used.add(qid)
            ans = parts[i + 1] if i + 1 < len(parts) else ""
            pairs.append((plain(hm.group(2)), ans, qid))
            part = f'<h2 id="{qid}">{hm.group(2)}<a class="anchor" href="#{qid}" aria-label="Link to this question">#</a></h2>'
        out.append(part)
    return "".join(out), pairs


def page_url(site, p):
    return site["SITE_URL"] + "/" if p["slug"] == "" else f'{site["SITE_URL"]}/{p["slug"]}/'


def store_buttons(site):
    return ('<div class="stores">'
            f'<a class="badge" href="{html.escape(site["APPSTORE_URL"])}" rel="noopener">'
            '<img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" '
            'alt="Download Puzzle Jar on the App Store" width="150" height="50"></a>'
            f'<a class="badge" href="{html.escape(site["PLAY_URL"])}" rel="noopener">'
            '<img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" '
            'alt="Get Puzzle Jar on Google Play" width="194" height="75"></a></div>')


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def org(site):
    return {"@type": "Organization", "name": site["STUDIO"], "url": "https://sultanofniyyat.github.io/",
            "email": site["SUPPORT_EMAIL"]}


def game_schema(site):
    return {
        "@context": "https://schema.org",
        "@type": ["VideoGame", "MobileApplication"],
        "name": site["GAME_NAME"],
        "alternateName": [site["APPSTORE_NAME"], site["PLAY_NAME"], "Route Duel"],
        "description": f'{site["GAME_NAME"]} is {site["ONE_LINE"]}.',
        "url": site["SITE_URL"] + "/",
        "image": site["SITE_URL"] + "/img/icon.png",
        "applicationCategory": "GameApplication",
        "genre": ["Puzzle", "Casual", "Board"],
        "gamePlatform": ["iOS", "Android"],
        "operatingSystem": f'{site["MIN_IOS"]}; {site["MIN_ANDROID"]}',
        "author": org(site), "publisher": org(site),
        "sameAs": [site["APPSTORE_URL"], site["PLAY_URL"]],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "contentRating": site["AGE_RATING_SHORT"],
        "inLanguage": "en",
        "dateModified": TODAY,
    }


def nav(prefix):
    return (f'<nav class="menu"><a href="{prefix}#games">Games</a><a href="{prefix}#questions">Questions</a>'
            f'<a href="{prefix}about/">About</a><a href="{prefix}help/">Help</a></nav>')


def render(site, p, by_slug, games, topics):
    is_home = p["slug"] == ""
    prefix = "./" if is_home else "../"
    url = page_url(site, p)
    body = p["body_ids"]

    schemas = []
    if is_home:
        schemas.append({"@context": "https://schema.org", "@type": "WebSite", "name": site["GAME_NAME"],
                        "url": site["SITE_URL"] + "/", "publisher": org(site)})
        schemas.append(game_schema(site))
    else:
        schemas.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": site["GAME_NAME"], "item": site["SITE_URL"] + "/"},
            {"@type": "ListItem", "position": 2, "name": plain(p["h1"]), "item": url}]})
    if p["pairs"]:
        schemas.append({
            "@context": "https://schema.org", "@type": "FAQPage", "url": url, "dateModified": TODAY,
            "about": {"@type": "VideoGame", "name": site["GAME_NAME"], "url": site["SITE_URL"] + "/"},
            "mainEntity": [{"@type": "Question", "name": q, "url": f"{url}#{qid}",
                            "acceptedAnswer": {"@type": "Answer", "text": plain(a)[:1500]}}
                           for q, a, qid in p["pairs"]]})

    # Home: game grid and topic list
    if is_home:
        cards = []
        for g in games:
            img = f'<img src="img/games/{g["image"]}" alt="{html.escape(g["alt"])}" loading="lazy" width="210" height="456">' if g.get("image") else ""
            cards.append(f'<li><a href="{g["slug"]}/">{img}<strong>{html.escape(g.get("name", plain(g["h1"])))}</strong>'
                         f'<span>{html.escape(g.get("blurb", ""))}</span></a></li>')
        grid = '<h2 id="games" class="plain">The 20 games in the jar</h2><ul class="games">' + "".join(cards) + "</ul>"
        tl = "".join(f'<li><a href="{t["slug"]}/">{t["h1"]}</a> <span class="count">({len(t["pairs"])} questions)</span></li>' for t in topics)
        tlist = '<h2 id="questions" class="plain">Questions people ask</h2><ul class="qlist">' + tl + "</ul>"
        body = body.replace("<!--GAMES-->", grid).replace("<!--TOPICS-->", tlist)

    body = body.replace("<!--STORES-->", store_buttons(site))

    toc = ""
    if len(p["pairs"]) >= 4 and not is_home:
        toc = ('<details class="toc"><summary>On this page: ' + str(len(p["pairs"])) + ' questions</summary><ol>'
               + "".join(f'<li><a href="#{qid}">{html.escape(q)}</a></li>' for q, a, qid in p["pairs"]) + "</ol></details>")

    shot = ""
    if p.get("image") and not is_home:
        shot = (f'<figure class="shot"><img src="{prefix}img/games/{p["image"]}" alt="{html.escape(p.get("alt", ""))}" '
                f'width="210" height="456"><figcaption>{html.escape(p.get("caption", "A real screenshot from the game."))}</figcaption></figure>')

    related = ""
    if p["related"]:
        links = []
        for s in p["related"]:
            if s not in by_slug:
                if DRAFT:
                    continue
                fail(f'{p["file"]}: related page "{s}" does not exist')
            links.append(f'<li><a href="{prefix}{s}/">{by_slug[s]["h1"]}</a></li>')
        related = '<aside class="related"><h2 class="plain">Read next</h2><ul>' + "".join(links) + "</ul></aside>"

    crumbs = "" if is_home else (
        f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{prefix}">{html.escape(site["GAME_NAME"])}</a> '
        f'<span aria-hidden="true">›</span> <span>{p["h1"]}</span></nav>')
    byline = "" if is_home else (
        f'<p class="updated">By the {html.escape(site["STUDIO"])} team, who make {html.escape(site["GAME_NAME"])}. '
        f'Last updated <time datetime="{TODAY}">{TODAY}</time>.</p>')
    cta = "" if p.get("cta") == "no" else (
        f'<section class="cta"><p><strong>{html.escape(site["GAME_NAME"])}</strong>: {html.escape(site["TAGLINE"])}</p>'
        f'{store_buttons(site)}</section>')
    title = p["title"]
    desc = p["description"]
    lead = ""
    if not is_home:
        m = re.search(r'<p class="answer">.*?</p>', body, re.S)
        if m:
            lead, body = m.group(0), body.replace(m.group(0), "", 1)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="{site['GOOGLE_VERIFY']}">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{'website' if is_home else 'article'}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{html.escape(site['GAME_NAME'])}">
<meta property="og:image" content="{site['SITE_URL']}/img/{('games/' + p['image']) if p.get('image') else 'icon.png'}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{prefix}img/icon.png">
<link rel="stylesheet" href="{prefix}style.css?v={TODAY}">
{''.join(jsonld(s) for s in schemas)}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{prefix}"><img src="{prefix}img/icon.png" alt="" width="36" height="36"><span>{html.escape(site['GAME_NAME'])}</span></a>
{nav(prefix)}
</div></header>
<main class="wrap">
{crumbs}
<article>
<h1>{p['h1']}</h1>
{byline}
{lead}
{shot}
{toc}
{body}
</article>
{related}
{cta}
</main>
<footer class="foot"><div class="wrap">
<p>© {site['YEAR']} {html.escape(site['STUDIO'])}. {html.escape(site['GAME_NAME'])} is an independent game.
Other game names on this site belong to their owners; we are not connected to them.</p>
<p><a href="{prefix}about/">About us</a> · <a href="{prefix}help/">Help</a> · <a href="{html.escape(site['SUPPORT_URL'])}">Support</a> ·
<a href="{html.escape(site['PRIVACY_IOS_URL'])}">Privacy (iPhone)</a> · <a href="{html.escape(site['PRIVACY_ANDROID_URL'])}">Privacy (Android)</a> ·
<a href="mailto:{site['SUPPORT_EMAIL']}">{site['SUPPORT_EMAIL']}</a></p>
</div></footer>
</body>
</html>
"""


def shingles(text, n=6):
    w = re.findall(r"[a-z0-9']+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def main():
    site = load_site()
    pages = [parse_page(f) for f in sorted((ROOT / "content").glob("*.html"))]
    problems, notes = [], []
    for p in pages:
        for k in ("title", "description", "h1", "body", "alt", "caption", "blurb"):
            if k in p:
                p[k] = fill(p[k], site, p["file"])
        for n in re.findall(r"<!--\s*VERIFY:(.*?)-->", p["body"], re.S):
            notes.append(f'{p["file"]}: {" ".join(n.split())}')
        p["body"] = re.sub(r"\s*<!--\s*VERIFY:.*?-->", "", p["body"], flags=re.S)
        p["body_ids"], p["pairs"] = split_questions(p["body"])

    pages.sort(key=lambda p: p["order"])
    by_slug = {p["slug"]: p for p in pages if p["slug"]}
    games = [p for p in pages if p.get("group") == "game"]
    topics = [p for p in pages if p.get("group") == "topic"]

    # --- checks ---
    seen = {}
    for p in pages:
        for q, a, qid in p["pairs"]:
            key = re.sub(r"[^a-z0-9 ]", "", q.lower())
            if key in seen:
                problems.append(f'Question asked twice: "{q}" ({seen[key]} and {p["file"]})')
            seen[key] = p["file"]
            if len(plain(a).split()) < 12:
                problems.append(f'{p["file"]}: answer too short for "{q}"')
    allqa = [(p["file"], q, shingles(plain(a))) for p in pages for q, a, qid in p["pairs"]]
    for i in range(len(allqa)):
        for j in range(i + 1, len(allqa)):
            a, b = allqa[i][2], allqa[j][2]
            if a and b:
                share = len(a & b) / min(len(a), len(b))
                if share > 0.35:
                    problems.append(f'Near-copy answers ({share:.0%} shared): "{allqa[i][1]}" [{allqa[i][0]}] and "{allqa[j][1]}" [{allqa[j][0]}]')
    review = []
    for p in pages:
        visible = plain(" ".join([p["title"], p["description"], p["h1"], p["body"], p.get("alt", ""), p.get("caption", "")]))
        for pat in BANNED:
            for m in re.finditer(pat, visible, re.I):
                problems.append(f'{p["file"]}: banned text "{m.group(0)}"')
        for pat in REVIEW:
            for m in re.finditer(pat, visible, re.I):
                s = max(0, m.start() - 70)
                review.append(f'{p["file"]}: ...{visible[s:m.end() + 70]}...')
        for link in re.findall(r'href="\.\./([a-z0-9-]+)/', p["body"]):
            if link not in by_slug and not DRAFT:
                problems.append(f'{p["file"]}: link to missing page "{link}"')
        if len(p["description"]) > 165:
            problems.append(f'{p["file"]}: description longer than 165 characters')
    if notes:
        problems += ["Unchecked claim: " + n for n in notes]

    total = sum(len(p["pairs"]) for p in pages)
    (ROOT / "review.txt").write_text("\n".join(review) + "\n", encoding="utf-8")
    print(f"{len(pages)} pages, {total} questions. {len(review)} lines to review in review.txt.")
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems))
        if not DRAFT:
            sys.exit(1)

    # --- write ---
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "static", OUT, dirs_exist_ok=True)
    for p in pages:
        target = OUT / "404.html" if p["slug"] == "404" else (OUT / "index.html" if p["slug"] == "" else OUT / p["slug"] / "index.html")
        target.parent.mkdir(parents=True, exist_ok=True)
        out = render(site, p, by_slug, games, topics)
        if p["slug"] == "404":
            out = out.replace('href="../', f'href="{site["SITE_URL"]}/').replace('src="../', f'src="{site["SITE_URL"]}/')
        target.write_text(out, encoding="utf-8")

    urls = [p for p in pages if p["slug"] != "404"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{page_url(site, p)}</loc><lastmod>{TODAY}</lastmod></url>" for p in urls]
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    g = site["GAME_NAME"]
    llms = [f"# {g}", "", f"> {g} is {site['ONE_LINE']}. Made by {site['STUDIO']}.", "",
            f"- App Store: {site['APPSTORE_URL']}", f"- Google Play: {site['PLAY_URL']}", "", "## Pages", ""]
    full = [f"# {g}: every question and answer", "", f"Source: {site['SITE_URL']}/ (updated {TODAY})", ""]
    for p in urls:
        llms.append(f"- [{plain(p['h1'])}]({page_url(site, p)}): {plain(p['description'])}")
        full.append(f"## {plain(p['h1'])}\n\nURL: {page_url(site, p)}\n")
        m = re.search(r'<p class="answer">(.*?)</p>', p["body"], re.S)
        if m:
            full.append(plain(m.group(1)) + "\n")
        for q, a, qid in p["pairs"]:
            full.append(f"### {q}\n\n{plain(a)}\n")
    (OUT / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
    (OUT / "llms-full.txt").write_text("\n".join(full) + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    # Last guard: the banned word must not appear in any built file except inside the Google Play address.
    pat = re.compile(r"arr" + r"ow", re.I)
    for f in OUT.rglob("*"):
        if f.is_file() and f.suffix in (".html", ".txt", ".xml"):
            t = f.read_text(encoding="utf-8").replace(site["PLAY_URL"], "").replace(html.escape(site["PLAY_URL"]), "")
            if pat.search(t):
                fail(f"Banned word found in {f.relative_to(ROOT)}")
    print(f"Built into docs/ ({'DRAFT' if DRAFT else 'final'}).")


if __name__ == "__main__":
    main()
