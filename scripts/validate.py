#!/usr/bin/env python3
"""Check catalogue structure and links with Python's standard library only."""
from pathlib import Path
import collections
import json
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
blank_ids = {key for key, kind, *_ in deck if kind in {"blank-status", "blank-event"}}
counts = collections.Counter()
for key, kind, copies, basis in deck:
    if not re.fullmatch(r"(?:ST|EV)-\d{3}", key):
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

event_numbers = [f"EV-{number:03}" for number in range(1, 332)]
event_deck = [record for record in deck if record[0].startswith("EV-")]
if [record[0] for record in event_deck] != event_numbers:
    errors.append("deck: event numbers must run in order from EV-001 through EV-331")
for key, kind, copies, _ in event_deck:
    if copies != "1":
        errors.append(f"deck: {key}: each physical event number must have exactly one copy")
    expected_kind = "final" if key == "EV-330" else "blank-event" if key == "EV-331" else "event"
    if kind != expected_kind:
        errors.append(f"deck: {key}: expected type {expected_kind}")
if blank_ids != {"EV-331", "ST-034"}:
    errors.append("deck: custom blanks must be EV-331 and ST-034")
if sum(counts[kind] for kind in ["event", "final", "blank-event"]) != 331:
    errors.append("deck: expected 331 physical events")
if sum(counts[kind] for kind in ["status", "blank-status"]) != 34:
    errors.append("deck: expected 34 physical statuses")

source = {}
source_records = {}
for category, prefix in [("events", "EV-"), ("statuses", "ST-")]:
    path = ROOT / f"game/ru/cards/{category}.md"
    records = rows(path, 3)
    source_records[category] = records
    source[category] = {r[0] for r in records}
    expected = {key for key in deck_ids if key.startswith(prefix)}
    if source[category] != expected:
        errors.append(f"{path.relative_to(ROOT)}: IDs differ from deck; missing={sorted(expected-source[category])}, extra={sorted(source[category]-expected)}")
    if category == "events" and [record[0] for record in records] != event_numbers:
        errors.append("ru/events: expected complete ascending EV-001–EV-331 order")
    for key, title, effect in records:
        if not title or (key not in blank_ids and not effect):
            errors.append(f"{path.relative_to(ROOT)}: missing Russian text for {key}")
    print(f"ru/{category}: {len(records)} records")

ru_events = {record[0]: record for record in source_records["events"]}
coffee_numbers = event_numbers[:30]
if all(key in ru_events for key in coffee_numbers):
    coffee = ru_events["EV-001"][1:]
    if coffee[0] != "Кофе" or any(ru_events[key][1:] != coffee for key in coffee_numbers):
        errors.append("ru/events: EV-001–EV-030 must be 30 identical Coffee copies")
if ru_events.get("EV-330", [None, None])[1] != "WAKE UP":
    errors.append("ru/events: EV-330 must be WAKE UP")

# The same physical numbers must identify the same effect and illustration.
art_path = ROOT / "design/event-illustration-ideas.ru.md"
art = rows(art_path, 4)
if [record[0] for record in art] != event_numbers:
    errors.append("illustrations: expected complete ascending EV-001–EV-331 order")
for key, title, effect, scene in art:
    if [key, title, effect] != ru_events.get(key):
        errors.append(f"illustrations: {key}: title/effect differs from Russian source")
    if key != "EV-331" and not scene:
        errors.append(f"illustrations: {key}: missing scene proposal")
coffee_art = [record[3] for record in art if record[0] in coffee_numbers]
if len(coffee_art) == 30 and len(set(coffee_art)) != 1:
    errors.append("illustrations: all 30 Coffee copies must share their scene")

try:
    number_map = json.loads((ROOT / "game/event-numbering.json").read_text(encoding="utf-8"))
    entries = number_map["entries"]
    legacy_ids = [entry["legacy_id"] for entry in entries]
    migrated_numbers = [number for entry in entries for number in entry["numbers"]]
    if len(set(legacy_ids)) != len(legacy_ids) or len(legacy_ids) != 302:
        errors.append("number map: expected 302 unique legacy records, including the blank")
    if sorted(migrated_numbers) != event_numbers:
        errors.append("number map: every physical number must have exactly one legacy origin")
    old_to_new = {entry["legacy_id"]: entry["numbers"] for entry in entries}
    if old_to_new.get("EV-143") != coffee_numbers or old_to_new.get("EV-311") != ["EV-330"] or old_to_new.get("EV-BLANK") != ["EV-331"]:
        errors.append("number map: Coffee, WAKE UP or blank mapping is inconsistent")
except (OSError, ValueError, KeyError, TypeError) as error:
    errors.append(f"number map: cannot read migration data: {error}")

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
        if category == "events" and [record[0] for record in records] != event_numbers:
            errors.append(f"{label}/events: expected complete ascending EV-001–EV-331 order")
        if category == "events" and label != "template" and all(records[i][1] and records[i][2] for i in range(min(30, len(records)))):
            if len({tuple(record[1:3]) for record in records[:30]}) != 1:
                errors.append(f"{label}/events: the 30 Coffee translations must match")
        translatable = [r for r in records if r[0] not in blank_ids]
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

print("Physical copy counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
print("Independent translation review, balance and print readiness are not validated.")
if errors:
    for error in errors:
        print("ERROR: " + error, file=sys.stderr)
    sys.exit(1)
print("OK: physical numbers, migration map, illustration correspondence, copy counts and local links are consistent.")
