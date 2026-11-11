"""Merge today's observations into the accepted index.

Rules:

* A new service is added when all sources agree on one address.
* A known service whose address is confirmed gets its ``last_verified`` bumped.
* A known service observed with a *different* address is never updated
  automatically. It goes to the pending list for human review, because a
  changed address at the source can also mean the source was compromised.
  The maintainer accepts a change by adding it to ``config/overrides.yml``.
* Nothing is ever removed automatically. Entries that stop being confirmed
  simply keep their old ``last_verified`` date and are shown as stale.
"""

from __future__ import annotations

from collections import OrderedDict

from .collectors import Observation

KIND_RANK = {"onion-location": 0, "official-list": 1, "directory": 2, "manual": 3}


def _sources(observations: list[Observation]) -> list[dict]:
    seen, out = set(), []
    for o in sorted(observations, key=lambda o: KIND_RANK.get(o.kind, 9)):
        key = (o.kind, o.source_url)
        if key in seen:
            continue
        seen.add(key)
        out.append({"kind": o.kind, "name": o.source, "url": o.source_url})
    return out


def _verified_date(observations: list[Observation], today: str) -> str:
    """Today if a machine-checked source confirmed it, else the hand-check date."""
    if any(o.kind != "manual" for o in observations):
        return today
    return max(o.verified or today for o in observations)


def merge(existing: list[dict], observations: list[Observation], today: str,
          accepted: dict[str, str] | None = None) -> tuple[list[dict], list[dict], list[dict]]:
    """Return (entries, events, pending)."""
    accepted = accepted or {}
    index: "OrderedDict[str, dict]" = OrderedDict((e["service"], dict(e)) for e in existing)
    grouped: "OrderedDict[str, list[Observation]]" = OrderedDict()
    for o in observations:
        grouped.setdefault(o.service, []).append(o)

    events: list[dict] = []
    pending: list[dict] = []

    for service, obs in grouped.items():
        onions = list(OrderedDict.fromkeys(o.onion for o in obs))
        best = min(obs, key=lambda o: KIND_RANK.get(o.kind, 9))
        current = index.get(service)

        if current is None:
            if len(onions) > 1:
                pending.append({
                    "service": service, "name": best.name, "reason": "sources disagree",
                    "current": None, "observed": onions,
                    "sources": _sources(obs),
                })
                continue
            index[service] = {
                "service": service, "name": best.name, "category": best.category,
                "onion": onions[0], "sources": _sources(obs),
                "first_seen": today, "last_verified": _verified_date(obs, today),
            }
            events.append({"type": "added", "service": service, "name": best.name, "onion": onions[0]})
            continue

        agreeing = [o for o in obs if o.onion == current["onion"]]
        differing = [o for o in obs if o.onion != current["onion"]]

        if agreeing:
            current["sources"] = _sources(agreeing)
            current["last_verified"] = max(current.get("last_verified", ""), _verified_date(agreeing, today))
            current["name"], current["category"] = best.name, best.category

        for new_onion in OrderedDict.fromkeys(o.onion for o in differing):
            group = [o for o in differing if o.onion == new_onion]
            if accepted.get(service) == new_onion:
                events.append({"type": "changed", "service": service, "name": current["name"],
                               "old": current["onion"], "onion": new_onion})
                current["onion"] = new_onion
                current["sources"] = _sources(group)
                current["last_verified"] = _verified_date(group, today)
            else:
                pending.append({
                    "service": service, "name": current["name"], "reason": "address differs from the accepted one",
                    "current": current["onion"], "observed": [new_onion],
                    "sources": _sources(group),
                })

    return list(index.values()), events, pending
