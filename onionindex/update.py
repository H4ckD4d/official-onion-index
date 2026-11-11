"""Daily update: collect, validate, merge, write.

Usage:
    python -m onionindex.update                # live run over HTTPS
    python -m onionindex.update --fixtures DIR # offline run from saved pages
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from . import collectors, render
from .merge import merge

ROOT = Path(__file__).resolve().parent.parent


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text("utf-8")) or {}


def _today() -> str:
    return os.environ.get("ONIONINDEX_TODAY") or datetime.now(timezone.utc).date().isoformat()


def run(root: Path, fetcher, today: str) -> dict:
    config = _load_yaml(root / "config" / "sources.yml")
    manual = _load_yaml(root / "config" / "manual.yml").get("entries", [])
    accepted = _load_yaml(root / "config" / "overrides.yml").get("accept") or {}
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)

    index_path = data_dir / "onions.json"
    existing = json.loads(index_path.read_text("utf-8"))["entries"] if index_path.exists() else []

    observations: list[collectors.Observation] = []
    status: list[dict] = []

    def attempt(label: str, fn):
        try:
            found = fn()
            observations.extend(found)
            status.append({"source": label, "ok": True, "addresses": len(found)})
        except Exception as exc:  # a failing source must never wipe or block the index
            status.append({"source": label, "ok": False, "error": f"{type(exc).__name__}: {exc}"})

    attempt("manual", lambda: collectors.collect_manual(manual))
    for spec in config.get("official_lists", []):
        attempt(spec["name"], lambda spec=spec: collectors.collect_official_list(fetcher, spec))
    if config.get("securedrop"):
        attempt("SecureDrop directory", lambda: collectors.collect_securedrop(fetcher, config["securedrop"]))

    sites = [{"url": m["site"], "name": m["name"], "category": m["category"]} for m in manual]
    sites += config.get("onion_location", [])
    notes: list[str] = []

    def onion_location():
        found, site_notes = collectors.collect_onion_location(fetcher, sites)
        notes.extend(site_notes)
        return found

    attempt("Onion-Location", onion_location)

    entries, events, pending = merge(existing, observations, today, accepted)
    order = config.get("category_order", [])
    meta = {"maintainer": config["maintainer"], "repository": config["repository"]}

    index_path.write_text(render.to_json(entries, today, meta, order), "utf-8")
    (data_dir / "onions.csv").write_text(render.to_csv(entries, order), "utf-8")
    render.update_readme(root / "README.md", render.index_markdown(entries, today, order))
    render.update_changelog(root / "CHANGELOG.md", events, today)

    pending_path = data_dir / "pending.json"
    previous = json.loads(pending_path.read_text("utf-8")).get("pending", []) if pending_path.exists() else []
    pending_changed = bool(pending) and pending != previous
    pending_path.write_text(json.dumps({"generated": today, "pending": pending}, indent=2) + "\n", "utf-8")
    pending_md = data_dir / "pending.md"
    if pending:
        pending_md.write_text(render.pending_markdown(pending, today), "utf-8")
    else:
        pending_md.unlink(missing_ok=True)
    (data_dir / "status.json").write_text(
        json.dumps({"generated": today, "sources": status, "onion_location_notes": notes}, indent=2) + "\n", "utf-8")

    return {"entries": len(entries), "events": events, "pending": pending,
            "pending_changed": pending_changed, "status": status}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", help="directory of saved pages (offline run)")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)

    fetcher = collectors.FixtureFetcher(args.fixtures) if args.fixtures else collectors.HttpFetcher()
    result = run(Path(args.root), fetcher, _today())

    for s in result["status"]:
        state = f"ok, {s['addresses']} addresses" if s["ok"] else f"FAILED - {s['error']}"
        print(f"{s['source']}: {state}")
    print(f"index: {result['entries']} entries, {len(result['events'])} changes, "
          f"{len(result['pending'])} pending review")

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as fh:
            fh.write(f"pending_changed={'true' if result['pending_changed'] else 'false'}\n")

    if result["entries"] == 0:
        print("no entries collected", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
