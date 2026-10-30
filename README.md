# frankarr-wiki

**Frank Arrigo — Digital Archive Wiki (2003–2026)**

A public archive of everything Frank Arrigo wrote across the web over 40+ years in Australian technology. 4,000+ posts. One place.

🌐 **[wiki.frankarr.com](https://wiki.frankarr.com)**

---

## What It Is

A searchable, browsable digital archive spanning Frank's entire writing life — from early blogging on Radio UserLand in 2003 through to frankarr.com in 2026. Built as a [Quartz](https://quartz.jzhao.xyz) digital garden, hosted on Cloudflare Pages.

---

## Sources

Each platform was scraped, cleaned, and converted to Markdown with consistent frontmatter (`title`, `date`, `platform`, `era`, `source_url`, `tags`).

| Platform | Posts | Span | Where found |
|----------|------:|------|-------------|
| [MSDN Blog](https://learn.microsoft.com/en-us/archive/blogs/frankarr/) | 1,709 | 2003–2013 | Microsoft Learn archive (`learn.microsoft.com/en-us/archive/blogs/frankarr/`) |
| [Radio UserLand](http://radio-weblogs.com/0124955/) | 1,421 | 2003–2008 | radio-weblogs.com — original blog host, still live |
| [Blogspot](https://frankarr.blogspot.com) | 117 | 2003–2008 | frankarr.blogspot.com |
| [frankarr.com](https://frankarr.com) | 744 | 2011–2026 | frankarr.com WordPress export |
| [LinkedIn Articles](https://www.linkedin.com/in/frankarr/) | 18 | 2017–2022 | LinkedIn Pulse (`linkedin.com/pulse/`) |

Posts are organised under `content/posts/<platform>/` with one `.md` file per post.

---

## Tools & Process

### Stack

- **[Quartz v5](https://quartz.jzhao.xyz)** — static site generator for digital gardens and wikis. Handles Markdown → HTML, full-text search, graph view, backlinks, and tag pages.
- **[Cloudflare Pages](https://pages.cloudflare.com)** — hosting and deployment. Auto-deploys on push to `main`.
- **Python 3** — all scraping, cleaning, and frontmatter generation.
- **GitHub Actions** — CI/CD pipeline (`ci.yaml` + `deploy-v5.yaml`).

### How Each Source Was Processed

**MSDN Blog**
Scraped from the Microsoft Learn archive at `learn.microsoft.com/en-us/archive/blogs/frankarr/`. The archive preserves post URLs in their original form (`/frankarr/<slug>`). Frontmatter `source_url` links back to the live archive page.

**Radio UserLand**
Fetched from `radio-weblogs.com/0124955/` — the original Radio UserLand host, which still serves Frank's posts at their original URLs. Posts include original tags (Technorati-era categories).

**Blogspot**
Scraped from `frankarr.blogspot.com`. Some posts had encoding issues (UTF-8 bytes stored as Latin-1) and missing or malformed dates — both fixed in the cleaning pass.

**frankarr.com**
Exported from the WordPress installation via WP export XML, then converted to Markdown. Post URLs preserved as `source_url`.

**LinkedIn Articles**
Scraped from LinkedIn Pulse (`linkedin.com/pulse/`). LinkedIn does not expose article content via API; articles were fetched from their public Pulse URLs.

### Cleaning (`scripts/fix_formatting.py`)

After initial scrape, a formatting pass was run across all 3,975+ files to fix:

1. **Mojibake** — UTF-8 multibyte sequences mis-decoded as Latin-1/Windows-1252, re-encoded to correct Unicode
2. **Bad dates** — malformed or missing dates recovered from `source_url` path or body date lines
3. **Untitled posts** — Blogspot posts with no frontmatter title had the real title extracted from the first body line
4. **Chrome footers** — comment counts, trackback sections, and copyright boilerplate stripped
5. **Tag deduplication** — tags normalised for case and exact duplicates removed

Run dry: `python3 scripts/fix_formatting.py --dry-run`
Run live: `python3 scripts/fix_formatting.py`
Run one platform: `python3 scripts/fix_formatting.py --platform msdn`

### Deployment

Push to `main` → GitHub Actions builds Quartz → deploys to Cloudflare Pages → live at `wiki.frankarr.com`.

---

## Browse by Era

Posts are also tagged by career era:

| Era | Years | Context |
|-----|-------|---------|
| Aspect Computing | 1984–1991 | Pre-internet. Mainframes, minis, PCs. |
| Microsoft | 1991–2014 | 23 years. .NET, TechEd, evangelism, Redmond. |
| Telstra | 2014–2018 | APIs, muru-D, startups, developer relations. |
| Amazon Web Services | 2018–2024 | ANZ Solutions Architecture. |
| Now | 2024– | SmallBizAI.au. Career break. London. |

---

*Built by [Claw 🦞](https://smallbizai.au)*
