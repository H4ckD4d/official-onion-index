"""Parsing and validation of v3 onion addresses."""

from __future__ import annotations

import base64
import hashlib
import re
from urllib.parse import urlsplit

_V3_LABEL = re.compile(r"^[a-z2-7]{56}$")
_ONION_HOST = re.compile(r"^(?:[a-z0-9-]+\.)*[a-z2-7]{56}\.onion$")


def is_valid_v3(host: str) -> bool:
    """Return True if ``host`` is a well-formed v3 onion host.

    A v3 address is base32(pubkey[32] + checksum[2] + version[1]). The checksum
    is the first two bytes of SHA3-256(".onion checksum" + pubkey + version),
    so a mistyped address fails here. Passing this check only proves the
    address is well-formed, not that it belongs to who you think it does.
    """
    host = host.lower().strip(".")
    if not _ONION_HOST.match(host):
        return False
    label = host[: -len(".onion")].split(".")[-1]
    if not _V3_LABEL.match(label):
        return False
    try:
        raw = base64.b32decode(label.upper())
    except (ValueError, TypeError):
        return False
    pubkey, checksum, version = raw[:32], raw[32:34], raw[34:]
    expected = hashlib.sha3_256(b".onion checksum" + pubkey + version).digest()[:2]
    return version == b"\x03" and checksum == expected


def extract_host(value: str | None) -> str | None:
    """Return the normalised onion host found in a URL or bare host, or None.

    Subdomains are kept (``search.<key>.onion``); scheme, port and path are
    dropped. Anything that is not a valid v3 address returns None.
    """
    if not value:
        return None
    value = value.strip()
    candidate = value if "://" in value else "http://" + value
    try:
        host = urlsplit(candidate).hostname
    except ValueError:
        return None
    if not host:
        return None
    host = host.lower().strip(".")
    return host if is_valid_v3(host) else None
