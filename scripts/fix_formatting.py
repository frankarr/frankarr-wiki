#!/usr/bin/env python3
"""
frankarr-wiki formatting fixes
Instinct audit — 25 Oct 2026 | Fix run — 26 Oct 2026

Fixes applied (all mechanical, prose preserved):
1. Mojibake: UTF-8 bytes mis-decoded as Latin-1/Windows-1252 → re-encode
2. Bad dates: recover from source_url path or body date line
3. Untitled Blogspot posts: extract real title from first body line
4. Chrome strip: remove comment/trackback/copyright footers
5. Tag deduplication: normalise case, remove exact dupes

Run dry: python3 fix_formatting.py --dry-run
Run live: python3 fix_formatting.py
"""

import os
import re
import sys
import argparse
from pathlib import Path

REPO = Path(__file__).parent.parent
POSTS = REPO / "content" / "posts"

DRY_RUN = False

stats = {
    "mojibake_fixed": 0,
    "dates_fixed": 0,
    "titles_fixed": 0,
    "chrome_stripped": 0,
    "tags_deduped": 0,
    "files_changed": 0,
    "files_scanned": 0,
}


# ---------------------------------------------------------------------------
# 1. Mojibake fix
#    Pattern: UTF-8 multibyte sequences were decoded as Latin-1 then stored.
#    Re-encoding: read raw bytes, try to fix mojibake by latin1→utf8 repair.
# ---------------------------------------------------------------------------

MOJIBAKE_PATTERN = re.compile(
    r'[\xc2-\xc3][\x80-\xbf]|'   # 2-byte UTF-8 stored as 2 latin1 chars
    r'â€™|â€œ|â€|â€™|â\x80\x99|â\x80\x9c|â\x80\x9d|â\x80\x93|â\x80\x94|â\x80¦'
)

def fix_mojibake(text: str) -> tuple[str, bool]:
    """Attempt to fix mojibake by re-encoding latin1→utf8."""
    if not MOJIBAKE_PATTERN.search(text):
        return text, False
    try:
        fixed = text.encode("latin-1").decode("utf-8")
        return fixed, True
    except (UnicodeDecodeError, UnicodeEncodeError):
        # Partial mojibake — fix known sequences manually
        replacements = [
            ("â\x80\x99", "'"),
            ("â\x80\x9c", "\u201c"),
            ("â\x80\x9d", "\u201d"),
            ("â\x80\x93", "\u2013"),
            ("â\x80\x94", "\u2014"),
            ("â\x80¦", "\u2026"),
            ("â€™", "'"),
            ("â€œ", "\u201c"),
            ("â€", "\u201d"),
            ("Ã©", "é"),
            ("Ã¨", "è"),
            ("Ã ", "à"),
            ("Ã¢", "â"),
            ("Ã´", "ô"),
            ("Ã¹", "ù"),
            ("Ã»", "û"),
            ("Ã§", "ç"),
            ("Ã«", "ë"),
            ("Ã®", "î"),
            ("Ã¯", "ï"),
            ("Ã¶", "ö"),
            ("Ã¼", "ü"),
            ("Ã±", "ñ"),
        ]
        changed = False
        for bad, good in replacements:
            if bad in text:
                text = text.replace(bad, good)
                changed = True
        return text, changed


# ---------------------------------------------------------------------------
# 2. Date recovery
#    - "Saturday, " → extract from source_url or body date line
#    - Missing date → try source_url
# ---------------------------------------------------------------------------

URL_DATE_RE = re.compile(r'/(\d{4})/(\d{2})(?:/(\d{2}))?')
BODY_DATE_RE = re.compile(
    r'(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\s+'
    r'(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})'
)
MONTH_MAP = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

def recover_date(frontmatter: dict, body: str) -> tuple[str | None, str]:
    """Return (recovered_date_str, method) or (None, '')."""
    source_url = frontmatter.get("source_url", "")
    
    # Try source_url first
    m = URL_DATE_RE.search(source_url)
    if m:
        y, mo = m.group(1), m.group(2)
        day = m.group(3) or "01"
        return f"{y}-{mo}-{day}", "source_url"
    
    # Try body date line
    m = BODY_DATE_RE.search(body[:500])
    if m:
        day = m.group(1).zfill(2)
        mo = MONTH_MAP[m.group(2)]
        y = m.group(3)
        return f"{y}-{mo}-{day}", "body"
    
    return None, ""

BAD_DATE_RE = re.compile(r'^(Saturday|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday),?\s*$')

def needs_date_fix(date_val: str) -> bool:
    if not date_val:
        return True
    if BAD_DATE_RE.match(date_val.strip()):
        return True
    # Import date pattern (2026-10-25 = today-ish)
    if date_val.startswith("2026-10-") or date_val.startswith("2026-09-"):
        return False  # could be genuine
    return False


# ---------------------------------------------------------------------------
# 3. Untitled Blogspot → extract title from first body line
# ---------------------------------------------------------------------------

def fix_untitled(frontmatter: dict, body: str) -> tuple[str | None, str]:
    """Return (new_title, method) or (None, '')."""
    title = frontmatter.get("title", "")
    if title.strip().lower() not in ("untitled", '""', ""):
        return None, ""
    # First non-empty line of body that isn't a date line
    for line in body.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Skip lines that look like date lines
        if BODY_DATE_RE.match(line):
            continue
        # Skip scraped chrome
        if line.startswith("comment [") or line.startswith("©"):
            continue
        # Stop at first sentence break, cap at 80 chars
        for sep in (".", "!", "?", " - ", " – "):
            idx = line.find(sep)
            if 0 < idx < 80:
                line = line[:idx + (1 if sep in ".\'!?" else 0)].strip()
                break
        if len(line) > 80:
            line = line[:77] + "..."
        return line, "body_first_line"
    return None, ""


# ---------------------------------------------------------------------------
# 4. Chrome strip — comment/trackback/copyright footers
# ---------------------------------------------------------------------------

CHROME_PATTERNS = [
    re.compile(r'comment\s*\[\s*\]\s*trackback\s*\[\s*\].*?(?=\n|$)', re.IGNORECASE),
    re.compile(r'G!\s+Geek\b', re.IGNORECASE),
    re.compile(r'©\s*Copyright\s+\d{4}\s+Frank Arrigo\.?.*?(?=\n|$)', re.IGNORECASE),
    re.compile(r'A Geek Microsoft Blogger\s*Last update:.*?(?=\n|$)', re.IGNORECASE),
    re.compile(r'Last updated on \d{4}-\d{2}-\d{2}\s*$', re.MULTILINE),
    re.compile(r'Additional resources\s*$', re.MULTILINE),
]

def strip_chrome(body: str) -> tuple[str, bool]:
    changed = False
    for pat in CHROME_PATTERNS:
        new = pat.sub("", body)
        if new != body:
            body = new
            changed = True
    # Clean up multiple trailing newlines
    body = re.sub(r'\n{3,}', '\n\n', body).rstrip() + "\n"
    return body, changed


# ---------------------------------------------------------------------------
# 5. Tag deduplication
# ---------------------------------------------------------------------------

def dedup_tags(tags_val: str | list) -> tuple[list, bool]:
    if isinstance(tags_val, str):
        tags = [t.strip().strip('"').strip("'") for t in tags_val.split(",")]
    elif isinstance(tags_val, list):
        tags = [str(t).strip() for t in tags_val]
    else:
        return [], False
    
    seen = {}
    for t in tags:
        key = t.lower()
        if key not in seen and t:
            seen[key] = t
    
    deduped = list(seen.values())
    changed = len(deduped) != len([t for t in tags if t])
    return deduped, changed


# ---------------------------------------------------------------------------
# Frontmatter parser (simple — no yaml dep needed for this structure)
# ---------------------------------------------------------------------------

def parse_file(path: Path) -> tuple[str, dict, str]:
    """Return (raw_text, frontmatter_dict, body)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return text, {}, text
    
    end = text.find("\n---", 3)
    if end == -1:
        return text, {}, text
    
    fm_raw = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    
    return text, fm, body


def rebuild_file(fm_raw_block: str, body: str) -> str:
    return f"---\n{fm_raw_block}\n---\n\n{body}"


def update_frontmatter_field(fm_raw: str, key: str, value: str) -> str:
    """Replace a field value in the raw frontmatter string."""
    pat = re.compile(rf'^({re.escape(key)}:\s*).*$', re.MULTILINE)
    replacement = f'{key}: "{value}"'
    if pat.search(fm_raw):
        return pat.sub(replacement, fm_raw)
    else:
        return fm_raw + f'\n{key}: "{value}"'


def update_tags_field(fm_raw: str, tags: list) -> str:
    """Replace tags field. Quartz uses: tags: ["a", "b"]"""
    tags_str = "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    pat = re.compile(r'^tags:.*$', re.MULTILINE | re.DOTALL)
    # Simple single-line tags replacement
    single = re.compile(r'^tags:.*$', re.MULTILINE)
    if single.search(fm_raw):
        return single.sub(f"tags: {tags_str}", fm_raw)
    return fm_raw + f'\ntags: {tags_str}'


# ---------------------------------------------------------------------------
# Main processing loop
# ---------------------------------------------------------------------------

def process_file(path: Path) -> bool:
    """Process one file. Returns True if changed."""
    stats["files_scanned"] += 1
    
    raw_text, fm, body = parse_file(path)
    
    # Extract raw frontmatter block for targeted edits
    if raw_text.startswith("---"):
        end = raw_text.find("\n---", 3)
        fm_raw = raw_text[3:end].strip()
    else:
        fm_raw = ""
    
    changed = False
    new_fm_raw = fm_raw
    new_body = body

    # --- 1. Mojibake ---
    fixed_text, moji_changed = fix_mojibake(raw_text)
    if moji_changed:
        stats["mojibake_fixed"] += 1
        # Re-parse after fix
        _, fm, body = parse_file.__wrapped__(fixed_text) if hasattr(parse_file, '__wrapped__') else _reparse(fixed_text)
        raw_text = fixed_text
        if raw_text.startswith("---"):
            end = raw_text.find("\n---", 3)
            new_fm_raw = raw_text[3:end].strip()
            new_body = raw_text[end + 4:].lstrip("\n")
        changed = True

    # --- 2. Bad dates ---
    date_val = fm.get("date", "")
    if needs_date_fix(date_val):
        recovered, method = recover_date(fm, new_body)
        if recovered:
            new_fm_raw = update_frontmatter_field(new_fm_raw, "date", recovered)
            stats["dates_fixed"] += 1
            changed = True

    # --- 3. Untitled ---
    new_title, title_method = fix_untitled(fm, new_body)
    if new_title:
        new_fm_raw = update_frontmatter_field(new_fm_raw, "title", new_title.replace('"', '\\"'))
        stats["titles_fixed"] += 1
        changed = True

    # --- 4. Chrome strip ---
    stripped_body, chrome_changed = strip_chrome(new_body)
    if chrome_changed:
        new_body = stripped_body
        stats["chrome_stripped"] += 1
        changed = True

    # --- 5. Tag dedup ---
    tags_val = fm.get("tags", "")
    if tags_val:
        deduped, tags_changed = dedup_tags(tags_val)
        if tags_changed:
            new_fm_raw = update_tags_field(new_fm_raw, deduped)
            stats["tags_deduped"] += 1
            changed = True

    if not changed:
        return False

    stats["files_changed"] += 1
    if not DRY_RUN:
        new_content = f"---\n{new_fm_raw}\n---\n\n{new_body}"
        path.write_text(new_content, encoding="utf-8")

    return True


def _reparse(text: str) -> tuple[str, dict, str]:
    if not text.startswith("---"):
        return text, {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return text, {}, text
    fm_raw = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return text, fm, body


def main():
    global DRY_RUN
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--platform", help="Only process this platform (e.g. msdn, blogspot)")
    args = parser.parse_args()
    DRY_RUN = args.dry_run

    if DRY_RUN:
        print("=== DRY RUN — no files will be written ===\n")

    # Collect files
    if args.platform:
        dirs = [POSTS / args.platform]
    else:
        dirs = [d for d in POSTS.iterdir() if d.is_dir()]

    all_files = []
    for d in dirs:
        all_files.extend(d.rglob("*.md"))

    print(f"Scanning {len(all_files)} files across {len(dirs)} platform(s)...\n")

    changed_files = []
    for path in sorted(all_files):
        if path.name == "_index.md":
            continue
        try:
            if process_file(path):
                changed_files.append(path)
        except Exception as e:
            print(f"ERROR {path}: {e}")

    print(f"\n=== Results {'(DRY RUN)' if DRY_RUN else ''} ===")
    print(f"Files scanned:      {stats['files_scanned']}")
    print(f"Files changed:      {stats['files_changed']}")
    print(f"  Mojibake fixed:   {stats['mojibake_fixed']}")
    print(f"  Dates recovered:  {stats['dates_fixed']}")
    print(f"  Titles fixed:     {stats['titles_fixed']}")
    print(f"  Chrome stripped:  {stats['chrome_stripped']}")
    print(f"  Tags deduped:     {stats['tags_deduped']}")

    if DRY_RUN and changed_files:
        print(f"\nFirst 20 files that would change:")
        for f in changed_files[:20]:
            print(f"  {f.relative_to(REPO)}")


if __name__ == "__main__":
    main()
