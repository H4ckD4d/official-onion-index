import csv
import io
import json

from onionindex import render
from onionindex.collectors import FixtureFetcher
from onionindex.update import run


def test_full_run_writes_all_outputs(project):
    root, addr = project["root"], project["addr"]
    result = run(root, FixtureFetcher(project["fixtures"]), "2026-11-11")

    doc = json.loads((root / "data" / "onions.json").read_text("utf-8"))
    by_service = {e["service"]: e for e in doc["entries"]}
    assert doc["maintainer"] == "h4ckd4d project"
    assert set(by_service) == {"search.example.com", "news.example.com", "blog.example.org",
                               "www.example.org", "securedrop:the-example-times"}
    # manual entry confirmed by the site's own <meta> tag is upgraded to machine evidence
    search = by_service["search.example.com"]
    assert search["onion"] == addr["search"]
    assert [s["kind"] for s in search["sources"]] == ["onion-location", "manual"]
    assert search["last_verified"] == "2026-11-11"

    rows = list(csv.DictReader(io.StringIO((root / "data" / "onions.csv").read_text("utf-8"))))
    assert len(rows) == 5 and rows[0]["category"] == "Search engines"

    readme = (root / "README.md").read_text("utf-8")
    assert "**5 addresses**" in readme and addr["blog"] in readme and readme.rstrip().endswith("footer")
    assert "## 2026-11-11" in (root / "CHANGELOG.md").read_text("utf-8")
    assert result["pending"] == [] and result["pending_changed"] is False
    assert all(s["ok"] for s in result["status"])


def test_second_run_is_idempotent_and_flags_a_changed_address(project, onion):
    root = project["root"]
    run(root, FixtureFetcher(project["fixtures"]), "2026-11-11")
    readme_before = (root / "README.md").read_text("utf-8")
    run(root, FixtureFetcher(project["fixtures"]), "2026-11-11")
    assert (root / "README.md").read_text("utf-8") == readme_before
    assert (root / "CHANGELOG.md").read_text("utf-8").count("## 2026-11-11") == 1

    # the news site now announces a different address
    manifest = dict(project["manifest"])
    manifest["https://news.example.com/"] = {"file": "plain.html",
                                             "headers": {"Onion-Location": f"http://{onion('evil')}/"}}
    (project["fixtures"] / "manifest.json").write_text(json.dumps(manifest), "utf-8")
    result = run(root, FixtureFetcher(project["fixtures"]), "2026-11-12")

    doc = json.loads((root / "data" / "onions.json").read_text("utf-8"))
    news = next(e for e in doc["entries"] if e["service"] == "news.example.com")
    assert news["onion"] == project["addr"]["news"]          # unchanged
    assert news["last_verified"] == "2026-11-11"             # not re-confirmed
    assert result["pending_changed"] is True
    assert onion("evil") in (root / "data" / "pending.md").read_text("utf-8")

    # same mismatch on the next day is not reported as new
    assert run(root, FixtureFetcher(project["fixtures"]), "2026-11-13")["pending_changed"] is False


def test_failed_source_never_removes_entries(project):
    root = project["root"]
    run(root, FixtureFetcher(project["fixtures"]), "2026-11-11")
    manifest = dict(project["manifest"])
    del manifest["https://onion.example.org/"]
    (project["fixtures"] / "manifest.json").write_text(json.dumps(manifest), "utf-8")
    result = run(root, FixtureFetcher(project["fixtures"]), "2026-11-12")
    assert result["entries"] == 5
    assert any(not s["ok"] for s in result["status"])


def test_stale_marker():
    entry = {"last_verified": "2026-10-01"}
    assert render.is_stale(entry, "2026-11-11")
    assert not render.is_stale({"last_verified": "2026-11-05"}, "2026-11-11")
