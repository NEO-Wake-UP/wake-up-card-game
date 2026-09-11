#!/usr/bin/env python3
"""Check catalogue structure and links with Python's standard library only."""
from pathlib import Path
import collections
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def rows(path, expected_columns):
    result = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not re.match(r"\|\s*(?:EV|ST)-", line):
            continue
        fields = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(fields) != expected_columns:
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: expected {expected_columns} columns")
            continue
        result.append(fields)
    ids = [r[0] for r in result]
    for key, count in collections.Counter(ids).items():
        if count > 1:
            errors.append(f"{path.relative_to(ROOT)}: duplicate ID {key}")
    if not result:
        errors.append(f"{path.relative_to(ROOT)}: no card records")
    return result


deck = rows(ROOT / "game/deck.md", 4)
deck_ids = {r[0] for r in deck}
counts = collections.Counter()
for key, kind, copies, basis in deck:
    if not re.fullmatch(r"(?:ST-\d{3,}|EV-\d{3,}|EV-BLANK)", key):
        errors.append(f"deck: invalid ID {key}")
    valid_kinds = {"status", "blank-status"} if key.startswith("ST-") else {"event", "final", "blank-event"}
    if kind not in valid_kinds:
        errors.append(f"deck: {key}: invalid type {kind}")
    try:
        qty = int(copies)
        if qty <= 0:
            raise ValueError
        counts[kind] += qty
    except ValueError:
        errors.append(f"deck: {key}: copies must be a positive integer")

source = {}
for category, prefix in [("events", "EV-"), ("statuses", "ST-")]:
    path = ROOT / f"game/ru/cards/{category}.md"
    records = rows(path, 3)
    source[category] = {r[0] for r in records}
    expected = {key for key in deck_ids if key.startswith(prefix)}
    if source[category] != expected:
        errors.append(f"{path.relative_to(ROOT)}: IDs differ from deck; missing={sorted(expected-source[category])}, extra={sorted(source[category]-expected)}")
    for key, title, effect in records:
        if not title or (key not in {"ST-005", "EV-BLANK"} and not effect):
            errors.append(f"{path.relative_to(ROOT)}: missing Russian text for {key}")
    print(f"ru/{category}: {len(records)} records")

locales = sorted(p for p in (ROOT / "game").iterdir() if p.is_dir() and p.name != "ru")
worksheets = [(p / "cards", p.name) for p in locales]
worksheets.append((ROOT / "templates/translation/cards", "template"))
for directory, label in worksheets:
    for category in ["events", "statuses"]:
        path = directory / f"{category}.md"
        if not path.is_file():
            errors.append(f"{label}: missing {category}.md")
            continue
        records = rows(path, 4)
        actual = {r[0] for r in records}
        if actual != source[category]:
            errors.append(f"{path.relative_to(ROOT)}: IDs differ from Russian source; missing={sorted(source[category]-actual)}, extra={sorted(actual-source[category])}")
        translatable = [r for r in records if r[0] not in {"ST-005", "EV-BLANK"}]
        complete = sum(bool(r[1] and r[2]) for r in translatable)
        print(f"{label}/{category}: {complete}/{len(translatable)} title/effect pairs filled (not a review status)")

# Historical snapshots intentionally preserve their old references.
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts or "archive/2026-09-10" in path.as_posix():
        continue
    content = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        target = target.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        resolved = (path.parent / unquote(parsed.path)).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")

print("Provisional copy counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
print("Deck-size approval, translation review, balance and print readiness are not validated.")
if errors:
    for error in errors:
        print("ERROR: " + error, file=sys.stderr)
    sys.exit(1)
print("OK: IDs, table structure, copy counts and local file links are consistent.")
