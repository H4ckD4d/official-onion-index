import base64
import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def make_onion(seed: str) -> str:
    """Build a checksum-valid v3 onion host from a seed (test data only)."""
    pubkey = hashlib.sha256(seed.encode()).digest()
    version = b"\x03"
    checksum = hashlib.sha3_256(b".onion checksum" + pubkey + version).digest()[:2]
    return base64.b32encode(pubkey + checksum + version).decode().lower() + ".onion"


@pytest.fixture
def onion():
    return make_onion


OFFICIAL_LIST = """
<p>This is a list of <a href="https://community.example.org/onion-services/">onion services</a>
run by <a href="https://www.example.org/">Example</a>.</p>
<ul>
<li><strong><a href="https://blog.example.org">blog.example.org</a></strong>
  <ul><li><a href="http://{blog}/">http://{blog}/</a></li></ul></li>
<li><strong><a href="https://grafana.example.org">grafana.example.org</a></strong>
  <ul><li><a href="http://{grafana}/">http://{grafana}/</a></li></ul></li>
<li><strong><a href="https://www.example.org">www.example.org</a></strong>
  <ul><li><a href="http://{www}/">http://{www}/</a></li></ul></li>
</ul>
<pre>deb tor+http://{apt}/debian stable main</pre>
<h2>Legacy adresses</h2>
<ul>
<li><strong><a href="https://git.example.org">git.example.org</a></strong>
  <ul><li>http://{legacy}/</li></ul></li>
<li><strong><a href="https://old.example.org">old.example.org</a></strong>
  <ul><li>http://expyuzz4wqqyqhjn.onion/</li></ul></li>
</ul>
"""


@pytest.fixture
def project(tmp_path, onion):
    """A miniature repository with config, README markers and saved pages."""
    root = tmp_path / "repo"
    (root / "config").mkdir(parents=True)
    fixtures = tmp_path / "fixtures"
    fixtures.mkdir()

    addr = {k: onion(k) for k in ["blog", "grafana", "www", "apt", "legacy", "news", "search", "drop"]}

    (root / "README.md").write_text(
        "# Test\n\n<!-- BEGIN:INDEX (generated, do not edit by hand) -->\n<!-- END:INDEX -->\n\nfooter\n", "utf-8")
    (root / "config" / "sources.yml").write_text(json.dumps({
        "maintainer": "h4ckd4d project",
        "repository": "https://github.com/H4ckD4d/official-onion-index",
        "category_order": ["Search engines", "News", "Example", "SecureDrop tip lines"],
        "official_lists": [{"name": "Example", "url": "https://onion.example.org/", "category": "Example",
                            "stop_at": "Legacy", "exclude": ["^grafana"]}],
        "securedrop": {"url": "https://securedrop.example/api/", "category": "SecureDrop tip lines"},
        "onion_location": [
            {"url": "https://news.example.com/", "name": "Example News", "category": "News"},
            {"url": "https://silent.example.com/", "name": "Silent", "category": "News"},
            {"url": "https://down.example.com/", "name": "Down", "category": "News"},
        ],
    }), "utf-8")  # JSON is valid YAML
    (root / "config" / "manual.yml").write_text(json.dumps({"entries": [{
        "name": "Example Search", "category": "Search engines", "site": "https://search.example.com/",
        "onion": addr["search"], "proof_url": "https://search.example.com/tor", "verified": "2026-01-02",
    }]}), "utf-8")
    (root / "config" / "overrides.yml").write_text("accept: {}\n", "utf-8")

    (fixtures / "list.html").write_text(OFFICIAL_LIST.format(**addr), "utf-8")
    (fixtures / "drop.json").write_text(json.dumps([
        {"title": "The Example Times", "onion_address": addr["drop"],
         "landing_page_url": "https://times.example.com/securedrop/"},
        {"title": "Broken Entry", "onion_address": "not-an-onion", "landing_page_url": "https://x.example/"},
    ]), "utf-8")
    (fixtures / "meta.html").write_text(
        f'<html><head><meta http-equiv="onion-location" content="http://{addr["search"]}/en/"></head></html>', "utf-8")
    (fixtures / "plain.html").write_text("<html><body>hello</body></html>", "utf-8")
    manifest = {
        "https://onion.example.org/": {"file": "list.html"},
        "https://securedrop.example/api/": {"file": "drop.json"},
        "https://news.example.com/": {"file": "plain.html",
                                      "headers": {"Onion-Location": f"https://{addr['news']}/index.html"}},
        "https://silent.example.com/": {"file": "plain.html"},
        "https://search.example.com/": {"file": "meta.html"},
    }
    (fixtures / "manifest.json").write_text(json.dumps(manifest), "utf-8")
    return {"root": root, "fixtures": fixtures, "addr": addr, "manifest": manifest}
