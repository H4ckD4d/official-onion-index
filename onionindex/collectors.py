"""Collectors: each one turns an official source into a list of observations.

Evidence kinds, strongest first:

* ``onion-location`` - the owner's HTTPS website announces the address itself
  (``Onion-Location`` response header or the equivalent ``<meta>`` tag).
* ``official-list``  - a list published by the organisation that runs the
  services (for example onion.torproject.org).
* ``directory``      - the SecureDrop directory run by Freedom of the Press
  Foundation.
* ``manual``         - copied by hand from a page published by the owner or,
  where the owner has none, from Tor Project documentation; see
  ``config/manual.yml`` for the proof URL and the date of the check.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

import requests

from .onion import extract_host

USER_AGENT = "official-onion-index/1.0 (+https://github.com/H4ckD4d/official-onion-index)"
TIMEOUT = 30
MAX_BODY = 400_000  # bytes of HTML inspected for a <meta> onion-location tag

_URL = re.compile(r"https?://[A-Za-z0-9.\-]+(?::\d+)?[^\s\"'<>)\]]*")
_META_A = re.compile(
    r"<meta[^>]+http-equiv\s*=\s*[\"']?onion-location[\"']?[^>]*?content\s*=\s*[\"']([^\"']+)[\"']",
    re.I,
)
_META_B = re.compile(
    r"<meta[^>]+content\s*=\s*[\"']([^\"']+)[\"'][^>]*?http-equiv\s*=\s*[\"']?onion-location[\"']?",
    re.I,
)


@dataclass(frozen=True)
class Observation:
    service: str       # stable key, usually the clearnet hostname
    name: str          # display name
    category: str
    onion: str         # normalised onion host
    kind: str          # onion-location | official-list | directory | manual
    source: str        # human-readable source name
    source_url: str    # where anyone can re-check the address
    verified: str | None = None  # date of a hand check (manual entries only)


@dataclass
class Page:
    url: str
    text: str
    headers: dict


class HttpFetcher:
    """Fetches pages over HTTPS with certificate verification."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT

    def get(self, url: str) -> Page:
        if not url.lower().startswith("https://"):
            raise ValueError(f"refusing non-HTTPS source: {url}")
        resp = self.session.get(url, timeout=TIMEOUT, stream=True)
        resp.raise_for_status()
        if not resp.url.lower().startswith("https://"):
            raise ValueError(f"redirected to non-HTTPS URL: {resp.url}")
        body = resp.raw.read(MAX_BODY, decode_content=True)
        text = body.decode(resp.encoding or "utf-8", errors="replace")
        return Page(url=resp.url, text=text, headers={k.lower(): v for k, v in resp.headers.items()})


class FixtureFetcher:
    """Serves saved pages from disk. Used by the tests and for offline runs.

    ``directory/manifest.json`` maps a URL to ``{"file": ..., "headers": {...}}``.
    """

    def __init__(self, directory: str | Path) -> None:
        self.directory = Path(directory)
        self.manifest = json.loads((self.directory / "manifest.json").read_text("utf-8"))

    def get(self, url: str) -> Page:
        entry = self.manifest.get(url)
        if entry is None:
            raise LookupError(f"no fixture for {url}")
        text = (self.directory / entry["file"]).read_text("utf-8") if entry.get("file") else ""
        headers = {k.lower(): v for k, v in entry.get("headers", {}).items()}
        return Page(url=url, text=text, headers=headers)


# --------------------------------------------------------------------------
# Official lists (onion.torproject.org, onion.debian.org)
# --------------------------------------------------------------------------

def parse_host_onion_pairs(text: str, stop_at: str | None = None) -> list[tuple[str, str]]:
    """Pair each clearnet hostname with the first onion address that follows it.

    Both official lists use the same shape: a link to the clearnet service
    followed by a link to its onion address. Text after ``stop_at`` (the
    "Legacy addresses" section) is ignored.
    """
    if stop_at:
        cut = text.find(stop_at)
        if cut != -1:
            text = text[:cut]
    pairs: list[tuple[str, str]] = []
    seen_hosts: set[str] = set()
    current: str | None = None
    for match in _URL.finditer(text):
        url = match.group(0)
        onion = extract_host(url)
        if onion:
            if current and current not in seen_hosts:
                pairs.append((current, onion))
                seen_hosts.add(current)
            continue
        host = (urlsplit(url).hostname or "").lower()
        if host and not host.endswith(".onion"):
            current = host
    return pairs


def collect_official_list(fetcher, spec: dict) -> list[Observation]:
    page = fetcher.get(spec["url"])
    exclude = [re.compile(p) for p in spec.get("exclude", [])]
    out = []
    for host, onion in parse_host_onion_pairs(page.text, spec.get("stop_at")):
        if any(p.search(host) for p in exclude):
            continue
        out.append(Observation(
            service=host, name=host, category=spec["category"], onion=onion,
            kind="official-list", source=f"{spec['name']} official list", source_url=spec["url"],
        ))
    if not out:
        raise ValueError(f"no addresses parsed from {spec['url']} (page layout changed?)")
    return out


# --------------------------------------------------------------------------
# Onion-Location (announced by the owner's own website)
# --------------------------------------------------------------------------

def find_onion_location(page: Page) -> str | None:
    header = page.headers.get("onion-location")
    host = extract_host(header)
    if host:
        return host
    for pattern in (_META_A, _META_B):
        m = pattern.search(page.text)
        if m:
            host = extract_host(m.group(1))
            if host:
                return host
    return None


def service_key(site_url: str) -> str:
    return (urlsplit(site_url).hostname or site_url).lower()


def collect_onion_location(fetcher, sites: list[dict]) -> tuple[list[Observation], list[str]]:
    """Check each site; return observations plus a list of per-site notes."""
    out: list[Observation] = []
    notes: list[str] = []
    for site in sites:
        url = site["url"]
        try:
            page = fetcher.get(url)
        except Exception as exc:  # one unreachable site must not stop the run
            notes.append(f"{url}: {type(exc).__name__}: {exc}")
            continue
        onion = find_onion_location(page)
        if not onion:
            notes.append(f"{url}: no Onion-Location announced")
            continue
        out.append(Observation(
            service=service_key(url), name=site["name"], category=site["category"], onion=onion,
            kind="onion-location", source="Onion-Location on the owner's website", source_url=url,
        ))
    return out, notes


# --------------------------------------------------------------------------
# SecureDrop directory (Freedom of the Press Foundation)
# --------------------------------------------------------------------------

def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def collect_securedrop(fetcher, spec: dict) -> list[Observation]:
    page = fetcher.get(spec["url"])
    entries = json.loads(page.text)
    out = []
    for entry in entries:
        title = (entry.get("title") or "").strip()
        onion = extract_host(entry.get("onion_address"))
        if not title or not onion:
            continue
        out.append(Observation(
            service=f"securedrop:{_slug(title)}", name=title, category=spec["category"], onion=onion,
            kind="directory", source="SecureDrop directory (Freedom of the Press Foundation)",
            source_url=(entry.get("landing_page_url") or "https://securedrop.org/directory/").strip(),
        ))
    if not out:
        raise ValueError("SecureDrop directory returned no usable entries")
    return out


# --------------------------------------------------------------------------
# Hand-checked entries
# --------------------------------------------------------------------------

def collect_manual(entries: list[dict]) -> list[Observation]:
    out = []
    for e in entries:
        onion = extract_host(e["onion"])
        if not onion:
            raise ValueError(f"manual entry {e.get('name')!r} has an invalid onion address")
        out.append(Observation(
            service=service_key(e["site"]), name=e["name"], category=e["category"], onion=onion,
            kind="manual", source="Published page (checked by hand)", source_url=e["proof_url"],
            verified=str(e["verified"]),
        ))
    return out
