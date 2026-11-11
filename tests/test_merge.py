from onionindex.collectors import Observation
from onionindex.merge import merge


def obs(service, onion, kind="official-list", verified=None):
    return Observation(service=service, name=service, category="Cat", onion=onion, kind=kind,
                       source=kind, source_url=f"https://{service}/", verified=verified)


def test_new_service_is_added(onion):
    entries, events, pending = merge([], [obs("a.org", onion("a"))], "2026-11-11")
    assert entries[0]["onion"] == onion("a")
    assert entries[0]["first_seen"] == entries[0]["last_verified"] == "2026-11-11"
    assert events == [{"type": "added", "service": "a.org", "name": "a.org", "onion": onion("a")}]
    assert pending == []


def test_confirmation_bumps_date_and_keeps_first_seen(onion):
    entries, _, _ = merge([], [obs("a.org", onion("a"))], "2026-11-11")
    entries, events, pending = merge(entries, [obs("a.org", onion("a"))], "2026-11-12")
    assert entries[0]["first_seen"] == "2026-11-11"
    assert entries[0]["last_verified"] == "2026-11-12"
    assert events == [] and pending == []


def test_changed_address_is_never_applied_automatically(onion):
    entries, _, _ = merge([], [obs("a.org", onion("a"))], "2026-11-11")
    entries, events, pending = merge(entries, [obs("a.org", onion("b"))], "2026-11-12")
    assert entries[0]["onion"] == onion("a")
    assert entries[0]["last_verified"] == "2026-11-11"
    assert events == []
    assert pending[0]["current"] == onion("a") and pending[0]["observed"] == [onion("b")]


def test_maintainer_override_applies_the_change(onion):
    entries, _, _ = merge([], [obs("a.org", onion("a"))], "2026-11-11")
    entries, events, pending = merge(entries, [obs("a.org", onion("b"))], "2026-11-12",
                                     accepted={"a.org": onion("b")})
    assert entries[0]["onion"] == onion("b")
    assert events[0]["type"] == "changed" and events[0]["old"] == onion("a")
    assert pending == []


def test_disagreeing_sources_for_a_new_service_go_to_review(onion):
    entries, events, pending = merge(
        [], [obs("a.org", onion("a")), obs("a.org", onion("b"), kind="onion-location")], "2026-11-11")
    assert entries == [] and events == []
    assert pending[0]["reason"] == "sources disagree"


def test_manual_entry_keeps_its_hand_check_date_until_a_machine_confirms(onion):
    manual = obs("a.org", onion("a"), kind="manual", verified="2026-01-02")
    entries, _, _ = merge([], [manual], "2026-11-11")
    assert entries[0]["last_verified"] == "2026-01-02"
    entries, _, _ = merge(entries, [manual, obs("a.org", onion("a"), kind="onion-location")], "2026-11-12")
    assert entries[0]["last_verified"] == "2026-11-12"
    assert entries[0]["sources"][0]["kind"] == "onion-location"


def test_unobserved_entries_are_kept(onion):
    entries, _, _ = merge([], [obs("a.org", onion("a")), obs("b.org", onion("b"))], "2026-11-11")
    entries, _, _ = merge(entries, [obs("a.org", onion("a"))], "2026-11-12")
    assert {e["service"] for e in entries} == {"a.org", "b.org"}
