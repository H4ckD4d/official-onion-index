from onionindex import collectors
from onionindex.collectors import FixtureFetcher, Page


def test_official_list_pairs_hosts_and_stops_at_legacy(project):
    fetcher = FixtureFetcher(project["fixtures"])
    spec = {"name": "Example", "url": "https://onion.example.org/", "category": "Example",
            "stop_at": "Legacy", "exclude": ["^grafana"]}
    found = {o.service: o.onion for o in collectors.collect_official_list(fetcher, spec)}
    addr = project["addr"]
    assert found == {"blog.example.org": addr["blog"], "www.example.org": addr["www"]}
    # the apt line after the list must not overwrite the last host, legacy entries are ignored
    assert addr["apt"] not in found.values()
    assert addr["legacy"] not in found.values()


def test_official_list_without_stop_marker_keeps_first_address_per_host(project):
    text = (project["fixtures"] / "list.html").read_text("utf-8")
    pairs = dict(collectors.parse_host_onion_pairs(text))
    assert pairs["www.example.org"] == project["addr"]["www"]
    assert pairs["git.example.org"] == project["addr"]["legacy"]
    assert "old.example.org" not in pairs  # v2 address is not valid


def test_onion_location_header_and_meta(project):
    addr = project["addr"]
    header = Page("https://a/", "", {"onion-location": f"https://{addr['news']}/x"})
    meta = Page("https://b/", f"<meta content='http://{addr['search']}/' http-equiv='Onion-Location'>", {})
    assert collectors.find_onion_location(header) == addr["news"]
    assert collectors.find_onion_location(meta) == addr["search"]
    assert collectors.find_onion_location(Page("https://c/", "<html></html>", {})) is None


def test_onion_location_collector_skips_silent_and_unreachable_sites(project):
    fetcher = FixtureFetcher(project["fixtures"])
    sites = [
        {"url": "https://news.example.com/", "name": "Example News", "category": "News"},
        {"url": "https://silent.example.com/", "name": "Silent", "category": "News"},
        {"url": "https://down.example.com/", "name": "Down", "category": "News"},
    ]
    found, notes = collectors.collect_onion_location(fetcher, sites)
    assert [(o.service, o.onion, o.kind) for o in found] == [
        ("news.example.com", project["addr"]["news"], "onion-location")]
    assert len(notes) == 2


def test_securedrop_directory_drops_invalid_rows(project):
    fetcher = FixtureFetcher(project["fixtures"])
    found = collectors.collect_securedrop(
        fetcher, {"url": "https://securedrop.example/api/", "category": "SecureDrop tip lines"})
    assert len(found) == 1
    assert found[0].service == "securedrop:the-example-times"
    assert found[0].source_url == "https://times.example.com/securedrop/"


def test_http_fetcher_refuses_plain_http():
    import pytest
    with pytest.raises(ValueError):
        collectors.HttpFetcher().get("http://example.com/")
