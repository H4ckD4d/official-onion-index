"""Write the index to JSON, CSV, the README tables and the changelog."""

from __future__ import annotations

import csv
import io
import json
from datetime import date
from pathlib import Path

BEGIN = "<!-- BEGIN:INDEX (generated, do not edit by hand) -->"
END = "<!-- END:INDEX -->"
STALE_AFTER_DAYS = 14

EVIDENCE_LABEL = {
    "onion-location": "Onion-Location",
    "official-list": "Official list",
    "directory": "SecureDrop directory",
    "manual": "Checked by hand",
}


def _sorted(entries: list[dict], category_order: list[str]) -> list[dict]:
    rank = {c: i for i, c in enumerate(category_order)}
    return sorted(entries, key=lambda e: (rank.get(e["category"], len(rank)), e["category"], e["name"].lower()))


def is_stale(entry: dict, today: str) -> bool:
    try:
        return (date.fromisoformat(today) - date.fromisoformat(entry["last_verified"])).days > STALE_AFTER_DAYS
    except ValueError:
        return True


def to_json(entries: list[dict], today: str, meta: dict, category_order: list[str]) -> str:
    doc = {
        "name": "official-onion-index",
        "maintainer": meta["maintainer"],
        "repository": meta["repository"],
        "license": "CC BY 4.0",
        "generated": today,
        "count": len(entries),
        "entries": _sorted(entries, category_order),
    }
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def to_csv(entries: list[dict], category_order: list[str]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["category", "name", "service", "onion", "evidence", "source_url", "first_seen", "last_verified"])
    for e in _sorted(entries, category_order):
        src = e["sources"][0]
        w.writerow([e["category"], e["name"], e["service"], e["onion"], src["kind"], src["url"],
                    e["first_seen"], e["last_verified"]])
    return buf.getvalue()


def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def index_markdown(entries: list[dict], today: str, category_order: list[str]) -> str:
    entries = _sorted(entries, category_order)
    fresh = sum(1 for e in entries
                if e["last_verified"] == today and any(s["kind"] != "manual" for s in e["sources"]))
    lines = [
        BEGIN, "",
        f"**{len(entries)} addresses** &middot; last run **{today}** (UTC) &middot; "
        f"{fresh} confirmed against a live source on this date", "",
    ]
    category = None
    for e in entries:
        if e["category"] != category:
            category = e["category"]
            lines += ["", f"### {category}", "",
                      "| Service | Onion address | Evidence | Last verified |",
                      "|---|---|---|---|"]
        evidence = ", ".join(
            f"[{EVIDENCE_LABEL.get(s['kind'], s['kind'])}]({s['url']})" for s in e["sources"]
        )
        verified = e["last_verified"] + (" (stale)" if is_stale(e, today) else "")
        lines.append(f"| {_cell(e['name'])} | `{e['onion']}` | {evidence} | {verified} |")
    lines += ["", END]
    return "\n".join(lines)


def update_readme(path: Path, block: str) -> None:
    text = path.read_text("utf-8")
    start, end = text.find(BEGIN), text.find(END)
    if start == -1 or end == -1:
        raise ValueError(f"{path} is missing the index markers")
    path.write_text(text[:start] + block + text[end + len(END):], "utf-8")


def changelog_section(events: list[dict], today: str) -> str:
    lines = [f"## {today}", ""]
    for ev in events:
        if ev["type"] == "added":
            lines.append(f"- Added **{ev['name']}**: `{ev['onion']}`")
        elif ev["type"] == "changed":
            lines.append(f"- Changed **{ev['name']}**: `{ev['old']}` -> `{ev['onion']}` (approved by the maintainer)")
    return "\n".join(lines) + "\n"


def update_changelog(path: Path, events: list[dict], today: str) -> None:
    if not events:
        return
    header = "# Changelog\n\nAddresses added to or changed in the index. Daily re-verification is not listed here.\n\n"
    body = path.read_text("utf-8") if path.exists() else header
    if not body.startswith("# Changelog"):
        body = header + body
    head, _, rest = body.partition("\n## ")
    rest = ("## " + rest) if rest else ""
    path.write_text(head.rstrip("\n") + "\n\n" + changelog_section(events, today) + ("\n" + rest if rest else ""), "utf-8")


def pending_markdown(pending: list[dict], today: str) -> str:
    lines = [
        f"The daily run of {today} found addresses that do not match the accepted index.",
        "Nothing was changed automatically. Please check each source by hand.", "",
    ]
    for p in pending:
        lines.append(f"### {p['name']} (`{p['service']}`)")
        lines.append(f"- Reason: {p['reason']}")
        lines.append(f"- Accepted address: `{p['current']}`" if p["current"] else "- Accepted address: none yet")
        for onion in p["observed"]:
            lines.append(f"- Observed address: `{onion}`")
        for s in p["sources"]:
            lines.append(f"- Source: [{s['name']}]({s['url']})")
        lines.append("")
    lines.append("To accept a change, add `service: new-address` under `accept:` in `config/overrides.yml`.")
    return "\n".join(lines) + "\n"
